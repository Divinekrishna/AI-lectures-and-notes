import os
from openai import OpenAI
from typing import Optional, List

class LLMHandler:
    """Handle interactions with OpenAI LLM API."""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        self.client = OpenAI(api_key=self.api_key)
    
    def chat(self, messages: List[dict], model: str = "gpt-3.5-turbo", 
             temperature: float = 0.7, max_tokens: int = 500) -> str:
        """Send chat message to OpenAI and get response."""
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error in chat request: {e}")
            return "Sorry, I encountered an error processing your request."
    
    def generate_text(self, prompt: str, temperature: float = 0.7) -> str:
        """Generate text based on a prompt."""
        messages = [{"role": "user", "content": prompt}]
        return self.chat(messages, temperature=temperature)
    
    def answer_question(self, context: str, question: str) -> str:
        """Answer a question based on provided context."""
        prompt = f"""Based on the following context, please answer the question.

Context:
{context}

Question: {question}

Answer:"""
        return self.generate_text(prompt)
    
    def summarize(self, text: str, max_tokens: int = 300) -> str:
        """Summarize provided text."""
        prompt = f"Please summarize the following text:\n\n{text}"
        return self.chat(
            [{"role": "user", "content": prompt}],
            max_tokens=max_tokens
        )
    
    def translate(self, text: str, target_language: str) -> str:
        """Translate text to target language."""
        prompt = f"Translate the following text to {target_language}:\n\n{text}"
        return self.generate_text(prompt)
    
    def find_relevant_resources(self, query: str, available_resources: List[str]) -> List[str]:
        """Find relevant resources based on query."""
        resources_text = "\n".join(available_resources)
        prompt = f"""Given the following resources, identify which ones are most relevant to the query.
        
Resources:
{resources_text}

Query: {query}

Please list the most relevant resources (one per line):"""
        response = self.generate_text(prompt)
        return [r.strip() for r in response.split('\n') if r.strip()]

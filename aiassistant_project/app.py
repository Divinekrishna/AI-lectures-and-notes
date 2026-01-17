import streamlit as st
import os
from dotenv import load_dotenv
from src.utils.file_handler import FileHandler
from src.utils.llm_handler import LLMHandler

# Optional imports for URL features
try:
    import yt_dlp
except ImportError:
    yt_dlp = None

try:
    import requests
except ImportError:
    requests = None

# Load environment variables
load_dotenv()

# Configure Streamlit page
st.set_page_config(
    page_title="AI Learning Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .sidebar .sidebar-content {
        padding: 2rem 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'llm_handler' not in st.session_state:
    try:
        st.session_state.llm_handler = LLMHandler()
    except ValueError as e:
        st.session_state.llm_handler = None
        st.error(f"⚠️ {e}")

if 'file_handler' not in st.session_state:
    st.session_state.file_handler = FileHandler()

if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'uploaded_resources' not in st.session_state:
    st.session_state.uploaded_resources = []

# Sidebar
with st.sidebar:
    st.title("📚 AI Learning Assistant")
    
    # Navigation
    page = st.radio(
        "Select a page:",
        ["🏠 Home", "📤 Upload Resources", "🎙️ Lecture Processing", "💬 Chatbot", "🔍 Resource Finder"]
    )
    
    st.divider()
    
    # Settings
    st.subheader("⚙️ Settings")
    language = st.selectbox(
        "Preferred Language:",
        ["English", "Spanish", "French", "German", "Italian", "Portuguese", "Japanese", "Chinese", "Hindi"]
    )
    
    st.divider()
    
    # API Status
    if st.session_state.llm_handler:
        st.success("✅ LLM API Connected")
    else:
        st.error("❌ LLM API Not Configured")

# Main Content
if page == "🏠 Home":
    st.title("🤖 AI Learning Assistant")
    st.write("""
    Welcome to the AI Learning Assistant! This application helps you:
    
    - 📤 **Upload Resources**: Upload lectures, documents, and materials
    - 🎙️ **Process Lectures**: Generate transcripts and summaries with AI
    - 💬 **Chat**: Ask questions about your resources using AI chatbot
    - 🔍 **Find Resources**: Discover relevant materials based on your queries
    
    ### Features:
    - 🌍 Multi-language support
    - 🎤 AI voice generation (text-to-speech)
    - 📄 Document processing and extraction
    - 🤖 Intelligent chatbot powered by LLM
    - 📊 Resource management and organization
    
    ### Getting Started:
    1. Go to **Upload Resources** to add your materials
    2. Use **Lecture Processing** to analyze your content
    3. Use the **Chatbot** to ask questions
    4. Use **Resource Finder** to discover related materials
    """)

elif page == "📤 Upload Resources":
    st.title("📤 Upload Resources")
    
    # Create tabs for different upload methods
    tab1, tab2 = st.tabs(["📁 Upload Files", "🌐 From URL"])
    
    with tab1:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            uploaded_files = st.file_uploader(
                "Upload your resources (PDF, TXT, DOCX, MP3, WAV, MP4)",
                accept_multiple_files=True,
                type=['pdf', 'txt', 'docx', 'mp3', 'wav', 'mp4']
            )
            
            if uploaded_files:
                for uploaded_file in uploaded_files:
                    if st.session_state.file_handler.is_supported_format(uploaded_file.name):
                        file_path = st.session_state.file_handler.save_uploaded_file(uploaded_file, 'resources')
                        if file_path:
                            st.session_state.uploaded_resources.append({
                                'name': uploaded_file.name,
                                'path': file_path,
                                'size': st.session_state.file_handler.get_file_size_mb(file_path),
                                'type': 'file'
                            })
                            st.success(f"✅ {uploaded_file.name} uploaded successfully!")
        
        with col2:
            st.metric("Uploaded Resources", len(st.session_state.uploaded_resources))
    
    with tab2:
        st.subheader("Add Resource from URL")
        
        url_type = st.radio("Select source type:", ["YouTube", "Google Classroom", "Direct URL"])
        
        if url_type == "YouTube":
            yt_url = st.text_input("Enter YouTube URL", placeholder="https://www.youtube.com/watch?v=...")
            if st.button("📥 Download from YouTube"):
                if yt_url:
                    with st.spinner("Downloading YouTube video..."):
                        try:
                            if not yt_dlp:
                                st.error("yt-dlp not installed. Please install it first.")
                            else:
                                ydl_opts = {
                                    'format': 'best',
                                    'outtmpl': 'uploads/resources/%(title)s.%(ext)s',
                                    'quiet': True,
                                }
                                
                                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                                    info = ydl.extract_info(yt_url, download=True)
                                    filename = info.get('title', 'video')
                                    ext = info.get('ext', 'mp4')
                                    file_path = f'uploads/resources/{filename}.{ext}'
                                    
                                    st.session_state.uploaded_resources.append({
                                        'name': f"{filename} (YouTube)",
                                        'path': file_path,
                                        'size': 0,
                                        'type': 'youtube'
                                    })
                                    st.success(f"✅ Downloaded: {filename}")
                        except Exception as e:
                            st.error(f"❌ Error downloading: {str(e)}")
                else:
                    st.warning("Please enter a YouTube URL")
        
        elif url_type == "Google Classroom":
            gc_url = st.text_input("Enter Google Classroom assignment/post URL", 
                                   placeholder="https://classroom.google.com/...")
            gc_info = st.text_area("Paste assignment details or content", height=100)
            
            if st.button("📥 Add from Google Classroom"):
                if gc_url or gc_info:
                    try:
                        # Save as text file
                        content = f"URL: {gc_url}\n\n{gc_info}"
                        file_path = f"uploads/resources/classroom_{len(st.session_state.uploaded_resources)}.txt"
                        os.makedirs('uploads/resources', exist_ok=True)
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(content)
                        
                        st.session_state.uploaded_resources.append({
                            'name': f"Classroom Assignment {len(st.session_state.uploaded_resources) + 1}",
                            'path': file_path,
                            'size': len(content) / (1024 * 1024),
                            'type': 'classroom'
                        })
                        st.success("✅ Added Google Classroom content!")
                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")
                else:
                    st.warning("Please enter URL or content")
        
        else:  # Direct URL
            direct_url = st.text_input("Enter direct URL to file", 
                                      placeholder="https://example.com/file.pdf")
            
            if st.button("📥 Download from URL"):
                if direct_url:
                    with st.spinner("Downloading file..."):
                        try:
                            if not requests:
                                st.error("requests module not installed.")
                            else:
                                response = requests.get(direct_url, timeout=30)
                                
                                # Extract filename from URL
                                filename = direct_url.split('/')[-1].split('?')[0] or 'downloaded_file'
                                file_path = f"uploads/resources/{filename}"
                                
                                os.makedirs('uploads/resources', exist_ok=True)
                                with open(file_path, 'wb') as f:
                                    f.write(response.content)
                                
                                file_size = len(response.content) / (1024 * 1024)
                                st.session_state.uploaded_resources.append({
                                    'name': filename,
                                    'path': file_path,
                                    'size': file_size,
                                    'type': 'url'
                                })
                                st.success(f"✅ Downloaded: {filename}")
                        except Exception as e:
                            st.error(f"❌ Error downloading: {str(e)}")
                else:
                    st.warning("Please enter a valid URL")
    
    st.divider()
    
    if st.session_state.uploaded_resources:
        st.subheader("📚 All Resources")
        for idx, resource in enumerate(st.session_state.uploaded_resources):
            col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
            with col1:
                resource_type = resource.get('type', 'file')
                icon = "🎥" if resource_type == "youtube" else "📚" if resource_type == "classroom" else "🔗" if resource_type == "url" else "📄"
                st.write(f"{icon} {resource['name']}")
            with col2:
                st.write(f"{resource['size']:.2f} MB")
            with col3:
                st.write(f"({resource.get('type', 'file')})")
            with col4:
                if st.button("❌", key=f"del_{idx}"):
                    try:
                        if os.path.exists(resource['path']):
                            os.remove(resource['path'])
                        st.session_state.uploaded_resources.pop(idx)
                        st.rerun()
                    except:
                        st.error("Error deleting resource")

elif page == "🎙️ Lecture Processing":
    st.title("🎙️ Lecture Processing")
    
    if not st.session_state.uploaded_resources:
        st.info("📤 Please upload resources first!")
    else:
        st.subheader("Select a resource to process:")
        
        resource_names = [r['name'] for r in st.session_state.uploaded_resources]
        selected_resource = st.selectbox("Choose resource:", resource_names)
        
        if selected_resource:
            resource = next(r for r in st.session_state.uploaded_resources if r['name'] == selected_resource)
            
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("📝 Extract Text"):
                    with st.spinner("Extracting text..."):
                        text = st.session_state.file_handler.extract_text_from_file(resource['path'])
                        if text:
                            st.text_area("Extracted Text:", value=text, height=300)
                            if st.session_state.llm_handler:
                                if st.button("📊 Generate Summary"):
                                    with st.spinner("Generating summary..."):
                                        summary = st.session_state.llm_handler.summarize(text)
                                        st.write("**Summary:**")
                                        st.write(summary)
            
            with col2:
                if st.session_state.llm_handler:
                    target_lang = st.selectbox("Translate to:", 
                        ["Spanish", "French", "German", "Italian", "Portuguese", "Japanese", "Chinese", "Hindi"])
                    if st.button("🌍 Translate"):
                        with st.spinner(f"Translating to {target_lang}..."):
                            text = st.session_state.file_handler.extract_text_from_file(resource['path'])
                            if text:
                                translated = st.session_state.llm_handler.translate(text[:2000], target_lang)
                                st.write(f"**Translation ({target_lang}):**")
                                st.write(translated)

elif page == "💬 Chatbot":
    st.title("💬 AI Chatbot")
    
    if not st.session_state.llm_handler:
        st.error("❌ LLM API not configured. Please set OPENAI_API_KEY in .env file")
    else:
        # Chat history
        for msg in st.session_state.messages:
            with st.chat_message(msg['role']):
                st.write(msg['content'])
        
        # User input
        user_input = st.chat_input("Ask me anything about your resources...")
        
        if user_input:
            # Add user message
            st.session_state.messages.append({"role": "user", "content": user_input})
            with st.chat_message("user"):
                st.write(user_input)
            
            # Generate response
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    # If resources exist, use context
                    context = ""
                    if st.session_state.uploaded_resources:
                        for resource in st.session_state.uploaded_resources[:3]:  # Use first 3 resources
                            resource_text = st.session_state.file_handler.extract_text_from_file(resource['path'])
                            context += resource_text[:1000] + "\n"
                    
                    if context:
                        response = st.session_state.llm_handler.answer_question(context, user_input)
                    else:
                        messages = [{"role": "user", "content": user_input}]
                        response = st.session_state.llm_handler.chat(messages)
                    
                    st.write(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})

elif page == "🔍 Resource Finder":
    st.title("🔍 Resource Finder")
    
    if not st.session_state.llm_handler:
        st.error("❌ LLM API not configured")
    elif not st.session_state.uploaded_resources:
        st.info("📤 Upload resources to find similar materials")
    else:
        query = st.text_input("What would you like to find?", placeholder="e.g., machine learning basics")
        
        if st.button("🔎 Search"):
            with st.spinner("Finding relevant resources..."):
                resource_names = [r['name'] for r in st.session_state.uploaded_resources]
                relevant = st.session_state.llm_handler.find_relevant_resources(query, resource_names)
                
                if relevant:
                    st.subheader("📌 Relevant Resources:")
                    for resource in relevant:
                        st.write(f"- {resource}")
                else:
                    st.info("No matching resources found")

# Footer
st.divider()
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>AI Learning Assistant v1.0 | Powered by Google Gemini</p>",
    unsafe_allow_html=True
)

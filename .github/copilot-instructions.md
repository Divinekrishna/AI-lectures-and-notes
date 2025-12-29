

# Copilot Instructions for aiassistant

-   The package `aiassistant` is a Python Project located in the folder `aiassistant-folder`.
-   You need to call the `Get Python Environment Information` tool on the `aiassistant` path to get the Python executable details.
-   Substitute the Python executable you get from the `Get Python Environment Information` tool anywhere you see `<python>` in these instructions.
    -   Run command for `aiassistant`: `<python> -m aiassistant`
    -   Command to run tests for `aiassistant`: `<python> -m pytest aiassistant/tests`
-   To run an editable install for the package `aiassistant`, use the `Install Python Package` tool with the `aiassistant-folder` path and arguments `['-e', '.']`.
-   In the workspace `launch.json` file, configurations related to this package have the prefix `aiassistant`.
-   The package `aiassistant` has a defined `pyproject.toml` file that you should use and keep up to date.

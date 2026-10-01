from langchain.tools import tool 
import os

project_dir = "Generated_respone"

os.makedirs(project_dir, exist_ok=True)


@tool
def create_file(file_path: str, content: str):
    """
    Create a new file inside the current website project.

    The file_path must be relative to the project directory.
    You can create files in subdirectories.

    Examples:
    - index.html
    - css/style.css
    - js/script.js
    - pages/about.html

    Automatically creates missing subdirectories.
    """
    full_path = os.path.join(project_dir, file_path)

    directory = os.path.dirname(full_path)

    if directory: 
        os.makedirs(directory, exist_ok=True)

    with open(full_path, "w",  encoding="utf-8") as file: 
        file.write(content)

    return f"Created file at {file_path}"

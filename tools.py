from langchain.tools import tool 
@tool
def save_to_html(data:str, filename:str= "index.html"):
    """Save the provided HTML code to an HTML file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(data)

@tool
def save_to_css(data:str, filename:str = "style.css"):
    """Save the provided CSS code to a CSS file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(data)

@tool
def save_to_js(data:str, filename:str = "script.css"):
    """Save the provided javaScript code to a script file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(data)


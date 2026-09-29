from dotenv import load_dotenv

from langchain_openrouter import ChatOpenRouter
from langchain.agents import create_agent
from tools import save_to_css, save_to_html, save_to_js

load_dotenv()


model = ChatOpenRouter(
    model = "openrouter/free"
)
agent = create_agent(
    model= model,
    tools = [save_to_html, save_to_css, save_to_js],
    system_prompt="""
    You are a website-building assistant.

    When the user asks you to create a website:
    1. Create a modern aesthetic code. 
    2. Generate the HTML code.
    3. Use save_to_html to save the HTML.
    4. Generate the CSS code.
    5. Use save_to_css to save the CSS.
    6. Generate some javaScript code to add some nice functionality.
    7. Use save_to_js to save the javaScript.
    8. Only tell the user the files were saved after the tools have
       successfully executed.
    """
)

def userInput():
    prompt = input('Hello, how may i help you ?: ')
    return prompt

prompt = userInput()

result = agent.invoke(
     {"messages": [{"role": "user", "content": prompt}]}
)
print(f"Content = {result['messages'][-1].content}")
print(result["messages"][-1].response_metadata)


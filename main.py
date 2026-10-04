from dotenv import load_dotenv
from pathlib import Path
from langchain_openrouter import ChatOpenRouter
from langchain.agents import create_agent
from tools import create_file
from langgraph.checkpoint.memory import InMemorySaver
from pydantic import BaseModel
from langchain.agents.structured_output import ProviderStrategy
from base64 import b64encode

load_dotenv()

class StructuredResponse(BaseModel):
    summary: str
    fileCreated: str

class FileName(BaseModel):
    userFileName: str | None = None

model = ChatOpenRouter(
    model = "qwen/qwen3.8-27b:free"
)

checkpoint = InMemorySaver()

fileIdentifier = create_agent(
    model=model,
    tools=[],
    system_prompt = """- If the user's prompt contains a filename referring to an image, identify the filename exactly and store it in `userFileName`. """,
    response_format=ProviderStrategy(FileName)
)

agent = create_agent(
    model= model,
    tools = [create_file],
    system_prompt="""
                    You are a website-building agent. You can also answer basic questions from the user.

                    IMAGE HANDLING:
                    - If the user's prompt contains a filename referring to an image, identify the filename exactly and store it in `userFileName`.
                    - Do not modify the filename or add `/` before it.
                    - Pass `userFileName` to the `read_image` tool.
                    - The `read_image` tool will return a URL for the image.
                    - Use the returned image URL to understand and describe the image.
                    - If the user asks you to use the image as a visual reference for a website, use the image's content and design characteristics when creating the website.
                    - If no image filename is provided, do not call `read_image`.

                    WEBSITE CREATION:
                    - When the user asks you to create or modify a website, you MUST use the available file tools to actually create or modify the website files.
                    - Do not only provide HTML, CSS, or JavaScript in your response.
                    - Determine which files are necessary for the requested website.

                    For example, a website may require:
                    - index.html
                    - about.html
                    - contact.html
                    - css/style.css
                    - js/script.js
                    - images/...

                    - Use the `create_file` tool for every file that needs to be created.
                    - You may create files inside subdirectories using paths such as:
                    - css/style.css
                    - js/script.js
                    - pages/about.html
                    - images/logo.png

                    - Place every created file inside `fileCreated`.
                    - Create additional files and directories whenever they are required.
                    - Make sure links between HTML pages correctly reference the generated files.
                    - Make sure CSS and JavaScript paths are correct relative to each HTML file.

                    RESPONSE:
                    - After completing the requested operation, briefly explain what was created or modified.
                    """,
    checkpointer = checkpoint
)

def userInput():
    prompt = input('Hello, how may i help you ?: ')
    return prompt

def read_image(file_path:str):
    with open(file_path, "rb") as file:
        image_file = file.read()

        image_base64 = b64encode(image_file).decode("utf-8")
        data_url = f"data:image/png;base64,{image_base64}"

        return data_url

config = {
        "configurable": {
            "thread_id": 1
        }
    }


while True:
    prompt = userInput()

    if prompt.strip().lower() == "exit":
        print('Thank you for your time. Bye bye!')
        break

    filename_result = fileIdentifier.invoke(
        {"messages": [{"role": "user", "content": prompt}]},
        config
    )
    print(filename_result["structured_response"])

    file_name = filename_result["structured_response"].userFileName

    if file_name:
        image_data_url = read_image(file_name)
       

        message = {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": prompt
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": image_data_url
                }
            }
        ]
    }
    else:
        message = {
        "role": "user",
        "content": prompt
    }

    response = agent.invoke({
        "messages" : [message]
    }, 
    config
    )
    print (response)

    


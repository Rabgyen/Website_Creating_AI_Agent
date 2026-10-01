from dotenv import load_dotenv
import uuid

from langchain_openrouter import ChatOpenRouter
from langchain.agents import create_agent
from tools import create_file
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()

model = ChatOpenRouter(
    model = "nvidia/nemotron-3-ultra-550b-a55b:free"
)

checkpoint = InMemorySaver()

agent = create_agent(
    model= model,
    tools = [create_file],
    system_prompt="""
        You are a website-building agent but you can also answer the basic questions of the user.

        When the user asks you to create or modify a website, you must use
        the available file tools to actually create or modify the website files.

        Do not only provide the HTML, CSS, or JavaScript in your response.

        Determine which files are necessary.

        For example, a website may require:
        - index.html
        - about.html
        - contact.html
        - css/style.css
        - js/script.js
        - images/...

        Use the create_file tool for every file that needs to be created.

        You may create files inside subdirectories by using paths such as:
        - css/style.css
        - js/script.js
        - pages/about.html

        Create additional files and directories whenever they are required.
        """,
    checkpointer = checkpoint
)

def userInput():
    prompt = input('Hello, how may i help you ?: ')
    return prompt

thread_id = str(uuid.uuid4())

config = {
        "configurable": {
            "thread_id": thread_id
        }
    }


while True:
    prompt = userInput()

    if prompt.strip().lower() == "exit":
        print('Thank you for your time. Bye bye!')
        break

    result = agent.invoke(
        {"messages": [{"role": "user", "content": prompt}]},
        config
    )
    print(f"Content = {result['messages'][-1].content}")
    print(result["messages"][-1].response_metadata)


# Website Creating AI Agent

A simple AI agent built with **Python**, **LangChain**, and **OpenRouter**.

This project is an introduction to building AI agents with LangChain. The agent receives a user's prompt, processes it using an OpenRouter-hosted language model, and generates a response.

## Technologies Used

- **Python** — Programming language
- **LangChain** — Framework for building LLM applications and agents
- **OpenRouter** — API provider for accessing different AI models
- **python-dotenv** — Loads environment variables from `.env`

## Requirements

Before starting, make sure you have:

- Python 3.12 (Recommanded)
- An OpenRouter account
- An OpenRouter API key
- Git, if cloning the repository

> **Note:** You can use an OpenRouter model that is currently available under its free tier. Free model availability can change over time.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Rabgyen/Website_Creating_AI_Agent.git
```

Navigate into the project directory:

```bash
cd Website_Creating_AI_Agent
```

### 2. Create a Virtual Environment

Create a Python virtual environment:

```bash
py -m venv .venv
```

This creates a `.venv` directory inside the project.

### 3. Activate the Virtual Environment

On Windows:

```bash
.venv\Scripts\activate
```

After activation, your terminal should look similar to:

```text
(.venv) C:\Users\...\Website_Creating_AI_Agent>
```

### 4. Install the Dependencies

The repository contains a `requirements.txt` file containing the project's Python dependencies.

Install all dependencies with:

```bash
py -m pip install -r requirements.txt
```

This installs the packages listed in `requirements.txt`, including the dependencies required by LangChain and OpenRouter.

## OpenRouter API Key

This project requires an OpenRouter API key.

Create an account and generate an API key through the OpenRouter website.

Create a file named:

```text
.env
```

in the root directory of the project.

Add your API key:

```env
OPENROUTER_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual API key.

### Keeping Your API Key Secure

Your `.gitignore` should contain:

```gitignore
.env
.venv/
__pycache__/
```

This prevents your API key and virtual environment from being committed to the repository.

## Running the Project

After activating the virtual environment and configuring your API key, run:

```bash
py main.py
```

The application will start and allow you to interact with the AI agent.

## Project Dependencies

The project includes a `requirements.txt` file containing the package versions used by the project.

The main packages currently used by the project include:

```text
langchain
langchain-openrouter
python-dotenv
```

The `requirements.txt` file also contains packages that are required internally by these libraries.

To install all dependencies:

```bash
py -m pip install -r requirements.txt
```

## Project Structure

```text
Website_Creating_AI_Agent/
│
├── main.py
├── tools.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── .env              # API key - not committed
└── .venv/            # Virtual environment - not committed
```

## Setting Up the Project on Another Computer

After cloning the repository:

```bash
git clone https://github.com/Rabgyen/Website_Creating_AI_Agent.git
cd Website_Creating_AI_Agent
```

Create the virtual environment:

```bash
py -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
py -m pip install -r requirements.txt
```

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_api_key_here
```

Then run the project:

```bash
py main.py
```

## What This Project Demonstrates

This project is intended as a learning project for understanding:

- How LangChain works
- How to connect an LLM to a Python application
- How to use OpenRouter with LangChain
- How API keys are stored using environment variables
- How Python virtual environments work
- How Python dependencies are managed with `requirements.txt`
- How to structure and publish a Python project using Git and GitHub

## Important Notes

- The `.venv` directory should not be committed to GitHub.
- The `.env` file should not be committed to GitHub.
- `requirements.txt` should be committed because it allows others to install the project's dependencies.
- OpenRouter's available models and free-tier limits may change over time.
- Keep your API keys private.

## License

This project is intended for learning and experimentation.

# LangChain Chatbot with History

A simple, interactive command-line chatbot built using LangChain and OpenRouter that remembers your conversation history.

## What is LangChain?
LangChain is a framework designed to make building applications with Large Language Models (LLMs) easier by connecting them to data sources, memory, and tools.

Documentation link: https://docs.langchain.com/oss/python/langchain/overview

## Why use LangChain?
It provides a unified interface to easily switch between different LLMs, manage conversation context, and chain multiple operations together without rewriting boilerplate code.

### Benefits & Model Switching
* **Connecting Multiple SDKs via LangChain:** LangChain acts as an abstraction layer with uniform code methods (like `.invoke()`). You can seamlessly switch between direct SDK integrations (like `langchain-openai`, `langchain-anthropic`, or `langchain-google-genai`) simply by swapping model wrappers—without rewriting your application logic.
* **SDK Integrations vs. OpenRouter (The Difference):**
  * **Direct SDK Integrations:** Connects directly to a specific provider's API (e.g., using OpenAI credentials to hit OpenAI directly, or Anthropic keys for Anthropic).
  * **OpenRouter:** A single multi-model API aggregator. Instead of managing separate SDKs and keys for OpenAI, Anthropic, and Google, OpenRouter provides a single API endpoint and key to access all these providers in one place.

## What does "Chain" mean in LangChain?
A "Chain" refers to linking multiple components together—such as taking a user prompt, passing it through an LLM, and feeding the output into another tool or function sequentially.

## Alternatives & When to Choose What
* **LangChain:** Best for linear applications, simple chatbots, and standard data-retrieval (RAG) tasks.
* **LangGraph:** Best when you need cyclic loops, complex state management, or multi-turn human-in-the-loop workflows.
* **CrewAI / AutoGen:** Best for multi-agent systems where independent specialized agents collaborate to achieve a common goal.

## Code Explanation: Persistent Memory
In this application, context memory is maintained via a Python list called `conversation_history`. 
Each turn, we append `("user", user_input)` and `("assistant", response.content)`. 
Passing this complete list to `model.invoke(conversation_history)` allows the LLM to read the entire chat history and retain context across messages.

---

## Prerequisites
Ensure you have the `uv` package manager installed. If not, install it via:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Setup Instructions

1. **Clone or create the project folder:**
   ```bash
   mkdir langchain-chatbot && cd langchain-chatbot
   ```

2. **Initialize the project environment with `uv`:**
   ```bash
   uv init
   ```

3. **Install the required dependencies:**
   ```bash
   uv add langchain-openrouter python-dotenv
   ```

4. **Configure environment variables:**
   Create a `.env` file in the root directory and add your OpenRouter API key and desired model:
   ```env
   OPENROUTER_API_KEY=your_api_key_here
   MODEL=meta-llama/llama-3-8b-instruct:free
   ```

5. **Create the script:**
   Save the corrected code into a file named `chatbot.py`.

## How to Run the Project
Execute the script using `uv run`:
```bash
uv run chatbot.py
```

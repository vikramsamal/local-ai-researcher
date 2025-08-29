# Local AI Document Assistant

**Build Your Personal AI Document Assistant Locally (and Offline!)**

Are you tired of endlessly sifting through PDFs, research papers, homework assignments, or even your favorite cookbook recipes? Do you wish you could just ask your documents questions and get instant, accurate answers? This project lets you build your own personal AI document assistant that runs entirely on your local machine, completely offline, and powered by open-source tools.

Whether you're in Mountain House, California, or anywhere else without a stable internet connection, this solution provides privacy, cost-effectiveness, and ultimate control over your data.

---

## 🚀 Why Go Local?

- **Privacy First:** Your documents and queries never leave your computer.
- **Zero Cost:** No subscription fees or cloud computing costs.
- **Offline Access:** Works anywhere, anytime.

---

## 🛠️ Prerequisites

- **Ollama:** Run Large Language Models (LLMs) locally.
  - Download from [ollama.com](https://ollama.com/)
  - Install required models:
    ```bash
    ollama pull llama3             # For generating answers
    ollama pull nomic-embed-text   # For creating text embeddings
    ```
- **Python 3.8+**

---

## 📂 Project Setup

1. **Clone or create your project directory:**
    ```bash
    mkdir my-ai-assistant
    cd my-ai-assistant
    ```

2. **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install langchain langchain_community pypdf chromadb sentence-transformers
    ```

4. **Create a `papers/` folder and add your PDFs:**
    ```bash
    mkdir papers
    # Place your PDF files in the papers/ folder
    ```

5. **Copy the [`app.py`](app.py) script into your project directory.**

Your project structure should look like:
```
my-ai-assistant/
├── papers/
│   ├── research_paper_1.pdf
│   ├── grandma_lasagna.pdf
│   └── user_manual.pdf
├── venv/
└── app.py
```

---

## 🧠 How It Works

[`app.py`](app.py) will:
- Load and split your PDFs into manageable text chunks.
- Create or load a ChromaDB vector store for fast document retrieval.
- Use Ollama's LLMs to answer your questions based only on your documents.

---

## 🚀 Running Your AI Assistant

1. **Ensure Ollama is running** (background app).
2. **Activate your virtual environment:**
    ```bash
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    ```
3. **Run the script:**
    ```bash
    python3 app.py
    ```

- **First Run:** Loads and processes all PDFs, builds the vector store (may take a few minutes).
- **Subsequent Runs:** Loads the existing vector store for fast startup. Delete the `chroma_db` folder if you add new documents.

---

## 💬 Example Questions

- "What are the main findings in the paper about quantum computing?"
- "Summarize the ingredients needed for the chocolate cake recipe."
- "According to the washing machine manual, what does error code E3 mean?"
- "What are the key differences between method A and method B discussed in [specific paper name]?"

Your AI will retrieve the most relevant sections from your `papers/` folder and synthesize an answer based only on that information.

---

## 🙌 Contribution

Feel free to fork this repository, open issues, or submit pull requests with improvements. Let's make local AI accessible for everyone!

---

## 📄 License

This project is open-source and available

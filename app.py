# app.py

# Step 3.1: Import Necessary Libraries
import sys
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

def main():
    # Step 3.2: Load and Split Your PDFs
    print("Step 1: Loading and splitting documents...")
    try:
        loader = PyPDFDirectoryLoader("papers/")
        docs = loader.load()
        if not docs:
            print("Error: No documents found in the 'papers' directory. Please add your PDFs.")
            sys.exit(1)
        
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        splits = text_splitter.split_documents(docs)
        print(f"Loaded and split {len(docs)} documents into {len(splits)} chunks.")
    except Exception as e:
        print(f"Error loading documents: {e}")
        sys.exit(1)

    # Step 3.3: Create the Knowledge Base (Vector Store)
    print("Step 2: Creating vector store from document chunks...")
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings, persist_directory="./chroma_db")
    print("Vector store created successfully.")

    # Step 3.4: Build the RAG Chain
    print("Step 3: Building the RAG chain...")
    llm = Ollama(model="llama3")
    retriever = vectorstore.as_retriever()

    prompt = ChatPromptTemplate.from_template("""
    **You are an expert research assistant.** Answer the following question based *only* on the provided context from the research papers.
    Provide a detailed, clear answer. If the answer is not present in the context, state that you cannot find the information in the provided documents.

    **Context:**
    {context}

    **Question:**
    {input}

    **Answer:**
    """)

    document_chain = create_stuff_documents_chain(llm, prompt)
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    print("RAG chain built successfully.")

    # Step 3.5: Ask Questions and Get Answers
    print("\n--- AI Research Assistant is Ready ---")
    print("You can now ask questions about your research papers. Type 'exit' to quit.")

    while True:
        try:
            user_question = input("\nYour question: ")
            if user_question.lower() == 'exit':
                break
            if not user_question.strip():
                continue

            print("\nThinking...")
            response = retrieval_chain.invoke({"input": user_question})
            
            print("\nAnswer:\n" + "="*8)
            print(response["answer"])
            print("="*8)

        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break

    print("\n--- Session Ended ---")

if __name__ == "__main__":
    main()
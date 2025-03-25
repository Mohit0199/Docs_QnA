import torch
import streamlit as st
from transformers import pipeline
import pdfplumber
import docx

# Load the model
model_path = "../Models/models--deepset--roberta-base-squad2/snapshots/adc3b06f79f797d1c575d5479d6f5efe54a9e3b4"
question_answer = pipeline("question-answering", model=model_path)

# Function to extract text from different file formats
def read_file_content(file):
    try:
        file_extension = file.name.split('.')[-1].lower()

        if file_extension == "txt":
            return file.getvalue().decode("utf-8")

        elif file_extension == "pdf":
            with pdfplumber.open(file) as pdf:
                text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
                return text if text else None

        elif file_extension in ["doc", "docx"]:
            doc = docx.Document(file)
            text = "\n".join([para.text for para in doc.paragraphs])
            return text if text else None

        else:
            return None
    except Exception as e:
        return None

# Function to get answer from extracted text
def get_answer(context, question):
    if not context:
        return "⚠️ No relevant text found in the document. Please try another file."

    try:
        answer = question_answer(question=question, context=context)
        return f"✅ **Answer:** {answer['answer']}"
    except Exception as e:
        return f"❌ Error processing the question: {e}"

# Streamlit UI
st.set_page_config(page_title="AI Document Q&A", page_icon="📖", layout="centered")

st.title("AskMyDoc AI")
st.write("Upload a document and ask questions. Supported formats: **TXT, PDF, DOCX**")

# File Upload
uploaded_file = st.file_uploader("📂 Upload your document", type=["txt", "pdf", "docx"])

# Question Input
question = st.text_input("🔎 Ask a Question", placeholder="Type your question here...")

# Process Button
if st.button("Get Answer"):
    if uploaded_file and question:
        extracted_text = read_file_content(uploaded_file)
        if extracted_text:
            answer = get_answer(extracted_text, question)
            st.success(answer)
        else:
            st.error("⚠️ Could not extract text. Please upload a valid document.")
    else:
        st.warning("⚠️ Please upload a file and enter a question.")

# Footer
st.markdown("---")
st.markdown("💡 **Tip:** Ensure your document contains readable text for better results.")


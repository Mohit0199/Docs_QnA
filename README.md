# AskMyDoc AI - AI-Powered Document Q&A

## 📌 Project Overview
AskMyDoc AI is a **Streamlit** application that allows users to upload **TXT, PDF, or DOCX** files and ask questions about the document's content. The application extracts text from the uploaded file and leverages a **pre-trained transformer model (RoBERTa)** using **Hugging Face's `pipeline`** for **question answering**.

## 🚀 Features
- 📂 **Supports multiple file formats** - TXT, PDF, and DOCX.
- 🔍 **Extracts and processes text** from uploaded documents.
- 🤖 **Utilizes RoBERTa-based model** for answering user queries.
- 🖥️ **Built with Streamlit** - simple and interactive UI.
- ✅ **Fast and accurate question answering** with minimal setup.

## 📦 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/AskMyDoc-AI.git
cd AskMyDoc-AI
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Download the Model
Before running the application, ensure you have downloaded the **RoBERTa-based SQuAD2 model** to your local machine.

You can download it using Hugging Face's CLI:
```bash
huggingface-cli download deepset/roberta-base-squad2 --local-dir ../Models/models--deepset--roberta-base-squad2
```
Or manually from [Hugging Face Model Hub](https://huggingface.co/deepset/roberta-base-squad2).

## 🏃‍♂️ Running the Application
```bash
streamlit run document_qna.py
```

## 🔧 How It Works
1. **User uploads a file** (TXT, PDF, DOCX).
2. **Application extracts text** using `pdfplumber` (for PDFs) and `python-docx` (for Word files).
3. **User enters a question** in the input field.
4. **RoBERTa-based model** processes the question and provides an answer based on the extracted text.
5. **Answer is displayed** in the Streamlit UI.

## 📚 Dependencies
- **Python** >= 3.7
- **torch**
- **transformers** (Hugging Face)
- **streamlit**
- **pdfplumber**
- **python-docx**

Install all dependencies using:
```bash
pip install -r requirements.txt
```

## 🎯 Future Enhancements
- 🔥 **Improve UI** with better styling.
- 📝 **Allow multi-page PDFs** to be processed efficiently.
- 🗣️ **Integrate speech-to-text** for voice-based questions.
- 📊 **Enable document summarization** for quick insights.

💡 _"Transforming documents into insights with AI!"_


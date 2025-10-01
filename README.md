```markdown
# AI-Powered Interview Flashcards Generator

This project is a **Flask web application** that generates **interview flashcards (questions & answers)** on any topic using **Google Gemini API**.  
It dynamically produces **6 unique flashcards** with randomized variations for more diversity.

---

## 🚀 Features
- Generates **6 unique interview flashcards** (Q&A format).  
- Topics can be customized by user input.  
- Uses **Google Gemini 2.0 Flash API** for AI-powered generation.  
- Randomized prompts for diverse output.  
- JSON-only responses for easy front-end integration.  
- Built with **Flask** (Python backend).  

---

## 🛠️ Tech Stack
- **Backend:** Python, Flask  
- **AI Model:** Google Gemini (`gemini-2.0-flash-exp`)  
- **Frontend:** HTML (served via Flask templates)  
- **Deployment Ready:** Works locally & can be deployed on Render, Railway, or Google Cloud Run  

---

## 📂 Project Structure
```

.
├── app.py              # Flask application
├── templates/
│   └── index.html      # Frontend UI
├── requirements.txt    # Dependencies
└── README.md           # Project documentation

````

---

## ⚙️ Setup & Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/your-username/ai-flashcards.git
   cd ai-flashcards
````

2. **Create virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your Google API Key**

   * Create an API key from **Google AI Studio (Gemini API)**.
   * Add it to your environment:

     ```bash
     export GOOGLE_API_KEY="your_api_key_here"   # Linux/Mac
     set GOOGLE_API_KEY="your_api_key_here"      # Windows PowerShell
     ```

5. **Run the Flask app**

   ```bash
   python app.py
   ```

6. **Open in browser**

   * Visit: `http://127.0.0.1:5000`

---

## 📌 API Endpoint

### **`POST /get_questions`**

Generates 6 flashcards for a given topic.

#### Request (JSON):

```json
{
  "topic": "Python programming"
}
```

#### Response (JSON):

```json
[
  {
    "question": "What is Python's GIL?",
    "answer": "The Global Interpreter Lock (GIL) is a mutex that protects access..."
  },
  {
    "question": "Explain list vs tuple in Python.",
    "answer": "Lists are mutable, while tuples are immutable..."
  }
]
```

---

## 📖 Example Usage

* Open the web app.
* Enter a topic (e.g., "Machine Learning").
* Get **6 random flashcards** (questions + answers).

---

## 🔮 Future Enhancements

* Add **difficulty level selection**.
* Support **multiple topics at once**.
* Flashcard **export to PDF/Excel**.
* User login & saving flashcards.

---

## 📝 License

This project is open-source and available under the **MIT License**.

---

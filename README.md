# 🤖 AI Code Review Agent

An AI-powered code review system that analyzes GitHub repositories using:

- AST Parsing
- Automated Code Review
- Confidence Scoring
- Severity Classification
- Interactive Streamlit Dashboard

---

# 🚀 Features

✅ Clone GitHub repositories automatically  
✅ Parse Python files using AST  
✅ Extract functions and classes  
✅ AI-powered review engine (mock/demo mode supported)  
✅ Confidence scoring system  
✅ Severity classification (Low / Medium / High)  
✅ Interactive Streamlit dashboard  
✅ CSV report export  
✅ Severity analytics charts  

---

# 📂 Project Structure

```bash
ai-code-review-agent/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── core/
│   ├── clone_repo.py
│   ├── parser.py
│   ├── chunker.py
│   ├── reviewer.py
│   ├── prompts.py
│   ├── confidence.py
│   └── utils.py
│
├── output/
│   └── reviews.json
│
├── assets/
│
└── temp_repo/
```

---

# ⚙️ Tech Stack

- Python
- Streamlit
- OpenAI API
- AST (Abstract Syntax Tree)
- Pandas
- GitPython

---

# 🧠 How It Works

## Step 1 — Clone Repository

The system clones a GitHub repository into a temporary folder.

---

## Step 2 — Parse Source Code

AST parsing extracts:

- Functions
- Classes
- Source code segments

---

## Step 3 — AI Review Engine

The AI reviewer analyzes code and generates:

- Severity
- Confidence score
- Review comments

---

## Step 4 — Dashboard Visualization

Results are displayed in Streamlit with:

- Filters
- Charts
- CSV export

---

# 📊 Dashboard Features

- GitHub repository input
- Real-time review processing
- Severity filtering
- Confidence labels
- Bar chart analytics
- Downloadable CSV reports

---

# ▶️ Installation

## Clone Repository

```bash
git clone https://github.com/your-username/ai-code-review-agent.git

cd ai-code-review-agent
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create `.env`

```env
OPENAI_API_KEY=your_openai_api_key
```

---

# ▶️ Run Streamlit App

```bash
streamlit run app.py
```

---

# 📈 Example Output

```json
{
  "issues": [
    {
      "type": "style",
      "severity": "low",
      "line": 2,
      "comment": "Consider adding spaces around operators.",
      "confidence": 85
    }
  ]
}
```

---

# 🛡️ Confidence Scoring

| Score Range | Label |
|---|---|
| 0–49 | VERIFY THIS |
| 50–74 | MEDIUM CONFIDENCE |
| 75–100 | HIGH CONFIDENCE |

---

# 📦 CSV Export

The dashboard supports downloading review reports as CSV files.

---

# 🔮 Future Improvements

- Multi-language support
- Real OpenAI review integration
- Docker deployment
- Authentication
- GitHub Actions integration
- Syntax-highlighted code viewer

---

# 👨‍💻 Author

## Ramya Adabala

---

# 📄 License

This project is for educational and internship assignment purposes.
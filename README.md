# Clinical Report Analyser

A full-stack web application that lets a clinician enter patient details, upload a medical report PDF, and receive AI-powered clinical suggestions from **Anthropic Claude**.

## How It Works

1. Fill in the patient's name, age, gender, and any symptoms/notes in the form.
2. Attach the medical report as a PDF.
3. Click **Analyse Report** — the backend extracts the PDF text and sends everything to Claude.
4. Claude returns structured clinical suggestions displayed directly on the page.

---

## Project Structure

```
MedicalApp/
├── frontend/                 # React + TypeScript (Vite)
│   └── src/
│       ├── App.tsx           # Single-page form + result display
│       └── App.css           # Styling
│
├── backend/                  # Python Flask API
│   ├── app.py                # Single endpoint: POST /api/analyze
│   ├── ai_processor.py       # Calls Claude API with patient info + PDF text
│   ├── pdf_processor.py      # Extracts text from PDF using PyPDF2
│   ├── requirements.txt
│   ├── .env                  # Your environment variables (not committed)
│   ├── .env.example          # Template
│   └── uploads/              # Saved PDFs (auto-created)
│
└── README.md
```

---

## Prerequisites

- **Node.js** v16+
- **Python** 3.8+
- **Anthropic API key** — https://console.anthropic.com/

---

## Setup

### 1. Backend

```bash
cd backend

# Create and activate virtual environment
python -m venv venv

# Windows
venv\Scripts\python.exe -m pip install -r requirements.txt

# macOS/Linux
source venv/bin/activate
pip install -r requirements.txt
```

Create your `.env` file:

```bash
# Windows
copy .env.example .env

# macOS/Linux
cp .env.example .env
```

Open `.env` and set your Anthropic API key:

```env
ANTHROPIC_API_KEY=sk-ant-...
```

### 2. Frontend

```bash
cd frontend
npm install
```

---

## Running the Application

**Terminal 1 — Backend:**

```bash
cd backend
venv\Scripts\python.exe app.py        # Windows
# or
python app.py                          # macOS/Linux (venv activated)
```

Backend runs on: http://localhost:5000

**Terminal 2 — Frontend:**

```bash
cd frontend
npm run dev
```

Frontend runs on: http://localhost:5173

---

## API

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| POST | `/api/analyze` | Analyse patient form + PDF |

### POST /api/analyze

Accepts `multipart/form-data`:

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Patient full name |
| `age` | Yes | Patient age |
| `gender` | Yes | Male / Female / Other |
| `symptoms` | No | Free-text symptoms or notes |
| `file` | Yes | PDF medical report |

Response:

```json
{
  "status": "success",
  "analysis": "### 1. Summary of Findings\n...",
  "model": "claude-haiku-4-5"
}
```

---

## Claude Integration

- **Model:** `claude-haiku-4-5`
- **Input:** Patient form fields + full PDF text (capped at 12,000 characters)
- **Prompt structure:** Patient info → PDF content → structured response format
- **Output sections:** Summary of Findings, Identified Conditions, Risk Factors, Recommendations, Follow-up

---

## Security Notes

- Never commit your `.env` file — it is listed in `.gitignore`
- Treat API keys like passwords; regenerate immediately if exposed
- Only PDF files are accepted for upload
- All API keys are loaded from environment variables, never hardcoded

---

## Troubleshooting

**401 from Claude** — API key is invalid or expired. Regenerate at https://console.anthropic.com/

**404 model not found** — Your plan may not have access to that model. Check available models in the Anthropic console and update `MODEL` in `backend/ai_processor.py`.

**Port in use:**

```bash
# Windows — find and kill process on port 5000
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

**Module not found:**

```bash
cd backend
venv\Scripts\pip.exe install -r requirements.txt
```

"""
AI Processor Module
Sends patient form data + PDF text to Claude and returns structured suggestions.
"""

import os
from dotenv import load_dotenv

load_dotenv()

MODEL = 'claude-haiku-4-5'


def analyze_report_with_claude(patient_info: dict, pdf_text: str) -> dict:
    """
    Send patient form data and PDF content to Claude for analysis.

    Args:
        patient_info: dict with keys: name, age, gender, symptoms
        pdf_text:     full text extracted from the uploaded PDF

    Returns:
        dict with keys: status, analysis (str), model (str)
                    or: status='failed', error (str)
    """
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        return {'status': 'failed', 'error': 'ANTHROPIC_API_KEY is not set in environment'}

    name = patient_info.get('name', 'Unknown')
    age = patient_info.get('age', 'Unknown')
    gender = patient_info.get('gender', 'Unknown')
    symptoms = patient_info.get('symptoms', '')

    symptoms_section = f"\nSymptoms / Notes from patient:\n{symptoms}" if symptoms else ""

    prompt = f"""You are a clinical decision-support assistant. A medical professional has submitted the following patient information and a scanned medical report. Provide a clear, structured analysis with actionable suggestions.

## Patient Information (from intake form)
- Name: {name}
- Age: {age}
- Gender: {gender}{symptoms_section}

## Medical Report (extracted from PDF)
{pdf_text}

---

Please respond using the following structure:

### 1. Summary of Findings
Briefly summarise the key clinical findings from the report.

### 2. Identified Conditions / Diagnoses
List any conditions, diagnoses, or abnormal values found in the report.

### 3. Risk Factors
Highlight any risk factors relevant to this patient based on age, gender, symptoms, and report data.

### 4. Recommendations
Provide specific, actionable clinical recommendations (investigations, treatments, referrals, lifestyle changes).

### 5. Follow-up
Suggest appropriate follow-up steps and timeline.

> Important: This is a decision-support tool only. Final clinical decisions must be made by a licensed medical professional.
"""

    try:
        from anthropic import Anthropic
        client = Anthropic(api_key=api_key)

        print(f"[Claude] Sending request — patient: {name}, PDF chars: {len(pdf_text)}")

        response = client.messages.create(
            model=MODEL,
            max_tokens=2048,
            messages=[{'role': 'user', 'content': prompt}],
        )

        analysis = response.content[0].text
        print(f"[Claude] Response received — {len(analysis)} chars")

        return {
            'status': 'success',
            'analysis': analysis,
            'model': MODEL,
        }

    except Exception as e:
        print(f"[Claude] Error: {e}")
        return {'status': 'failed', 'error': str(e)}


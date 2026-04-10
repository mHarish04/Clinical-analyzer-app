#!/usr/bin/env python
"""
Test script to validate PDF extraction without uploading
Run: python test_extraction.py
"""

from pdf_processor import extract_key_sections, format_extracted_data

# Sample medical report text
SAMPLE_MEDICAL_REPORT = """
PATIENT INFORMATION
Name: Jane Smith
Age: 52
Date of Birth: 1971-03-15
Medical Record #: MR-2024-001234
Date of Examination: March 31, 2026

CHIEF COMPLAINT
Patient presents with persistent headaches and fatigue

PATIENT HISTORY
Patient reports 6 months of intermittent headaches, worse in the mornings.
Associated with fatigue and occasional dizziness.
No vision changes or neurological symptoms reported.

PHYSICAL EXAMINATION
Vital Signs:
- Blood Pressure: 138/88 mmHg
- Heart Rate: 72 bpm
- Temperature: 37.1°C
- Respiratory Rate: 16 breaths/min
- Weight: 68 kg

General: Patient appears alert and oriented
Cardiovascular: Regular rate and rhythm, no murmurs
Neurological: Cranial nerves II-XII intact, no focal deficits

LABORATORY FINDINGS
Complete Blood Count:
- Hemoglobin: 11.2 g/dL (LOW - normal 12.0-15.5)
- Hematocrit: 33.5% (LOW)
- WBC: 7.2 K/uL (normal)

Metabolic Panel:
- Glucose: 92 mg/dL (normal)
- BUN: 18 mg/dL (normal)
- Creatinine: 0.9 mg/dL (normal)
- Electrolytes: normal

ASSESSMENT AND DIAGNOSIS
1. Anemia, likely iron-deficient based on lab values
2. Fatigue, secondary to anemia
3. Tension headaches
4. Hypertension, stage 1

PLAN AND RECOMMENDATIONS
1. Start Iron supplementation: Ferrous sulfate 325mg daily with vitamin C
2. Dietary recommendations: increase iron-rich foods (red meat, spinach, beans)
3. Follow-up labs in 4 weeks
4. Blood pressure monitoring at home, twice weekly
5. Refer to cardiology if BP remains elevated
6. Return to office if symptoms worsen or new symptoms develop
7. Exercise 30 minutes daily, light to moderate intensity

MEDICATIONS
- Iron supplement 325mg daily
- Aspirin 81mg daily for cardiovascular health

FOLLOW-UP
Recheck CBC in 4 weeks, follow up in office in 6 weeks
"""

def test_extraction():
    """Test the extraction pipeline"""
    
    print("\n" + "="*70)
    print("PDF EXTRACTION TEST")
    print("="*70)
    
    print(f"\n1. ORIGINAL TEXT")
    print(f"   Length: {len(SAMPLE_MEDICAL_REPORT)} characters")
    print(f"   Estimated tokens: {len(SAMPLE_MEDICAL_REPORT) // 4}")
    print(f"   First 300 chars:\n   {SAMPLE_MEDICAL_REPORT[:300]}...\n")
    
    # Extract sections
    print(f"\n2. EXTRACTING KEY SECTIONS")
    print("   Looking for: Patient Info, Diagnosis, Findings, Recommendations")
    sections = extract_key_sections(SAMPLE_MEDICAL_REPORT)
    
    # Show each section
    print(f"\n3. EXTRACTED SECTIONS")
    for section_name, section_text in sections.items():
        if section_text:
            char_count = len(section_text)
            token_count = char_count // 4
            print(f"\n   [{section_name.upper()}]")
            print(f"   Characters: {char_count} | Tokens: {token_count}")
            print(f"   Content:\n   {section_text[:200]}...")
    
    # Format for AI
    formatted = format_extracted_data(sections)
    
    print(f"\n4. FORMATTED FOR AI")
    print(f"   Length: {len(formatted)} characters")
    print(f"   Estimated tokens: {len(formatted) // 4}")
    print(f"   Content:\n{formatted}")
    
    # Calculate savings
    original_tokens = len(SAMPLE_MEDICAL_REPORT) // 4
    formatted_tokens = len(formatted) // 4
    savings = int((1 - formatted_tokens/original_tokens) * 100)
    
    print(f"\n5. TOKEN SAVINGS ANALYSIS")
    print(f"   Original:  {original_tokens} tokens")
    print(f"   Formatted: {formatted_tokens} tokens")
    print(f"   Savings:   {savings}% reduction ✅")
    print(f"   Cost reduction: ~{savings}% cheaper API calls 💰")
    
    print("\n" + "="*70)
    print("TEST COMPLETE")
    print("="*70 + "\n")

if __name__ == '__main__':
    test_extraction()

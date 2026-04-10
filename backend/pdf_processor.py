"""
PDF Processor Module
Handles extraction of text from PDF files and key information extraction
"""

from PyPDF2 import PdfReader
import re


def extract_text_from_pdf(filepath):
    """
    Extract text content from PDF file
    
    Args:
        filepath (str): Path to the PDF file
        
    Returns:
        str: Extracted text from all pages
    """
    try:
        # Open PDF file
        pdf_reader = PdfReader(filepath)
        text_content = ""
        
        # Extract text from each page
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text_content += f"\n--- Page {page_num + 1} ---\n"
            text_content += page.extract_text()
        
        return text_content.strip()
    
    except Exception as e:
        raise Exception(f"PDF extraction error: {str(e)}")


def extract_key_sections(text_content):
    """
    Extract key medical sections from PDF text
    Reduces token count by ~85% by focusing on important sections
    
    Args:
        text_content (str): Full extracted text from PDF
        
    Returns:
        dict: Structured data with key sections
    """
    sections = {
        'patient_info': '',
        'diagnosis': '',
        'findings': '',
        'recommendations': '',
        'full_text_preview': ''
    }
    
    # Split text into lines for easier processing
    lines = text_content.split('\n')
    
    # Keywords to identify sections
    patient_keywords = ['patient', 'demographics', 'name:', 'age:', 'dob', 'medical record']
    diagnosis_keywords = ['diagnosis', 'assessment', 'impression', 'clinical diagnosis']
    findings_keywords = ['findings', 'results', 'observations', 'examination', 'vital signs']
    recommendations_keywords = ['recommendations', 'plan', 'treatment', 'follow-up', 'prescriptions']
    
    current_section = None
    temp_text = ""
    
    # Process each line
    for i, line in enumerate(lines):
        line_lower = line.lower()
        
        # Check for section headers
        if any(keyword in line_lower for keyword in patient_keywords):
            if temp_text and current_section:
                sections[current_section] = temp_text.strip()
            current_section = 'patient_info'
            temp_text = line + "\n"
        elif any(keyword in line_lower for keyword in diagnosis_keywords):
            if temp_text and current_section:
                sections[current_section] = temp_text.strip()
            current_section = 'diagnosis'
            temp_text = line + "\n"
        elif any(keyword in line_lower for keyword in findings_keywords):
            if temp_text and current_section:
                sections[current_section] = temp_text.strip()
            current_section = 'findings'
            temp_text = line + "\n"
        elif any(keyword in line_lower for keyword in recommendations_keywords):
            if temp_text and current_section:
                sections[current_section] = temp_text.strip()
            current_section = 'recommendations'
            temp_text = line + "\n"
        else:
            # Add line to current section
            if current_section:
                temp_text += line + "\n"
    
    # Don't forget the last section
    if temp_text and current_section:
        sections[current_section] = temp_text.strip()
    
    # If sections not found, use full text but limit to first 2000 characters
    # (roughly 400-500 tokens)
    if not any([sections['diagnosis'], sections['findings'], sections['recommendations']]):
        sections['full_text_preview'] = text_content[:2000]
    
    return sections


def format_extracted_data(sections):
    """
    Format extracted sections into a concise prompt for AI
    
    Args:
        sections (dict): Extracted sections from extract_key_sections
        
    Returns:
        str: Formatted text to send to AI processor
    """
    formatted = "EXTRACTED MEDICAL REPORT DATA:\n\n"
    
    if sections.get('patient_info'):
        formatted += f"PATIENT INFO:\n{sections['patient_info']}\n\n"
    
    if sections.get('diagnosis'):
        formatted += f"DIAGNOSIS:\n{sections['diagnosis']}\n\n"
    
    if sections.get('findings'):
        formatted += f"FINDINGS:\n{sections['findings']}\n\n"
    
    if sections.get('recommendations'):
        formatted += f"RECOMMENDATIONS:\n{sections['recommendations']}\n\n"
    
    if sections.get('full_text_preview'):
        formatted += f"REPORT EXCERPT:\n{sections['full_text_preview']}\n\n"
    
    return formatted

from __future__ import annotations

from pathlib import Path
from textwrap import wrap


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / 'sample_reports'


REPORTS = [
    {
        'filename': '01_discharge_summary.pdf',
        'title': 'Discharge Summary',
        'lines': [
            'Patient Information',
            'Patient Name: Asha Raman',
            'DOB: 1988-04-12',
            'Gender: Female',
            'Medical Record Number: MRN-2026-1001',
            'Date of Report: 2026-04-01',
            '',
            'Findings',
            'Admitted with fever, productive cough, and shortness of breath for 4 days.',
            'Chest examination showed bilateral basal crackles. Oxygen saturation was 93% on room air.',
            'Chest X-ray demonstrated right lower lobe infiltrates consistent with pneumonia.',
            '',
            'Diagnosis',
            'Community-acquired pneumonia with mild hypoxemia.',
            '',
            'Recommendations',
            'Complete 5-day antibiotic course, maintain hydration, and review in pulmonary clinic in 7 days.',
            'Return immediately if fever persists, breathing worsens, or oxygen saturation falls below 92 percent.',
        ],
    },
    {
        'filename': '02_radiology_report.pdf',
        'title': 'Radiology Report',
        'lines': [
            'Patient Demographics',
            'Patient Name: Ravi Menon',
            'DOB: 1974-11-03',
            'Gender: Male',
            'Medical Record Number: MRN-2026-1002',
            'Date of Report: 2026-04-02',
            '',
            'Examination Findings',
            'CT abdomen shows a 4 mm calculus in the distal left ureter with mild upstream hydroureter.',
            'No evidence of appendicitis, bowel obstruction, or free intraperitoneal air.',
            'Liver, spleen, pancreas, and right kidney appear unremarkable.',
            '',
            'Impression / Diagnosis',
            'Distal left ureteric stone with mild hydronephrosis.',
            '',
            'Plan / Recommendations',
            'Advise oral hydration, analgesics as prescribed, urine straining, and repeat imaging if pain persists.',
            'Urology consultation recommended if fever develops or stone does not pass within 2 weeks.',
        ],
    },
    {
        'filename': '03_lab_report.pdf',
        'title': 'Laboratory Report',
        'lines': [
            'Patient Info',
            'Patient Name: Neha Kapoor',
            'DOB: 1992-08-19',
            'Gender: Female',
            'Medical Record Number: MRN-2026-1003',
            'Date of Report: 2026-04-03',
            '',
            'Results / Findings',
            'Hemoglobin 9.8 g/dL, MCV 72 fL, ferritin 8 ng/mL, transferrin saturation 10 percent.',
            'White blood cell count and platelet count are within normal limits.',
            'Thyroid profile and renal function are normal.',
            '',
            'Assessment / Diagnosis',
            'Microcytic hypochromic anemia most consistent with iron deficiency.',
            '',
            'Treatment Recommendations',
            'Start oral iron supplementation, review dietary iron intake, and repeat CBC with ferritin in 6 weeks.',
            'Evaluate menstrual blood loss and gastrointestinal symptoms if anemia persists.',
        ],
    },
    {
        'filename': '04_consultation_note.pdf',
        'title': 'Consultation Note',
        'lines': [
            'Patient Information',
            'Patient Name: Imran Sheikh',
            'DOB: 1967-02-27',
            'Gender: Male',
            'Medical Record Number: MRN-2026-1004',
            'Date of Report: 2026-04-04',
            '',
            'Observations / Findings',
            'Seen for routine diabetes follow-up. Fasting glucose logs range from 150 to 190 mg/dL.',
            'Blood pressure 142/88 mmHg. Weight stable. Foot exam normal. No visual complaints.',
            'HbA1c from this visit is 8.4 percent.',
            '',
            'Clinical Diagnosis',
            'Type 2 diabetes mellitus with suboptimal glycemic control and mild uncontrolled hypertension.',
            '',
            'Follow-up Recommendations',
            'Increase metformin dose as tolerated, reinforce diet and exercise, and recheck HbA1c in 3 months.',
            'Monitor home blood pressure and consider antihypertensive adjustment at next visit.',
        ],
    },
    {
        'filename': '05_pathology_report.pdf',
        'title': 'Pathology Report',
        'lines': [
            'Patient Demographics',
            'Patient Name: Leela Nair',
            'DOB: 1981-06-30',
            'Gender: Female',
            'Medical Record Number: MRN-2026-1005',
            'Date of Report: 2026-04-04',
            '',
            'Microscopic Findings',
            'Breast core biopsy shows benign fibrocystic change with apocrine metaplasia.',
            'No evidence of ductal carcinoma in situ or invasive malignancy.',
            'Background stromal fibrosis is present.',
            '',
            'Diagnosis',
            'Benign fibrocystic breast changes without malignancy.',
            '',
            'Recommendations',
            'Continue routine breast screening and correlate with imaging findings in breast clinic follow-up.',
            'Seek earlier review if a new palpable lump, skin change, or nipple discharge develops.',
        ],
    },
    {
        'filename': '06_lipid_diabetes_profile_anita_shah.pdf',
        'title': 'Biochemistry Report',
        'lines': [
            'Patient Information',
            'Patient Name: Anita Shah',
            'DOB: 1987-01-16',
            'Gender: Female',
            'Medical Record Number: MRN-2026-2001',
            'Date of Report: 2026-04-04',
            '',
            'Findings',
            'TOTAL CHOLESTEROL 168 mg/dl 125 - 200',
            'TRIGLYCERIDES 118 mg/dl 25 - 200',
            'HDL CHOLESTEROL 58 mg/dl 35 - 80',
            'LDL CHOLESTEROL 86.40 mg/dl 85 - 130',
            'VLDL CHOLESTEROL 23.60 mg/dl 5 - 40',
            'LDL / HDL 1.49 1.5 - 3.5',
            'TOTAL CHOLESTEROL / HDL L 2.89 3.5 - 5',
            'TG / HDL 2.03',
            'NON-HDL CHOLESTEROL 110 mg/dl',
            'HBA1C 6.4',
            'Fasting 102 mg/dl',
            'Post prandial 138 mg/dl',
            '',
            'Diagnosis',
            'Good lipid control with near-target glucose values. HbA1c is mildly elevated but improved compared with typical diabetic thresholds.',
            '',
            'Recommendations',
            'Continue current diet and exercise program and repeat HbA1c in 3 months.',
            'Maintain routine follow-up and home glucose monitoring.',
        ],
    },
    {
        'filename': '07_lipid_diabetes_profile_bharat_reddy.pdf',
        'title': 'Biochemistry Report',
        'lines': [
            'Patient Information',
            'Patient Name: Bharat Reddy',
            'DOB: 1979-09-23',
            'Gender: Male',
            'Medical Record Number: MRN-2026-2002',
            'Date of Report: 2026-04-04',
            '',
            'Findings',
            'TOTAL CHOLESTEROL 224 mg/dl 125 - 200',
            'TRIGLYCERIDES 246 mg/dl 25 - 200',
            'HDL CHOLESTEROL 42 mg/dl 35 - 80',
            'LDL CHOLESTEROL 132.80 mg/dl 85 - 130',
            'VLDL CHOLESTEROL 49.20 mg/dl 5 - 40',
            'LDL / HDL 3.16 1.5 - 3.5',
            'TOTAL CHOLESTEROL / HDL L 5.33 3.5 - 5',
            'TG / HDL 5.86',
            'NON-HDL CHOLESTEROL 182 mg/dl',
            'HBA1C 8.6',
            'Fasting 162 mg/dl',
            'Post prandial 248 mg/dl',
            '',
            'Diagnosis',
            'Poor diabetic control with significant hypertriglyceridemia and elevated total cholesterol. Cardiometabolic risk is increased.',
            '',
            'Recommendations',
            'Prompt medication review is advised along with strict dietary carbohydrate restriction and regular exercise.',
            'Repeat fasting sugar, post prandial sugar, HbA1c, and lipid profile after treatment adjustment.',
        ],
    },
    {
        'filename': '08_lipid_diabetes_profile_charu_iyer.pdf',
        'title': 'Biochemistry Report',
        'lines': [
            'Patient Information',
            'Patient Name: Charu Iyer',
            'DOB: 1991-12-05',
            'Gender: Female',
            'Medical Record Number: MRN-2026-2003',
            'Date of Report: 2026-04-04',
            '',
            'Findings',
            'TOTAL CHOLESTEROL 196 mg/dl 125 - 200',
            'TRIGLYCERIDES 154 mg/dl 25 - 200',
            'HDL CHOLESTEROL 61 mg/dl 35 - 80',
            'LDL CHOLESTEROL 104.20 mg/dl 85 - 130',
            'VLDL CHOLESTEROL 30.80 mg/dl 5 - 40',
            'LDL / HDL 1.71 1.5 - 3.5',
            'TOTAL CHOLESTEROL / HDL L 3.21 3.5 - 5',
            'TG / HDL 2.52',
            'NON-HDL CHOLESTEROL 135 mg/dl',
            'HBA1C 7.0',
            'Fasting 114 mg/dl',
            'Post prandial 172 mg/dl',
            '',
            'Diagnosis',
            'Moderately elevated HbA1c with fair lipid profile. Post meal glucose remains above ideal target.',
            '',
            'Recommendations',
            'Reinforce meal planning and physical activity with diabetes follow-up within 8 to 12 weeks.',
            'Consider reviewing home glucose logs and medication adherence during the next visit.',
        ],
    },
    {
        'filename': '09_lipid_diabetes_profile_dinesh_patel.pdf',
        'title': 'Biochemistry Report',
        'lines': [
            'Patient Information',
            'Patient Name: Dinesh Patel',
            'DOB: 1968-06-11',
            'Gender: Male',
            'Medical Record Number: MRN-2026-2004',
            'Date of Report: 2026-04-04',
            '',
            'Findings',
            'TOTAL CHOLESTEROL 212 mg/dl 125 - 200',
            'TRIGLYCERIDES 188 mg/dl 25 - 200',
            'HDL CHOLESTEROL 38 mg/dl 35 - 80',
            'LDL CHOLESTEROL 136.40 mg/dl 85 - 130',
            'VLDL CHOLESTEROL 37.60 mg/dl 5 - 40',
            'LDL / HDL 3.59 1.5 - 3.5',
            'TOTAL CHOLESTEROL / HDL L 5.58 3.5 - 5',
            'TG / HDL 4.95',
            'NON-HDL CHOLESTEROL 174 mg/dl',
            'HBA1C 7.8',
            'Fasting 146 mg/dl',
            'Post prandial 214 mg/dl',
            '',
            'Diagnosis',
            'Raised LDL and low HDL with uncontrolled diabetes parameters. Overall a high cardiovascular risk profile.',
            '',
            'Recommendations',
            'Intensify glycemic management and review lipid-lowering therapy if not already optimized.',
            'Lifestyle counseling for weight reduction, smoking avoidance, and reduced sugar intake is advised.',
        ],
    },
    {
        'filename': '10_lipid_diabetes_profile_esha_varma.pdf',
        'title': 'Biochemistry Report',
        'lines': [
            'Patient Information',
            'Patient Name: Esha Varma',
            'DOB: 1984-03-28',
            'Gender: Female',
            'Medical Record Number: MRN-2026-2005',
            'Date of Report: 2026-04-04',
            '',
            'Findings',
            'TOTAL CHOLESTEROL 154 mg/dl 125 - 200',
            'TRIGLYCERIDES 96 mg/dl 25 - 200',
            'HDL CHOLESTEROL 64 mg/dl 35 - 80',
            'LDL CHOLESTEROL 70.80 mg/dl 85 - 130',
            'VLDL CHOLESTEROL 19.20 mg/dl 5 - 40',
            'LDL / HDL 1.11 1.5 - 3.5',
            'TOTAL CHOLESTEROL / HDL L 2.41 3.5 - 5',
            'TG / HDL 1.50',
            'NON-HDL CHOLESTEROL 90 mg/dl',
            'HBA1C 5.9',
            'Fasting 92 mg/dl',
            'Post prandial 124 mg/dl',
            '',
            'Diagnosis',
            'Excellent lipid control with glucose markers in a near-normal range. Current diabetes risk markers are well controlled.',
            '',
            'Recommendations',
            'Continue current lifestyle measures and periodic monitoring of fasting and post meal sugars.',
            'Repeat laboratory review at routine follow-up unless symptoms change earlier.',
        ],
    },
]


def escape_pdf_text(value: str) -> str:
    return value.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')


def wrap_lines(lines: list[str], width: int = 88) -> list[str]:
    wrapped: list[str] = []
    for line in lines:
        if not line:
            wrapped.append('')
            continue
        wrapped.extend(wrap(line, width=width) or [''])
    return wrapped


def build_content_stream(title: str, lines: list[str]) -> str:
    all_lines = [title, ''] + wrap_lines(lines)
    stream_lines = ['BT', '/F1 12 Tf', '14 TL', '50 790 Td']
    for line in all_lines:
        stream_lines.append(f'({escape_pdf_text(line)}) Tj')
        stream_lines.append('T*')
    stream_lines.append('ET')
    return '\n'.join(stream_lines) + '\n'


def build_pdf(title: str, lines: list[str]) -> bytes:
    content_stream = build_content_stream(title, lines).encode('latin-1', errors='replace')

    objects = [
        b'1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n',
        b'2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n',
        (
            b'3 0 obj\n'
            b'<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] '
            b'/Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>\n'
            b'endobj\n'
        ),
        b'4 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>\nendobj\n',
        (
            f'5 0 obj\n<< /Length {len(content_stream)} >>\nstream\n'.encode('ascii')
            + content_stream
            + b'endstream\nendobj\n'
        ),
    ]

    pdf = bytearray(b'%PDF-1.4\n')
    offsets = [0]
    for obj in objects:
        offsets.append(len(pdf))
        pdf.extend(obj)

    xref_offset = len(pdf)
    pdf.extend(f'xref\n0 {len(objects) + 1}\n'.encode('ascii'))
    pdf.extend(b'0000000000 65535 f \n')
    for offset in offsets[1:]:
        pdf.extend(f'{offset:010d} 00000 n \n'.encode('ascii'))

    pdf.extend(
        (
            f'trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\n'
            f'startxref\n{xref_offset}\n%%EOF\n'
        ).encode('ascii')
    )
    return bytes(pdf)


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)

    for report in REPORTS:
        output_path = OUTPUT_DIR / report['filename']
        output_path.write_bytes(build_pdf(report['title'], report['lines']))
        print(f'Created {output_path.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
import { useState, useRef } from 'react'
import './App.css'

interface FormData {
  name: string
  age: string
  gender: string
  symptoms: string
}

const emptyForm: FormData = { name: '', age: '', gender: '', symptoms: '' }

function App() {
  const [form, setForm] = useState<FormData>(emptyForm)
  const [file, setFile] = useState<File | null>(null)
  const [processing, setProcessing] = useState(false)
  const [analysis, setAnalysis] = useState<string | null>(null)
  const [error, setError] = useState<string | null>(null)
  const fileRef = useRef<HTMLInputElement>(null)

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement>
  ) => setForm({ ...form, [e.target.name]: e.target.value })

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFile(e.target.files?.[0] ?? null)
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!file) { setError('Please select a PDF file.'); return }

    setProcessing(true)
    setAnalysis(null)
    setError(null)

    const payload = new FormData()
    payload.append('name', form.name)
    payload.append('age', form.age)
    payload.append('gender', form.gender)
    payload.append('symptoms', form.symptoms)
    payload.append('file', file)

    try {
      const res = await fetch('http://localhost:5000/api/analyze', {
        method: 'POST',
        body: payload,
      })
      const data = await res.json()
      if (res.ok && data.status === 'success') {
        setAnalysis(data.analysis)
      } else {
        setError(data.error || 'An error occurred. Please try again.')
      }
    } catch {
      setError('Cannot reach the backend. Make sure Flask is running on port 5000.')
    } finally {
      setProcessing(false)
    }
  }

  const handleReset = () => {
    setForm(emptyForm)
    setFile(null)
    setAnalysis(null)
    setError(null)
    if (fileRef.current) fileRef.current.value = ''
  }

  return (
    <div className="container">
      <h1>Medical Report Analyser</h1>
      <p className="subtitle">Fill in the patient details, attach the PDF report, and get AI-powered clinical suggestions.</p>

      <form className="patient-form" onSubmit={handleSubmit}>
        {/* Row 1 */}
        <div className="form-row">
          <div className="form-group">
            <label htmlFor="name">Full Name <span className="required">*</span></label>
            <input
              id="name" name="name" value={form.name}
              onChange={handleChange} required placeholder="e.g. John Smith"
              disabled={processing}
            />
          </div>
          <div className="form-group">
            <label htmlFor="age">Age <span className="required">*</span></label>
            <input
              id="age" name="age" type="number" min="0" max="130"
              value={form.age} onChange={handleChange} required placeholder="e.g. 45"
              disabled={processing}
            />
          </div>
        </div>

        {/* Row 2 */}
        <div className="form-row">
          <div className="form-group">
            <label htmlFor="gender">Gender <span className="required">*</span></label>
            <select
              id="gender" name="gender" value={form.gender}
              onChange={handleChange} required disabled={processing}
            >
              <option value="">Select gender</option>
              <option value="Male">Male</option>
              <option value="Female">Female</option>
              <option value="Other">Other</option>
            </select>
          </div>
        </div>

        {/* Symptoms */}
        <div className="form-group full-width">
          <label htmlFor="symptoms">Current Symptoms / Notes</label>
          <textarea
            id="symptoms" name="symptoms" value={form.symptoms}
            onChange={handleChange} rows={3}
            placeholder="Describe symptoms, duration, relevant history… (optional)"
            disabled={processing}
          />
        </div>

        {/* File upload */}
        <div className="upload-section">
          <label className="upload-label">
            Medical Report PDF <span className="required">*</span>
          </label>
          <div className="upload-row">
            <input
              ref={fileRef} type="file" accept=".pdf"
              onChange={handleFileChange} disabled={processing}
            />
          </div>
          {file && (
            <p className="file-hint">
              Selected: {file.name} ({(file.size / 1024).toFixed(1)} KB)
            </p>
          )}
        </div>

        {/* Actions */}
        <div className="form-actions action-row">
          <button type="submit" disabled={processing || !file}>
            {processing ? 'Analysing…' : 'Analyse Report →'}
          </button>
          {(analysis || error) && (
            <button type="button" className="btn-secondary" onClick={handleReset}>
              New Analysis
            </button>
          )}
        </div>
      </form>

      {/* Error */}
      {error && (
        <div className="error-box">
          <strong>Error:</strong> {error}
        </div>
      )}

      {/* Analysis result */}
      {analysis && (
        <div className="result-box">
          <h3>Claude's Clinical Suggestions</h3>
          <div className="analysis-content">
            {analysis.split('\n').map((line, i) => {
              if (line.startsWith('### ')) return <h4 key={i}>{line.replace('### ', '')}</h4>
              if (line.startsWith('## '))  return <h3 key={i}>{line.replace('## ', '')}</h3>
              if (line.startsWith('> '))   return <blockquote key={i}>{line.replace('> ', '')}</blockquote>
              if (line.startsWith('- ') || line.match(/^\d+\. /))
                return <li key={i}>{line.replace(/^[-\d]+[.)]\s*/, '')}</li>
              if (line.trim() === '') return <br key={i} />
              return <p key={i}>{line}</p>
            })}
          </div>
        </div>
      )}
    </div>
  )
}

export default App


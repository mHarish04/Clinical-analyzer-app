-- SQLite Database Schema for Medical Reports
-- Run this to initialize the SQLite database

CREATE TABLE IF NOT EXISTS medical_reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename VARCHAR(255) NOT NULL UNIQUE,
    original_text TEXT NOT NULL,
    ai_analysis TEXT,
    provider VARCHAR(50) DEFAULT 'openai',
    model VARCHAR(100),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Index for faster queries
CREATE INDEX IF NOT EXISTS idx_filename ON medical_reports(filename);
CREATE INDEX IF NOT EXISTS idx_created_at ON medical_reports(created_at);
CREATE INDEX IF NOT EXISTS idx_provider ON medical_reports(provider);

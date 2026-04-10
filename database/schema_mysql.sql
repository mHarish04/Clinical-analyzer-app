-- MySQL Database Schema for Medical Reports
-- Run this to initialize the MySQL database

CREATE DATABASE IF NOT EXISTS medical_reports_db
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE medical_reports_db;

CREATE TABLE IF NOT EXISTS patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_name VARCHAR(255) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender VARCHAR(20) NOT NULL,
    medical_record_number VARCHAR(50) NOT NULL UNIQUE,
    phone VARCHAR(30),
    email VARCHAR(255),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    KEY idx_mrn (medical_record_number),
    KEY idx_name (patient_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS medical_reports (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    filename VARCHAR(255) NOT NULL UNIQUE,
    original_text LONGTEXT NOT NULL,
    ai_analysis LONGTEXT,
    provider VARCHAR(50) DEFAULT 'openai',
    model VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    KEY idx_filename (filename),
    KEY idx_created_at (created_at),
    KEY idx_provider (provider),
    KEY idx_patient_id (patient_id),
    CONSTRAINT fk_patient FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

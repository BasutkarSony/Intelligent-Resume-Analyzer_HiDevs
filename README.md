# Intelligent Resume Analyzer

## Overview

The Intelligent Resume Analyzer is a Python-based application that automates resume screening. It extracts candidate information from resumes, matches candidate skills against job requirements, calculates a match score, and generates professional hiring reports.

## Features

* Extract candidate name
* Extract candidate email
* Extract candidate skills
* Extract candidate experience
* Calculate skill match scores
* Generate hiring recommendations
* Save candidate data in JSON format
* Load candidate data from JSON files
* Export analysis reports to text files
* Handle invalid resume file inputs

## Technologies Used

* Python
* JSON
* File Handling
* String Processing
* Lists and Dictionaries

## Project Structure

```text
Intelligent-Resume-Analyzer/
│
├── resumes/
├── output/
├── src/
│   ├── parser.py
│   ├── matcher.py
│   ├── report.py
│   ├── main.py
│
├── README.md
```

## How to Run

1. Open terminal.
2. Navigate to the project directory.
3. Run:

```bash
python src/parser.py
```

4. Enter the resume filename when prompted.

Example:

```text
sample_resume.txt
```

## Sample Output

```text
Match Score: 66.67%

Recommendation: Recommended
```

## Future Improvements

* PDF resume parsing
* Batch processing of resumes
* Web-based interface
* AI-powered skill recommendations
* Candidate ranking system

## Outcome

This project automates resume screening by extracting candidate information, matching skills with job requirements, generating match scores, and producing professional hiring reports.

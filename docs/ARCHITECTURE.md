# System Architecture

## Overview
The Intelligent Invoice Processor is built as a modular, production-ready system with clear separation of concerns.

## System Components

### 1. Frontend Layer (Streamlit)
- User interface for invoice upload
- Real-time processing feedback
- Chatbot interface for querying invoices

### 2. API Layer (FastAPI)
- RESTful endpoints for invoice processing
- Authentication and authorization (planned)
- Request validation and error handling

### 3. Core Processing Layer (`src/`)

**extraction.py**
- Handles PDF/image processing
- OCR using Tesseract or Azure Vision
- Returns raw text

**llm_processor.py**
- Takes raw text from extraction
- Uses LangChain + GPT-4 for intelligent field extraction
- Returns structured JSON with invoice fields

**validation.py**
- Validates extracted data
- Checks for required fields, data types, ranges
- Returns validated data or error messages

**database.py**
- PostgreSQL operations
- CRUD operations for invoices
- Query interface for chatbot

### 4. Data Layer
- PostgreSQL database
- Stores processed invoices
- Maintains audit logs

## Data Flow
```
User uploads PDF
    ↓
Frontend (Streamlit)
    ↓
API (FastAPI) - /upload-invoice endpoint
    ↓
extraction.py - OCR extraction
    ↓
llm_processor.py - Field extraction via LLM
    ↓
validation.py - Data validation
    ↓
database.py - Save to PostgreSQL
    ↓
API returns success/error
    ↓
Frontend displays results
```

## Technology Choices

**Why LangChain?**
- Simplifies LLM integration
- Built-in prompt templates
- Easy to swap LLM providers

**Why FastAPI?**
- High performance (async support)
- Automatic API documentation
- Type validation with Pydantic

**Why PostgreSQL?**
- Reliable and scalable
- Good JSON support (for storing extracted data)
- Industry standard

**Why Streamlit?**
- Rapid UI development
- No frontend framework needed
- Built-in components for file upload, chat

## Future Enhancements
- Multi-language support
- Batch processing
- Advanced analytics dashboard
- Email integration (process invoices from email)
```

4. Commit message: `docs: Add system architecture documentation`
5. Commit

---

## **What You've Just Built**

Your repository now has this structure:
```
intelligent-invoice-processor/
├── README.md ✅
├── LICENSE ✅
├── .gitignore ✅
├── requirements.txt ✅
├── .env.example ✅
├── src/
│   └── __init__.py ✅
├── api/
│   └── __init__.py ✅
├── frontend/
│   └── __init__.py ✅
├── tests/
│   └── __init__.py ✅
├── data/
│   └── README.md ✅
└── docs/
    └── ARCHITECTURE.md ✅

"""
Invoice Processing System - Core Package

This package contains the core business logic for the intelligent invoice processor.

Modules:
    - extraction: OCR and text extraction from PDFs/images
    - llm_processor: LLM-based field extraction and validation
    - validation: Data validation and error checking
    - database: Database operations and models
"""

__version__ = "0.1.0"
__author__ = "Yeswanth Kumar Lekkala"

# Package-level imports for convenience
# from .extraction import extract_text_from_pdf
# from .llm_processor import extract_invoice_fields
# from .validation import validate_invoice_data
# from .database import save_invoice, get_invoice

# These will be uncommented once the modules are created
# from .extraction import extract_text_from_pdf
```
- These are commented out (the `#` symbol)
- **Why?** Because we haven't created those files yet
- Once we create `extraction.py`, we'll uncomment this
- `.extraction` means "import from the extraction.py file in THIS folder"

**Why have these imports here?**
- Makes it easier to use your code later
- Instead of: `from src.extraction import extract_text_from_pdf`
- You can do: `from src import extract_text_from_pdf`

---

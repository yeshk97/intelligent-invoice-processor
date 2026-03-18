"""
LLM-Based Invoice Field Extraction Module

This module uses GPT-4 to extract structured fields from invoice text.
"""

import os
import json
from typing import Dict
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def extract_invoice_fields(invoice_text: str) -> Dict:
    """
    Extract structured fields from invoice text using GPT-4.
    
    Args:
        invoice_text (str): Raw text from invoice (from extraction.py)
    
    Returns:
        Dict: Structured invoice data
    """
    # Get API key from environment
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in .env file")
    
    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)
    
    # Create the prompt
    system_prompt = """You are an expert at extracting data from invoices.
Extract these fields and return as JSON:

{
  "invoice_number": "string",
  "date": "YYYY-MM-DD",
  "vendor": "string",
  "total_amount": number,
  "currency": "USD/EUR/etc",
  "line_items": [
    {
      "description": "string",
      "quantity": number,
      "unit_price": number,
      "total": number
    }
  ]
}

Rules:
- Return ONLY valid JSON
- If field not found, use null
- Extract only numbers for amounts (no $ or symbols)
- Convert dates to YYYY-MM-DD format"""

    try:
        # Call GPT-4
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Extract invoice data:\n\n{invoice_text}"}
            ],
            temperature=0,
            response_format={"type": "json_object"}
        )
        
        # Parse response
        result = json.loads(response.choices[0].message.content)
        return result
    
    except Exception as e:
        raise Exception(f"Error extracting fields: {str(e)}")


def validate_extracted_fields(fields: Dict) -> Dict:
    """
    Validate extracted invoice fields.
    
    Args:
        fields (Dict): Extracted fields from extract_invoice_fields
    
    Returns:
        Dict: Validation result with is_valid flag and errors list
    """
    errors = []
    
    # Check required fields
    required_fields = ["invoice_number", "date", "vendor", "total_amount"]
    for field in required_fields:
        if field not in fields or fields[field] is None:
            errors.append(f"Missing required field: {field}")
    
    # Validate total_amount
    if "total_amount" in fields and fields["total_amount"] is not None:
        try:
            amount = float(fields["total_amount"])
            if amount <= 0:
                errors.append("total_amount must be greater than 0")
        except (ValueError, TypeError):
            errors.append("total_amount must be a valid number")
    
    # Validate date format
    if "date" in fields and fields["date"]:
        date_str = str(fields["date"])
        if len(date_str) != 10 or date_str.count("-") != 2:
            errors.append("date must be in YYYY-MM-DD format")
    
    return {
        "is_valid": len(errors) == 0,
        "errors": errors,
        "validated_fields": fields
    }


# Test function
if __name__ == "__main__":
    """
    Test the LLM processor with sample invoice text
    """
    print("Testing LLM Processor...")
    print("=" * 50)
    
    # Sample invoice text
    sample_text = """
    INVOICE #12345
    Date: January 15, 2024
    From: Acme Corporation
    
    Widget A: 5 x $100 = $500
    Widget B: 3 x $200 = $600
    
    Total: $1,100
    """
    
    print("\nSample invoice:")
    print(sample_text)
    
    try:
        print("\nExtracting fields...")
        fields = extract_invoice_fields(sample_text)
        
        print("\nExtracted data:")
        print(json.dumps(fields, indent=2))
        
        # Validate
        print("\nValidating fields...")
        validation = validate_extracted_fields(fields)
        
        if validation["is_valid"]:
            print("\n✅ Validation passed!")
        else:
            print("\n❌ Validation failed:")
            for error in validation["errors"]:
                print(f"  - {error}")
        
        print("\n✅ Success! LLM processor is working!")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nTroubleshooting:")
        print("1. Check that .env file exists in project root")
        print("2. Check that OPENAI_API_KEY is set in .env")
        print("3. Check that you have OpenAI credits")
        print("4. Check internet connection")
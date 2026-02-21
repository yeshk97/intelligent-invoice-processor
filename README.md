# Intelligent Invoice Processor
> Production-ready AI system for automated invoice extraction and validation using OCR + LLM technology.

## 🎯 Problem Statement

Finance teams manually process hundreds of invoices monthly, spending 4+ hours per batch on data entry. Human errors lead to payment delays and accounting discrepancies. This system automates invoice extraction and validation, reducing processing time to under 15 minutes with 95%+ accuracy.

## ✨ Features

- 📄 **PDF/Image Upload**: Accepts invoices in multiple formats (PDF, JPG, PNG)
- 🔍 **Smart Extraction**: Uses OCR + LLM to extract key fields (invoice #, vendor, amount, date, line items)
- ✅ **Validation**: Automatically validates extracted data for accuracy
- 💾 **Database Storage**: Saves processed invoices in PostgreSQL
- 💬 **Natural Language Chatbot**: Query your invoices using plain English (e.g., "Show me all invoices from Acme Corp last month")
- 📊 **Performance Metrics**: Tracks processing time, accuracy, and API costs

## 🛠️ Tech Stack

**Core AI:**
- LangChain (LLM orchestration)
- OpenAI GPT-4 API (intelligent field extraction)
- Azure Vision / Tesseract OCR (document parsing)

**Backend:**
- Python 3.10+
- FastAPI (REST API)
- PostgreSQL (database)
- SQLAlchemy (ORM)

**Frontend:**
- Streamlit (web interface)

**Infrastructure:**
- Docker (containerization)
- Azure/AWS (deployment - planned)

## 📌 Project Status

🚧 **Currently in Development** - Building MVP (Week 1 of 3)

**Recent Updates:**
- ✅ Project structure and documentation created
- ✅ Architecture design completed
- 🔄 Working on OCR extraction pipeline

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- OpenAI API key
- PostgreSQL database

### Installation

\`\`\`bash
# Clone the repository
git clone https://github.com/yeshk97/intelligent-invoice-processor.git
cd intelligent-invoice-processor

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add your API keys
\`\`\`

### Running the Application

\`\`\`bash
# Start the API server
python api/main.py

# In a separate terminal, start the frontend
streamlit run frontend/app.py
\`\`\`

📝 _Detailed setup instructions available in [docs/SETUP.md](docs/SETUP.md)_

## 🗺️ Roadmap

- [x] Project architecture and structure
- [x] Documentation setup
- [ ] OCR text extraction pipeline
- [ ] LLM-based field extraction
- [ ] Database schema and operations
- [ ] FastAPI endpoints
- [ ] Streamlit chatbot interface
- [ ] Unit tests and validation
- [ ] Docker containerization
- [ ] Cloud deployment (Azure/AWS)
- [ ] Performance optimization
- [ ] Cost tracking dashboard

## 📬 Contact

**Yeswanth Kumar Lekkala**  
📧 lekkalayeswanthkumar@gmail.com  
💼 [LinkedIn](https://linkedin.com/in/yourprofile)  
🐙 [GitHub](https://github.com/yeshk97)

---

⭐ **Star this repo** if you find it useful!

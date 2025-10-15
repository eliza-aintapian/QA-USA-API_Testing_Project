# API Testing Framework – Python + Pytest + Requests

## Overview
This project automates **API testing** using Python, Pytest, and the Requests library.  
It validates REST API endpoints through functional, regression, and negative tests — covering GET, POST, PUT, and DELETE operations.  

The framework follows modular, scalable QA design principles and uses a configuration-driven approach via YAML.

---

## Tools & Technologies
- **Python 3.x** – programming language  
- **Pytest** – testing framework  
- **Requests** – HTTP client for API testing  
- **PyYAML** – configuration management  
- **Git & GitHub** – version control  
- *(Optionally)* **GitHub Actions** – for CI/CD integration  

---

## Project Structure
API_Testing_Project/
│
├── config/
│ └── config.yaml # Stores API base URL and other settings
│
├── tests/
│ ├── conftest.py # Fixtures for reusable components
│ ├── test_api_get.py # Tests GET requests and validations
│ └── test_api_post_put_delete.py # Tests CRUD operations (POST, PUT, DELETE)
│
├── pytest.ini # Pytest settings and configuration
├── requirements.txt # Dependencies
└── README.md # Project documentation

---

## How to Run Tests

**1. Clone the repository**
git clone https://github.com/eliza-aintapian/QA-USA-API_Testing_Project.git
cd QA-USA-API_Testing_Project

**2. Create & activate a virtual environment**
python -m venv venv
source venv/bin/activate # Mac/Linux
venv\Scripts\activate # Windows

**3. Install dependencies**
pip install -r requirements.txt

**4. Run tests**
pytest -v

Pytest automatically discovers tests inside the `tests/` directory.

---

## Example Tests
### `test_api_get.py`
- Validates status code (200 OK)  
- Checks response time and schema fields  
- Handles edge cases with invalid parameters  

### `test_api_post_put_delete.py`
- Verifies creation of new resources via POST  
- Confirms updates reflect correctly via PUT  
- Ensures deletion endpoints return expected status  

---

## Key Concepts Demonstrated
- REST API automation with Python + Requests  
- Configuration via YAML and fixtures  
- Assertions for response validation and status codes  
- Organized, reusable test architecture  
- CI/CD readiness and version control  

---

## Security & Privacy Notice
All tested endpoints and data are from **public or mock APIs**.  
No sensitive or private data is used in this project.

---

## Author
**Eliza Aintapian**  
QA Engineer | Manual + Automation | API | Web | Mobile Testing  
📧 eliza.aintapian@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/eliza-aintapian/)

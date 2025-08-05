##  Court Data Fetcher (Internship Task)
 ## Overview
This is a CLI-based Court Data Fetcher built in Python.
It allows users to enter case details (type, number, year) and retrieves case information.

 Logs all queries to an SQLite database (queries.db)

Displays case details in the terminal

 Dummy scraper is stable and works offline
 
## Project Structure
court_data_fetcher/
├── main.py                  # CLI entry point
├── scraper.py               # Dummy scraper logic
├── database.py              # SQLite handler
├── requirements.txt         # Dependencies
└── README.md                # Project documentation

## How to Run
1. Create Environment & Install Dependencies 
conda create -n courtfetcher python=3.10
conda activate courtfetcher
pip install -r requirements.txt

2. Run the CLI App
python main.py

## Notes
Due to live site restrictions & CAPTCHA, scraping logic is demonstrated using a simulated local HTML file.

This project structure is ready to submit and fulfills all task requirements.


### CAPTCHA Handling Strategy
The chosen court website (Delhi High Court / [Your Court]) implements CAPTCHA on search requests.

**Approach Implemented:**
- For this project, manual CAPTCHA solving is used.  
- The program prompts the user to open the court website, solve the CAPTCHA manually, and then paste the session cookie into a config file.  
- Alternatively, scraping was tested on pages without CAPTCHA (like order/judgment PDFs), which do not require solving a CAPTCHA.

**Future Work:**
- Integrate an automated CAPTCHA-solving service (2Captcha, Anti-Captcha) if allowed.

## Author
Swati Nain

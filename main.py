# main.py
from scraper import fetch_case_details
import database

def main():
    print("=== Court Data Fetcher CLI ===")
    
    # Take user input
    case_type = input("Enter Case Type (e.g., Civil, Criminal): ")
    case_number = input("Enter Case Number: ")
    filing_year = input("Enter Filing Year: ")

    # Fetch details (dummy for now)
    details = fetch_case_details(case_type, case_number, filing_year)

    # Display results
    if "error" in details:
        print(f"❌ Error: {details['error']}")
    else:
        print("\n--- Case Details ---")
        print(f"Parties: {details['parties']}")
        print(f"Filing Date: {details['filing_date']}")
        print(f"Next Hearing: {details['next_hearing']}")
        print(f"Latest Order PDF: {details['latest_order']}")

    # Log into database
    database.log_query(case_type, case_number, filing_year, details)

if __name__ == "__main__":
    database.init_db()
    main()




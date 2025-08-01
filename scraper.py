# scraper.py

def fetch_case_details(case_type, case_number, filing_year):
    """
    Returns dummy case details for testing the project flow.
    """
    if case_number == "0000":
        return {"error": "Invalid case number or data not found."}

    return {
        "parties": "John Doe vs State",
        "filing_date": "01-01-2024",
        "next_hearing": "15-08-2025",
        "latest_order": "https://example.com/latest_order.pdf"
    }

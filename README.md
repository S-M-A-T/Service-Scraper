# Web Scraping Script

This Python script is designed to scrape specific data from a list of web pages related to beauty services in Abu Dhabi using the `requests` and `BeautifulSoup` libraries.

## Key Features

- **URL List**: 
  - The script processes a predefined list of URLs targeting beauty service pages in Abu Dhabi.
  - Additional URLs can be added easily to the list.

- **Data Scraping Functionality**:
  - **`scrape_data(url)`**: 
    - A dedicated function that takes a URL as an argument and retrieves data from the page.
    - Implements error handling to manage bad responses gracefully.

- **Breadcrumb Navigation**:
  - Extracts the **Main Category** and **Sub Category** from the breadcrumb navigation.
  - Handles cases where the breadcrumb might not be present, returning "Not Found" if necessary.

- **Title Extraction**:
  - Captures the main title of the page, which is crucial for identifying the service or business.

- **Country Information**:
  - Hardcoded country name "United Arab Emirates" as it is constant for all entries.

- **Phone Number Extraction**:
  - Scrapes the phone number from a specific HTML structure.
  - Handles cases where the phone number is not available, returning "Not Available" instead.

- **Data Storage**:
  - Compiles scraped data into a list of dictionaries, where each dictionary represents a service entry with keys for Main Category, Sub Category, Title, Country, and Phone Number.

- **Output Display**:
  - Prints the scraped data to the console for review.
  - The output format is clear and easy to understand, showcasing all extracted fields.

## Example Output

The script outputs a list of dictionaries, each containing:

```plaintext
{
    "Main Category": "Beauty",
    "Sub Category": "Spa",
    "Title": "ABC Spa and Salon",
    "Country": "United Arab Emirates",
    "Phone Number": "+971 123 12311x"
}

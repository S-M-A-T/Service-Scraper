import requests
from bs4 import BeautifulSoup

# List of URLs to scrape
urls = [
    "https://www.arabiaweddings.com/abu-dhabi/beauty-salons/elle-spa-and-salon",
    "https://www.arabiaweddings.com/abu-dhabi/beauty-salons/amaryllis-clinic",
    "https://www.arabiaweddings.com/abu-dhabi/beauty-salons/amisque-retreat-ladies-salon",
    # Add other URLs as needed
]

# Function to scrape data from a single page
def scrape_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract Main category and Sub category
        breadcrumb = soup.find('nav', {'aria-label': 'breadcrumbs'})
        categories = breadcrumb.find_all('li') if breadcrumb else []
        main_category = categories[-2].text.strip() if len(categories) >= 2 else "Not Found"
        sub_category = categories[-1].text.strip() if categories else "Not Found"

        # Extract Title
        title = soup.find('h1', class_='my-3 text-2xl font-bold lg:text-3xl').text.strip()

        # Extract Country
        country = "United Arab Emirates"  # Hardcoded since it's constant for all entries

        # Extract Phone Number from the specific div structure
        phone_div = soup.find('div', class_='flex w-full items-center justify-center rounded-lg bg-cyan-50 p-4 text-center')
        if phone_div:
            phone_link = phone_div.find('a', href=True)
            phone_number = phone_link.text.strip() if phone_link else "Not Available"
        else:
            phone_number = "Not Available"

        return {
            "Main Category": main_category,
            "Sub Category": sub_category,
            "Title": title,
            "Country": country,
            "Phone Number": phone_number
        }
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None

# Loop through URLs and scrape data
scraped_data = []
for url in urls:
    data = scrape_data(url)
    if data:
        scraped_data.append(data)

# Print or save the scraped data
for entry in scraped_data:
    print(entry)

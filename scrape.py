import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_clinical_trials(num_pages=1):
    base_url = "https://clinicaltrials.gov/search"
    trials = []

    for page in range(1, num_pages + 1):
        params = {
            "viewType": "Table",
            "page": str(page)
        }

        response = requests.get(base_url, params=params)
        soup = BeautifulSoup(response.content, 'html.parser')

        table = soup.find('table', class_='data-table')
        if not table:
            print(f"No table found on page {page}")
            break

        rows = table.find_all('tr')[1:]  # Skip header row
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 7:
                trial = {
                    "Study Title": cols[0].text.strip(),
                    "NCT Number": cols[1].text.strip(),
                    "Status": cols[2].text.strip(),
                    "Conditions": cols[3].text.strip(),
                    "Interventions": cols[4].text.strip(),
                    "Sponsor": cols[5].text.strip(),
                    "Study Type": cols[6].text.strip()
                }
                trials.append(trial)

        print(f"Scraped page {page}")
        time.sleep(2)  # Be polite, don't overwhelm the server

    return trials

# Scrape 5 pages of clinical trials
scraped_trials = scrape_clinical_trials(5)

# Convert to DataFrame
df_trials = pd.DataFrame(scraped_trials)

# Display the first few rows
print(df_trials.head())

# Save to CSV
df_trials.to_csv('clinical_trials.csv', index=False)
print("Saved to clinical_trials.csv")
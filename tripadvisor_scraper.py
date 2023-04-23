import requests
from bs4 import BeautifulSoup

location = input("Enter a location within the United States: ")
url = f"https://www.tripadvisor.com/Attractions-g191-Activities-{location}.html"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

attractions = soup.find_all("div", {"class": "attraction_element"})

print(f"\nTop 10 points of interest in {location}:")
for i in range(10):
    attraction_name = attractions[i].find("div", {"class": "listing_title"}).text.strip()
    attraction_ranking = attractions[i].find("div", {"class": "popIndex"}).text.strip()
    print(f"{attraction_ranking}. {attraction_name}")

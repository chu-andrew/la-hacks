from dataclasses import dataclass

import requests


@dataclass
class YelpPlace:
    name: str
    rating: float
    review_count: int
    url: str


def search_yelp(query="Restaurants", city="Los Angeles, CA"):
    search_url = f"https://www.yelp.com/search/snippet?find_desc={query}&find_loc={city}&request_origin=user"
    search_response = requests.get(search_url)
    search_results = search_response.json()['searchPageProps']['mainContentComponentsListProps']

    yelp_results = []
    for result in search_results:
        if result['searchResultLayoutType'] == "iaResult":
            name = result['searchResultBusiness']['name']
            rating = result['searchResultBusiness']['rating']
            review_count = result['searchResultBusiness']['reviewCount']
            url = "https://www.yelp.com" + result['searchResultBusiness']['businessUrl']

            x = YelpPlace(
                name, rating, review_count, url
            )

            yelp_results.append(x)

    return yelp_results


if __name__ == '__main__':
    results = search_yelp("ice cream", "Los Angeles, CA")
    if len(results) == 0:
        print("No results found.")
    else:
        for location in results:
            print(f"{location.name} --- "
                  f"{location.rating} STARS ({location.review_count} reviews)\n"
                  f"{location.url}\n")

import requests as req
from dataclasses import dataclass

quote_url: str = "https://api.quotable.io/random"


@dataclass
class Quote:
    author: str
    quote: str


def get_random_quote() -> Quote:
    try:
        response: req.Response = req.get(quote_url, verify=False, timeout=5)
        data = response.json()
        author = data.get("author", "Unknown")
        content = data.get("content", "Could not retrieve quote.")
        quote: Quote = Quote(author=author, quote=content)
    except req.exceptions.Timeout:
        print("Error: request timed out after 5 seconds.")
        quote: Quote = Quote(author="Unknown", quote="Request timed out.")
    except Exception as e:
        print(f"Error retrieving quote: {e}")
        quote: Quote = Quote(author="Unknown", quote="Could not retrieve quote.")
    return quote


if __name__ == "__main__":

    for i in range(3):
        random_quote: Quote = get_random_quote()
        print(f"Quote {i + 1}:")
        print(f'"{random_quote.quote}" - {random_quote.author}')
        print()

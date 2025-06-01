# url_shortener.py

import pyshorteners

def shorten_url(url: str) -> str:
    """
    Shortens the provided URL using TinyURL service.

    Args:
        url (str): The original long URL.

    Returns:
        str: The shortened URL.
    """
    try:
        shortener = pyshorteners.Shortener()
        short_url = shortener.tinyurl.short(url)
        return short_url
    except Exception as e:
        return f"❌ Error: Unable to shorten URL. {e}"

def main():
    print("🔗 Welcome to the URL Shortener!")
    url = input("Enter the URL to shorten: ").strip()
    
    if not url.startswith(("http://", "https://")):
        print("❌ Please enter a valid URL starting with http:// or https://")
        return

    result = shorten_url(url)
    print(f"\n✅ Shortened URL: {result}")

if __name__ == "__main__":
    main()

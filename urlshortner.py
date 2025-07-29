import pyshorteners
import argparse
import re

try:
    import pyperclip
    CLIPBOARD_AVAILABLE = True
except ImportError:
    CLIPBOARD_AVAILABLE = False

def is_valid_url(url: str) -> bool:
    pattern = re.compile(r'^(http|https)://[^\s]+$')
    return bool(pattern.match(url))

def shorten_url(url: str, service: str = "tinyurl") -> str:
    """
    Shortens the provided URL using the specified service.
    """
    try:
        shortener = pyshorteners.Shortener()
        if service == "tinyurl":
            return shortener.tinyurl.short(url)
        elif service == "isgd":
            return shortener.isgd.short(url)
        elif service == "dagd":
            return shortener.dagd.short(url)
        else:
            return "❌ Error: Service not supported."
    except Exception as e:
        return f"❌ Error: Unable to shorten URL. {e}"

def main():
    parser = argparse.ArgumentParser(
        description="Shorten URLs using various services."
    )
    parser.add_argument(
        'url', nargs='?', default=None,
        help="The URL to shorten"
    )
    parser.add_argument(
        '-s', '--service', default='tinyurl',
        choices=['tinyurl', 'isgd', 'dagd'],
        help="URL shortening service to use"
    )
    parser.add_argument(
        '--copy', action='store_true',
        help="Copy the shortened URL to clipboard"
    )

    args = parser.parse_args()

    while True:
        url = args.url
        if not url:
            url = input("Enter the URL to shorten (or press Enter to exit): ").strip()
            if not url:
                break

        if not is_valid_url(url):
            print("❌ Please enter a valid URL starting with http:// or https://")
            if args.url:
                break
            continue

        result = shorten_url(url, args.service)
        print(f"\n✅ Shortened URL: {result}")

        if args.copy and CLIPBOARD_AVAILABLE and not result.startswith("❌"):
            pyperclip.copy(result)
            print("📋 Shortened URL copied to clipboard!")

        if args.url:
            break

        # Reset for next loop
        args.url = None

if __name__ == "__main__":
    main()

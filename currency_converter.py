import requests
from config import EXCHANGE_API_KEY  # Keep keys separate for security

def get_exchange_rate(base_currency="USD"):
    """
    Fetch exchange rates for the given base currency.
    """
    url = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_API_KEY}/latest/{base_currency}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if data["result"] == "success":
            return data["conversion_rates"]
        else:
            print(f"❌ API Error: {data.get('error-type', 'Unknown error')}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
        return None

def convert_currency(amount, from_currency, to_currency):
    """
    Convert an amount from one currency to another.
    """
    rates = get_exchange_rate(from_currency)
    if not rates:
        return None

    rate = rates.get(to_currency)
    if not rate:
        print(f"❌ Unsupported currency code: {to_currency}")
        return None

    return amount * rate

def main():
    print("💱 Welcome to the Currency Converter")

    while True:
        try:
            amount = float(input("Enter the amount: "))
            from_currency = input("Convert from (e.g. USD): ").strip().upper()
            to_currency = input("Convert to (e.g. EUR): ").strip().upper()

            result = convert_currency(amount, from_currency, to_currency)
            if result is not None:
                print(f"✅ {amount:.2f} {from_currency} = {result:.2f} {to_currency}")
            else:
                print("⚠️ Conversion failed. Check currency codes and try again.")
        except ValueError:
            print("❌ Please enter a valid numeric amount.")
        
        again = input("Do you want to convert another amount? (y/n): ").lower()
        if again != 'y':
            print("👋 Exiting Currency Converter. Goodbye!")
            break

if __name__ == "__main__":
    main()

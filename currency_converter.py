import requests

def get_exchange_rates(base_currency="USD"):
    url = f"https://v6.exchangerate-api.com/v6/<Api_Key>/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    if data["result"] == "success":
        return data["conversion_rates"]
    else:
        print("Error fetching exchange rates.")
        return None

def convert_currency(amount, from_currency, to_currency):
    rates = get_exchange_rates(from_currency)
    if rates and to_currency in rates:
        converted_amount = amount * rates[to_currency]
        return converted_amount
    else:
        print("Invalid currency code or data not available.")
        return None

if __name__ == "__main__":
    rates = get_exchange_rates()
    if rates:
        currency_list = list(rates.keys())
        for i, currency in enumerate(currency_list, 1):
            print(f"{i}. {currency}")
        
        from_choice = int(input("Choose the number of the currency to convert from: "))
        from_currency = currency_list[from_choice - 1]
        
        to_choice = int(input("Choose the number of the currency to convert to: "))
        to_currency = currency_list[to_choice - 1]
        
        amount = float(input("Enter amount: "))
        
        result = convert_currency(amount, from_currency, to_currency)
        if result:
            print(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}")

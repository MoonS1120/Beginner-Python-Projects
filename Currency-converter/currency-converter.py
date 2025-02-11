import requests

def convert(from_currency, to_currency, amount, url):
    data = requests.get(url).json()
    rates = data['rates']
    initial_amount = amount
    amount = amount/rates[from_currency]*rates[to_currency]
    return initial_amount, amount

def main():
    api = 'API-key'
    url = 'http://data.fixer.io/api/latest?access_key=' + api
    from_c = input("From: ")
    to_c = input("To: ")
    amount = int(input("Amount: "))
    initial_amount, amount = convert(from_c, to_c, amount, url)
    print(f"{initial_amount} {from_c} is equal to {amount:.2f} {to_c}")

if __name__ == "__main__":
    main()
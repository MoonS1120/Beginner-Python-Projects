import requests

def convert(from_currency, to_currency, amount, url):
    data = requests.get(url).json()
    rates = data['rates']
    initial_amount = amount
    amount = round(amount/rates[from_currency]*rates[to_currency], 2)
    return initial_amount, amount

def main():
    url = 'http://data.fixer.io/api/latest?access_key=' + 'api-key'
    from_c = input("From: ")
    to_c = input("To: ")
    amount = int(input("Amount: "))
    initial_amount, amount = convert(from_c, to_c, amount, url)
    print(f"{initial_amount} {from_c} is equal to {amount} {to_c}")

if __name__ == "__main__":
    main()
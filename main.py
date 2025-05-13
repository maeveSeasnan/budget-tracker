import csv

# Dictionary to hold transaction data
transactions = []

def add_transaction():
    t_type = input("Is this income or expense? ").strip().lower()
    category = input("Enter category (e.g., rent, groceries, paycheck): ").strip()
    amount = float(input("Enter amount: $"))

    if t_type not in ["income", "expense"]:
        print("Invalid type! Must be 'income' or 'expense'.")
        return

    transactions.append({
        "type": t_type,
        "category": category,
        "amount": amount
    })
    print("Transaction added.\n")

def view_balance():
    income = sum(transaction["amount"] for transaction in transactions if transaction["type"] == "income")
    expenses = sum(transaction["amount"] for transaction in transactions if transaction["type"] == "expense")
    balance = income - expenses

    # Debug prints
    print(f"Income: {income}, Expenses: {expenses}, Balance: {balance}")

    print(f"\nTotal Income: ${income:.2f}")
    print(f"Total Expenses: ${expenses:.2f}")
    print(f"Balance: ${balance:.2f}\n")

def save_to_file():
    with open("transactions.csv", mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["type", "category", "amount"])
        writer.writeheader()
        writer.writerows(transactions)
    print("Data saved to transactions.csv\n")

def load_from_file():
    try:
        with open("transactions.csv", mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["amount"] = float(row["amount"])
                print(f"Loaded transaction: {row}")  # Debug line
                transactions.append(row)
        print("Data loaded from transactions.csv\n")
    except FileNotFoundError:
        print("No previous data found. Starting fresh.\n")

def main():
    load_from_file()
    while True:
        print("=== Budget Tracker Menu ===")
        print("1. Add a transaction")
        print("2. View balance")
        print("3. Save and exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_balance()
        elif choice == "3":
            save_to_file()
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()

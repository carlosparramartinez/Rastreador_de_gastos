import argparse
import json
import os
from datetime import datetime
from tabulate import tabulate

DATA_FILE = "expenses.json"
 #Si no existe, retorna una lista vacía ([]).
 # #Si existe, abre el archivo y retorna los datos cargados en formato JSON (una lista de gastos).
def load_data(): 
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)
#Abre (o crea) el archivo expenses.json y guarda la información (la lista de gastos) 
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_expense(description, amount):
    data = load_data()
    expense_id = data[-1]['id'] + 1 if data else 1
    expense = {
        "id": expense_id,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "description": description,
        "amount": amount
    }
    data.append(expense)
    save_data(data)
    print(f"Expense added successfully (ID: {expense_id})")

def delete_expense(expense_id):
    data = load_data()
    new_data = [e for e in data if e["id"] != expense_id]
    if len(new_data) == len(data):
        print("Error: Expense ID not found.")
    else:
        save_data(new_data)
        print("Expense deleted successfully")

def list_expenses():
    data = load_data()
    if not data:
        print("No expenses found.")
        return
    table = [[e["id"], e["date"], e["description"], f"${e['amount']}"] for e in data]
    print(tabulate(table, headers=["ID", "Date", "Description", "Amount"]))

def summary(month=None):
    data = load_data()
    total = 0
    if month:
        filtered = [e for e in data if datetime.strptime(e["date"], "%Y-%m-%d").month == month]
        total = sum(e["amount"] for e in filtered)
        print(f"Total expenses for {datetime(1900, month, 1).strftime('%B')}: ${total}")
    else:
        total = sum(e["amount"] for e in data)
        print(f"Total expenses: ${total}")

def update_expense(expense_id, description, amount):
    data = load_data()
    for e in data:
        if e["id"] == expense_id:
            e["description"] = description or e["description"]
            e["amount"] = amount if amount is not None else e["amount"]
            save_data(data)
            print("Expense updated successfully")
            return
    print("Error: Expense ID not found.")

def main():
    parser = argparse.ArgumentParser(prog="expense-tracker")
    subparsers = parser.add_subparsers(dest="command")

    # Add
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--description", required=True)
    add_parser.add_argument("--amount", type=float, required=True)

    # Delete
    del_parser = subparsers.add_parser("delete")
    del_parser.add_argument("--id", type=int, required=True)

    # List
    subparsers.add_parser("list")

    # Summary
    sum_parser = subparsers.add_parser("summary")
    sum_parser.add_argument("--month", type=int)

    # Update
    upd_parser = subparsers.add_parser("update")
    upd_parser.add_argument("--id", type=int, required=True)
    upd_parser.add_argument("--description")
    upd_parser.add_argument("--amount", type=float)

    args = parser.parse_args()

    if args.command == "add":
        if args.amount <= 0:
            print("Amount must be positive.")
        else:
            add_expense(args.description, args.amount)
    elif args.command == "delete":
        delete_expense(args.id)
    elif args.command == "list":
        list_expenses()
    elif args.command == "summary":
        summary(args.month)
    elif args.command == "update":
        update_expense(args.id, args.description, args.amount)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
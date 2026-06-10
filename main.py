import json
import csv
import os

FILE_NAME = "expenses.json"


def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    date = input("Enter Date (DD-MM-YYYY): ")
    category = input("Enter Category: ")

    try:
        amount = float(input("Enter Amount: ₹"))
    except ValueError:
        print("Invalid amount!")
        return

    description = input("Enter Description: ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }

    expenses.append(expense)

    save_expenses(expenses)

    print("\nExpense Added Successfully!\n")


def view_expenses(expenses):
    if not expenses:
        print("\nNo expenses found.\n")
        return

    print("\n===== EXPENSE LIST =====\n")

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. "
            f"{expense['date']} | "
            f"{expense['category']} | "
            f"₹{expense['amount']} | "
            f"{expense['description']}"
        )

    print()
def edit_expense(expenses):
    view_expenses(expenses)

    if not expenses:
        return

    try:
        index = int(input("Enter expense number to edit: ")) - 1

        if 0 <= index < len(expenses):

            print("\nLeave blank to keep old value.\n")

            new_date = input(
                f"Date ({expenses[index]['date']}): "
            )

            new_category = input(
                f"Category ({expenses[index]['category']}): "
            )

            new_amount = input(
                f"Amount ({expenses[index]['amount']}): "
            )

            new_description = input(
                f"Description ({expenses[index]['description']}): "
            )

            if new_date:
                expenses[index]["date"] = new_date

            if new_category:
                expenses[index]["category"] = new_category

            if new_amount:
                expenses[index]["amount"] = float(new_amount)

            if new_description:
                expenses[index]["description"] = new_description

            save_expenses(expenses)

            print("\nExpense Updated Successfully!\n")

        else:
            print("Invalid expense number.")

    except ValueError:
        print("Invalid input.")


def delete_expense(expenses):
    view_expenses(expenses)

    if not expenses:
        return

    try:
        index = int(
            input("Enter expense number to delete: ")
        ) - 1

        if 0 <= index < len(expenses):

            removed = expenses.pop(index)

            save_expenses(expenses)

            print(
                f"\nDeleted: {removed['description']}\n"
            )

        else:
            print("Invalid expense number.")

    except ValueError:
        print("Invalid input.")


def show_total(expenses):
    total = sum(
        expense["amount"]
        for expense in expenses
    )

    print(
        f"\nTotal Expenses: ₹{total:.2f}\n"
    )


def search_by_category(expenses):
    category = input(
        "Enter category: "
    ).strip().lower()

    found = False

    print("\n===== RESULTS =====\n")

    for i, expense in enumerate(expenses, start=1):

        if expense["category"].lower() == category:

            print(
                f"{i}. "
                f"{expense['date']} | "
                f"{expense['category']} | "
                f"₹{expense['amount']} | "
                f"{expense['description']}"
            )

            found = True

    if not found:
        print("No matching expenses found.")

    print()


def category_summary(expenses):
    summary = {}

    for expense in expenses:

        category = expense["category"]

        summary[category] = (
            summary.get(category, 0)
            + expense["amount"]
        )

    print(
        "\n===== CATEGORY SUMMARY ====="
    )

    for category, total in summary.items():

        print(
            f"{category}: ₹{total:.2f}"
        )

    print()


def highest_expense(expenses):
    if not expenses:
        print("No expenses found.")
        return

    highest = max(
        expenses,
        key=lambda x: x["amount"]
    )

    print(
        "\n===== HIGHEST EXPENSE ====="
    )

    print(
        f"{highest['date']} | "
        f"{highest['category']} | "
        f"₹{highest['amount']} | "
        f"{highest['description']}"
    )

    print()
def export_csv(expenses):
    if not expenses:
        print("\nNo expenses to export.\n")
        return

    with open(
        "expenses.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow(
            [
                "Date",
                "Category",
                "Amount",
                "Description"
            ]
        )

        for expense in expenses:

            writer.writerow(
                [
                    expense["date"],
                    expense["category"],
                    expense["amount"],
                    expense["description"]
                ]
            )

    print(
        "\nExpenses exported successfully to expenses.csv\n"
    )
def monthly_report(expenses):
    month = input("Enter Month (MM): ")

    total = 0

    for expense in expenses:
        if expense["date"][3:5] == month:
            total += float(expense["amount"])

    print(f"\nTotal Expenses for Month {month}: ₹{total}")

def sort_by_amount(expenses):
    sorted_expenses = sorted(
        expenses,
        key=lambda x: float(x["amount"]),
        reverse=True
    )

    print("\n===== SORTED BY AMOUNT (HIGH TO LOW) =====\n")

    for i, expense in enumerate(sorted_expenses, start=1):
        print(
            f"{i}. "
            f"{expense['date']} | "
            f"{expense['category']} | "
            f"₹{expense['amount']} | "
            f"{expense['description']}"
        )

    print()


def sort_by_date(expenses):
    sorted_expenses = sorted(
        expenses,
        key=lambda x: x["date"]
    )

    print("\n===== SORTED BY DATE =====\n")

    for i, expense in enumerate(sorted_expenses, start=1):
        print(
            f"{i}. "
            f"{expense['date']} | "
            f"{expense['category']} | "
            f"₹{expense['amount']} | "
            f"{expense['description']}"
        )

    print()


def main():
    expenses = load_expenses()

    while True:

        print(
            "\n===== EXPENSE TRACKER ====="
        )

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Edit Expense")
        print("4. Delete Expense")
        print("5. Show Total Expenses")
        print("6. Search by Category")
        print("7. Category Summary")
        print("8. Highest Expense")
        print("9. Export to CSV")
        print("10. Monthly Expense Report")
        print("11. Sort Expenses by Amount")
        print("12. Sort Expenses by Date")
        print("13. Exit")
        

        choice = input(
            "\nChoose an option: "
        )

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            edit_expense(expenses)

        elif choice == "4":
            delete_expense(expenses)

        elif choice == "5":
            show_total(expenses)

        elif choice == "6":
            search_by_category(expenses)

        elif choice == "7":
            category_summary(expenses)

        elif choice == "8":
            highest_expense(expenses)

        elif choice == "9":
            export_csv(expenses)
    
        elif choice == "10":
            monthly_report(expenses)

        elif choice == "11":
            sort_by_amount(expenses)

        elif choice == "12":
            sort_by_date(expenses)

        elif choice == "13":
            print(
                "\nThank you for using Expense Tracker!"
            )
            break

        else:
            print(
                "\nInvalid choice. Try again."
            )


if __name__ == "__main__":
    main()
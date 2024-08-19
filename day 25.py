# Simple Expense Tracker

# Empty list to store expenses
expenses = []

# Valid categories
categories = ["food", "transportation", "entertainment", "other"]

def add_expense():
    # Get expense details from the user
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category (food, transportation, entertainment, other): ")
    description = input("Enter expense description: ")

    # Validate input
    if amount <= 0:
        print("Invalid amount. Please enter a positive number.")
        return
    if category not in categories:
        print("Invalid category. Please choose from: food, transportation, entertainment, other")
        return

    # Add the new expense to the list
    new_expense = {"amount": amount, "category": category, "description": description}
    expenses.append(new_expense)
    print("Expense added successfully.")

def display_summary():
    # Initialize a dictionary to store total spending per category
    summary = {category: 0 for category in categories}

    # Calculate total spending per category
    for expense in expenses:
        summary[expense["category"]] += expense["amount"]

    # Display the summary
    print("Expense Summary:")
    for category, total in summary.items():
        print(f"{category.capitalize()}: ${total:.2f}")

def main():
    while True:
        print("\nSimple Expense Tracker")
        print("1. Add Expense")
        print("2. Display Summary")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            display_summary()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
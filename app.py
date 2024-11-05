import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('chocolate_house.db')
cursor = conn.cursor()

# Create tables if they don't already exist
cursor.execute('''CREATE TABLE IF NOT EXISTS seasonal_flavors (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    flavor_name TEXT NOT NULL,
                    description TEXT,
                    availability TEXT
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS ingredients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ingredient_name TEXT NOT NULL,
                    quantity INTEGER,
                    unit TEXT
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS customer_suggestions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_name TEXT,
                    flavor_suggestion TEXT,
                    allergy_info TEXT
                )''')

# Function to add a seasonal flavor
def add_seasonal_flavor(name, description, availability):
    cursor.execute("INSERT INTO seasonal_flavors (flavor_name, description, availability) VALUES (?, ?, ?)",
                   (name, description, availability))
    conn.commit()
    print(f"Seasonal flavor '{name}' added successfully.")

# Function to add an ingredient to inventory
def add_ingredient(name, quantity, unit):
    cursor.execute("INSERT INTO ingredients (ingredient_name, quantity, unit) VALUES (?, ?, ?)",
                   (name, quantity, unit))
    conn.commit()
    print(f"Ingredient '{name}' added successfully.")

# Function to add a customer suggestion
def add_customer_suggestion(customer_name, suggestion, allergy_info):
    cursor.execute("INSERT INTO customer_suggestions (customer_name, flavor_suggestion, allergy_info) VALUES (?, ?, ?)",
                   (customer_name, suggestion, allergy_info))
    conn.commit()
    print(f"Customer suggestion from '{customer_name}' added successfully.")

# Function to list all entries in a table
def list_table(table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Simple menu to interact with the application
def main():
    while True:
        print("\nChocolate House Management")
        print("1. Add Seasonal Flavor")
        print("2. Add Ingredient")
        print("3. Add Customer Suggestion")
        print("4. List Seasonal Flavors")
        print("5. List Ingredients")
        print("6. List Customer Suggestions")
        print("7. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter flavor name: ")
            description = input("Enter description: ")
            availability = input("Enter availability: ")
            add_seasonal_flavor(name, description, availability)
        elif choice == '2':
            name = input("Enter ingredient name: ")
            quantity = int(input("Enter quantity: "))
            unit = input("Enter unit: ")
            add_ingredient(name, quantity, unit)
        elif choice == '3':
            customer_name = input("Enter customer name: ")
            suggestion = input("Enter flavor suggestion: ")
            allergy_info = input("Enter allergy info: ")
            add_customer_suggestion(customer_name, suggestion, allergy_info)
        elif choice == '4':
            list_table('seasonal_flavors')
        elif choice == '5':
            list_table('ingredients')
        elif choice == '6':
            list_table('customer_suggestions')
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function if the script is executed
if __name__ == "__main__":
    main()

# Close the connection to the database
conn.close()

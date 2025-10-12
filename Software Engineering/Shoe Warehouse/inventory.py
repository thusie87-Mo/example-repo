# ==============Shoe Warehouse==========
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"{self.country}, {self.code}, {self.product}, R{self.cost}, {self.quantity} pairs"

# ==============Global Branches===========
shoe_list = []

# ==============Calculations==============
def read_shoe_data():
    """Read shoe data from inventory.txt and populate shoe_list."""
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # Skip header
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 5:
                    country, code, product, cost, quantity = parts
                    shoe = Shoe(country, code, product, cost, quantity)
                    shoe_list.append(shoe)
    except FileNotFoundError:
        print("The file 'inventory.txt' was not found.")
    except Exception as e:
        print("Error reading file:", e)

def capture_shoes():
    """Allows user to add a new shoe."""
    country = input("Enter country: ")
    code = input("Enter code: ")
    product = input("Enter product name: ")
    cost = float(input("Enter cost: "))
    quantity = int(input("Enter quantity: "))

    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)
    print("Shoe added successfully!")

def view_all():
    """Display all shoes in inventory."""
    print("\n--- Shoe Inventory ---")
    for shoe in shoe_list:
        print(shoe)

def re_stock():
    """Find shoe with lowest quantity and restock it."""
    if not shoe_list:
        print("No shoes in inventory.")
        return
    lowest = min(shoe_list, key=lambda s: s.quantity)
    print(f"\nLowest stock item: {lowest.product} ({lowest.quantity} pairs)")
    choice = input("Would you like to restock this shoe? (y/n): ").lower()
    if choice == "y":
        add_qty = int(input("Enter quantity to add: "))
        lowest.quantity += add_qty
        print("Shoe restocked successfully!")

def search_shoe():
    """Search for a shoe by code."""
    code = input("Enter shoe code to search: ")
    for shoe in shoe_list:
        if shoe.code == code:
            print("Shoe found:", shoe)
            return
    print("Shoe not found.")

def value_per_item():
    """Calculate total value per shoe (cost * quantity)."""
    print("\n--- Total Value per Shoe ---")
    for shoe in shoe_list:
        total_value = shoe.cost * shoe.quantity
        print(f"{shoe.product} - Total Value: R{total_value:.2f}")

def highest_qty():
    """Find shoe with the highest quantity."""
    if not shoe_list:
        print("No shoes in inventory.")
        return
    highest = max(shoe_list, key=lambda s: s.quantity)
    print(f"\nShoe for sale: {highest.product} ({highest.quantity} pairs available)")

# =============Menu===========
def main():
    read_shoe_data()

    while True:
        print("\n========== Shoe Inventory Menu ==========")
        print("1. View all shoes")
        print("2. Add new shoe")
        print("3. Restock lowest item")
        print("4. Search shoes by code")
        print("5. View value per item")
        print("6. View highest quantity (for sale)")
        print("7. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            view_all()
        elif choice == "2":
            capture_shoes()
        elif choice == "3":
            re_stock()
        elif choice == "4":
            search_shoe()
        elif choice == "5":
            value_per_item()
        elif choice == "6":
            highest_qty()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
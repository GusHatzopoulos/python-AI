discount = 20

def calculate_total(price):
    # Default values
    tax_rate = 0.88
    discount = 10

    # Calculation
    tax = price * tax_rate
    final_price = price + tax - discount

    # Print final answer
    print(f"Total price: ${final_price}")

calculate_total(price = 100)
# Path: discount_calculator.py

def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying the discount.
    If discount_percent is 20 or higher, apply the discount.
    Otherwise, return the original price.
    """
    if discount_percent >= 20:
        discounted_price = price * (1 - discount_percent / 100)
        return discounted_price
    return price

def main():
    try:
        # Prompt user for input
        price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage: "))
        
        # Calculate final price
        final_price = calculate_discount(price, discount_percent)
        
        # Display result
        if final_price < price:
            print(f"The final price after a {discount_percent}% discount is: ${final_price:.2f}")
        else:
            print(f"No discount applied. The original price is: ${price:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values for price and discount percentage.")

# Run the program
if __name__ == "__main__":
    main()

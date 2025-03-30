def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Args:
        price: The original price of the item
        discount_percent: The discount percentage
        
    Returns:
        The final price after discount if discount_percent >= 20,
        otherwise the original price
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

def main():
    # Get user input
    try:
        original_price = float(input("Enter the original price of the item: $"))
        discount_percent = float(input("Enter the discount percentage: "))
        
        # Validate inputs
        if original_price < 0 or discount_percent < 0:
            print("Error: Price and discount percentage cannot be negative.")
            return
            
        # Calculate and display the final price
        final_price = calculate_discount(original_price, discount_percent)
        
        if final_price < original_price:
            print(f"Original price: ${original_price:.2f}")
            print(f"Discount applied: {discount_percent:.1f}%")
            print(f"Final price after discount: ${final_price:.2f}")
        else:
            print(f"No discount applied. Original price: ${original_price:.2f}")
            
    except ValueError:
        print("Error: Please enter valid numerical values.")

if __name__ == "__main__":
    main()
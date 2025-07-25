def minimize_loss(prices):
    """
    Calculate the minimum loss when buying and selling a house over years,
    with the constraint that we must sell at a loss.
    
    Args:
        prices (list): List of house prices for each year
    
    Returns:
        tuple: (buy_year, sell_year, loss_value)
            buy_year is the year (1-indexed) to buy the house
            sell_year is the year (1-indexed) to sell the house
            loss_value is the minimum possible loss (a positive number)
    """
    n = len(prices)
    
    # We need at least 2 years of data to buy and sell
    if n < 2:
        return None
    
    min_loss = float('inf')
    buy_year = 0
    sell_year = 0
    
    # To minimize loss, we need to buy high and sell as high as possible below our buying price
    # For each possible buying year (1 to n-1)
    for i in range(n):
        buy_price = prices[i]
        # For each possible selling year after buying (i+1 to n)
        for j in range(i+1, n):
            sell_price = prices[j]
            # Calculate loss (must be positive for a loss)
            if buy_price > sell_price:
                loss = buy_price - sell_price
                
                # Update min_loss if this combination gives a smaller loss
                if loss < min_loss:
                    min_loss = loss
                    buy_year = i + 1  # +1 because years are 1-indexed in the problem
                    sell_year = j + 1  # +1 because years are 1-indexed in the problem
    
    # If no loss scenario found, return None
    if min_loss == float('inf'):
        return None
        
    return (buy_year, sell_year, min_loss)

# Optimized solution with O(n) time complexity
def minimize_loss_optimized(prices):
    """
    More efficient implementation of the minimize_loss function.
    
    Args:
        prices (list): List of house prices for each year
    
    Returns:
        tuple: (buy_year, sell_year, loss_value)
            buy_year is the year (1-indexed) to buy the house
            sell_year is the year (1-indexed) to sell the house
            loss_value is the minimum possible loss (a positive number)
    """
    n = len(prices)
    
    # We need at least 2 years of data to buy and sell
    if n < 2:
        return None
    
    # Keep track of potential future selling prices
    # For each buying price, find the highest selling price that's still lower
    min_loss = float('inf')
    buy_year = 0
    sell_year = 0
    
    # Create pairs of (price, year)
    price_years = [(prices[i], i+1) for i in range(n)]
    
    # For each year as buying year
    for i in range(n):
        buy_price = prices[i]
        buy_year_idx = i + 1
        
        # Look at all future years as potential selling years
        for j in range(i+1, n):
            sell_price = prices[j]
            sell_year_idx = j + 1
            
            # We must sell at a loss
            if buy_price > sell_price:
                loss = buy_price - sell_price
                if loss < min_loss:
                    min_loss = loss
                    buy_year = buy_year_idx
                    sell_year = sell_year_idx
    
    # If no loss scenario found, return None
    if min_loss == float('inf'):
        return None
        
    return (buy_year, sell_year, min_loss)

# Example usage
if __name__ == "__main__":
    # Example from the problem statement
    prices = [20, 15, 7, 2, 13]
    
    result = minimize_loss(prices)
    print(f"Brute force approach: Buy in year {result[0]}, sell in year {result[1]}, with loss {result[2]}")
    
    optimized_result = minimize_loss_optimized(prices)
    print(f"Optimized approach: Buy in year {optimized_result[0]}, sell in year {optimized_result[1]}, with loss {optimized_result[2]}")
    
    # Additional test case
    prices2 = [10, 5, 15, 7, 6]
    result2 = minimize_loss(prices2)
    print(f"\nTest case 2 - Brute force: Buy in year {result2[0]}, sell in year {result2[1]}, with loss {result2[2]}")
    
    optimized_result2 = minimize_loss_optimized(prices2)
    print(f"Test case 2 - Optimized: Buy in year {optimized_result2[0]}, sell in year {optimized_result2[1]}, with loss {optimized_result2[2]}") 
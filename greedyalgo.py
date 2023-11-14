# Structure for an item which stores weight and
# corresponding value of Item
class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

# Main greedy function to solve the problem
def fractionalKnapsack(W, arr):
    # Sorting Item on the basis of the profit-to-weight ratio
    arr.sort(key=lambda x: x.profit / x.weight, reverse=True)

    # Result (value in Knapsack)
    final_value = 0.0

    # Looping through all Items
    for item in arr:
        # If adding the item won't overflow, add it completely
        if item.weight <= W:
            W -= item.weight
            final_value += item.profit
        else:
            # If we can't add the current item, add the fractional part of it
            final_value += item.profit * W / item.weight
            break

    # Returning the final value
    return final_value

# Driver Code
if __name__ == "__main__":
    W = 50
    arr = [Item(60, 10), Item(100, 20), Item(120, 30)]

    # Function call
    max_val = fractionalKnapsack(W, arr)
    print(max_val)
    
# INSTRUCTIONS:

# Create a function called calc_dollars. In the function body, define a dictionary and store it in a variable named piggyBank. The dictionary should have the following keys defined.

# quarters
# nickels
# dimes
# pennies
# For each coin type, give yourself as many as you like.

# piggyBank = {
#     "pennies": 342,
#     "nickels": 9,
#     "dimes": 32
# }
# Once you have given yourself a large stash of coins in your piggybank, look at each key and perform the appropriate math on the integer value to determine how much money you have in dollars. Store that value in a variable named dollarAmount and print it.

# Given the coins shown above, the output would be 7.07 when you call calc_dollars()


def calc_dollars():
    piggyBank = {
        "quarters":  8,
        "pennies":  342,
        "nickels": 9,
        "dimes": 32
    }
    return piggyBank


available_amount = calc_dollars()

available_amount_in_dollars = (available_amount["quarters"]*0.25 + available_amount["pennies"]
                               * 0.01 + available_amount["nickels"]*0.05 + available_amount["dimes"]*0.10)

print("Total amount in my piggy bank-->$", available_amount_in_dollars)

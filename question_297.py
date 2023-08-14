# At a popular bar, each customer has a set of favorite drinks,
# and will happily accept any drink among this set. For example,
# in the following situation, customer 0 will be satisfied with drinks 0, 1, 3, or 6.

# preferences = {
#     0: [0, 1, 3, 6],
#     1: [1, 4, 7],
#     2: [2, 4, 7, 5],
#     3: [3, 2, 5],
#     4: [5, 8]
# }

# A lazy bartender working at this bar is trying to reduce his effort by
# limiting the drink recipes he must memorize. Given a dictionary input
# such as the one above, return the fewest number of drinks he must learn
# in order to satisfy all customers.

# For the input above, the answer would be 2, as drinks 1 and 5 will satisfy everyone.

# Intuition:
# This problem is similar to the set cover problem, which is a well-known NP-hard problem.
# Here, the sets are the preferences of the customers, and the goal is to find the smallest
# number of drinks (elements) that cover all the customers.

# The set cover problem can be described as: given a universe U and a collection S of subsets of
# U, find the smallest sub-collection T such that the union of the subsets in T is equal to U.

# To solve the problem, we can use a greedy algorithm:

# While there are customers that are not satisfied:
# 1.1. Find the drink that can satisfy the maximum number of unsatisfied customers.
# 1.2. Add this drink to the bartender's list.
# 1.3. Mark all the customers satisfied by this drink as satisfied.

# Return the number of drinks in the bartender's list.

# Note: This greedy algorithm does not guarantee an optimal solution for all instances of
# the set cover problem, but it should work well for many practical instances.


def lazy_bartender(prefs: dict[int, list[int]]):
    # set of all customers
    all_custs: set[int] = set(prefs.keys())

    # satisfied custs
    satisfied = set()

    # drinks bartender knows
    drinks_to_know = set()

    # While there are customers that are not satisfied
    while satisfied != all_custs:
        # dict to store the num of custs satisfied by each drink
        drink_counts: dict[int, int] = {}

        # for each cust's prefs
        for cust, drinks in prefs.items():
            # if the cust is not satisfied
            if cust not in satisfied:
                # for each drink in the cust's prefs
                for drink in drinks:
                    # if the drink is not in the dict
                    if drink not in drink_counts:
                        # add it to the dict
                        drink_counts[drink] = 0
                    # increment the count
                    drink_counts[drink] += 1

        # get the drink that can satisfy the max num of unsatisfied custs
        best_drink = max(drink_counts, key=lambda drink: drink_counts[drink])

        # add the drink to the list of drinks the bartender knows
        drinks_to_know.add(best_drink)

        # mark all the customers satisfied by this drink as satisfied
        for cust, drinks in prefs.items():
            if best_drink in drinks:
                satisfied.add(cust)

    # return the number of drinks in the bartender's list
    return len(drinks_to_know)


# Test with the given preferences
preferences = {
    0: [0, 1, 3, 6],
    1: [1, 4, 7],
    2: [2, 4, 7, 5],
    3: [3, 2, 5],
    4: [5, 8]
}

print(lazy_bartender(preferences))

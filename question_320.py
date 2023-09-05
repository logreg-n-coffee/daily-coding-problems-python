# Given a string, find the length of the smallest window that contains every distinct character. Characters may appear more than once in the window.

# For example, given "jiujitsu", you should return 5, corresponding to the final five letters.

from collections import defaultdict


# Function to find the length of the smallest window that contains every distinct character in a string.
# The function uses O(N) time and space complexity by employing a two-pointer approach.
def window(string: str | list[str]) -> int:
    # Convert input string to list for easier character manipulation
    string = list(string)

    # Initialize variables
    char_seen = 0  # Counter for distinct characters seen so far
    # Total distinct characters in the input string
    char_total = len(set(string))
    # Dictionary to keep count of each character's occurrence
    char_counts = defaultdict(int)

    start_idx = 0  # Start index of the current window
    result = float('inf')  # Initialize result to positive infinity

    # Loop through the string
    for end_idx, char in enumerate(string):
        # Increment count for the current character
        char_counts[char] += 1

        # If this is the first occurrence of the current character, increment char_seen
        if char_counts[char] == 1:
            char_seen += 1

        # If all distinct characters have been seen
        if char_seen == char_total:
            # If the count of the character at our start index is greater than one,
            # we know that character will reappear later on in the window
            while char_counts[string[start_idx]] > 1:
                char_counts[string[start_idx]] -= 1
                start_idx += 1

            # Calculate the length of the current window
            window_length = end_idx - start_idx + 1

            # Update the result if the current window is smaller
            if window_length < result:
                result = window_length

    # Return the length of the smallest window that contains all distinct characters
    return int(result)


# Test case
# Input: "jiujitsu"
# The smallest window that contains all distinct characters is "ujits" (5 characters long)
# Therefore, the expected output is 5
print(window("jiujitsu"))  # Output should be 5

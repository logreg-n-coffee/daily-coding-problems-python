# You are going on a road trip, and would like to create a suitable music playlist.
# The trip will require N songs, though you only have M songs downloaded, where M < N.
# A valid playlist should select each song at least once, and guarantee a buffer of B songs between repeats.

# Given N, M, and B, determine the number of valid playlists.


# Define a function called valid_playlists that takes three arguments:
# n: number of total songs needed in the playlist
# m: number of unique songs you have downloaded
# b: minimum number of songs between any repeated song
def valid_playlists(n, m, b):
    # Initialize a 2D list called dp with all elements set to 0.
    # dp[i][j] will represent the number of valid playlists of length i that uses j unique songs.
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    # Base case: There is exactly one valid playlist of 0 length that uses 0 unique songs, which is an empty playlist.
    dp[0][0] = 1

    # Loop through all playlist lengths from 1 to n.
    for i in range(1, n + 1):
        # Loop through all unique song counts from 1 to m.
        for j in range(1, m + 1):
            # Case 1: Add a new song that hasn't been used in the playlist.
            # There are (m - (j - 1)) such new songs available.
            dp[i][j] += dp[i - 1][j - 1] * (m - (j - 1))

            # Case 2: Add an old song that has already been used in the playlist.
            # There are max(0, j - b) such old songs available, accounting for the buffer of b.
            dp[i][j] += dp[i - 1][j] * max(0, j - b)

    # Return the number of valid playlists of length n that uses all m unique songs.
    return dp[n][m]

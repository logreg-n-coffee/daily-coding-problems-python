# On election day, a voting machine writes data in the form (voter_id, candidate_id) to a text file.
# Write a program that reads this file as a stream and returns the top 3 candidates at any given time.
# If you find a voter voting more than once, report this as fraud.


import random
import os
from collections import defaultdict, Counter


def generate_dataset(filename):
    with open(filename, 'w') as f:
        for _ in range(NUM_VOTES):
            voter_id = f"voter{random.randint(1, NUM_VOTERS)}"
            candidate_id = f"candidate{random.randint(1, NUM_CANDIDATES)}"

            f.write(f"{voter_id}, {candidate_id}\n")
    f.close()


def detect_fraud_and_top_candidates(file_name):
    votes = Counter()
    voters = defaultdict(int)

    with open(file_name, 'r') as f:
        for line in f:
            voter_id, candidate_id = line.strip().split(", ")
            voters[voter_id] += 1

            if voters[voter_id] > 1:
                print(
                    f"Fraud detected! Voter ID: {voter_id} has voted multiple times!")
                continue

            votes[candidate_id] += 1
            top_3 = votes.most_common(3)

            print(f"Current Top 3 candidates:")
            for candidate, vote_count in top_3:
                print(f"Candidate {candidate}: {vote_count} votes")

            print("---------")

    f.close()


if __name__ == "__main__":
    NUM_VOTERS = 100
    NUM_CANDIDATES = 10
    NUM_VOTES = 1000
    DIRECTORY = "test_dataset"
    FILENAME = os.path.join(DIRECTORY, "question_300_votes.txt")

    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)

    generate_dataset(FILENAME)
    detect_fraud_and_top_candidates(FILENAME)

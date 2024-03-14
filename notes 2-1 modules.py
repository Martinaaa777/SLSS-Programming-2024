# Author: Ubial
# Mrs. Ubial's Birthday

import random

# 1. Greets the user
print("Hello there!")

# 2. Asks them, "how are you?" or something like it
print("How are you doing?")
user_feeling = input().strip(",.?! ").lower()

# 3. Responds with a general statement
#       that is randomly chosen
#         - create a list of possible responses
#         - randomly choose a response
#         - print that response

good_possible_resp = [
    "I'm really happy for you.",
    "That's really good news!!",
    "That's awesome.",
]
bad_possible_resp = ["I'm sorry you're feeling that way.", "There, there.", "🥺"]
neutral_possible_resp = ["Thanks for sharing that with me.", "Cool!", "🤜🤛"]

if user_feeling == "good" or user_feeling == "great":
    print(random.choice(good_possible_resp))
elif user_feeling == "bad" or user_feeling == "not too good":
    print(random.choice(bad_possible_resp))
else:
    print(random.choice(neutral_possible_resp))

# 4. Says goodbye
print("Well thank you for your time! 😊")








# Martina panosetti
# 11 March 2024
# lists and moduls

import random

# Demonstrate some parts of the random module
# random.random() -> (0, 1.0]


def coin_flip():
    # Return either heads, tails, or other?
    # Heads -- (0, 0.5]
    # Tails -- (0.5, 0.999999]
    # Other --- the rest
    result = random.random()

    if result < 0.5:
        return "heads"
    elif result < 0.999999:
        return "tails"
    else:
        return "other"


def draw_card():
    # Simulate drawing a card
    # Return a card value from A, 2, 3, ..., Q, K
    #   random.randrange() -> int in some range
    result = random.randrange(1, 14)

    if result == 1:
        return "A"
    elif result == 11:
        return "J"
    elif result == 12:
        return "Q"
    elif result == 13:
        return "K"
    else:
        return str(result)


def main():
    # Repeat the coin flip 1000 times
    # Keep track of heads, tails, and others
    heads = 0
    tails = 0
    others = 0

    drawn_cards = []

    for _ in range(1_000_000):
        # flip coin
        result = coin_flip()
        drawn_cards.append(draw_card())

        if result == "heads":
            heads = heads + 1  # increment
        elif result == "tails":
            tails += 1  # increment
        else:
            others += 1

    # Print results
    print(f"Heads: {heads}")
    print(f"Tails: {tails}")
    print(f"Others: {others}")
    print(drawn_cards[0:100])  # print first 100 cards


main()
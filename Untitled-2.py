import random

subjects = [
    "Nayab",
    "Amna G",
    "Iram",
    "Toper Fiza",
    "A group of pagals",
    "A farmer Zuhaib",
    "Coder Abdullah"
]

actions = [
    "launches",
    "works",
    "eats",
    "looked ",
    "forgets",
    "dances with",
    "jumps on"
]

place_or_things = [
    " doms cafe",
    " nathya gali farms",
    "toys",
    "halky dogs",
    "K2 ",
    "golgapy near sports cafe",
    " mirror and shocked"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(place_or_things)

    headline = f"Breaking News: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (Yes/No): ").strip()

    if user_input.lower() == "no":
        break

print("\nThanks for using Fake Headline Generator. Have a Fun Day!")

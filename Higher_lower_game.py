# this is a higher lower game where you guess the higher or lower between two instagram accounts here are the accounts

instagram_accounts = {
    "kyliejenner": {
        "name": "kyliejenner",
        "follower_count": 1000000,
        "description": "social media platform",
        "country": "United States"
    },
    "selenagomez": {
        "name": "selenagomez",
        "follower_count": 2000000,
        "description": "social media platform",
        "country": "United States"
    },
    "elonmusk": {
        "name": "elonmusk",
        "follower_count": 3000000,
        "description": "social media platform",
        "country": "United States"
    },
    "jackma": {
        "name": "jackma",
        "follower_count": 4000000,
        "description": "social media platform",
        "country": "United States"
    },
    "billgates": {
        "name": "billgates",
        "follower_count": 5000000,
        "description": "social media platform",
        "country": "United States"
    },
    "jeffbezos": {
        "name": "jeffbezos",
        "follower_count": 6000000,
        "description": "social media platform",
        "country": "United States"
    },
    "larrypage": {
        "name": "larrypage",
        "follower_count": 7000000,
        "description": "social media platform",
        "country": "United States"
    },
    "sergeybrin": {
        "name": "sergeybrin",
        "follower_count": 8000000,
        "description": "social media platform",
        "country": "United States"
    },
    "markzuckerberg": {
        "name": "markzuckerberg",
        "follower_count": 9000000,
        "description": "social media platform",
        "country": "United States"
    },
}
import random


def get_random_account():
    return random.choice(list(instagram_accounts.values()))

def format_account(account):
    return f"{account['name']}, a {account['description']}, from {account['country']}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    
score = 0
game_over = False

account_a = get_random_account()
account_b = get_random_account()

while account_a == account_b:
    account_b = get_random_account()

while not game_over:
    print(f"Compare A: {format_account(account_a)}")
    print(f"Against B: {format_account(account_b)}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_followers = account_a['follower_count']
    b_followers = account_b['follower_count']
    is_correct = check_answer(guess, a_followers, b_followers)
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")

        if a_followers > b_followers:
            account_b = get_random_account()
        else:
            account_a = account_b
            account_b = get_random_account()
        while account_a == account_b:
            account_b = get_random_account()
    else:
        game_over = True
        print(f"Sorry, that's wrong. Final score: {score}.")

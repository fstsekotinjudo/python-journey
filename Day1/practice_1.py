import random

secret = random.randint(1, 10)
guess = int(input("Guess the number:"))
if guess < secret:
    print("Больше")
elif guess > secret:
    print("меньше")
else:
    print("угадал")
for attempt in range(3):
    # логика тут
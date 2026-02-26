with open("Russia/Russiaday1.txt", "r", encoding="utf-8") as file:
    text = file.read()
punctuation = ".,!?;:-'/*()^\|"

for symbol in punctuation:
    text = text.replace(symbol, "")

text = text.lower()

words = text.split()

alphabet = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")

for letter in alphabet:
    ab_words = [word for word in words if word.startswith(letter)]

    if ab_words:
        ab_words = sorted(set(ab_words))

        with open(f"{letter}", "w", encoding="utf-8") as file:
            for word in ab_words:
                file.write(word + "\n")
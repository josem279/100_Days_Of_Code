import pandas as pd

alpha_letters = pd.read_csv(r"Intermediate_Days\Day26\nato_phonetic_alphabet.csv")
nato_dict = {code.letter: code.code for (index, code) in alpha_letters.iterrows()}

user_input = input(f"Please enter a word you would like to convert to the NATO phonetic alphabet:\n")

nato_response = [nato_dict[letter.upper()] for letter in user_input]

print(f"The response is: {nato_response}")
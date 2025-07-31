import pandas

data = pandas.read_csv(r"Intermediate_Days\Day30\nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

def generate_phonetic():
    try:
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError as e:
        print(f"Sorry, {e} is not a valid word. Only letters in the alphabet please")
        generate_phonetic()
    else:
        print(output_list)
        
generate_phonetic()
invitees = []
with open("Names/invited_names.txt") as names:
    for line in names:
        invitees.append(line.strip())
        
with open("Letters/starting_letter.txt") as letter:
    letter_content = letter.read()
    for name in invitees:
        personalized_letter = letter_content.replace("[name]", name)
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as output_file:
            output_file.write(personalized_letter)
            print(f"Letter for {name} created.")
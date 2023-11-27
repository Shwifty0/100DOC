PLACEHOLDER = '[name]'
# Get the starting letter text
with open("./Input/Letters/starting_letter.txt", 'r') as f:
    data = f.read()
    
# Get the names list
with open("./Input/Names/invited_names.txt", 'r') as f:
    names = f.read().split('\n')
    # Replace names and create text files for every name
    for name in names:
        dedicated_letter = data.replace(PLACEHOLDER, name)
        with open(f"./Ouput/ReadyToSend/letter_to_{name}.txt", "w") as f:
            f.write(dedicated_letter)

import pandas as pd

data = pd.read_csv('de_words.csv')

with open('de_words.txt', "r") as f:
    data = f.readlines()
    st = ""
    for i in range(len(data)):
        with open('clean_data.txt', 'w') as new_f:
            word = data[i].split(' ')
            print(word)
            word.pop()
            st += f"{word[0]}\n"

with open('clean_data.txt', 'w') as f:
    f.write(st)
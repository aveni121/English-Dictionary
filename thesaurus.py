import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def word_meaning(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        print("Did you mean %s instead?" % get_close_matches(w, data.keys())[0])
        choice = input("Please enter (Y/N): ")
        if choice == 'Y' or choice == 'y':
            return get_close_matches(w, data.keys())[0]
        elif choice == 'N' or choice == 'n':
            print("The word does not exist.")
            return "FAIL"
        else:
            print("We didn't understand your entry.")
            return "FAIL"
    else:
        print("The word does not exist. Please double check it.")
        return "FAIL"


word = input("Enter a word: ")

output = word_meaning(word)

if type(output) == list:
    for item in output:
        print(item)
elif output == "FAIL":
        pass
else:
    output = word_meaning(output)
    for index, item in enumerate(output, start = 1):
        print("Definition ",index, ": ",item)
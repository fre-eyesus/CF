word = input("Enter a word: ").lower()
if len(word) >= 10:
    first_char = word[0] 
    last_char =  word[-1]
    middle_length = len(word[1:-1])
    print(f"{first_char}{middle_length}{last_char}")
else:
    print(word)
from termcolor import colored
from getpass import getpass



print(colored("\n\n\n\n\nHello to HANGMAN.", "blue"))
word = getpass(colored("Please enter the word to be guessed: ", "blue")).lower()
print("Okay let's start the game!\n\n\n\n")

counter = 0
hangman = ["  |-----\n  |    \n  |   \n  |   \n  |\n__|__", "  |-----\n  |    O\n  |   \n  |   \n  |\n__|__", "  |-----\n  |    O\n  |    |\n  |   \n  |\n__|__", "  |-----\n  |    O\n  |   ∖|\n  |   \n  |\n__|__", "  |-----\n  |    O\n  |   ∖|∕\n  |   \n  |\n__|__", "  |-----\n  |    O\n  |   ∖|∕\n  |   ∕ \n  |\n__|__","  |-----\n  |    O\n  |   ∖|∕\n  |   ∕ ∖\n  |\n__|__"]

character_options = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

word_lst = [i for i in word]

word_lst_hidden = ["-" for i in range(len(word))]

print(hangman[counter])
print("")
print(word_lst_hidden)
print("\n\n\n")

while True:
    character = input(colored("Enter your guess: ", "blue")).lower()

    if character in character_options:
        if character not in word: 
            counter += 1
            print(colored(character, "red"))
            print(hangman[counter])
            character_options.remove(character)
            if counter == 6:
                print("\n\n\n")
                print(colored("You lose.", "red"))
                print("----------------------------")
                print("\n\n\n")
                break
            print(word_lst_hidden)
            print("\n\n\n")
        else:
            print(colored(character, "green"))
            character_options.remove(character)
            character_index =[i for i in range(len(word)) if word[i] == character]
            for s in range(len(character_index)):
                del word_lst_hidden[character_index[s]]
                word_lst_hidden.insert(character_index[s], character)
            if word_lst == word_lst_hidden:
                print("\n\n\n")
                print(colored("You win!!!", "green"))
                print("The word was:", word.capitalize())
                print("----------------------------")
                print("\n\n\n")
                break
            print(hangman[counter])
            print(word_lst_hidden)
            print("\n\n\n")
    else:
        print("You already had this one. Try another")






 

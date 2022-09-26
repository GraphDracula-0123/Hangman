from termcolor import colored
from getpass import getpass
import requests
import random

def game():
    play_again = "y"
    while play_again == "y":
        print(colored("\n\n\n\n\nHello to HANGMAN.", "cyan", attrs=["bold"]))
        while True:
            choice_random = input(colored("Do you want a random word? Type 'y' for yes or 'n' for no: ", "blue"))
            if choice_random == "y":
                while True:
                    choice_language = input(colored("Do you want german or english words? Type 'g' for german and 'e' for english: ", "blue"))
                    if choice_language == "g":
                        word_site = "http://www.netzmafia.de/software/wordlists/deutsch.txt"
                        break
                    elif choice_language == "e":
                        word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
                        break
                    print("Please enter a valid answer.")
                response = requests.get(word_site)
                WORDS = response.content.splitlines()
                words = []
                for i in range(len(WORDS)):
                    try:
                        words.append(WORDS[i].decode('utf-8'))
                    except:
                        continue
                word = random.choice(words)
                break
            elif choice_random == "n":
                word = getpass(colored("Please enter the word to be guessed (It won't be displayed, but it's there): ", "blue")).lower()
                break
            else: 
                print("Please enter a valid answer")
        print("Okay let's start the game!\n\n\n\n")

        counter = 0
        hangman = ["  |-----\n  |    \n  |   \n  |   \n  |\n__|__", "  |-----\n  |    O\n  |   \n  |   \n  |\n__|__", "  |-----\n  |    O\n  |    |\n  |   \n  |\n__|__", "  |-----\n  |    O\n  |   ∖|\n  |   \n  |\n__|__", "  |-----\n  |    O\n  |   ∖|∕\n  |   \n  |\n__|__", "  |-----\n  |    O\n  |   ∖|∕\n  |   ∕ \n  |\n__|__","  |-----\n  |    O\n  |   ∖|∕\n  |   ∕ ∖\n  |\n__|__"]

        character_options = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

        word_lst = [i for i in word]

        word_lst_hidden = ["_" for i in range(len(word))]

        print(hangman[counter])
        print("")
        for i in word_lst_hidden:
            print(i, end=" ")
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
                        print("The word was:", word.capitalize())
                        print("----------------------------")
                        print("\n\n\n")
                        while True:
                            play_again = input(colored("Do you want to play again? 'y' for yes or 'n' for no: ", "cyan"))
                            if play_again == "y" or play_again == "n":
                                break
                            else:
                                print("Please enter valid answer")
                        break
                    print("\n")
                    for i in word_lst_hidden:
                        print(i, end=" ")
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
                        while True:
                            play_again = input(colored("Do you want to play again? 'y' for yes or 'n' for no: ", "cyan"))
                            if play_again == "y" or play_again == "n":
                                break
                            else:
                                print("Please enter valid answer")
                        break
                    print(hangman[counter])
                    print("\n")
                    for i in word_lst_hidden:
                        print(i, end=" ")
                    print("\n\n\n")
            else:
                print("You already had this one. Try another")
    print(colored("Thanks for playing. See you soon", "cyan"))
    print("\n\n\n")

game()
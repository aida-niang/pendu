#import the necessary libraries :
import random 
import datetime
import names

#######################################################################################
#In the beginning I will define a liste in the same file, containning some words
#Then later, I will create a separated text file
words = ['amina', 'aida', 'yannis']

########################################################################################
#to generate a list of nouns and stock them in an independent file, I can use them as my DB
def generate_n() :
    while True:
        choice_name = input("Do you want to generate man names or woman names? (m/w): ").strip().lower()
        
        if choice_name == 'm':
            chosen_name = names.get_first_name(gender='male')
            save_names(chosen_name)
            return chosen_name

        elif choice_name == 'w':
            chosen_name = names.get_first_name(gender='female')
            save_names(chosen_name)
            return chosen_name
#########################################################################################
#Define the functions :
# This function allows to select randomly an element from the defined list
#I create an empty list and I will fill it with the randomly selected word and its size
def hasard_word() :

    choosen_word = random.choice(words)
    len_word = len(choosen_word)

    return choosen_word, len_word

#########################################################################################
# In this function, I ask the user to fill in the blanks letters, if the letters exists in the selected word, 
# the letter will be appended to the user_word after verification of the emplacement of the letter compared to the selected word
def ask_user(choosen_word, len_word) :
    user_name = input(f"Please, enter your name : ").strip().lower()
    print(f"Hello {user_name}, I have selected randomly a word from the list. It contains {len_word} letters ! ")
    user_word = [' _ ']*len_word #This word is the one the user builds up as4 they go along
    print(f"{user_word}\n")

    score = 0
    while True :
        user_choice = input(f"Please, select a letter from your choice to fill in the blanks : ").strip().lower()
        if user_choice in choosen_word :  #verify if the letter entered by the user exists in the randomly choosen word
            print('Congratulations, you have found one letter of the word !')
            for i in range (0, len_word) :
                if user_choice == choosen_word[i] : #verify the emplacement of the entered letter compared to the emplacement of the letter in the randomly choosen word
                    user_word[i] = user_choice
            score += 1
                    
        else :
            print(f"Unfound letter")
            score -= 1

        print(user_word)

        # I want to join all the found letters in one string, for this I use the function join(), it is the inverse of split(),
        #it allows to assemble the elements of different sequences like tuples or list (the case here)
        word = ''.join(user_word)
        if ' _ ' not in user_word :
            print(f"Congratulations. You have found the word, it is : {word}")
            break
    return user_word, score, user_name
###########################################################################################
#Here I ask the user if he wants to launch again the game
def play_again() :  
    retry = input(f"Do you want to play again ? (yes/no) :").strip()   
    return retry == 'yes'
       
#############################################################################################
# This function affects the score for each player depending if he finds or not the word
def score_player(user_name, score) :
    if score > 0 :
        print(f"Player n°1 : {user_name} has {score} points")
        
    elif score < 0 :
        print(f"You lost. Good luch for the next time!")

    save_score(user_name, score)
##########################################################################################
# Create 3 function saving, reading ans clearing the data (time, user name and score)
def save_score(user_name, score):
    try:
        current_time = datetime.datetime.now().strftime("%A %d %B %Y à %H:%M:%S")
        score_entry = f"{current_time} - {user_name} : {score}"
        with open("score.txt", "a", encoding="utf-8") as file:
            file.write(score_entry + "\n")
    except Exception as e:
        print(f"An error occurred while saving score file: {e}")

def read_score():
    try:
        with open("score.txt", "r") as file:
            score_f = file.readlines()
            if not score_f:
                print("No operations in score file.")
            else:
                print("The scores are :")
                for line in score_f:
                    print(line.strip())
    except FileNotFoundError:
        print("No score file found.")
    except Exception as e:
        print(f"An error occurred while reading score file: {e}")

def clear_score():
    try:
        with open("score.txt", "w") as file:
            file.truncate(0)
        print("Score file cleared successfully.")
    except Exception as e:
        print(f"An error occurred while clearing score file: {e}")

#############################################################################################
# Create 3 functions to save the generated names from the library names, read and clear them
def save_names(name):
    try:
        names_entry = f" - {name}"
        with open("names.txt", "a", encoding="utf-8") as file:
            file.write(names_entry + "\n")
    except Exception as e:
        print(f"An error occurred while saving names file: {e}")

def read_names():
    try:
        with open("names.txt", "r") as file:
            names_f = file.readlines()
            if not names_f:
                print("There is no names.")
            else:
                print("The generated names:")
                for line in names_f :
                    print(line.strip())
    except FileNotFoundError:
        print("No names file found.")
    except Exception as e:
        print(f"An error occurred while reading names file: {e}")

def clear_names():
    try:
        with open("names.txt", "w") as file:
            file.truncate(0)
        print("Names file cleared successfully.")
    except Exception as e:
        print(f"An error occurred while clearing names file: {e}")


############################################################################################
#Create the menu
def display_menu(): 
    print(f"\nWelcome to Our hangman game !")
    print(f"\n****** Menu *******")
    print(f"1. Launch the game")
    print(f"2. View score file")
    print(f"3. Clear score file")
    print(f"4. Generate names randomly")
    print(f"5. View names file")
    print(f"6. Clear names file")
    print(f"7. Exit")

#############################################################################################
#The main loop of the game
try:
    while True:
        display_menu()
        choice = input(f"Choose an option (1 - 2 - 3 - 4 - 5 - 6) :")
        if choice == '1' :
            choosen_word, len_word = hasard_word()
            user_word, score, user_name = ask_user(choosen_word, len_word)
            score_player(user_name, score)
            if not play_again():
                print("Thank you for playing. Come back soon!")
                break
        elif choice == '2' :
            read_score()
            break
        elif choice == '3' :
            while True:  
                confirm = input("Do you really want to clear the score file ? (yes/no): ").strip().lower()
                if confirm == "yes":
                    clear_score()
                    break  
                elif confirm == "no":
                    print("The score file not cleared.")
                    break  
                else:
                    print("Invalid input. Please type 'yes' or 'no'.")
                    break
        elif choice == '4' :
            generate_n()
        elif choice == '5' :
            read_names()
            break
        elif choice == '6' :
            while True:  
                confirm = input("Do you really want to clear the names file ? (yes/no): ").strip().lower()
                if confirm == "yes":
                    clear_names()
                    break  
                elif confirm == "no":
                    print("The names file not cleared.")
                    break  
                else:
                    print("Invalid input. Please type 'yes' or 'no'.")
                    break

        elif choice == '7' :
            print("\nExiting the game...")
            exit()
except KeyboardInterrupt:
    print("\nExiting the game...")
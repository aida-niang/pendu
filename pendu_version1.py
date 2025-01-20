#import the necessary libraries :
import random 

#######################################################################################
#In the beginning I will define a liste in the same file, containning some words
#Then later, I will create a separated text file
words = ['amina', 'aida', 'yannis']

#########################################################################################
#Define the functions :
# This function allows to select randomly an element from the defined list
#I create an empty list and I will fill it with the randomly selected word and its size
def hasard_word() :
    global len_word, choosen_word  #Here I created the global variable in order to use it in another function
    my_data = []

    choosen_word = random.choice(words)
    len_word = len(choosen_word)

    my_data.append(choosen_word)
    my_data.append(len_word)
    
    #I want to acceed to the word index (see down)
    # index0 = choosen_word[0]
    # index1 = choosen_word[1]
    # index2 = choosen_word[2]
      

    print(my_data)

###########################################################################################
# In this function, I ask the user to fill in the blanks letters, if the letters exists in the selected word, 
# the letter will be appended to the user_word after verification of the emplacement of the letter compared to the selected word
def ask_user() :
    print(f"I have selected randomly a word from the list. It contains {len_word} letters ! ")
    user_word = [' _ ']*len_word #This word is the one the user builds up as they go along
    print(f"{user_word}\n")

    
    while True :
        user_choice = input(f"Please, select a letter from your choice to fill in the blanks : ").strip()

        if user_choice in choosen_word :  #verify if the letter entered by the user exists in the randomly choosen word
            print('Congratulations, you have found one letter of the word !')
            for i in range (0, len_word) :
                if user_choice == choosen_word[i] : #verify the emplacement of the entered letter compared to the emplacement of the letter in the randomly choosen word
                    user_word[i] = user_choice
                    
        else :
            print(f"Unfound letter")

        print(user_word)

        # I want to join all the found letters in one string, for this I use the function join(), it is the inverse of split(),
        #it allows to assemble the elements of different sequences like tuples or list (the case here)
        word = ''.join(user_word)
        

        if ' _ ' not in user_word :
            print(f"Congratulations. You have found the word, it is : {word}")
            break


############################################################################################
#call the function (maybe another function calling main in which we put a loop?????)
hasard_word()
ask_user()
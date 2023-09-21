#Import Trie class from Trie.py
from trie import Trie

#Create a variable to keep track of whether the user wants to keep searching
search_running = True
#Create Trie object
trie = Trie()

#Create a while loop to keep asking the user what they want to do until they quit
while search_running:
   #Ask the user what they want to do
    user_choice = input(str("""What action would you like to perform?
'1': Add a word to Trie
'2': Check if a word is in Trie
'3': Check for substring
'4': Print Trie
'5': Quit\n"""))
    
    #Try to perform the action the user wants to do1
    try:
        #If the user wants to add a word, ask them what word they want to add and call add_word
        if user_choice == '1':
            word = input(str("What word would you like to add?\n"))
            trie.add_word(word)
        #If the user wants to check if a word is in the Trie, ask them what word they want to check and call check_for_word
        elif user_choice == '2':
            word = input(str("What word would you like to check?\n"))
            print(trie.check_for_word(word))
        #If the user wants to check for a substring, ask them what substring they want to check for and call substring_check
        elif user_choice == '3':
            substring = input(str("What substring would you like to check?\n"))
            print(trie.substring_check(substring))
        #If the user wants to print the Trie, call print_words
        elif user_choice == '4':
            trie.print_words()
        #If the user wants to quit, set search_running to False and end program
        elif user_choice == '5':
            search_running = False
            print("Goodbye!")
    #Handles exceptions if the user enters an invalid choice and asks them to make choice again
    except:
        print("Invalid choice, please select from menu choices\n")


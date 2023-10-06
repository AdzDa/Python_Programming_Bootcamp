#Problem 1(Writing for loops to iterate over a list)
#You have a list of Disney characters and you want to find out if each of them contain i, o, or u in their names. Loop through each character in the list and print out the following:

disney_characters = ["simba", "ariel", "pumba", 
                     "flounder", "nala", "ursula",
                     "scar", "flotsam", "timon"]

for x in range(len(disney_characters)):
    if disney_characters[x].__contains__("i") == True: 
        print(disney_characters[x],", I bet you're Impressively Intelligent!")
    elif disney_characters[x].__contains__("u") == True: 
        print(disney_characters[x],", U are so Uniquely U!")
    elif disney_characters[x].__contains__("o") == True: 
        print(disney_characters[x],", O My! How Original!")
    else:
        print(disney_characters[x],", Ehh, a's and e's are so ordinary.")


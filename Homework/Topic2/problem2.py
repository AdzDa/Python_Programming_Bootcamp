# Problem 2: I Came, I 'Saur, I Conquered
# Writing conditionals with multiple conditions

angry = True
bored = True
hungry = False
tired = False

if angry and hungry and bored:      #True && False && True = False
    print("The T-Rex will eat the Triceratops.")        #Not printed
elif tired and hungry:      #False && False = False
    print("The T-Rex will eat the Iguanadon.")      #Not printed
elif hungry and bored:      #False && True = False
    print("The T-Rex will eat the Stegasaurus.")        #Not printed
elif tired:     #False
    print("The T-Rex will go to sleep")     #Not printed
elif angry and bored:       #True && True = True
    print("The T-Rex will fight with the Velociraptor.")        #Printed as the first True statement
elif angry or bored:        #True || True = True
    print("The T-Rex roars")
else:
    print("The T-Rex gives a toothy smile.")
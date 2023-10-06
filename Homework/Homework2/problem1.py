# Part 2: Code Challenges
# Problem 1: Most Clocks Are Normal, But Some Are Cuckoo!
# Writing conditionals

#12hr system but only the hr part is considered
time = 21

if time < 9:        #9am=0900
    print("Morning is wonderful. Its only drawback is that it comes at such an inconvenient time of day.")
elif time <= 16:    #4pm=1600
    print("Working hard or hardly working?")
elif time < 20:     #8pm=2000
    print( "How did it get so late so soon?")
elif time < 22:     #10pm=2200
    print("A day without sunshine is like, you know, night.")
else :      #Between 2200 to 2400
    print("Burning the midnight oil!")
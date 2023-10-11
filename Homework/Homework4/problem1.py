"""
Problem 1: I Love You, Tuple
Create some print statements that access the appropriate values inside each tuple to produce the expected output.
    Tuple(can't edit, yes2index):  Var_Name = ()

My favorite romance movies
title, release year, runtime, tagline, main characters
"""

romantic_movie1 =   ("The Princess Bride", 1987, 98, "The story of a man and a woman who lived happily ever after.", 
                    ["Buttercup", "Westley", "Fezzik", "Inigo Montoya", "Vizzini"])

romantic_movie2 =   ("Groundhog Day", 1993, 101, "He's having the day of his life…over and over again.", 
                    ["Phil Connors"])

romantic_movie3 =   ("Amélie", 2001, 122, "One person can change your life forever.",
                    ["Amélie Poulain", "Nino Quincampoix", "The Garden Gnome"])

print("First Method:")
print("Here are my favorite romance movies:\n")
print(f"\t{romantic_movie1[0]} ({romantic_movie1[1]}): {romantic_movie1[3]}\n")
print(f"\t{romantic_movie2[0]} ({romantic_movie2[1]}): {romantic_movie2[3]}\n")
print(f"\t{romantic_movie3[0]} ({romantic_movie3[1]}): {romantic_movie3[3]}")

"""
Bonus:
    Change the print statement's separator character to an empty string "" instead of a space so that
    you can print the year as (1987) instead of ( 1987 ).
"""
print("\n\nSecond Method:\n")
print("\t" + romantic_movie1[0] + " (" + str(romantic_movie1[1]) + "):" + " " + romantic_movie1[3] + "\n")
a = " "     #Other; empty space str variable
print("\t" + romantic_movie2[0] + a + "(" + str(romantic_movie2[1]) + "):" + a + romantic_movie2[3] + "\n")
print("\t" + romantic_movie3[0] + " (" + str(romantic_movie3[1]) + "):" + " " + romantic_movie3[3])
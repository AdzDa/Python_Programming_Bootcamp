# Problem 2: Writing while loops.
    # It's 90 degrees Fahrenheit and you are sweating buckets! Luckily you have air conditioning, 
    # but it's really old and kind of finicky. It cools the room by three degrees and shuts off, 
    # so you have to keep turning it back on until the temperature gets to where you want it to be.
    # Seventy five sounds much more pleasant than 90, so that's what you're shooting for

    # While the temperature is greater than 75 degrees Fahrenheit, print "The temperature is XX — crank the AC!" 
    # and subtract 3 degrees from the temperature.
    # Once the temperature is cool enough and the loop is done, print "75. Ahh, that's better."

temperature = 90

while temperature != 75:
    print("Temperature is", temperature, " — crank the AC!")
    temperature -= 3
print("75. Ahh, that's better.")

import markovify
import random
import time
from math import *
import os
import sys
from numpy.random import multinomial

# Queen Album Generator - by Matthack
# Relatives paths

script_path = os.path.abspath(__file__)
script_dir = os.path.split(script_path)[0]

queentxt_path = "queen.txt"
queen_path = os.path.join(script_dir, queentxt_path)

titretxt_path = "titresqueen.txt"
titre_path = os.path.join(script_dir, titretxt_path)

albumtxt_path = "album.txt"
album_path = os.path.join(script_dir, albumtxt_path)

# Lyrics (using markovify)

with open(queen_path) as f:
    paroles = f.read()

paroles_model = markovify.NewlineText(paroles)
    
# Song title (using markovify too)

with open(titre_path) as f:
    titre = f.read()

titre_model = markovify.NewlineText(titre)

# Album title (still using markovify)

with open(album_path) as f:
    album = f.read()

album_model = markovify.NewlineText(album)

# Song numbers and duration
nbchansons = random.randint(9,13) # Random song number
nbfaceB = ceil(nbchansons/2) # Number of songs on side B of the record (there are usually more songs on side B than on side A)
nbfaceA = nbchansons - nbfaceB # Remaining number of songs (which is the number of songs on side A)

maxfaceA = random.randint(1006,1434) # Duration of side A in seconds
maxfaceB = random.randint(1080,1498) # Duration of side B in seconds
cfaceA = 1 # number of the song for side A (no longer unused)
cfaceB = 1 # same thing but for side B (no longer unused too) 
chansonmax = random.randint(229,500) # duration of one song in seconds
faceA = multinomial(maxfaceA, [1/nbfaceA] * nbfaceA) # A function that gives each song a duration in a way that their total duration doesn't exceed the maximum duration of one side
faceB = multinomial(maxfaceB, [1/nbfaceB] * nbfaceB) # same thing, but for side B
songnumber = 0 # Variable used for referencing the durations of the songs in the list given by the above function.*

# Seconds to min conversion (a very nice function for on-the-fly minutes to seconds conversion)
def convert(seconds): 
	min, sec = divmod(seconds, 60) 
	return "%02d min %02d sec" % (min, sec) 

# haha album machine goes brrr (actual text generation)
# Side A

def chansonA():
    global songnumber
    global nbfaceA
    global cfaceA
    for i in range (nbfaceA):
        print("A{} - {}".format(cfaceA,titre_model.make_sentence(tries=1000))) # Prints the song title
        print("Song duration:",convert(faceA[songnumber])) # Prints the song duration, taken and converted from the 'faceA' array
        cfaceA = cfaceA + 1 # Number of the current song (different for each face)
        songnumber = songnumber + 1 # Add one to the variable to grab the duration of the next song
        print("Lyrics :")                        #                      #
        for i in range(random.randint(45, 80)):  # Prints the lyrics    #
            print(paroles_model.make_sentence()) #                      #
        print(" ")

# Side B
        
def chansonB():
    global songnumber
    global nbfaceB
    global cfaceB
    for i in range (nbfaceB):
        print("B{} - {}".format(cfaceB,titre_model.make_sentence(tries=1000)))  #***************************#
        print("Song duration:",convert(faceB[songnumber]))                      #                           #
        songnumber = songnumber + 1                                             #  Same as side A,          #
        cfaceB = cfaceB + 1                                                     #                           #
        print("Lyrics :")                                                       #  but for side B.          #
        for i in range(random.randint(45, 80)):                                 #                           #
            print(paroles_model.make_sentence())                                #***************************#
        print(" ")
    
# Render
print("Queen Album Generator - Made by Matthack")
print("Album name:", album_model.make_sentence(tries=1000)) # Generates an album title
print("Year:", random.randint(1973, 1991)) # Generates a year
print("Number of tracks:", nbfaceA + nbfaceB)
print("Total length of the album :",convert(maxfaceA + maxfaceB))
print(" ")
print("SIDE A -",nbfaceA,"songs --- Duration :",convert(maxfaceA)) # Prints the duration and the number of songs on side A
print(" ")
print("SIDE A :")
print(" ")
chansonA()
songnumber=0 # Resets the variable because the durations of the songs on side B is in a separate array
print("SIDE B -",nbfaceB,"songs --- Duration :",convert(maxfaceB)) # Same thing as side A
print(" ")
chansonB()

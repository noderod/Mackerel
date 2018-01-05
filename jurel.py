"""
BASICS

Provided a topic, finds the information in wikipedia, summarizes it accordingly
to the user's slides number and returns it to the main program.
"""

import wikipedia
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
import os, sys
import gc



# Checks if any of the following elements are present in a list, True if correct
# ltc (list): List to check
# el2c (list): elements to be checked in the list

def anyelem(ltc, el2c):

    for thisel in el2c:
        if thisel in ltc:
            return True
    else:
        return False



################################################################################
# ACTUAL DEVELOPMENT
################################################################################


postopic = str(sys.argv[1]) # 'Augustus'

# Creates a new for the presentation
if len(sys.argv) <= 2:
    pw_title = postopic
else:
    pw_title = ''

    for hh in range(2, len(sys.argv)):
        pw_title += str(sys.argv[hh])+' '

wiktop = wikipedia.page(postopic).content


sumtop = wikipedia.summary(postopic, sentences = 1)

# List of words which indicates a certain topic

artictop = {
    'person' : ['activist', 'actor', 'artist', 'bussinessman', 'CEO', 'designer',
                'doctor', 'emperor', 'entrepeneur', 'inventor', 'king', 'photographer',
                'politician', 'polymath', 'president', 'producer', 'prophet'],
    'place' : ['capital', 'city', 'country', 'municipality', 'prefecture', 'state',
              'town', 'village'],
    'art' : ['statue', 'painting', 'film', 'movie'],
    'common object' : [],
    'lifeform' : ['animal', 'bacteria', 'organism', 'plant', 'protozoo', 'species'],
    'religion' : ['relig', 'theism'],
    'ideology' : ['politic']
}


# Determines the topic of the article
notfound = True

for postt in artictop.keys():

    for identifier in artictop[postt]:
        if identifier in sumtop.lower():
            topic = postt
            notfound = False
            break

    if notfound == False:
        break


print(topic)


# If the topic is a person, then there are several things needed
if topic == 'person':
    occupations = []
    for posocc in artictop['person']:
        if posocc in sumtop:
            occupations.append(posocc)

    # Obtains the birth-death dates
    repbar = sumtop.replace('(', '|||').replace(')', '|||').split('|||')
    for elem in repbar:
        if ';' in elem:
            birdea = elem
            break

    birdea = birdea.split(';')[1]
    birdea = birdea.split('–') # This is not a keyboard key
    if len(birdea) == 1:
        # Still alive
        Bdat = birdea[0]
        Ddat = 'Alive'
    else:
        Bdat = birdea[0]
        Ddat = birdea[1]


# Dumps all the content into a text file, except the last part
tobeus = wiktop.split('== See also ==')


# Skips the titles
actualtext = tobeus[0].replace('=', '\n')
gc.collect()


# Transforms the unicode into ascii to avoid future problems
tobeus_enc = actualtext.encode('ascii', errors='ignore').decode()

with open('Tempfile___.txt', 'w') as lolfil:
    lolfil.write(tobeus_enc)


thefile = "Tempfile___.txt" #name of the plain-text file
parser = PlaintextParser.from_file(thefile, Tokenizer("english"))
summarizer = LexRankSummarizer()

summary = summarizer(parser.document, 15) #Summarize the document with 5 sentences

print(sumtop)

for sentence in summary:
    # Skips contents already looked over and possible titles
    if (anyelem(str(sentence), ['born', 'died in']) == True) or (len(str(sentence).split()) < 5):
        continue

    print(sentence)

# summarizes the text file using the number of slides provided by the user
os.remove('Tempfile___.txt') # Removes the file
gc.collect


# Creates a new presentation and a title slide with the name provided
print(pw_title)

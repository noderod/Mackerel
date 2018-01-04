"""
BASICS

Provided a topic, finds the information in wikipedia, summarizes it accordingly
to the user's slides number and returns it to the main program.
"""

import wikipedia
import sumy
import os

# No actual functions being developed, experimental so far

postopic = 'Augustus'

wiktop = wikipedia.page(postopic).content


# Nature of the article
topicart = ['person', 'place', 'art', 'common object', 'lifeform', 'religion','ideology']


sumtop = wikipedia.summary(postopic, sentences = 1)
print(sumtop)

# List of words which indicates a certain topic

artictop = {
    'person' : ['activist', 'actor', 'artist', 'bussinessman', 'CEO', 'designer',
                'emperor', 'entrepeneur', 'founder', 'inventor', 'king', 'polymath',
                'producer'],
    'place' : ['country', 'state'],
    'art' : [],
    'common object' : [],
    'lifeform' : ['species'],
    'religion' : ['relig'],
    'ideology' : []
}


# Determines the topic of the article

for postt in artictop.keys():
    if postt in sumtop.lower():
        topic = postt
        break

    for identifier in artictop[postt]:
        if identifier in sumtop.lower():
            topic = postt
            break


print(topic)

# Obtains the information in parenthesis
repbar = sumtop.replace('(', '|||').replace(')', '|||').split('|||')[1]



# Finds the name of the sections


# Identifies if the URL is about a person, place, or thing

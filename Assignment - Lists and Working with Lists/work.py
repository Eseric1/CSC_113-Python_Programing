# Eric Samano
# Chapter 3 & 4 - Lists

import random
# ask the user whether they want to use default data or enter their own words
choice = input("Do you want to use default data or enter your own words? (y/n): ")

# if the user chooses to enter their own words, input the data from the user
if choice == "y":
  # input 3 nouns and store them in a noun list
  noun_list = []
  for noun in range(3):
    noun = input("Enter a noun: ")
    noun_list.append(noun)
# input  verbs and store in list
  verb_list = []
  for i in range(3):
    verb = input("Enter a verb: ")
    verb_list.append(verb)
# input adjectives and store list
  adjective_list = []
  for i in range(3):
    adjective = input("Enter an adjective: ")
    adjective_list.append(adjective)
# input 2 articles and store them in an article list
  article_list = []
  for i in range(2):
    article = input("Enter an article: ")
    article_list.append(article)

# if the user chooses to use the default words, hard code four lists with your own words
else:
  # hard code noun list
  noun_list = ["puppy", "deer", "rabbit", "girl", "monkey"]
  # hard code verb list
  verb_list = ["runs", "hits", "jumps", "creeps", "cries"]
  # hard code adjective list 
  adjective_list = ["adorable", "clueless", "dirty", "odd", "silly"]
  # hard code article list 
  article_list = ["the", "a"]

# Create 3 unique sentences 
for i in range(3):
  # randomly selects an article 
  article = random.choice(article_list)
  # randomly select an 
  adjective = random.choice(adjective_list)
  # randomly select a noun 
  noun = random.choice(noun_list)
  # randomly select a verb 
  verb = random.choice(verb_list)

  # print the sentence
  sentence = article + " " + adjective + " " + noun + " " + verb + "."
  print(sentence)
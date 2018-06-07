from scripts import intent_classifier
from scripts import entity_classifier
import json
import nltk
from nltk.stem.lancaster import LancasterStemmer

def answer(question):
	
	intent=intent_classifier.predict(question)
	entity=entity_classifier.entity(question)


	read_file = open("datasets/desc_sol.json")
	data = json.load(read_file)

	ite=data['items']
	if type(entity)==str:
		for d in ite:
			if entity==d['title'].lower():
				if intent=="Code":
					print("Work under progress")
					ques=input("enter another question ")
					answer(ques)
				else:
					print(d[intent])
	else:
		print(entity)
		ques=input("enter your choice ")
		answer(ques)	

question=input("Enter Question ")
answer(question)


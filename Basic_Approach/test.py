from scripts import intent_classifier
from scripts import entity_classifier
from scripts import code_classify
import json
import nltk
from nltk.stem.lancaster import LancasterStemmer

def answer(question):
	
        intent=intent_classifier.predict(question)
        if intent=="Description" or intent=="Solution":
                   des_sol(question,intent)
        else:
                   code(question,intent)


def des_sol(question,intent):
        entity=entity_classifier.entity(question)
        read_file = open("datasets/desc_sol.json")
        data = json.load(read_file)
        ite=data['items']
        if type(entity)==str:
            for d in ite:
                 if entity==d['title'].lower():
                      if intent=="Description":
                          print("Description is : "+ d[intent])
                          intent="NULL"
                      else:
                          print("Solution is : "+ d[intent])
                          intent="NULL"
                      ques=input("\n Do you have more Questions Y/N ")
                      if(ques=="y" or ques=="Y"):
                          question=input("Enter new question ")
                          answer(question)
                      else:
                          print("Thanks for using ")
        else:
             print("Please select from these options ")
             print(entity)
             question=input("enter your choice ")
             des_sol(question,intent)
               
def code(question,intent):
        code_entity=code_classify.entity(question)
        read_file = open("datasets/code_data.json")
        code_data = json.load(read_file)
        code_ite=code_data['items']
        if len(code_entity)==2:
            entity=str(code_entity[0].strip("\n").lower())
            lang=str(code_entity[1].strip("\n").lower())
            for d in code_ite:
                 if entity==d['title'].lower():
                      print(d['content'])
                      print("\n Code language is " + d['code_lang'])
                      intent="NULL"
                      ques=input("\n Do you have more Questions Y/N ")
                      if(ques=="y" or ques=="Y"):
                          question=input("Enter new question ")
                          answer(question)
                      else:
                          print("Thanks for using")

        else:
             print("Please select from these options ")
             print(code_entity)
             question=input("enter your choice ")
             code(question,"Code")

question=input("Enter Question ")
answer(question)


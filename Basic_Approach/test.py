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
                   lang=None
                   code(question,intent,lang)


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
                          break
                      else:
                          print("Solution is : "+ d[intent])
                          intent="NULL"
                          break

            ques=input("\n Do you have more Questions Y/N ")
            if(ques=="y" or ques=="Y"):
                question=input("Enter new question ")
                answer(question)
            else:
                print("Thanks for using ")
        else:
             if len(entity)>0:
                print("Please select from these options ")
                print(entity)
                question=input("enter your choice ")
                des_sol(question,intent)
             else:
                print("Please be more specific ")
                question=input("enter your question again ")
                answer(question)
                               
def code(question,intent,language):
        code_entity=code_classify.entity(question)
        read_file = open("datasets/code_data.json")
        code_data = json.load(read_file)
        code_ite=code_data['items']
        code_languages=[]
        count=0
        if len(code_entity)==2:
            entity=str(code_entity[0].strip("\n").lower())
            language=str(code_entity[1].strip("\n").lower())
            for d in code_ite:
                 if entity==d['title'].lower():
                    code_languages.append(d['code_lang'])
            for d in code_ite:
                 if entity==d['title'].lower() and language in code_languages:
                    if language==d['code_lang'].lower():
                       print(d['content'])
                       print("\n Code language is " + d['code_lang'])
                       count=count+1

                 
            if count==0:
                    entity=str(code_entity[0].strip("\n").lower())      
                    print(code_languages)
                    lang=input("Select a language ")
                    for d in code_ite:
                        if entity==d['title'].lower() and lang in code_languages:
                              if lang==d['code_lang'].lower():
                                 print(d['content'])
                                 print("\n Code language is " + d['code_lang'])
                                 count=count+1





            ques=input("\n Do you have more Questions Y/N ")
            if(ques=="y" or ques=="Y"):
                   question=input("Enter new question ")
                   answer(question)
            else:
                   print("Thanks for using")

        else:
             language=None
             print("Please select from these options ")
             print(code_entity)
             
             question=input("enter your choice ")
             code(question,"Code",language)

question=input("Enter Question ")
answer(question)



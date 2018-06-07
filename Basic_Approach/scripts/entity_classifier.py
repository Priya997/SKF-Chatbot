from rake_nltk import Rake
import nltk
def data():
    with open("datasets/entity_data.txt") as title:
        title=title.readlines()
    return title

def phrase(ques):
    phrase=[]
    new_list=[]
    r=Rake()
    question=ques
    r.extract_keywords_from_text(question)
    phrase=r.get_ranked_phrases()
    for items in phrase:
        new_list.extend(items.lower().split())
    return new_list    

def lis(l):
    new_l=l
    ans=[]
    title=data()
    for i in new_l:
        i=i.lower()
        i=i.strip("\n")
        for t in title:
            t=t.lower()
            if i in t:
                ans.append(t)

    return ans

def entity(ques):
    count=0
    list_p=phrase(ques)
    ans=lis(list_p)
    for i in ans:
        i=i.strip("\n")
        i=i.lower()
        if i in ques.lower():
            count=count+1
            ent=i
            
            break
    if count==1:
        return ent
    else:
        if len(ans)==1:
           abc=ans[0]
           abc=abc.lower().strip("\n")
           return abc
        else:
           print("Select from these\n")
           return ans


    
        


#question=input("Enter question")
#entity(question)

import json
with open("data.json", "r") as read_file:
    data = json.load(read_file)

a=data['items']
des=[]
title=[]
con=[]
for d in a:
	title.append((d['title']))
	
ques=[]
sol=[]
code=[]

for t in title:
	ques.append("What is "+ t + " ?")
	ques.append("What does "+ t + " mean ?")
	ques.append("Tell me something about "+ t + " ?")
	ques.append(t)
	ques.append("Explain " + t +" ?")
	ques.append("Elaborate " + t +" ?")
	ques.append("Can you tell me about " + t + " ?")
	ques.append("What do you know about " + t + " ?")
	ques.append("What can you tell me about " + t + " ?")
	ques.append("I want to know about XSS " + t )
	ques.append("Do you have information about " + t + " ?")

for t in title:
        sol.append("How to solve "+ t + " ?")
        sol.append("How to resolve "+ t + " ?")
        sol.append("How to mitigate "+ t + " ?")
        sol.append("How to stop "+ t + " ?")
        sol.append("How to defend "+ t + " ?")
        sol.append("How to get secured against "+ t + " ?")

for t in title:
        code.append("Give me some sample code of "+ t )
        code.append("Code example of "+ t + " ?")
        code.append("Code of "+ t )
        
	

data=open("naive_data.json","w")
i=1;

for x in ques:
	data.write("{")
	data.write('"Class": '+ json.dumps("Description")+",")
	data.write('"Question": '+ json.dumps(x))
	data.write("}\n")

for y in sol:
	data.write("{")
	data.write('"Class": '+ json.dumps("Solution")+",")
	data.write('"Question": '+ json.dumps(y))
	data.write("} \n")
	
for z in code:
	data.write("{")
	data.write('"Class": '+ json.dumps("Code")+",")
	data.write('"Question": '+ json.dumps(y))
	data.write("}\n")
	

data.close()


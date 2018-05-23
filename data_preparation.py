import json
with open("kb_item_data.json", "r") as read_file:
    data = json.load(read_file)

a=data['items']
des=[]
title=[]
con=[]
for d in a:
	title.append((d['title']))
	con=d['content'].split("\n\n")
	des.append(con[1])
	del con[:]
	#a=dict()
	#print(d['items'])
	#print(a['title'])
#x=a['content'].split("\n\n")
#print(x[1])
#print(data['items'][2])

#print(des)
#print(title)

#print(json.dumps(title))
ques=[]
ques_list=[]
for t in title:
	ques.append("What is "+ t + " ?")
	ques.append("What does "+ t + " mean ?")
	ques.append("Tell me something about "+ t + " ?")
	ques.append(t)
	ques_list.append(ques)
	ques=[]

#print(ques_list)

#print(dict(zip(title,des)))
#print(ques_list)
#print(des)
#print(ques_list)
#with open("abc.json", 'w') as outfile:
 #   json.dumps(ques_list, indent=4)
    #json.dump(des,outfile)
data=open("data_set.json","w")
i=1;
print(len(des))
data.write("{\n"+'"items": [\n')
for x,y in zip(ques_list,des):
	data.write("{")
	data.write('"Id": '+ json.dumps(i)+", ")
	data.write('"Ques": '+ json.dumps(x)+",")
	data.write('"Ans": '+ json.dumps(y))
	if i<len(des):
		data.write("},\n")
	else:
		data.write("}\n")
	i=i+1
data.write("]\n"+"}")
data.close()

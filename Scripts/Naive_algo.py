# use natural language toolkit
import json
import nltk
from nltk.stem.lancaster import LancasterStemmer
# word stemmer
stemmer = LancasterStemmer()
training_data=[]
#with open("new.txt", "r") as read_file:
 #   data = read_file.readlines()
#for i in data:
 #    training_data.append(i)
#training_data=training_data.split(",")
#print(training_data[1])



training_data.append({"Class": "Description","Question": "What is Filename injection Path traversel ?"})
training_data.append({"Class": "Description","Question": "What does Filename injection Path traversel mean ?"})
training_data.append({"Class": "Description","Question": "Tell me something about Filename injection Path traversel ?"})
training_data.append({"Class": "Description","Question": "Filename injection Path traversel"})
training_data.append({"Class": "Description","Question": "Explain Filename injection Path traversel ?"})
training_data.append({"Class": "Description","Question": "Elaborate Filename injection Path traversel ?"})
training_data.append({"Class": "Description","Question": "Can you tell me about Filename injection Path traversel ?"})
training_data.append({"Class": "Description","Question": "What do you know about Filename injection Path traversel ?"})
training_data.append({"Class": "Description","Question": "What can you tell me about Filename injection Path traversel ?"})
training_data.append({"Class": "Description","Question": "I want to know about XSS Filename injection Path traversel"})
training_data.append({"Class": "Description","Question": "Do you have information about Filename injection Path traversel ?"})
training_data.append({"Class": "Description","Question": "What is xss injection ?"})
training_data.append({"Class": "Description","Question": "What does xss injection mean ?"})
training_data.append({"Class": "Description","Question": "Tell me something about xss injection ?"})
training_data.append({"Class": "Description","Question": "xss injection"})
training_data.append({"Class": "Description","Question": "Explain xss injection ?"})
training_data.append({"Class": "Description","Question": "Elaborate xss injection ?"})
training_data.append({"Class": "Description","Question": "Can you tell me about xss injection ?"})
training_data.append({"Class": "Description","Question": "What do you know about xss injection ?"})
training_data.append({"Class": "Description","Question": "What can you tell me about xss injection ?"})
training_data.append({"Class": "Description","Question": "I want to know about XSS xss injection"})
training_data.append({"Class": "Description","Question": "Do you have information about xss injection ?"})
training_data.append({"Class": "Solution","Question": "How to solve Filename injection Path traversel ?"}) 
training_data.append({"Class": "Solution","Question": "How to resolve Filename injection Path traversel ?"}) 
training_data.append({"Class": "Solution","Question": "How to mitigate Filename injection Path traversel ?"}) 
training_data.append({"Class": "Solution","Question": "How to stop Filename injection Path traversel ?"}) 
training_data.append({"Class": "Solution","Question": "How to defend Filename injection Path traversel ?"}) 
training_data.append({"Class": "Solution","Question": "How to get secured against Filename injection Path traversel ?"}) 
training_data.append({"Class": "Solution","Question": "How to solve xss injection ?"}) 
training_data.append({"Class": "Solution","Question": "How to resolve xss injection ?"}) 
training_data.append({"Class": "Solution","Question": "How to mitigate xss injection ?"}) 
training_data.append({"Class": "Solution","Question": "How to stop xss injection ?"}) 
training_data.append({"Class": "Solution","Question": "How to defend xss injection ?"}) 
training_data.append({"Class": "Solution","Question": "How to get secured against xss injection ?"}) 
training_data.append({"Class": "Solution","Question": "How to solve Command injection ?"}) 
training_data.append({"Class": "Solution","Question": "How to resolve Command injection ?"}) 
training_data.append({"Class": "Solution","Question": "How to mitigate Command injection ?"}) 
training_data.append({"Class": "Solution","Question": "How to stop Command injection ?"}) 
training_data.append({"Class": "Solution","Question": "How to defend Command injection ?"}) 
training_data.append({"Class": "Solution","Question": "How to get secured against Command injection ?"})
training_data.append({"Class": "Code","Question": "How to get secured against not available item ?"})
training_data.append({"Class": "Code","Question": "How to get secured against not available item ?"})
training_data.append({"Class": "Code","Question": "How to get secured against not available item ?"})
training_data.append({"Class": "Code","Question": "How to get secured against not available item ?"})
training_data.append({"Class": "Code","Question": "How to get secured against not available item ?"})
training_data.append({"Class": "Code","Question": "How to get secured against not available item ?"})
training_data.append({"Class": "Code","Question": "How to get secured against not available item ?"})
training_data.append({"Class": "Code","Question": "How to get secured against not available item ?"})
training_data.append({"Class": "Code","Question": "How to get secured against not available item ?"})
training_data.append({"Class": "Code","Question": "How to get secured against not available item ?"})
training_data.append({"Class": "Code","Question": "How to get secured against not available item ?"})
training_data.append({"Class": "Code","Question": "How to get secured against not available item ?"})
training_data.append({"Class": "Code","Question": "How to get secured against not available item ?"})
training_data.append({"Class": "Code","Question": "How to get secured against not available item ?"})
training_data.append({"Class": "Code","Question": "How to get secured against not available item ?"})
training_data.append({"Class": "Code","Question": "How to get secured against not available item ?"})
training_data.append({"Class": "Code","Question": "How to get secured against not available item ?"})
training_data.append({"Class": "Code","Question": "How to get secured against not available item ?"})
training_data.append({"Class": "Code","Question": "How to get secured against not available item ?"})
training_data.append({"Class": "Code","Question": "How to get secured against not available item ?"})



#training_data.append({"class":"greeting", "Question":"how are you?"})
#training_data.append({"class":"greeting", "Question":"how is your day?"})
#training_data.append({"class":"greeting", "Question":"good day"})
#training_data.append({"class":"greeting", "Question":"how is it going today?"})

#training_data.append({"class":"goodbye", "Question":"have a nice day"})
#training_data.append({"class":"goodbye", "Question":"see you later"})
#training_data.append({"class":"goodbye", "Question":"have a nice day"})
#training_data.append({"class":"goodbye", "Question":"talk to you soon"})

#training_data.append({"class":"sandwich", "Question":"make me a sandwich"})
#training_data.append({"class":"sandwich", "Question":"can you make a sandwich?"})
#training_data.append({"class":"sandwich", "Question":"having a sandwich today?"})
#training_data.append({"class":"sandwich", "Question":"what's for lunch?"})

print ("%s Questions of training data" % len(training_data))


# capture unique stemmed words in the training corpus
corpus_words = {}
class_words = {}
# turn a list into a set (of unique items) and then a list again (this removes duplicates)
classes = list(set([a['Class'] for a in training_data]))
for c in classes:
    # prepare a list of words within each class
    class_words[c] = []

# loop through each Question in our training data
for data in training_data:
    # tokenize each Question into words
    for word in nltk.word_tokenize(data['Question']):
        # ignore a some things
        if word not in ["?", "'s"]:
            # stem and lowercase each word
            stemmed_word = stemmer.stem(word.lower())
            # have we not seen this word already?
            if stemmed_word not in corpus_words:
                corpus_words[stemmed_word] = 1
            else:
                corpus_words[stemmed_word] += 1

            # add the word to our words in class list
            class_words[data['Class']].extend([stemmed_word])

# we now have each stemmed word and the number of occurances of the word in our training corpus (the word's commonality)
print ("Corpus words and counts: %s \n" % corpus_words)
# also we have all words in each class
print ("Class words: %s" % class_words)
# calculate a score for a given class
def calculate_class_score(Question, class_name, show_details=True):
    score = 0
    # tokenize each word in our new Question
    for word in nltk.word_tokenize(Question):
        # check to see if the stem of the word is in any of our classes
        if stemmer.stem(word.lower()) in class_words[class_name]:
            # treat each word with same weight
            score += 1
            
            if show_details:
                print ("   match: %s" % stemmer.stem(word.lower() ))
    return score

# we can now calculate a score for a new Question
Question = input("Enter question")

# now we can find the class with the highest score
for c in class_words.keys():
    print ("Class: %s  Score: %s \n" % (c, calculate_class_score(Question, c)))

    # calculate a score for a given class taking into account word commonality
def calculate_class_score(Question, class_name, show_details=True):
    score = 0
    # tokenize each word in our new Question
    for word in nltk.word_tokenize(Question):
        # check to see if the stem of the word is in any of our classes
        if stemmer.stem(word.lower()) in class_words[class_name]:
            # treat each word with relative weight
            score += (1 / corpus_words[stemmer.stem(word.lower())])

            if show_details:
                print ("   match: %s (%s)" % (stemmer.stem(word.lower()), 1 / corpus_words[stemmer.stem(word.lower())]))
    return score

# return the class with highest score for Question
def classify(Question):
    high_class = None
    high_score = 0
    # loop through our classes
    for c in class_words.keys():
        # calculate score of Question for each class
        score = calculate_class_score_commonality(Question, c, show_details=False)
        # keep track of highest score
        if score > high_score:
            high_class = c
            high_score = score

    return high_class, high_score


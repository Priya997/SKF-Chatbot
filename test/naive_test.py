import json
import nltk
from nltk.stem.lancaster import LancasterStemmer
import naive_data
stemmer = LancasterStemmer()
training_data=[]
training_data=naive_data.trng_data()
print ("%s Questions of training data" % len(training_data))


corpus_words = {}
class_words = {}
classes = list(set([a['Class'] for a in training_data]))
for c in classes:
    class_words[c] = []
print(type(class_words))
for data in training_data:
    for word in nltk.word_tokenize(data['Question']):
        if word not in ["?", "'s"]:
            stemmed_word = stemmer.stem(word.lower())
            if stemmed_word not in corpus_words:
                corpus_words[stemmed_word] = 1
            else:
                corpus_words[stemmed_word] += 1

            class_words[data['Class']].extend([stemmed_word])
            

#print ("Corpus words and counts: %s \n" % corpus_words)
#print ("Class words: %s" % class_words)
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
print("Type done after completion or to end")
Question = input("Enter question ")

while(Question!="done"):
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
            score = calculate_class_score(Question, c, show_details=False)
            # keep track of highest score
            if score > high_score:
                high_class = c
                high_score = score

        return high_class, high_score

    z=classify(Question)

    print("The most relevant intent is: "+ str(z))
    Question = input("Enter question ")


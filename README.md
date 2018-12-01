# SKF-Chatbot [GSOC'18]

### What is SKF?
Security Knowledge Framework (SKF) is a tool that is used as a guide for building and verifying secure software. It can also be used to train developers about application security. The OWASP Security Knowledge Framework is an expert system web-application that uses the OWASP Application Security Verification Standard and other resources. It can be used to support developers in pre-development (security by design) as well as after code is released (OWASP ASVS Level 1-3).

### Introduction of SKF-Chatbot:

#### What is Chatbot?
Chatbots are software agents that interact with the user in a conversation. A chatbot is a service which is provided by websites so that users can easily able to fetch information interactively. They can reach out to a large audience on messaging apps and be more effective. A chatbot provides a speedy and quick response and available around the clock. Chatbot will be an attempt to reduce the pain of the user and will help users in finding solutions to their problems and thus improving the security of code and infrastructure.

#### What is SKF-Chatbot?
SKF-Chatbot is the bot which will help you with the details or answer your queries about the different vulnerabilities. The bot can be asked about the **description, solution** of the vulnerability and also help you with the **code snippet** in various languages.
**Language Supported: Django, Java, Flask, Php, Ruby**

##### For ex: If you ask What is XSS?
It will answer you with the description of xss.
**Something like this:** Description for xss injection is : Every time the application gets userinput, whether this showing it on screen or processingthis data in the application background, these parameters should be escaped for maliciouscode in order to prevent crosssite scripting injections.When an attacker gains the possibility to perform an XSS injection,he is given the opportunity to inject HTML and JavaScript code directly into theapplication. This could lead to accounts being compromised by stealing session cookies or directly affect the operation of the target application. 

Similarly, you can ask for the **solution** like: How to solve xss, How to resolve csrf etc. And for the **code** example it can be like code for xss filtering in java. 


## SKF-Chatbot Terminal Version:

**Link:** https://github.com/Priya997/SKF-Chatbot

This is the **Terminal version** of SKF-chatbot. By using it you can easily run this project offline.

Instructions for running it can be checked here:

 https://github.com/Priya997/SKF-Chatbot/blob/master/Basic_Approach/readme.md

### Introduction:
The problem statement was to analyze the user's query and provide him with the perfect response or the most closest response to his query. So, I divided the proble in three phases.
   1. Intent classification: To understand what user want to know. Like he want to know the description, solution or he wants the code    snippet. That need to be classified. So, the problem I faced here is, I need to classify the multiple labels and am not able to find a   good method.
   
        a. Here, you can see my first approach which is really naive but it worked:
           https://github.com/Priya997/SKF-Chatbot/blob/master/test/naive_test.py
           The problem with this one is: It is not efficient and a good approach.
   
        b. At last, I used **SKLearn** library and compared various algorithms and got the best solution to classify multiple labels.
           To check the graphs and the result of all the algorithm which I have used you can check this notebook:
           https://github.com/Priya997/SKF-Chatbot/blob/master/Notebooks/implementing%20multiclass.ipynb
        
        c. You can read this blog https://towardsdatascience.com/multi-label-intent-classification-1cdd4859b93 for understanding intent            classification and my method to get the best accuracy.
        
   2. Entity Recognition: After classifying intent, I need to recognize the entity (To know about which vulnerability user is talking).       This one was little confusing and time taking. Because, I have to make a custom entity recognizer which need to recognize atleast       250 different entities.
      
      I used **Rake-Nltk** -> It is a python package can be installed using 
        ``` pip install rake-nltk ``` It is usedfor removing the common words from the sentence and gives us the keywords.
        
      So, Now I have keywords the last thing I need to do is to check whether the keyword is in my list or not. Once find we got the           entity. You can check the code here :https://github.com/Priya997/SKF-Chatbot/tree/master/Basic_Approach/scripts 
      
   3. Responding Back: The most important step. After recodnizing the intent and entity we need to parse the data and provide the user         a correct response. For responding with the correct answer you need to have the proper dataset.
      
      For preparing dataset for all the steps this script is being used : https://github.com/Priya997/skf-flask/blob/master/skf/api/chatbot/dataset_prepare/data.py
      
      And for the main script you can refer here : https://github.com/Priya997/SKF-Chatbot/blob/master/Basic_Approach/test.py
      
**Note:** The chatbot have only knowledge base item and code item of SKF.

https://demo.securityknowledgeframework.org/api/kb/items -> *KB Item*

https://demo.securityknowledgeframework.org/api/code/items -> *Code Item*
      
# SKF-Hubot Gitter Version:

### What is Gitter.im?
Gitter is an open source instant messaging and chat room system for developers and users of GitHub repositories. Gitter is provided as software-as-a-service, with a free option providing all basic features and the ability to create a single private chat room, and paid subscription options for individuals and organisations, which allows them to create arbitrary numbers of private chat rooms.

  Link: https://github.com/Priya997/skfbot
  
  This is the **Gitter version** of SKF-chatbot. It is live on Gitter at: https://gitter.im/Security-Knowledge-Framework/Lobby
  
  Steps to use this or run this can be found here:
  
  https://github.com/Priya997/skfbot/blob/master/README.md
  
  
# My Contribution in Security Knowledge Framework:

  https://github.com/blabla1337/skf-flask/commits?author=Priya997
  These are my contributions in **SKF project**. These includes adding my chatbot(or my work) with the existing project.
  
## Future Scope:
 1. Can be integrated with various chat platforms like: Slack, Messenger etc.
 2. It can be extended with ASVS, checklist and other items which are present in the SKF web version.
 3. A Desktop version of the chatbot can be created.




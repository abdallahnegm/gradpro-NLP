#!/usr/bin/env python
# coding: utf-8

# In[1]:


import spacy
import speech_recognition as sr
import regex as re
import gtts
from gtts import gTTS
import os
import PyPDF2
from playsound import playsound  
import time


# In[2]:



pip install playsound==1.2.2


# In[3]:


pip install spacy


# In[4]:


nlp=spacy.load("en_core_web_lg")


# In[7]:


file1 = open('exampdf.txt', 'r')
count = 0
listofresult=[]
while True:
    count += 1
    x=0
    # Get next line from file
    line = file1.readline()
  
    # if line is empty
    # end of file is reached
    if not line:
        break
    print("{}".format(line.strip()))
    if(line.startswith("Q")):
        text=line
        obj = gTTS(text=text, lang="en", slow=True)  
        obj.save("exxxaaam"+str(x)+".mp3") 
        time.sleep(1)
        playsound("exxxaaam"+str(x)+".mp3") 
        os.remove("exxxaaam"+str(x)+".mp3")
        x=x+1
    elif(line.startswith("A")):
        global datasetans
        datasetans=line
        r=sr.Recognizer()
        with sr.Microphone() as source:
          print("Say Your Answer...")
          audio=r.listen(source)
          try:
            userans=r.recognize_google(audio)
            print("You Said: {}".format(userans))
          except:
            print("Sorry can't listen")
            continue
        userans=nlp(userans)
        datasetans=nlp(datasetans)
        finalresult=datasetans.similarity(userans)
        listofresult.append(finalresult)
        print(finalresult)
        print(listofresult)
    else:
        print("No Answer")
total=sum(listofresult)
rate=(total/len(listofresult))*100
print(total)
print(rate)


# In[ ]:





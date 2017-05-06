import numpy as np
import string
import re
from nltk.corpus import stopwords
from string import digits

i=0

#stopwords=np.array(stopwords)

temp1=[]
filtered_words=[[] for i in range(50)]
#filtered_words=np.array(filtered_words)
for i in range(50):
    inputtext=[]
    j=i+1
    s="C:/Users/chill/Desktop/Spring 2017/NC/Document/Doc"+str(j)+".txt"
    print(s)
    for line in open(s,'r').readlines():
        line=line.lower()
        #removing punctuations
        for data in string.punctuation:
                line=line.replace(data,"")
        #removing years
        remove_digits = str.maketrans('', '', digits)
        line = line.translate(remove_digits)
        

        line = re.sub('[!@#$–‘’“”—]', '', line)

        temp1=line.split()
        inputtext.extend(temp1)
  
     #removingstopwords   
    filtered_words[i] = [word for word in inputtext if word not in stopwords.words('english')]
    

filtered_words=np.array(filtered_words)

a=np.unique(filtered_words[1])
i=0
#calculating total unique words
for i in range(50):
  b=np.unique(filtered_words[i])
  a=np.concatenate((a,b),axis=0)     
  a=np.unique(a)
  
  
wordscount=[[0 for j in range(len(a))] for i in range(50)]
wordscount=np.array(wordscount)  
i=0;

#calculating the count
for i in range(50):
    temp=filtered_words[i]
   
    for l in range(len(a)):
          for j in range(len(temp)):
              if temp[j] == a[l]:
                  #print(temp[j],a[1])
                  wordscount[i][l]+=1
                  
                  








    
import itertools  

file = open('C:/Users/chill/Desktop/Spring 2017/NC/output.txt', 'w')
for i in range(len(a)):  
    file.write(a[i]+' '+' ')
file.write('\n')
for k in range(50):
    for i in range(len(a)):
        file.write(str(wordscount[k][i])+' '+' ')
    file.write('\n')
    
file.close()

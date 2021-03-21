#!/usr/bin/python
import os
import sys
 
#filterArr = {"a","an","and","at","from","of","or","to","on","in","the","is","are"}
#filterArr = []
# with open('filterWords.txt', 'r') as fd:
     # filterArr = fd.read().splitlines()
#print(filterArr)

n = len(sys.argv)
# Using argparse module
for i in range(1, n):

    if i == 1:
       titleFile = sys.argv[i]
    elif i == 2:
       ignoreFile = sys.argv[i]
    else:
        requireFile = sys.argv[i]
    
ignoreList = []
with open(f"{ignoreFile}.txt") as f:
    wordsIgnored = f.readlines()

    if len(wordsIgnored) < 1:
        checkRequired = False
        
    for wordIgnored in wordsIgnored:
        wordIgnored = wordIgnored.replace('\n', '')
        ignoreList.append(wordIgnored.lower())
            
    #print(ignoreList)  
    
requiredList = []
with open(f"{requireFile}.txt") as f:
    wordsRequired = f.readlines()
    
    for wordRequired in wordsRequired:
        wordRequired = wordRequired.replace('\n', '')
        requiredList.append(wordRequired.lower())
            
    #print(requiredList)  
    
with open(f"{titleFile}.txt") as f:

    titles = f.readlines()
    
    index = 0;
    
    printOut = []
    
    for title in titles:
        title = title.replace('\n', '')
        titleArr = title.rsplit(' ')
        index = index + 1
        
        currentTitle = title
        
        for i in range(0, len(titleArr)):
        
            currentWord = titleArr[i]
            skip = True
            
            # if not currentWord.lower() in filterArr:
            if (len(ignoreList)>0):
                if not currentWord.lower() in ignoreList:
                    skip = False
                    if (len(requiredList)>0):                
                        if currentWord.lower() in requiredList:
                            skip = False
                        else:
                            skip = True
            elif (len(requiredList)>0):              
                if currentWord.lower() in requiredList:
                    skip = False
                else:
                    skip = True
            else:
                skip = False
                
            if not skip:
                printOut.append(currentTitle)
                
            currentTitle = currentTitle.replace(currentWord+' ', '')
            currentTitle = currentTitle + " " + currentWord
                 
    printOut.sort(key=str.lower)
    #print(printOut)
    
    for i in range(0, len(printOut)):
        print(printOut[i])  



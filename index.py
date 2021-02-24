#!/usr/bin/python
import os
    
#filterArr = {"a","an","and","at","from","of","or","to","on","in","the","is","are"}
filterArr = []
# with open('filterWords.txt', 'r') as fd:
     # filterArr = fd.read().splitlines()
#print(filterArr)

files = os.listdir("input_files")
for txtFile in files:
    print()
    with open(f"input_files\\{txtFile}") as f:

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
                
                if not currentWord.lower() in filterArr:
                    printOut.append(currentTitle)
                    
                currentTitle = currentTitle.replace(currentWord+' ', '')
                currentTitle = currentTitle + " " + currentWord
                     
        printOut.sort(key=str.lower)
        #sorted(printOut, key=str.lower)
        #print(printOut)
        
        for i in range(0, len(printOut)):
            print(printOut[i])  
    


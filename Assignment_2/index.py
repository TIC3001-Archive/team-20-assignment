#!/usr/bin/python
import os
import sys
 
#filterArr = {"a","an","and","at","from","of","or","to","on","in","the","is","are"}
#filterArr = []
# with open('filterWords.txt', 'r') as fd:
     # filterArr = fd.read().splitlines()
#print(filterArr)

def assertFunc(assertion:bool, msg:str = "", fatal:bool = False) -> bool:
    try:
        assert assertion
    except AssertionError:
        if len(msg) > 0:
            print(msg)  
        if fatal:
            print("Exiting program.")
            exit(1)
        else:
            return assertion
    return assertion
    
def circularShift(titleFile):
    path = f"{titleFile}.txt"                                                           #bad practice, but no time to change. :stare: at Yan Shuang
    assertFunc(os.path.isfile(path), "Input titleFile is not a valid filepath!", True)  # Case 1: titleFile is valid file path
    with open(path) as f:
        
        titles = f.readlines()
        
        index = 0
        
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

        return(printOut)

def sort(printOut:str) -> list:           
    printOut.sort(key=str.lower)
    return (printOut)
    
def output(printOut:str) -> list:
    for i in range(0, len(printOut)):
        print(printOut[i])  

def getIgnoreList(ignoreFile):
    path = f"{ignoreFile}.txt"
    assertFunc(os.path.isfile(path), "Input ignoreFile is not a valid filepath!", True) # Case 1: ignoreFile is valid file path
    with open(path) as f:
        wordsIgnored = f.readlines()

        if len(wordsIgnored) < 1:
            checkRequired = False
            
        for wordIgnored in wordsIgnored:
            wordIgnored = wordIgnored.replace('\n', '')
            ignoreList.append(wordIgnored.lower())
            
    return(ignoreList)

def getRequiredList(requireFile):
    path = f"{requireFile}.txt"
    assertFunc(os.path.isfile(path), "Input requireFile is not a valid filepath!", True) # Case 1: requireFile is valid file path
    with open(path) as f:
        wordsRequired = f.readlines()
        
        for wordRequired in wordsRequired:
            wordRequired = wordRequired.replace('\n', '')
            requiredList.append(wordRequired.lower())
            
    return(requiredList)
 

def main():
    assertFunc(len(sys.argv) == 4, "Invalid number of arguments! Please follow the format: py index.py path_of_titles_file path_of_ignore_file path_of_require_file", True) # Case 2: Valid number of argument
    titleFile = sys.argv[1]
    ignoreFile = sys.argv[2]
    requireFile = sys.argv[3]
    
    ignoreList = getIgnoreList(ignoreFile)
    requiredList = getRequiredList(requireFile)
            
    printOut = circularShift(titleFile)
                
    sort(printOut)
    output(printOut)
    return False



ignoreList = []
requiredList = [] 
    
main()





import os, sys

def main(arg1:str = "", arg2:str = "", arg3:str = ""):
    assertFunc((sys.version_info[0] == 3 and sys.version_info[1] >= 6), "Your version of python is too old! Please use at least 3.6 and above.", True)
    paths = [arg1, arg2, arg3]
    if os.path.isfile(paths[0]) and not os.path.isfile(paths[1]) and not os.path.isfile(paths[2]):  # potentially search facility.
        # try to open the first file and see if it's filled with paths of other files.
        dirPath = os.path.dirname(paths[0])
        with open(arg1) as f:
            filePaths = [s.strip() for s in f.readlines()]
            kwic = {}
            reqArr = []
            for fp in filePaths:
                kwic[fp] = []
                phrases = parseFile(fp) if os.path.isfile(fp) else parseFile(os.path.join(dirPath, fp))
                for p in phrases:
                    kwic[fp].extend(circularShift(p))
        inputStr = input("In search mode. Input keyword, or input 'q' to exit.\n")
        reqArr.append(inputStr)
        while inputStr != 'q':
            for k in kwic:
                filteredArr = filterKeywords(kwic[k], [], reqArr)
                if len(filteredArr) > 0:
                    print(k)
                    sortAndPrint(filteredArr)
            inputStr = input()
        exit(0) # when input is q, exit.
    while not os.path.isfile(paths[0]) or not os.path.isfile(paths[1]) or not os.path.isfile(paths[2]): #while any of the the paths provided are not file paths
        path = input("Please try again, input file paths.\n")
        args = path.split(" ")
        for i in range(len(args)):
            paths[i] = args[i].strip()
    permutations = parseFiles(paths[0], paths[1], paths[2])
    sortAndPrint(permutations)

def sortAndPrint(permutations:list, output:bool = False):
    # print(f"\n{os.path.splitext(txtFile)[0].upper()}")    #prints file name.
    permutations.sort(key=(lambda string: string.lower()))  #default sort takes upper/lower to account, which is not intuitive. 
    if output:
        with open(f"./output_files/output.txt", "w") as f:
            f.write("\n".join(permutations))
    for p in permutations:
        print(p)

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
        
def parseFile(fp: str) -> list:
    assertFunc(os.path.isfile(fp), "path is not a file or not valid.")   #makes sure that path param is a file 
    results = []
    with open(fp, "r") as f:
        results = [s.strip() for s in f.readlines()]
    return results

def parseFiles(title:str, ignore:str = "", required:str = "") -> list:
    """Takes 3 args: title, ignore, required, which are all paths to files and returns all permutations."""
    results = []
    titles = parseFile(title)
    ignores = [] if not ignore else parseFile(ignore)
    requires = [] if not required else parseFile(required)
    for t in titles:
        results.extend(filterKeywords(circularShift(t), ignores, requires)) #ensure that the "\n" is not included by stripping.
    return results

def circularShift(title:str) -> list:
    counter = 0
    currentPerm = title
    results = []
    words = title.split(" ")
    while counter < len(words):
        results.append(currentPerm)    #if first word not in ignore, add current perm, then shift.
        temp = words[0]
        words.pop(0)
        words.append(temp)
        currentPerm = " ".join(words)
        counter += 1
    return results

def isValidKeyword(keyWord:str, ignoreArr: list, requiredArr: list) -> bool:
    # turn everything to lowercase here.
    ignoreArr = [s.lower() for s in ignoreArr]
    requiredArr = [s.lower() for s in requiredArr]
    words = [s.lower() for s in keyWord.split()]
    return words[0] not in ignoreArr and ((len(requiredArr) > 0 and words[0] in requiredArr) or len(requiredArr) == 0)

def filterKeywords(keywordArr: list, ignoreArr: list = [], requiredArr: list = [])-> list:
    return list(filter(lambda x: isValidKeyword(x, ignoreArr, requiredArr), keywordArr))

if __name__ == "__main__":
    assertFunc((len(sys.argv) <= 5), "Too many arguments! Check your input.", True)
    if len(sys.argv) == 4:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2:
        main(sys.argv[1])
    elif len(sys.argv) == 1:
        main()
import os, sys

def main(arg1:str = "", arg2:str = "", arg3:str = ""):
    assertFunc((sys.version_info[0] == 3 and sys.version_info[1] >= 6), "Your version of python is too old! Please use at least 3.6 and above.", True)
    paths = [arg1, arg2, arg3]
    while not os.path.isfile(paths[0]) or not os.path.isfile(paths[1]) or not os.path.isfile(paths[2]): #while any of the the paths provided are not file paths
        path = input("Please try again, input file paths.\n")
        args = path.split(" ")
        for i in range(len(args)):
            paths[i] = args[i].strip()
    sortAndPrint(paths[0], paths[1], paths[2])

def sortAndPrint(title:str, ignore:str, required:str):
    # print(f"\n{os.path.splitext(txtFile)[0].upper()}")    #prints file name.
    permutations = parseFiles(title, ignore, required)
    permutations.sort(key=(lambda string: string.lower()))  #default sort takes upper/lower to account, which is not intuitive. 
    with open(f"./output_files/{os.path.splitext(os.path.basename(title))[0]}_output2.txt", "w") as f:
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
        

def parseFiles(title:str, ignore:str, required:str) -> list:
    """Takes 3 args: title, ignore, required, which are all paths to files. """
    assertFunc(os.path.isfile(title), "path is not a file or not valid.")   #makes sure that path param is a file 
    assertFunc(os.path.isfile(ignore), "path is not a file or not valid.") 
    assertFunc(os.path.isfile(required), "path is not a file or not valid.")
    results = []
    with open(title) as f1, open(ignore) as f2, open(required) as f3:
        titles = [s.strip() for s in f1.readlines()]
        ignores = [s.strip() for s in f2.readlines()]
        requires = [s.strip() for s in f3.readlines()]
        for t in titles:
            results.extend(circularShift(t, ignores, requires)) #ensure that the "\n" is not included by stripping.
    return results

def circularShift(title:str, ignores:list, requires:list) -> list:
    counter = 0
    currentPerm = title
    results = []
    words = title.split(" ")
    while counter < len(words):
        if words[0] not in ignores:
            if (len(requires) > 0 and words[0] in requires) or len(requires) == 0:
                results.append(currentPerm)    #if first word not in ignore, add current perm, then shift.
        temp = words[0]
        words.pop(0)
        words.append(temp)
        currentPerm = " ".join(words)
        counter += 1
    return results


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
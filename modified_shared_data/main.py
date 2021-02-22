import os, sys

def main():
    assertFunc((sys.version_info[0] == 3 and sys.version_info[1] >= 6), "Your version of python is too old! Please use at least 3.6 and above.", True)
    permutations = parseFile("input_files\\anime.txt")
    permutations.sort(key=(lambda string: string.lower()))  #default sort takes upper/lower to account, which is not intuitive. 
    print(permutations)
    # files = os.listdir("input_files")
    # for txtFile in files:
    #     print(f"\n{os.path.splitext(txtFile)[0].upper()}")
    #     circularShift(f"input_files\\{txtFile}")


def assertFunc(assertion:bool, msg:str = "", fatal:bool = False):
    try:
        assert assertion
    except AssertionError:
        print(msg)
        if fatal:
            print("Exiting program.")
            exit(1)
        

def parseFile(path:str) -> list:
    assertFunc(os.path.isfile(path), "path is not a file or not valid.") #makes sure that path param is a file 
    results = []
    with open(path) as f:
        titles = f.readlines()
        for title in titles:
            results.extend(circularShift(title.strip())) #ensure that the "\n" is not included by stripping.
    return results

def circularShift(title:str) -> list:
    results = []
    words = title.split(" ")
    currentPerm = title
    while currentPerm not in results:
        results.append(currentPerm)    #add current perm, then shift.
        temp = words[0]
        words.pop(0)
        words.append(temp)
        currentPerm = " ".join(words)
    return results


if __name__ == "__main__":
    main()
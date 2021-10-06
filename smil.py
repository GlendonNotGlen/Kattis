
def main():
    givenString = input()
    size = len(givenString)
    i = 0 #index of eyes
    indexArr = []
    while i < size:
        if givenString[i] == ':' or givenString[i] == ';':
            j = i+1
            if j < size and givenString[j] == ')':
                indexArr.append(int(i))
            elif j < size and givenString[j] == '-':
                j += 1
                if j < size and givenString[j] == ')':
                    indexArr.append(i)
        i += 1
    for iterator in (range(len(indexArr))):
        print(indexArr[iterator])





if __name__ == '__main__':
        main()

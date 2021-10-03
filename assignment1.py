def countWords():
    file = input("Enter file name")
    f = open(file,'r')
    count = 0
    for i in f:
        word = i.split()
        print(word)
        count = count+len(word)
    print("Total words are", count)
#main
countWords()

import sys

def indico(file,strings):
    f = open(file,encoding="ISO-8859-1")
    donne = f.read()
    f.close()
    print(donne)

    for x in strings.split():
        if(donne.find(x)):
            print(x +" est dans le dictionnaire")
        else:
            print(x + "n'est pas dans le dictionnaire")

print(indico(sys.argv[1],sys.argv[2]))
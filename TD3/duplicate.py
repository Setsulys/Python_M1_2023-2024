#!/usr/bin/python3

import sys
import os
import hashlib

def hashfile(dicto,root,name):
    f = open(os.path.join(root,name),"r",encoding='latin-1')
    read = f.read()
    hash = hashlib.sha1(read.encode('latin-1')).hexdigest()
    if(hash not in dicto):
        dicto[hash] = [os.path.join(root,name)]
    else:
        dicto[hash].append(os.path.join(root,name))
    return dicto


def duplicate(extension,directory,output):
    dicto = {}

    for (root,directories,files) in os.walk(directory):
        for name in files:
            if((not len(extension))==0):
                if(name.endswith(extension)):
                    dicto = hashfile(dicto,root,name)
            else:
                dicto =hashfile(dicto,root,name)
    
    if((not len(output))==0):
        f =open(output,"w")
        for x in dicto.values():
            for e in x:
                f.write(e+"\n")
            f.write("\n")
        f.close()
    else:
        for x in dicto.values():
            for e in x:
                print(e)
            print("\n")


if __name__ == "__main__":
    extension,directory,output="",".",""
    for i in range(1,len(sys.argv)):
        if(sys.argv[i]=="-e" or sys.argv[i]=="--extension"):
            extension=sys.argv[i+1]
        elif(sys.argv[i]=="-d" or sys.argv[i]=="--directory"):
            directory=sys.argv[i+1]
        elif(sys.argv[i]=="o" or sys.argv[i]=="--output"):
            output=sys.argv[i+1]

duplicate(extension,directory,output)

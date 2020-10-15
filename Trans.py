import sys
import re
import ColorCode
ledControl = {}

outFileName = "transError.out"

def main():
    argv = sys.argv
    argc = len(argv)
    debug = False
    if(argc <= 1):
        path = input("Please input file path : ")
    elif(argc <= 2):
        path = sys.argv[1]
    elif(True):
        if(argv[2] == "-d" or argv[2] == "--debug"):
            debug = True

    trans(path)

    if(debug):
        print(ledControl)

def trans(path):
    outStr = "error point\n-----------\n"
    pattern = []
    tmp = []
    patternName = ""
    isFirstSet = True

    file = open(path)

    row = 0
    for line in file.readlines():#1行読む
        isLineHead = True
        row += 1
        for word in re.split("[\s,]+", line):#区切り文字で分割
            if(isLineHead):
                isLineHead = False
                items = 0
                if(re.match("~-+$", word) !=None or word==""):#続き|空白行
                    None
                elif(re.match("^[0-9]+$", word) !=None and patternName !=""):#新規フレーム
                    if(isFirstSet):
                        isFirstSet = False
                    else:
                        pattern.append(tmp)
                    tmp = [int(word)]
                else:#新規パターン
                    if(patternName != ""):
                        pattern.append(tmp)
                        ledControl[patternName] = pattern
                        pattern = []
                        isFirstSet = True
                    patternName = word
            else:
                rgb = ColorCode.Name2RGB(word)
                if(re.match("^#??[0-9A-Fa-f]{6}$", word) !=None):
                    tmp.append(ColorCode.Code2RGB(word))
                elif(rgb!=None):
                    tmp.append(rgb)
                else:
                    outStr += str(row) + ", " + str(items) + "\t"
    if(patternName != ""):
        pattern.append(tmp)
        ledControl[patternName] = pattern

    file.close()

    file = open(outFileName, mode="w")
    file.write(outStr)
    file.close()

if(__name__=="__main__"):
    main()
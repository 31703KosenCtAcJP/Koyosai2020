import sys

class ReadPattern:
    import sys
    import re
    import ColorCode
    import traceback

    # "RP" = "ReadPattern"
    RP_LINE_HEAD_NO_CHECK = 0b00
    RP_LINE_HEAD_NULL = 0b01
    RP_LINE_HEAD_FRAME_TIME = 0b10
    RP_LINE_HEAD_PATTERN_NAME = 0b11

    _debug = False

    patternAll = {}
    patternX = []
    frameXY = []
    colorAndGradation = []
    patternName = ""
    outStr = "error point\n--------------------"
    outFileName = "transError.out"

    def debugConf(self, blnYesNo):
        self._debug = blnYesNo

    def trans(self, path):
        try:
            f = open(path)
        except FileNotFoundError:
            print(self.traceback.format_exc())
            return None
        self.outStr += "open: " + path + "\n"

        row = 0 # エラー出力用
        for line in f.readlines(): # 1行読む
            isLineHead = True
            patternHead = self.RP_LINE_HEAD_NO_CHECK
            items = 0 # エラー出力用
            line = line.strip()
            for word in self.re.split("[\s,]+", line): # 区切り文字で分割
                isGradation = False # グラデーションか
                if(isLineHead): # 行の最初か
                    isLineHead = False
                    if(self.re.match("^-+", word) != None or word == ""): # オプション もしくは 空白
                        patternHead = self.RP_LINE_HEAD_NULL
                        break # この行は無視して次の行へ
                    elif(self.re.match("^[0-9]+$", word) != None and self.patternName != ""): # フレーム
                        patternHead = self.RP_LINE_HEAD_FRAME_TIME
                        self.frameXY = [int(word)] # フレームのサイズ(継続時間)を入力
                    else: # 新規パターン
                        patternHead = self.RP_LINE_HEAD_PATTERN_NAME
                        if(self.patternName != ""): # 2つ目以降のパターン
                            if(self.patternName in self.patternAll):
                                self.outStr += self.patternName + "is already exsist in row " + row + "\n"
                            self.patternAll[self.patternName] = self.patternX # パターンをプッシュ
                            self.patternX = []
                        self.patternName = word

                else: # 行の最初ではない
                    if(patternHead == self.RP_LINE_HEAD_PATTERN_NAME): # 新規パターン フレーム継続時間か
                        if(self.re.match("^[0-9]+[Mm][Ss]$", word) != None): # ms指定
                            m = self.re.match("^[0-9]+")
                            self.patternX.append(int(m.group()))
                        elif(self.re.match("^[0-9]+[Hh][Zz]$", word) != None): # フレームレート指定
                            m = self.re.match("^[0-9]+")
                            self.patternX.append(int(m.group()))
                        break # この後には何もないので次の行へ
                    elif(patternHead == self.RP_LINE_HEAD_FRAME_TIME): # 色
                        # 色判定
                        rgb = self.ColorCode.Name2RGB(word)
                        if(self.re.match("^#?[0-9A-Fa-f]{6}_?$", word) != None): # カラーコードか
                            self.colorAndGradation = [self.ColorCode.Code2RGB(word)]
                        elif(rgb != None): # 色文字列か ([r,g,b]取得)
                            self.colorAndGradation = [rgb]
                        else: # 判定不可
                            self.outStr += str(row) + ":" + str(items) + ",word=" + word + "\t"
                            self.colorAndGradation = [tuple([0x00, 0x00, 0x00])] # LEDオフ
                        # グラデーション判定
                        if(self.re.match(".+_$", word) != None):
                            self.colorAndGradation.append(True)
                        else:
                            self.colorAndGradation.append(False)
                        # フレームに追加
                        self.frameXY.append(self.colorAndGradation)
                # word終了時
                items += 1
                self.outStr += "\n"
            # 改行時
            if(patternHead == self.RP_LINE_HEAD_FRAME_TIME):
                self.patternX.append(self.frameXY) # フレームをプッシュ
            row += 1
        # EoF
        self.patternAll[self.patternName] = self.patternX # パターンをプッシュ

        f.close()
        self.outStr += "close: " + path + "\n\n"

        return self.patternAll

    def ErrorOut(self): # デバッグ出力用
        f = open(self.outFileName, mode="w")
        f.write(self.outStr)
        f.close()
    
def main():
    argv = sys.argv
    argc = len(argv)
    debug = False

    rp = ReadPattern()

    if(argc <= 1):
        path = input("Pleas input file path : ")
    elif(argc <= 2):
        path = argv[1]
    elif(True):
        if(argv[2] == "-D" or argv[2] == "--debug"):
            rp.debugConf(True)

    while True:
        rp.trans(path)
        path = input("input path if you want to continue : ")
        if(path == "" or path == "\n"):
            break
    
    print(rp.patternAll)
    rp.ErrorOut()

if __name__ == "__main__":
    main()
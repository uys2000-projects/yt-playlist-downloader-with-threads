from json import dump
import os
li = []


class YLogger(object):
    def debug(self, msg: str = ""):
        pass

    def warning(self, msg: str = ""):
        l(msg)

    def error(self, msg: str = ""):
        l(msg)


def addToClearList(fileName):
    f = open("log/clearList.txt", "a")
    print(fileName, file=f)
    f.close()


def checkAddToClearList(fileName):
    if (not (fileName in li)):
        li.append(fileName)
        addToClearList(fileName)


def clearLogs():
    try:
        f = open("log/clearList.txt", "r")
        for file in f.readlines():
            os.remove(f"log/{file}".replace("\n", ""))
        f.close()
        open("log/clearList.txt", "w").close()
    except:
        pass


def l(*args):
    checkAddToClearList("log.txt")
    f = open("log/log.txt", "a")
    print(*args, file=f)
    f.close()


def t(*args):
    checkAddToClearList("t.txt")
    f = open("log/t.txt", "a")
    print(*args, file=f)
    f.close()


def le(text, fName: str = "fName"):
    checkAddToClearList(fName)
    f = open(f"log/{fName}", "a")
    print(text, f)
    f.close()


def j(jsonObj, fName: str = "fName"):
    checkAddToClearList(fName)
    f = open(f"log/{fName}", "w")
    dump(jsonObj, f)
    f.close()

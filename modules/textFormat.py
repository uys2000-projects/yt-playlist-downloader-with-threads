from modules.logger import l
from json import load


def getLastIDList():
    l("tF : C : getLastIDList")
    f = open("./log/idList.json", "r")
    idList = load(f)
    f.close()
    l("tF : R : getLastIDList :", "idList :", idList)
    return idList


def getOptions():
    l("tF : C : getOptions")
    f = open("./options.json", "r")
    options = load(f)
    f.close()
    l("tF : R : getOptions :", "options :", options)
    return options


def getListId(listUrl: str):
    l("tF : C : getListId", listUrl)
    listUrl = listUrl.split("&")
    if (len(listUrl) > 1):
        listUrl = listUrl[1]
    else:
        listUrl = listUrl[0]
    listUrl = listUrl.split("list=")[1]
    l("tF : R : getListId", listUrl)
    return listUrl


def getUrl(apiUrl: str, pageToken: str):
    l("tF : C : getUrl : ", "apiUrl : ", apiUrl, "pageToken : ", pageToken)
    if (pageToken != ""):
        apiUrlS = apiUrl.split("&")
        if (len(apiUrlS) == 4):
            apiUrlS.insert(2, f"pageToken={pageToken}")
        else:
            apiUrlS[2] = f"pageToken={pageToken}"
        apiUrl = "&".join(apiUrlS)
    l("tF : R : getUrl : ", "apiUrl : ", apiUrl)
    return apiUrl

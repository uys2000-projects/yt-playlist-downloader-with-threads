import requests
from modules.logger import l, t, j
from modules.textFormat import getUrl


def _request(apiUrl: str, idList: list = [], pageToken: str = ""):
    l("F : C : _request : ", "apiUrl : ", apiUrl,
      "idList : ", len(idList), "pageToken : ", pageToken)
    apiUrl = getUrl(apiUrl, pageToken)
    r = requests.get(apiUrl).json()
    idList = idList + r["items"]
    if ("nextPageToken" in r.keys()):
        pageToken = r["nextPageToken"]
        l("F : R : _request : ", "apiUrl : ", apiUrl,
          "idList : ", len(idList), "pageToken : ", pageToken)
        return _request(apiUrl, idList, pageToken)
    else:
        l("F : R : _request : ", "idList : ", len(idList))
        return idList


def getList(token: str, listId: str):
    l("F : C : getList : ", "token : ", token, "listId : ",  listId)
    apiUrl = f"https://youtube.googleapis.com/youtube/v3/playlistItems?part=contentDetails%2Cid%2Csnippet&maxResults=50&playlistId={listId}&key={token}"
    idList = _request(apiUrl)
    l("F : R : getList : ", "idList : ", len(idList))
    j(idList, "idList.json")
    return idList

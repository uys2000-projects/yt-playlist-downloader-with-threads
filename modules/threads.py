from modules.youtubeDl import dowload
import threading
from modules.logger import l


def mapper(idList):
    l("t : C : mapper :", "idList :", len(idList))

    def m(n):
        return {"videoId": n["contentDetails"]["videoId"],
                "videoTitle": n["snippet"]["title"]}
    l("t : R : mapper :", "idList :", len(idList))
    return list(map(m, idList))


def _getlistCount(idList: list, threadCount: int):
    l("t : C : _getlistCount :", "idList :", len(
        idList), "threadCount :", threadCount)
    left = len(idList) % threadCount
    c = int((len(idList) - left) / threadCount)
    res = [c for i in range(threadCount)]
    res[threadCount-1] = res[threadCount-1] + left
    l("t : R : _getlistCount :", "idList :", len(res))
    return res


def listSeperater(idList: list, threadCount: int):
    l("t : C : listSeperater :", "idList :", len(
        idList), "threadCount :", threadCount)
    idList = mapper(idList)
    li, z = [], 0
    c = _getlistCount(idList, threadCount)
    for i in range(threadCount):
        li.append(idList[z: z+c[i]])
        z = z + c[i]
    l("t : R : listSeperater :", "idList :", len(li))
    return li


def _threadFunc(idList: list, options: dict):
    l("t : C : _threadFunc :", "idList :", len(idList), "options :", options)
    for i in idList:
        dowload(i, options)
    l("t : R : _threadFunc")


def startThreads(seperatedIdList, options, threadCount):
    l("t : C : startThreads :", "seperatedIdList :", len(seperatedIdList),
      "options :", options, "threadCount :", threadCount)
    for i in range(len(seperatedIdList)):
        threading.Thread(target=_threadFunc, args=(
            seperatedIdList[i], options, )).start()

    l("t : R : startThreads")

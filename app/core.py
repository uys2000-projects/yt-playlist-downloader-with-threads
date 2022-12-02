
from modules.textFormat import getListId, getOptions, getLastIDList
from modules.logger import clearLogs
from modules.youtubeDl import dowload
from modules.youtubeApi import getList
from modules.threads import listSeperater, startThreads


def main(token):
    link = input("Enter Music List Link :")
    if (link == ""):
       link = r"https://www.youtube.com/playlist?list=PLKJtOlwTyds3Q6URKhJKCPO5gmdvdsgaA"
    clearLogs()

    listId = getListId(link)
    idList = getList(token, listId)
    #idList = getLastIDList()
    options = getOptions()
    separetedList = listSeperater(idList, options["threads"])
    startThreads(separetedList, options["ytdl"], options["threads"])
    #getList(token, link)

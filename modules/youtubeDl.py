from youtube_dl import YoutubeDL as ytdl
from modules.logger import YLogger
from modules.logger import l
from youtube_dl.utils import DownloadError


def dowload(videoID, ytdlOptions, t: int = 0):
    l("yD : C : dowload :", "videoID :", videoID, "ytdlOptions :", ytdlOptions)
    opions = ytdlOptions
    opions["logger"] = YLogger
    if t == 12:
        return
    try:
        ytdl(ytdlOptions).download(
            [f'https://www.youtube.com/watch?v={videoID["videoId"]}'])
    except DownloadError:
        t = t + 1
        dowload(videoID, ytdlOptions, t)
    l("yD : R : dowload")

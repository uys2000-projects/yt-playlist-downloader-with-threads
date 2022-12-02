# YT MP3 List Downloader

## General Information

This project just makes youtube_dl able to work with threading

## Youtube Data Api

You should get apıkey from Youtube Api you can go to [link][APILINK] and you can get it from there.  
You also should save that API key to `.env` file like this

```env
APIKEY=YOUTUBEDATAAPIKEY
```

## Usage

Set `options.json` for your download prefences.
More information about settings is [here][MAINLINK] and [here][SECLINK]

### Supported Qualities

`best`: Select the best quality format represented by a single file with video and audio.  
`worst`: Select the worst quality format represented by a single file with video and audio.  
`bestvideo`: Select the best quality video-only format (e.g. DASH video). May not be available.  
`worstvideo`: Select the worst quality video-only format. May not be available.  
`bestaudio`: Select the best quality audio only-format. May not be available.  
`worstaudio`: Select the worst quality audio only-format. May not be available.  

### Supported Output Extensions

`3gp`, `aac`, `flv`, `m4a`, `mp3`, `mp4`, `ogg`, `wav`, `webm`

[APILINK]:https://console.cloud.google.com/apis/api/youtube.googleapis.com
[MAINLINK]:https://github.com/ytdl-org/youtube-dl#embedding-youtube-dl
[SECLINK]:https://github.com/ytdl-org/youtube-dl/blob/3e4cedf9e8cd3157df2457df7274d0c842421945/youtube_dl/YoutubeDL.py#L137-L312

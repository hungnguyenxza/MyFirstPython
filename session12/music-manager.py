import youtube_dl

youtube_opt = {

'outtmpl': '%(id)s', # lấy tên file đown về là id của video

'postprocessors': [{

'key': 'FFmpegExtractAudio', # Tách lấy audio

'preferredcodec': 'mp3', # Format ưu tiên là mp3

'preferredquality': '192', # Chất lượng bitrate

}],

}

with youtube_dl.YoutubeDL(youtube_opt) as yt:
    print(yt.extract_info("Hello"))

    yt.sear

    pass
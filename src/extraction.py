import yt_dlp


def download_video(url, directory):
    ydl_opts = {
        'format': 'bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4] / bv*+ba/b',
        'outtmpl': directory + '%(title)s.%(ext)s',
        "quiet": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)


def download_audio(url, directory):
    ydl_opts = {
        'format': 'mp3/m4a/bestaudio/best',
        "quiet": True,
        'outtmpl': directory + '%(title)s.%(ext)s',
        # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(url)


def getDataPlaylist(url):
    data = []
    ydl_opts = {
        "quiet": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

        print("\n INFO \n")
        for entry in info["entries"]:
            data.append([entry["title"], entry["webpage_url"]])

    return data

# PlaylistSynchronizer
## Description
  This software was created to facilitate the synchronization between local and online playlists. Using it, it’s possible to manage a playlist completely online and then downloaded locally or updated if some of the elements     are already downloaded. The program works with multiple websites thanks to the <a href="https://github.com/yt-dlp/yt-dlp">yt-dlp</a> and <a href="https://www.ffmpeg.org/">ffmpeg</a> libraries.

## Installation
  There are two ways to run this application. For both of them you’ll need to install <a href="https://www.ffmpeg.org/">ffmpeg version 7.1</a>. Then you can either download and run the <a href="https://github.com/Vega32/PlaylistSynchonizer/releases/tag/1.0">executable</a>  or run the python code directly. To do that you’ll need to download the dependencies using the following command:
  ```
  pip install -r requirements.txt
  ```
  Afterwards simply run the `main.py` file to run the program

## User Guide
  The application has two modes. The first one is a standard video and audio downloader similar to the ones you’d find online (only this one isn’t riddled with ads). The second mode is the playlist manager. In this one, you    can select an existing playlist or creating a new one. A playlist is just a dedicated folder on your machine with a .config.playlist file. Afterwards you can update the playlist. This will download any files that the local   version is missing and delete files not present in the online version.

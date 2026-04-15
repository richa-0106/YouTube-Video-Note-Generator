import yt_dlp

def download_audio(url):

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'audio.%(ext)s',

        # playlist disable
        'noplaylist': True,

        # SSL issue fix
        'nocheckcertificate': True,

        # retry settings
        'retries': 10,
        'fragment_retries': 10,

        # timeout increase
        'socket_timeout': 60,

        # slow network support
        'concurrent_fragment_downloads': 1,

        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return "audio.mp3"
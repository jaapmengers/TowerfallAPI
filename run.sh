livestreamer --http-header Client-ID=jzkbprff40iqj646a697cyrvl0zt2m6 -O http://www.twitch.tv/jaapem best | ffmpeg -i - -vf fps=5 -f image2pipe -pix_fmt rgb24 -vcodec rawvideo - | python main.py

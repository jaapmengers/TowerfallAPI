import subprocess as sp
import numpy
import time

command = [ 'livestreamer',
            '--http-header', 'Client-ID=jzkbprff40iqj646a697cyrvl0zt2m6',
            '--player', '"ffmpeg -i - -vf fps=1 -pix_fmt rgb24 -vcodec rawvideo -f image2pipe -"',
            '-O', 'https://www.twitch.tv/epicenter_en1', '360p30']

pipe = sp.Popen(command, stdout = sp.PIPE, bufsize=10**8)

while True:
    raw_image = pipe.stdout.read(640*360*3)
    # transform the byte read into a numpy array
    image =  numpy.fromstring(raw_image, dtype='uint8')
    image = image.reshape((360,640,3))
    # throw away the data in the pipe's buffer.
    pipe.stdout.flush()

    print 'snor'
    print image
    print 'test'

    time.sleep(0.2)

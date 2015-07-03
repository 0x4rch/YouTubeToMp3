from __future__ import print_function
from pytube import YouTube

yt = YouTube()
# Set the video URL.
yt.url = raw_input('Enter url: ')
#yt.url = "http://www.youtube.com/watch?v=Ik-RsDGPI5Y"

print('Video Name: %s' % yt.filename)
yt.filename = 'video'
video = yt.get('mp4', '720p')
video.download('vidtemp')
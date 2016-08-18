#!/bin/bash
echo "Coded by Nathan Parker"
python pytubetest.py
ffmpeg -i video/video.mp4 songs/song.mp3

rm video/video.mp4
echo "#################################"
echo "######### ALL FINISHED ##########"
echo "#################################"
echo "Coded by Nathan Parker, using pytube + ffmpeg"

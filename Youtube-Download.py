#!/usr/bin/python3
# -*- coding: utf-8 -*-
#!/usr/bin/env python 3
#YTDL - Conv V0.3 Source
#Date 1/1/2021 0h00'000

print("YouTube Downloader and Converter v0.3 Alpha Code By NeuralNine Mod By PTJ312")
print("Loading...")

import pytube, os
from moviepy.editor import VideoFileClip

os.system("color 0a")
os.system("title YouTube Downloader and Converter v0.3 Alpha")
print('''
---------------------------------------------------------------
             ~Code By NeuralNine, Mod By PTJ312~              -
What do you want? Choose one of the list choice...            -
                                                              -
(1) Download YouTube Videos Manually                          -
(2) Download a YouTube Playlist                               -
(3) Download YouTube Videos and Convert Into MP3              -
                                                              -
Downloading copyrighted YouTube videos is illegal!            -
I am not responsible for your downloads! Go at your own risk! -
---------------------------------------------------------------
''')

def download_video(url, resolution):
    itag = choose_resolution(resolution)
    video = pytube.YouTube(url)
    stream = video.streams.get_by_itag(itag)
    stream.download()
    return stream.default_filename

def download_videos(urls, resolution):
    for url in urls:
        download_video(url, resolution)

def download_playlist(url, resolution):
    playlist = pytube.Playlist(url)
    download_videos(playlist.video_urls, resolution)

def choose_resolution(resolution):
    if resolution in ["low", "360", "360p"]:
        itag = 18
    elif resolution in ["medium", "720", "720p", "hd"]:
        itag = 22
    elif resolution in ["high", "1080", "1080p", "fullhd", "full_hd", "full hd"]:
        itag = 137
    elif resolution in ["very high", "2160", "2160p", "4K", "4k"]:
        itag = 313
    else:
        itag = 18
    return itag

def input_links():

    print("[+] Enter the links of the videos (end by entering Input'GO'): ")
    links = []
    link = ""
    while link != "GO" and link != "go":
        link = input()
        links.append(link)
    links.pop()
    return links

def convert_to_mp3(filename):
    clip = VideoFileClip(filename)
    clip.audio.write_audiofile(filename[:-4] + ".mp3")
    clip.close()

choice = input("> Your Choice: ")

if choice == "1" or choice == "2":
    nums_quality = input("[+] Choose a quality (low[1], medium[2], high[3], very high[4]): ")
    if nums_quality =="1":
       quality = "low"
    if nums_quality =="2":
       quality = "medium"
    if nums_quality =="3":
       quality = "high"
    if nums_quality =="4":
       quality = "very high"
    if choice == "2":
        link = input("[+] Enter the link to the playlist: ")
        print("> Downloading playlist...")
        download_playlist(link, quality)
        print("> Download finished!")
    if choice == "1":
        links = input_links()
        for link in links:
            download_video(link, quality)
elif choice == "3":
    links = input_links()
    for link in links:
        print("> Downloading...")
        filename = download_video(link, 'low')
        print("> Converting...")
        convert_to_mp3(filename)
else:
    print("> Invalid input! Terminating...")

from pytube import  YouTube

link=input("Enter the Link:")
ytube=YouTube(link)
yvideo=ytube.streams.get_highest_resolution()

yvideo.download("D:\Beginner Projects\Youtube Downloader\Downloaded Videos")

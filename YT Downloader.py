from pytube import  YouTube

link=input("Enter the Link:")
ytube=YouTube(link)
yvideo=ytube.streams.get_highest_resolution()

yvideo.download("D:\Beginner Projects\Youtube Downloader\Downloaded Videos")

sk-proj-0EKYCUQmgrJ9EcLMYKBbT3BlbkFJKh297x6eeLwX9h0Uj3Rm
sk-proj-NEjPxKTrLFbr4Zeum5qKT3BlbkFJaFQgU2o8YLtgdkfUH8Ak

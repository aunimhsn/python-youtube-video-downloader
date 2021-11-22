from pytube import YouTube

link = 'https://www.youtube.com/watch?v=FmoIM6bEpxI'
yt = YouTube(link)

# Showing details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)
# Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

# Starting download
print("Downloading...")

# https://stackoverflow.com/questions/70060263/pytube-attributeerror-nonetype-object-has-no-attribute-span
ys.download()
print("Download completed!")
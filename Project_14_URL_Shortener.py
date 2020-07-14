import pyshorteners

url=input("Enter the url: ")
print("URL after shortening:- ",pyshorteners.Shortener().tinyurl.short(url))
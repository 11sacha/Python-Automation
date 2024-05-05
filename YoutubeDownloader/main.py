import ssl
import requests
from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
# import AppKit

# class AppDelegate(AppKit.NSObject):
#     def applicationSupportsSecureRestorableState_(self, app):
#         return True

requests.packages.urllib3.disable_warnings()

ssl._create_default_https_context = ssl._create_unverified_context


def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        high_resolution_stream = streams.get_highest_resolution()
        high_resolution_stream.download(output_path=save_path)
        print("Video downloaded successfully!")


    except Exception as e:
        print(e)


def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder

if __name__ == "__main__":
    # app = AppKit.NSApplication.sharedApplication()
    # delegate = AppDelegate.alloc().init()
    # app.setDelegate_(delegate)
    # AppKit.NSApp().run()

    root = tk.Tk()
    root.withdraw()

    video_url = input("Enter youtube URL: ")
    save_folder = open_file_dialog()

    if save_folder:
        print("Download started..")
        download_video(video_url, save_folder)
    else:
        print("Invalid save location..")
        
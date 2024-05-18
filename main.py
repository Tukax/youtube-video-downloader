import os
from pytube import YouTube

def download_youtube_video(url, save_path):
    try:
        yt = YouTube(url)
        
        video = yt.streams.get_highest_resolution()
        
        video.download(save_path)
        
        print("\nDownload Process is Done!")
    except Exception as e:
        print(f"\nAn Error Occurred: {e}")

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  
        
        print("YouTube Video Downloader")
        print("======================")
        
        video_url = input("Enter the URL of the YouTube video you want to download: ").strip()
        save_path = input("Enter the directory where you want to save the video: ").strip()
        
        save_path = save_path.strip('\"')
        save_path = r"{}".format(save_path)
        
        download_youtube_video(video_url, save_path)
        
        input("\nYou downloaded the video. Press Enter to close the program.")

if __name__ == "__main__":
    main()

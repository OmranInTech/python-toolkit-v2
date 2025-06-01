# youtube_downloader.py

from pytube import YouTube
import os

def download_video(url: str, download_path: str = "."):
    """
    Downloads the highest resolution YouTube video from the provided URL.
    
    Args:
        url (str): The full URL of the YouTube video.
        download_path (str): The directory where the video will be saved.
    """
    try:
        yt = YouTube(url)
        print(f"\n🔍 Title: {yt.title}")
        print(f"📺 Channel: {yt.author}")
        print(f"🕒 Length: {yt.length // 60} min {yt.length % 60} sec")
        print(f"📅 Published on: {yt.publish_date}")

        stream = yt.streams.get_highest_resolution()
        print("\n⬇️ Downloading in highest resolution...")
        stream.download(output_path=download_path)
        print(f"✅ Download completed and saved to: {os.path.abspath(download_path)}\n")
        
    except Exception as e:
        print(f"\n❌ An error occurred: {e}\n")

def main():
    print("🎥 YouTube Video Downloader")
    url = input("🔗 Enter YouTube video URL: ").strip()
    
    if not url.startswith("http"):
        print("❌ Invalid URL. Please enter a full YouTube video link.")
        return

    folder = input("📁 Enter download folder (leave empty for current directory): ").strip()
    download_path = folder if folder else "."
    
    download_video(url, download_path)

if __name__ == "__main__":
    main()

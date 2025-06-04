from pytube import YouTube

def download_youtube_video():
    try:
        url = input("Enter YouTube video URL: ").strip()
        yt = YouTube(url)

        print(f"\n🎬 Title: {yt.title}")
        print(f"📺 Channel: {yt.author}")
        print(f"⏱ Duration: {yt.length} seconds")
        print("\nDownloading...")

        stream = yt.streams.get_highest_resolution()
        stream.download()

        print("✅ Download completed successfully!")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    download_youtube_video()

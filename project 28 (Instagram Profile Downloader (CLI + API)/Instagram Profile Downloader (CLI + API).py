import instaloader

def download_instagram_profile(username):
    loader = instaloader.Instaloader()

    try:
        print(f"⏳ Downloading profile picture for: {username}")
        loader.download_profile(username, profile_pic_only=True)
        print("✅ Download completed successfully.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("📸 Instagram Profile Picture Downloader")
    user = input("Enter Instagram username: ").strip()
    download_instagram_profile(user)

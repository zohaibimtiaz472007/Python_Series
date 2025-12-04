import re
import requests

def download_thumbnail(url):
    
    match = re.search(r"(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})", url)
    if not match:
        print("Invalid YouTube URL")
        return
    video_id = match.group(1)

    
    urls = [
        f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg",
        f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
    ]

    for img_url in urls:
        response = requests.get(img_url)
        if response.status_code == 200 and len(response.content) > 1000:
            with open("thumbnail.jpg", "wb") as f:
                f.write(response.content)
            print(f"Thumbnail downloaded as thumbnail.jpg from {img_url}")
            return

    print("Thumbnail not found!")

# Input YouTube URL
video_url = input("Enter YouTube video URL: ")
download_thumbnail(video_url)

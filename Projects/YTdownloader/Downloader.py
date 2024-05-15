import requests
from bs4 import BeautifulSoup
import json

def main() -> None:

    def get_video_info(url: str) -> tuple:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            print("HTML Content:", soup)  # Debugging statement

            title = soup.find("title").get_text()
            print("Title:", title)  # Debugging statement

            stream_map = {}
            stream_data = soup.find_all("script", {"type": "application/ld+json"})
            for data in stream_data:
                stream_json = data.string.strip()
                if '"@type":"VideoObject"' in stream_json:
                    stream_info = json.loads(stream_json)
                    print("Stream Info:", stream_info)  # Debugging statement
                    stream_url = stream_info.get("contentUrl")
                    stream_quality = stream_info.get("quality")
                    if stream_url and stream_quality:
                        stream_map[stream_quality] = stream_url

            return title, stream_map
        except Exception as e:
            print("Error:", e)
            return None, None

    def download_video(url: str) -> None:
        try:
            title, stream_map = get_video_info(url)
            if not title or not stream_map:
                print("Failed to get video information")
                return
            
            stream_url = max(stream_map.values())
            print("Selected Stream URL:", stream_url)  # Debugging statement

            response = requests.get(stream_url)
            with open('downloads/video.mp4', "wb") as f:
                f.write(response.content)

            print("Video downloaded")
        except Exception as e:
            print("Error:", e)

    video_url = input("Paste video URL: ")
    download_video(video_url)

if __name__ == '__main__':
    main()

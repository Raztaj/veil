import os
import re
import urllib.request
import urllib.error
from urllib.parse import urljoin

BASE_URL = "https://veiltail.net/"
OUTPUT_DIR = r"d:\veiltail training\veil-feat-static-veiltail-site"
CSS_DIR = os.path.join(OUTPUT_DIR, "css")
IMG_DIR = os.path.join(OUTPUT_DIR, "images")

os.makedirs(CSS_DIR, exist_ok=True)
os.makedirs(IMG_DIR, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def download_file(url, filepath):
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as response, open(filepath, 'wb') as f:
            f.write(response.read())
        print(f"Downloaded: {filepath}")
    except Exception as e:
        print(f"Failed to download {repr(url)}: {e}")

def main():
    # 1. Fetch Homepage
    try:
        req = urllib.request.Request(BASE_URL, headers=HEADERS)
        with urllib.request.urlopen(req) as response:
            html_content = response.read().decode('utf-8')
    except Exception as e:
        print(f"Failed to fetch homepage: {e}")
        return

    # 2. Extract CSS LInks
    css_links = re.findall(r'<link[^>]+rel=["\']stylesheet["\'][^>]+href=["\'](.*?)["\']', html_content)
    print(f"Found CSS links: {css_links}")
    
    for link in css_links:
        full_url = urljoin(BASE_URL, link)
        if "style.css" in full_url or "main.css" in full_url:
            download_file(full_url, os.path.join(CSS_DIR, "style-live.css"))

    # 3. Extract Images
    img_srcs = re.findall(r'<img[^>]+src=["\'](.*?)["\']', html_content)
    print(f"Found {len(img_srcs)} images.")
    
    for src in img_srcs:
        full_url = urljoin(BASE_URL, src)
        filename = os.path.basename(full_url.split("?")[0])
        
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.svg', '.gif', '.webp')):
            continue

        download_file(full_url, os.path.join(IMG_DIR, filename))

if __name__ == "__main__":
    main()

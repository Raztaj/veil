import urllib.request
import os

urls = [
    'https://veiltail.net/wp-content/uploads/2026/01/1.png',
    'https://veiltail.net/wp-content/uploads/2026/01/2.png',
    'https://veiltail.net/wp-content/uploads/2026/01/3.png',
    'https://veiltail.net/wp-content/uploads/2026/01/5.png',
    'https://veiltail.net/wp-content/uploads/2026/01/7.png',
    'https://veiltail.net/wp-content/uploads/2026/01/8.png',
    'https://veiltail.net/wp-content/uploads/2025/07/Untitled-design-13.png',
    'https://veiltail.net/wp-content/uploads/2025/07/Untitled-design-14.png',
    'https://veiltail.net/wp-content/uploads/2025/06/120000-2.jpg'
]

os.makedirs('images', exist_ok=True)
for url in urls:
    name = url.split('/')[-1]
    print(f"Downloading {name}...")
    try:
        urllib.request.urlretrieve(url, f"images/{name}")
        print(f"Success: {name}")
    except Exception as e:
        print(f"Failed {name}: {e}")

import urllib.request
import os

urls = [
    'https://veiltail.net/wp-content/uploads/2025/08/11-scaled-r7dq7cee24s7ndkfnao89l91mlcfbbq6rncv82jbg0.png',
    'https://veiltail.net/wp-content/uploads/2025/08/12-scaled-r7dq7v75uthy3kt4lisrngi9iarrl9sti8ektlrfzk.png',
    'https://veiltail.net/wp-content/uploads/2025/08/13-scaled-r7dq95995p8zwgy84kphjmvum6gr2fvo0kddc5v5io.png',
    'https://veiltail.net/wp-content/uploads/2025/08/14-scaled-r7dq9tp23e6gabyq5v9scgpu274amkkorxbztcux0w.png',
    'https://veiltail.net/wp-content/uploads/2025/08/15-scaled-r7dqaqleqlfhkomxtrhq9qeyuom53z7akg5zm1i4z4.png',
    'https://veiltail.net/wp-content/uploads/2025/08/16-scaled-r7dqbr9454to5h5ovpc6gz5y0plgg68tphlxbtzs8g.png',
    'https://veiltail.net/wp-content/uploads/2025/08/17-scaled-r7dqcxjuoofknxg90pme36hor1sz2jwqvayrxa92gg.png',
    'https://veiltail.net/wp-content/uploads/2025/08/18-scaled-r7dqdfesaj40siqb4fcawjzg1dcy4svn9rd01jil68.png',
    'https://veiltail.net/wp-content/uploads/2025/08/19-scaled-r7dqe038gvwbvxw9roa3ferl3uj0u55qolpolmnxdc.png',
    'https://veiltail.net/wp-content/uploads/2025/08/20-scaled-r7dqekron8omzd28ex7vy9jq6bp3jhfu3g2d5pt9kg.png',
    'https://veiltail.net/wp-content/uploads/2025/08/21-scaled-r7dqfho1afxo9pqg2tftvj8uyt6y0w2fvywcyeghio.png',
    'https://veiltail.net/wp-content/uploads/2025/08/22-scaled-r7dqg9v6zh09y0lhi5mmyc4osdbyft6dzugxcpaoc0.png',
    'https://veiltail.net/wp-content/uploads/2025/08/23-scaled-r7dqhea95cjlt8yry53lfjxibxsqmsmuheiszlmqwg.png',
    'https://veiltail.net/wp-content/uploads/2025/08/25-scaled-r7dqk5x59sbzzwy1sc61rusdas5napme73o9uxj0kw.png',
    'https://veiltail.net/wp-content/uploads/2025/08/26-scaled-r7dqlgx2ri4c4f1s5whe8ixf01pzzksz1kajurlbxs.png'
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

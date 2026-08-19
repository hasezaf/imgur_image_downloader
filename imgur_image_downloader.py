import bs4, requests, sys
from pathlib import Path
print('Images will be downloaded to a folder named "downloads" in the current directory i.e the path in your at start of your command prompt.')
if len(sys.argv) < 3:
    sys.exit('Error: Not enough arguments provided. Usage: python imgur_image_downloader.py <search term> <number of images>')
try:
    ask_for_num = int(sys.argv[-1].strip())
except ValueError:
    sys.exit('Error: Number of images must be an integer.')
headers = {'User-Agent': 'Mozilla/5.0'}
search = ' '.join(sys.argv[1:-1]).strip()
print('Downloading Search Page...')
content = requests.get(f'https://imgur.com/search?q={search}', headers=headers)
content.raise_for_status()
soup = bs4.BeautifulSoup(content.text, 'html.parser')
images = soup.select('.image-list-link img')
if not images:
    sys.exit('No images found for the given search term.')
path = Path('downloads')/search.replace(' ','_')
path.mkdir(parents= True, exist_ok= True)
num = min(ask_for_num, len(images))
for i in range(num):
    print(f'Downloading {i+1} image...')
    try:
        image = requests.get(f"https:{images[i].get('src')}",headers=headers, timeout=10)
        image.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f'Skipping {images[i].get("src")}: {e}')
        continue
    with open(path/f'image{i+1}.jpg','wb') as file:
        for chunk in image.iter_content(1000000):
            file.write(chunk)
    print(f'image{i+1} saved to {path.absolute()}')










# imgur_image_downloader\n
**Automatically searches and downloads number of images, specified by you in command terminal, from Imgur and stores them in local directory neatly. Uses beautiful soup and requests modules in python.**\n

**What can it do?:**\n
Can Retrieve images based on multi word search queries\n
Can set maximum number of images to download or if less than the number specified, download all images that appear on searching\n
Can automatically create a folder in your current working directly with subfolders (./downloads/<search term>)\n
Can handle errors, skipping broken urls, timeouts and misinputs\n

**Prerequisites:**\n
Python 3.7 or higher installed in your system\n

**Installation:**\n
Clone repository:\n
```bash
   git clone [https://github.com/hasezaf/imgur-image-downloader.git](https://github.com/hasezaf/imgur-image-downloader.git)
   cd imgur-image-downloader
```
Install dependencies:\n
```bash
pip install -r requirements.txt
```
 OR ALTERNATIVELY

 ```bash
pip install beautifulsoup4 requests
```

**How to use:**\n
Run your command in this format in command terminal "python imgur_image_downloader.py <search term> <number of images>" replacing text within <> with your inputs for example this command on my pc would look like this:

C:\Users\users> python imgur_image_downloader cats 10\n
will download 10 images of cats at path 'C:/Users/users/downloads/cats', it forms a downloads folder at your current working directory.\n

Thank you for using this.

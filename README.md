# Web Scraping & Automation Collection

A collection of lightweight Python automation scripts for web scraping, media retrieval, and data extraction.

## Included Projects

| Project | Description | Dependencies |
| :--- | :--- | :--- |
| **Imgur Downloader** | Downloads images from Imgur based on search queries and saves in current working directory | `requests`, `bs4`|
| **2048 Bot** | Opens and plays 2048 with random inputs and loops upon game over infinitely until user input | `playwright`|


## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/hasezaf/web-scraping-python.git](https://github.com/hasezaf/web-scraping-python.git)
   cd web-scraping-python
   ```
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```  
   Run command below as well for 2048 bot:   
   ```bash
   playwright install
   ```
3. **Run a Script**
   ```bash
   python imgur_image_downloader.py (followed by relevant command arguments if needed)
   ```
   Replace imgur_image_downloader.py with any other script that you want to run
   
**How to use:**

1. **Imgur image downloader:** Run your command in this format in command terminal:
```bash
python imgur_image_downloader.py <search term> <number of images>
```
replacing text within <> with your inputs for example this command on my pc would look like this:
C:\Users\users> python imgur_image_downloader cats 10  
and will download 10 images of cats at path 'C:/Users/users/downloads/cats', it forms a downloads folder at your current working directory.

2. **2048 Bot:**   
Just run the .py file in command terminal:
```bash
python 2048_bot.py
```
To quit the program, do Ctrl+C in you command terminal.  
You can also see your scores after every game over in your command terminal  

Thank you for using this.

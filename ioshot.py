import argparse
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from concurrent.futures import ThreadPoolExecutor
from PIL import Image

# ASCII Art Title
def print_title():
    ascii_art = r"""
                  ___           ___           ___           ___                          
    ___          /  /\         /  /\         /__/\         /  /\          ___            
   /  /\        /  /::\       /  /:/_        \  \:\       /  /::\        /  /\           
  /  /:/       /  /:/\:\     /  /:/ /\        \__\:\     /  /:/\:\      /  /:/           
 /__/::\      /  /:/  \:\   /  /:/ /::\   ___ /  /::\   /  /:/  \:\    /  /:/            
 \__\/\:\__  /__/:/ \__\:\ /__/:/ /:/\:\ /__/\  /:/\:\ /__/:/ \__\:\  /  /::\            
    \  \:\/\ \  \:\ /  /:/ \  \:\/:/~/:/ \  \:\/:/__\/ \  \:\ /  /:/ /__/:/\:\           
     \__\::/  \  \:\  /:/   \  \::/ /:/   \  \::/       \  \:\  /:/  \__\/  \:\          
     /__/:/    \  \:\/:/     \__\/ /:/     \  \:\        \  \:\/:/        \  \:\         
     \__\/      \  \::/        /__/:/       \  \:\        \  \::/          \__\/         
                 \__\/         \__\/         \__\/         \__\/  ioshot by Daryll Deatherage
"""
    print(ascii_art)

def take_screenshot(url, output_dir):
    """Takes a screenshot of a single URL and saves it to the specified directory."""
    try:
        # Set up Selenium with headless Chromium
        options = Options()
        options.add_argument('--headless')  # Run in headless mode (no UI)
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        driver = webdriver.Chrome(options=options)  # Ensure ChromeDriver is in your PATH
        driver.get(url)

        # Wait for the page to load
        time.sleep(3)

        # Set filename based on URL
        url_name = url.replace("https://", "").replace("http://", "").replace("/", "_")
        screenshot_path = os.path.join(output_dir, f"{url_name}.png")

        # Take screenshot
        driver.save_screenshot(screenshot_path)
        driver.quit()

        print(f"[+] Screenshot saved for: {url} -> {screenshot_path}")
    except Exception as e:
        print(f"[!] Failed to capture screenshot for {url}: {e}")

def process_urls(file_path, mode, output_dir, threads):
    """Reads the URL file and filters them based on the selected mode, then takes screenshots concurrently."""
    urls = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                url = line.strip()

                if mode == "https" and url.startswith("https://"):
                    urls.append(url)
                elif mode == "http" and url.startswith("http://"):
                    urls.append(url)
                elif mode == "no-http" and not url.startswith("http://") and not url.startswith("https://"):
                    urls.append(f"https://{url}")  # Assume HTTPS if no protocol is given

        if not urls:
            print("[!] No valid URLs found based on the selected mode.")
            return

        # Create output directory if not exists
        os.makedirs(output_dir, exist_ok=True)

        # Use ThreadPoolExecutor to process URLs concurrently
        with ThreadPoolExecutor(max_workers=threads) as executor:
            # Submit the screenshot task for each URL to be processed concurrently
            for url in urls:
                executor.submit(take_screenshot, url, output_dir)

        print(f"[+] Screenshots saved to: {output_dir}")

    except FileNotFoundError:
        print(f"[!] Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"[!] Unexpected error: {e}")

def main():
    print_title()  # Print ASCII Art Title

    parser = argparse.ArgumentParser(description="Capture website screenshots using Selenium.")
    parser.add_argument("-f", "--file", required=True, help="File containing URLs")
    parser.add_argument("-d", "--directory", required=True, help="Directory to save screenshots")
    parser.add_argument("-t", "--threads", type=int, default=4, help="Number of threads to run concurrently")
    parser.add_argument("-https", action="store_true", help="Capture only HTTPS sites")
    parser.add_argument("-http", action="store_true", help="Capture only HTTP sites")
    parser.add_argument("-no-http", action="store_true", help="Treat URLs without 'http://' or 'https://' as HTTPS")

    args = parser.parse_args()

    # Determine mode
    if args.https:
        mode = "https"
    elif args.http:
        mode = "http"
    elif args.no_http:
        mode = "no-http"
    else:
        print("[!] Error: You must specify either -https, -http, or -no-http.")
        return

    # Process the URLs and take screenshots with the specified number of threads
    process_urls(args.file, mode, args.directory, args.threads)

if __name__ == "__main__":
    main()

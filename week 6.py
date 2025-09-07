import requests
import os
from urllib.parse import urlparse
import hashlib

def get_filename_from_url(url):
    """
    Extracts the filename from the URL.
    If the URL does not contain a valid filename, generates a unique filename using a hash.
    """
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if not filename:
        # Generate a unique filename based on the URL
        filename = hashlib.md5(url.encode()).hexdigest() + ".jpg"
    return filename

def fetch_image(url):
    """
    Fetches an image from the given URL and saves it in the Fetched_Images directory.
    Handles HTTP errors and prevents duplicate downloads.
    """
    try:
        # Create the directory if it doesn't exist
        os.makedirs("Fetched_Images", exist_ok=True)
        
        # Set headers to be polite to the server
        headers = {
            "User-Agent": "Ubuntu Image Fetcher - respectful bot"
        }
        
        # Send HTTP GET request to fetch the image
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise error for bad HTTP status
        
        # Determine the filename
        filename = get_filename_from_url(url)
        filepath = os.path.join("Fetched_Images", filename)

        # Check if the file already exists to avoid duplicates
        if os.path.exists(filepath):
            print(f"⚠ Image '{filename}' already exists. Skipping download.")
            return
        
        # Save the image in binary mode
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        
    except requests.exceptions.RequestException as e:
        # Handle network-related errors gracefully
        print(f"✗ Connection error: {e}")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"✗ An error occurred: {e}")

def main():
    """
    Main function that prompts the user for image URLs,
    processes each URL, and fetches images.
    """
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    # Ask the user for one or more image URLs (comma-separated)
    urls_input = input("Please enter image URL(s), separated by commas: ")
    urls = [url.strip() for url in urls_input.split(",") if url.strip()]
    
    if not urls:
        print("No URLs provided. Exiting.")
        return
    
    # Fetch each image one by one
    for url in urls:
        fetch_image(url)
    
    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()

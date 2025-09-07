# Ubuntu Image Fetcher

> "I am because we are." – Ubuntu Philosophy

A Python tool for mindfully fetching and organizing images from the web, inspired by the Ubuntu principles of community, respect, and sharing.

---

## Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Precautions](#precautions)  
- [Contribution](#contribution)  
- [License](#license)  

---

## Overview

The Ubuntu Image Fetcher connects to the global community of the internet to retrieve publicly shared images. It organizes them in a local folder while handling errors gracefully and avoiding duplicates.  

This project emphasizes:

- **Community:** Connects you to shared content online.  
- **Respect:** Handles errors without crashing and avoids overwriting existing images.  
- **Sharing:** Saves images in an organized directory for later appreciation.  

---

## Features

- Prompt for **one or multiple image URLs** (comma-separated).  
- Create a **`Fetched_Images`** directory if it doesn’t exist.  
- Download images **safely** with error handling.  
- Automatically **generate filenames** if missing from the URL.  
- **Prevent duplicate downloads**.  
- Friendly terminal output aligned with Ubuntu philosophy.  

---

## Installation

1. **Clone the repository**:

```bash
git clone https://github.com/YourUsername/Ubuntu_Requests.git
cd Ubuntu_Requests

Example Terminal Session:

Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Please enter image URL(s), separated by commas: https://example.com/ubuntu-wallpaper.jpg, https://example.com/ubuntu2.jpg
✓ Successfully fetched: ubuntu-wallpaper.jpg
✓ Image saved to Fetched_Images/ubuntu-wallpaper.jpg
✓ Successfully fetched: ubuntu2.jpg
✓ Image saved to Fetched_Images/ubuntu2.jpg

Connection strengthened. Community enriched.

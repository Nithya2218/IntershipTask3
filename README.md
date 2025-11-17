# IntershipTask3
# 📰 News Headline Scraper  
A simple Python script that scrapes the latest news headlines from a public website using **Requests** and **BeautifulSoup**.

---

## 📌 Features
- Sends an HTTP GET request to fetch webpage HTML  
- Extracts all `<h2>` headline tags using BeautifulSoup  
- Cleans and saves the headlines to a `headlines.txt` file  
- Automatically creates the file if it doesn’t exist  
- Simple, beginner-friendly scraper for learning web automation  

---

## 🛠️ Technologies Used
- **Python 3**
- **requests** (for sending HTTP requests)
- **beautifulsoup4** (for HTML parsing)

---

## 📥 Installation

Install the required packages:

```bash
pip install requests
pip install beautifulsoup4

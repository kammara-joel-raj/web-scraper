import requests
from bs4 import BeautifulSoup

#i used https://novelfull.com/my-abilities-come-with-special-effects/chapter-
#but you can use any novel or book from this website
base_url = "https://novelfull.com/my-abilities-come-with-special-effects/chapter-"

# Set the start and end chapter numbers
start_chapter = 34
end_chapter = 104

# Open the text file in append mode
with open("novel_content.txt", "a", encoding="utf-8") as file:
    for chapter in range(start_chapter, end_chapter + 1):
        url = base_url + str(chapter) + ".html"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
            
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            chapter_text = soup.find('div', class_='chapter-c').get_text()  # Adjust based on the HTML structure
            
            file.write(f"Chapter {chapter}\n\n")
            file.write(chapter_text)
            file.write("\n\n---\n\n")
        except requests.RequestException as e:
            print(f"Failed to download Chapter {chapter}: {e}")

print("Novel content downloaded successfully.")
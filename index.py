import urllib.request
from bs4 import BeautifulSoup
import pdfkit

url = "https://libreboot.org/docs"

# print Single mage
def printpage(url):
    pdfkit.from_url('https://libreboot.org/docs/', 'out.pdf')

# will step threw and print everything with route example: https://libreboot.org/docs/
def printContent():
    # while True:
    #     page = requests.get(url)
    #     soup = BeautifulSoup(page.content, 'html.parser')
    #     print(soup)
    #     newLink = soup.find_all('a', href=True)[1]['href']
         print("content")

#this will prompt the user to select th content they want
def custom():
    print("custom")

printpage(url)
print(complete)

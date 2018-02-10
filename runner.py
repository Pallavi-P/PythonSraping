from bs4 import BeautifulSoup
from docx import Document
from docx.shared import Inches
import requests
import os
import sys


#r  = requests.get("https://www.reliablesoft.net/top-10-search-engines-in-the-world/")
url = "https://www.reliablesoft.net/top-10-search-engines-in-the-world/"
r  = requests.get(url)
data = r.text

soup = BeautifulSoup(data, "lxml")
document = Document()
document.add_heading('List of urls')

yes = {'yes','y'}
no = {'no','n'}
#input('Would you like to download Docx file Please respond with yes or no:')

choice = input('Would you like to download Docx file Please respond with yes or no:').lower()
if choice in yes:
        try:
                for link in soup.find_all('a'):
                        # If docx file has some error please uncomment the below print line
                        # print(link.get('href'))

                        # Adding data to docx file
                        document.add_paragraph(link.get('href'))
                document.save('scrap.docx')

        except OSError:
                pass

elif choice in no:
        for link in soup.find_all('a'):
                print(link.get('href'))
else:
   sys.stdout.write("Please respond with 'yes' or 'no'")


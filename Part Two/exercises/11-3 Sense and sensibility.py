import PyPDF2
import os

path = os.path.dirname(os.path.abspath(__file__))

file_handle = open(path+"/"+'Sense-and-Sensibility-by-Jane-Austen.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(file_handle)
page_text = ""
page_number = len(pdfReader.pages)
for i in range(page_number):    
    page_object = pdfReader.pages[i]
    page_text += page_object.extract_text()

frequency_table = dict()
text_list = page_text.split("\n")


for line in text_list:
    for word in line.split(" "):
        if "https://www.fulltextarchive.com" in word:
            word = word.replace("https://www.fulltextarchive.com", "")

print(text_list)

# for word in text_list:
#     if "https://www.fulltextarchive.com" in word:
#         word = word.replace("https://www.fulltextarchive.com", "")
#     if word.isalpha():
#         word = word.lower()
        


print(type(page_text))
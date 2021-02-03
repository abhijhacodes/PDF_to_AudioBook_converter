import pyttsx3
import PyPDF2

# creating the speaker
speaker = pyttsx3.init()

# opening the book and reading using module
book = open('The_Theory_Of_Everything.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)

# total pages
pages = pdfReader.numPages

# reading the book for desired page numbers
# you can adjust that value as you need

for n in range(11, pages):
    # getting the page and extracting text from it
    page = pdfReader.getPage(n)
    text = page.extractText()

    # calling the speaker to say text
    speaker.say(text)
    speaker.runAndWait()


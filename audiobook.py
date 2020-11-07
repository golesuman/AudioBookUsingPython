import pyttsx3
import time
import PyPDF2
#put your pdf here
book=open('qmc.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages
print(pages)
speaker=pyttsx3.init()
voices=speaker.getProperty('voices')
speaker.setProperty('rate', 130)
#enter 1 for female voice and 0 for the male voice
speaker.setProperty('voice', voices[1].id)
for num in range(0, pages):
    page=pdfReader.getPage(0)
    text=page.extractText()
    speaker.say(text)
    speaker.runAndWait()
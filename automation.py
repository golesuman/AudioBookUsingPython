import pyttsx3
import PyPDF2
bk=open('qmc.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(bk)
pages=pdfReader.numPages
print(pages)
speaker=pyttsx3.init()
voices=speaker.getProperty('voices')
speaker.setProperty('voice',voices[0].id)
for i in range(0, pages):
    page=pdfReader.getPage(1)
    text=page.extractText()
    speaker.say(text)
    speaker.runAndWait()

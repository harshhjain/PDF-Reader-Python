import pyttsx3
import PyPDF2

myPDF = open('XXXXXX.pdf', 'rb')            # XXXXXX.pdf is the fileName.pdf
                                            # rb = Read Binary as we are opening PDF file
pdfReader = PyPDF2.PdfFileReader(myPDF)
pages = pdfReader.numPages                  # Total number of pages in this PDF
speak = pyttsx3.init() 
for number in range(22, pages):             # (22, pages) - 22 is start page till total number of pages in this PDF
    page = pdfReader.getPage(number)
    text = page.extractText()               # Extract into text
    speak.say(text)                         # Speak / say our loud the extracted text
    speak.runAndWait()

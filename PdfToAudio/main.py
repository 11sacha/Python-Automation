import pyttsx3
from PyPDF2 import PdfReader
import os
import objc

# Define file paths
FilePath = os.path.dirname(__file__)
AudiobooksPath = os.path.join(FilePath, r'Audios')
PdfPath = os.path.join(FilePath, r'Files')

# Create Audiobooks directory if it doesn't exist
os.makedirs(AudiobooksPath, exist_ok=True)

try:
    # Loop through PDF files in the directory
    for filename in os.listdir(PdfPath):
        if filename.endswith('.pdf'):
            pdf_file_path = os.path.join(PdfPath, filename)
            audiobook_file_path = os.path.join(AudiobooksPath, f"{os.path.splitext(filename)[0]}.mp3")

            # Read PDF
            with open(pdf_file_path, 'rb') as book:
                reader = PdfReader(book)
                full_text = ""

                # Extract text from each page
                for page in range(len(reader.pages)):
                    content = reader.pages[page].extract_text()
                    full_text += content

                # Initialize pyttsx3 and save audio
                audio_reader = pyttsx3.init()
                audio_reader.setProperty('rate', 100)
                audio_reader.save_to_file(full_text, audiobook_file_path)

    # Run the converter engine
    audio_reader.runAndWait()
except Exception as e:
    print(f'Error occured: {e}')

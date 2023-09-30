# PDF Utility

PDF Utility is a Python GUI application that provides various features for working with PDF files. It allows users to browse PDF files, export them to DOC format, save PDF content as audio, and adjust the playback speed of the generated audio.

![Screenshot from 2023-09-22 14-54-14](https://github.com/Charlieissa/PDF2Voice/assets/59963704/ec188fb8-9dd7-45a9-b8a5-0643c6f9acec)

## Introduction

PDF Utility simplifies common PDF-related tasks and enhances accessibility through text-to-speech functionality.

## Dependencies

PDF Utility relies on the following dependencies:

- docx==0.2.4
- gTTS==2.3.2
- lingua==4.15.0
- pdfminer==20191125
- pdfminer.six==20221105
- PyQt5==5.15.9
- PyQt5_sip==12.12.2
- PyQt5_sip==12.9.1
- python_bidi==0.4.2
- python_docx==0.8.11
- pyttsx3==2.90

**You can install these dependencies using pip:**

pip install -r requirements.txt


**Tested On**

PDF Utility has been tested on the following platforms:
    Ubuntu 20.04
But should works on all OS.

**Usage**

**PDF to DOC Export**
To export a PDF file to DOC format, follow these steps:

    Launch the PDF Utility application.
    Click the "Browse PDF" button to select the PDF file you want to convert.
    Click the "Export to DOC" button.
    Choose a destination folder to save the DOC file.
    Click "Save."

**Text-to-Speech (PDF to Audio)**
PDF Utility allows you to convert PDF text to audio (support only English) and adjust playback speed. Here's how:

    Launch the PDF Utility application.
    Click the "Browse PDF" button to select the PDF file.
    Click the "Play" button.
    Adjust the playback speed using the provided options.
    Click "Save audio" to save the audio file.

**Translate text**
To translate a PDF file to different language, follow these steps :

    Launch the PDF Utility application.
    Click the "Browse PDF" button to select the PDF file you want to convert.
    Click the language you want to translate to.
    Click the "Translate" button.

    
**Supported Language**

Playing without saving:

  -English

Saving:

  -English
  -Arabic
  -Hebrew
  -French
  -German
  -Spanish

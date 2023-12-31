# PDF Utility

PDF Utility is a Python GUI application that provides various features for working with PDF files. It allows users to browse PDF files, export them to DOC format, save PDF content as audio, and adjust the playback speed of the generated audio.

![Screenshot from 2023-09-30 14-51-52](https://github.com/Charlieissa/PDF2Voice/assets/59963704/781557f4-917b-4fa6-84f3-eb39f953058d)

## Introduction

PDF Utility simplifies common PDF-related tasks and enhances accessibility through text-to-speech functionality.

## Dependencies

PDF Utility relies on the following dependencies:

-deep_translator==1.11.4<br/>
-docx==0.2.4<br/>
-gTTS==2.3.2<br/>
-lingua==4.15.0<br/>
-pdfminer==20191125<br/>
-pdfminer.six==20221105<br/>
-PyQt5==5.15.9<br/>
-PyQt5_sip==12.12.2<br/>
-PyQt5_sip==12.9.1<br/>
-python_bidi==0.4.2<br/>
-python_docx==0.8.11<br/>
-pyttsx3==2.90<br/>


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
suppoerted language translate to -> Arabic,Hebrew,English,German,French,Italy
To translate a PDF file to different language, follow these steps :

    Launch the PDF Utility application.
    Click the "Browse PDF" button to select the PDF file you want to convert.
    Click the language you want to translate to.
    Click the "Translate" button.

    
**Supported Language**

Playing without saving:

  -English

Saving:

  -English<br/>
  -Arabic<br/>
  -Hebrew<br/>
  -French<br/>
  -German<br/>
  -Spanish<br/>

import datetime
import sys
import textwrap
import os
import signal
import time
import pyttsx3
from pdfminer.high_level import extract_text
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt
import docx
from sys import platform
from gtts import gTTS
from threading import Thread
import re
from bidi.algorithm import get_display
from lingua import Language, LanguageDetectorBuilder
from deep_translator import GoogleTranslator

languages = [Language.ENGLISH, Language.HEBREW, Language.ARABIC, Language.FRENCH, Language.GERMAN, Language.SPANISH]
detector = LanguageDetectorBuilder.from_languages(*languages).build()
language_mapping = {
    "ENGLISH": "en",
    "HEBREW": "iw",
    "ARABIC": "ar",
    "GERMAN": "de",
    "SPANISH": "es",
    "FRENCH": "fr",
    "ITALY": "it"
}


# GUI configuration
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(766, 680)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(766, 680))
        MainWindow.setMaximumSize(QtCore.QSize(766, 680))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_browse = QtWidgets.QPushButton(self.centralwidget)
        self.btn_browse.setGeometry(QtCore.QRect(640, 50, 89, 25))
        self.btn_browse.setObjectName("btn_browse")
        self.txt_pdf_location = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_pdf_location.setEnabled(True)
        self.txt_pdf_location.setGeometry(QtCore.QRect(180, 50, 441, 25))
        self.txt_pdf_location.setReadOnly(True)
        self.txt_pdf_location.setObjectName("txt_pdf_location")
        self.txt_pdf_content = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_pdf_content.setGeometry(QtCore.QRect(30, 120, 701, 441))
        self.txt_pdf_content.setTabChangesFocus(False)
        self.txt_pdf_content.setObjectName("txt_pdf_content")
        self.btn_play = QtWidgets.QPushButton(self.centralwidget)
        self.btn_play.setEnabled(False)
        self.btn_play.setGeometry(QtCore.QRect(640, 580, 89, 25))
        self.btn_play.setObjectName("btn_play")
        self.btn_export_doc = QtWidgets.QPushButton(self.centralwidget)
        self.btn_export_doc.setEnabled(False)
        self.btn_export_doc.setGeometry(QtCore.QRect(30, 600, 89, 25))
        self.btn_export_doc.setObjectName("btn_export_doc")
        self.btn_save_audio = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save_audio.setEnabled(False)
        self.btn_save_audio.setGeometry(QtCore.QRect(130, 600, 89, 25))
        self.btn_save_audio.setObjectName("btn_save_audio")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 50, 121, 25))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 90, 121, 25))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.combo_speed = QtWidgets.QComboBox(self.centralwidget)
        self.combo_speed.setEnabled(False)
        self.combo_speed.setGeometry(QtCore.QRect(540, 580, 86, 25))
        self.combo_speed.setObjectName("combo_speed")
        self.combo_speed.addItem("")
        self.combo_speed.addItem("")
        self.combo_speed.addItem("")
        self.txt_select_speed = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_select_speed.setEnabled(False)
        self.txt_select_speed.setGeometry(QtCore.QRect(410, 580, 121, 25))
        self.txt_select_speed.setReadOnly(True)
        self.txt_select_speed.setObjectName("txt_select_speed")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(640, 90, 89, 25))
        self.btn_clear.setObjectName("btn_clear")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 640, 111, 25))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.txt_language = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_language.setEnabled(True)
        self.txt_language.setGeometry(QtCore.QRect(150, 640, 71, 25))
        self.txt_language.setReadOnly(True)
        self.txt_language.setObjectName("txt_language")
        self.btn_stop = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stop.setEnabled(False)
        self.btn_stop.setGeometry(QtCore.QRect(640, 620, 89, 25))
        self.btn_stop.setObjectName("btn_stop")
        self.btn_pause = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pause.setEnabled(False)
        self.btn_pause.setGeometry(QtCore.QRect(410, 620, 89, 25))
        self.btn_pause.setObjectName("btn_pause")
        self.btn_resume = QtWidgets.QPushButton(self.centralwidget)
        self.btn_resume.setEnabled(False)
        self.btn_resume.setGeometry(QtCore.QRect(530, 620, 89, 25))
        self.btn_resume.setObjectName("btn_resume")
        self.btn_translate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_translate.setGeometry(QtCore.QRect(30, 570, 191, 25))
        self.btn_translate.setObjectName("btn_translate")
        self.combo_translate_lang = QtWidgets.QComboBox(self.centralwidget)
        self.combo_translate_lang.setGeometry(QtCore.QRect(240, 570, 86, 25))
        self.combo_translate_lang.setObjectName("combo_translate_lang")
        self.combo_translate_lang.addItem("")
        self.combo_translate_lang.addItem("")
        self.combo_translate_lang.addItem("")
        self.combo_translate_lang.addItem("")
        self.combo_translate_lang.addItem("")
        self.combo_translate_lang.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PDF To Voice"))
        self.btn_browse.setText(_translate("MainWindow", "Browse"))
        self.btn_play.setText(_translate("MainWindow", "Play"))
        self.btn_export_doc.setText(_translate("MainWindow", "Export Doc"))
        self.btn_save_audio.setText(_translate("MainWindow", "Save Audio"))
        self.lineEdit.setText(_translate("MainWindow", "Choose PDF FIle "))
        self.lineEdit_2.setText(_translate("MainWindow", "PDF Content"))
        self.combo_speed.setItemText(0, _translate("MainWindow", "Slow"))
        self.combo_speed.setItemText(1, _translate("MainWindow", "Medium"))
        self.combo_speed.setItemText(2, _translate("MainWindow", "Fast"))
        self.txt_select_speed.setText(_translate("MainWindow", "Select Speed"))
        self.btn_clear.setText(_translate("MainWindow", "Clear"))
        self.lineEdit_4.setText(_translate("MainWindow", "PDF Language"))
        self.btn_stop.setToolTip(_translate("MainWindow", "<html><head/><body><p>Stop</p></body></html>"))
        self.btn_stop.setText(_translate("MainWindow", "⏹"))
        self.btn_pause.setToolTip(_translate("MainWindow", "<html><head/><body><p>Pause</p></body></html>"))
        self.btn_pause.setText(_translate("MainWindow", "▐▐"))
        self.btn_resume.setToolTip(_translate("MainWindow", "<html><head/><body><p>Play</p></body></html>"))
        self.btn_resume.setText(_translate("MainWindow", "▶"))
        self.btn_translate.setText(_translate("MainWindow", "Translate"))
        self.combo_translate_lang.setItemText(0, _translate("MainWindow", "ARABIC"))
        self.combo_translate_lang.setItemText(1, _translate("MainWindow", "HEBREW"))
        self.combo_translate_lang.setItemText(2, _translate("MainWindow", "ENGLISH"))
        self.combo_translate_lang.setItemText(3, _translate("MainWindow", "FRENCH"))
        self.combo_translate_lang.setItemText(4, _translate("MainWindow", "GERMAN"))
        self.combo_translate_lang.setItemText(5, _translate("MainWindow", "ITALY"))


class MyGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.running = None
        self.speed_speech = None
        self.show()
        self.pdf_text = ""
        self.lang = None
        self.paused = False
        self.engine = pyttsx3.init()
        self.ui.btn_translate.setEnabled(False)
        self.ui.btn_clear.clicked.connect(self.ui.txt_pdf_content.clear)
        self.ui.btn_browse.clicked.connect(self.browse_file)
        self.ui.btn_play.clicked.connect(self.thread_fun)
        self.ui.btn_export_doc.clicked.connect(self.export_doc)
        self.ui.btn_save_audio.clicked.connect(self.save_audio)
        self.ui.btn_stop.clicked.connect(self.stop)
        self.ui.btn_pause.clicked.connect(self.pause)
        self.ui.btn_resume.clicked.connect(self.resume)
        self.ui.btn_translate.clicked.connect(self.translate_text)

    def stop(self) -> None:
        """
        Function to control the text playing
        :return:
        """
        self.running = False

    def pause(self) -> None:
        """
        Function to control the text playing
        :return:
        """
        self.paused = True

    def resume(self) -> None:
        """
        Function to control the text playing
        :return:
        """
        self.paused = False

    def closeEvent(self, event) -> None:
        """
        This function is closing the app and stopping the sound of the speech with it.
        :param event: form event
        :return: None
        """
        reply = QMessageBox.question(self, 'Window Close',
                                     'Are you sure you want to close the window?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            if platform == "linux" or platform == "linux2":
                os.kill(os.getpid(), signal.SIGTERM)
            elif platform == "win32":
                os.system("taskkill /im python.exe")
            event.accept()
        else:
            event.ignore()

    def browse_file(self) -> None:
        """
        The function ask the user for file (it must be pdf) and check in which language it is and convert it to text
        if the language is not english it disable the sound buttons
        :return:None
        """
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_filter = "PDF Files (*.pdf)"  # Filter for PDF files
        file_name, _ = QFileDialog.getOpenFileName(self, "Open PDF File", "/home/", file_filter, options=options)
        if file_name.endswith(".pdf"):
            self.ui.btn_translate.setEnabled(True)
            self.ui.txt_pdf_location.setText(file_name)
            self.pdf_text = extract_text(file_name)
            self.pdf_text = get_display(self.pdf_text)
            self.lang = detector.detect_language_of(self.pdf_text).name
            self.ui.btn_save_audio.setEnabled(True)
            if self.lang == "ENGLISH":
                self.ui.btn_play.setEnabled(True)
                self.ui.txt_select_speed.setEnabled(True)
                self.ui.combo_speed.setEnabled(True)

            else:
                self.ui.btn_play.setEnabled(False)
                self.ui.txt_select_speed.setEnabled(False)
                self.ui.combo_speed.setEnabled(False)
            self.ui.txt_language.setText(self.lang)
            self.pdf_text = re.sub(r'\s{5,}', ' ', self.pdf_text)  # Reformat string without alot of spaces
            self.pdf_text = re.sub(r'https?://\S+|www\.\S+', '', self.pdf_text)  # remove all the links from text
            self.ui.txt_pdf_content.insertPlainText(self.pdf_text)
            self.ui.btn_export_doc.setEnabled(True)

        else:
            message = QMessageBox()
            message.setText("File Must Be PDF!")
            message.exec_()

    def pdf_to_voice(self) -> None:
        """
        The function split the text in chunks to make the program more responsive and not stuck
        and then read it with male voice
        :return:
        """
        if self.lang == "ENGLISH":
            self.ui.btn_stop.setEnabled(True)
            self.ui.btn_pause.setEnabled(True)
            self.ui.btn_resume.setEnabled(True)
        splitted_text = textwrap.wrap(self.ui.txt_pdf_content.toPlainText(), 10)
        self.running = True
        for i, chunk in enumerate(splitted_text):
            self.speed_speech = self.ui.combo_speed.currentText()
            if self.speed_speech == "Slow":
                rate = 100
            elif self.speed_speech == "Medium":
                rate = 150
            else:
                rate = 200
            if self.running and not self.paused:
                self.engine.setProperty("rate", rate)  # speed reading
                self.engine.setProperty('voice', str(self.lang).lower())
                self.engine.say(chunk)
                self.engine.runAndWait()
            else:
                while self.paused:
                    time.sleep(2)
        self.running = False

    def thread_fun(self) -> None:
        """
        Function to make the threads for reading pdf  function to make it  faster
        :return:
        """
        t = Thread(target=self.pdf_to_voice, name="PdfToVoiceThread")
        t.start()

    def export_doc(self) -> None:
        """
        the function save the generated text from pdf file to doc file
        :return:
        """
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_filter = "Word Documents (*.docx);;All Files (*)"  # Filter for Word documents
        file_name, _ = QFileDialog.getSaveFileName(self, "Save as Word Document", "converted_doc", file_filter,
                                                   options=options)
        if file_name:
            doc = docx.Document()
            doc.add_paragraph(self.ui.txt_pdf_content.toPlainText())
            doc.save(file_name + ".docx")
            QMessageBox.information(self, "File Saved", f"Text has been saved to {file_name}", QMessageBox.Ok)

    def save_audio(self) -> None:
        """
        the function add an option to the user to save the audio that generated from text
        :return:
        """

        if self.lang in language_mapping:
            lang = language_mapping[self.lang]
        else:
            message = QMessageBox()
            message.setWindowTitle("Info")
            message.setText("Language is not supported! ")
            message.exec_()
            return
        file_path = "pdf_audio.mp3"
        message = QMessageBox()
        message.setWindowTitle("Info")
        message.setText(f"It Could Take a While Depends On Words Count...Will Generate In Background, MeanWile You "
                        f"Can Continue to use the program ")
        message.exec_()
        save_thread = Thread(target=save_audio_to_file, args=(self.ui.txt_pdf_content.toPlainText(), lang, file_path))
        save_thread.start()

    def translate_text(self):
        """
        the function translate the pdf file to different language that supported
        [Arabic,Hebrew,English,German,French,Italy]
        :return:
        """
        message = QMessageBox()
        message.setWindowTitle("Info")
        message.setText("Translating,it may take a while...")
        message.exec_()
        translate_lang = self.ui.combo_translate_lang.currentText()
        if translate_lang in language_mapping:
            lang = language_mapping[translate_lang]
        text_chunks = [self.pdf_text[i:i + 3000] for i in range(0, len(self.pdf_text), 3000)]
        translations = []

        for chunk in text_chunks:
            translation = GoogleTranslator(source='auto', target=lang).translate(chunk)
            translations.append(translation)

        self.ui.txt_pdf_content.clear()
        final_translation = " ".join(translations)
        if lang == "iw" or lang == "ar":
            self.ui.txt_pdf_content.setAlignment(Qt.AlignRight)
            self.ui.txt_pdf_content.setLayoutDirection(Qt.RightToLeft)
        self.ui.txt_language.setText(translate_lang)
        self.ui.txt_pdf_content.insertPlainText(final_translation)
        self.lang = detector.detect_language_of(self.ui.txt_pdf_content.toPlainText()).name
        if not self.lang == "ENGLISH":
            self.ui.btn_play.setEnabled(False)
            self.ui.txt_select_speed.setEnabled(False)
            self.ui.combo_speed.setEnabled(False)
            self.ui.btn_stop.setEnabled(False)
            self.ui.btn_pause.setEnabled(False)
            self.ui.btn_resume.setEnabled(False)


def save_audio_to_file(text, lang, file_path):
    try:
        tts = gTTS(text=text, lang=lang)
        tts.save(datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p") + ".mp3")
        message = QMessageBox()
        message.setText(f"Audio save to file {file_path}")
        message.exec_()
    except Exception as e:
        message = QMessageBox()
        message.setText(f"Error saving audio: {str(e)}")
        message.exec_()


def main():
    app = QApplication(sys.argv)
    window = MyGUI()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QListWidget, QProgressBar, QMessageBox
from pytube import Search, YouTube
import sys
from src.transcribe import transcribe_audio_mp4

import os

# Import your Ollama class here
#from src.ollama_api import OllamaAPI  # Adjust the import according to your file's name

class YouTubeDownloader(QMainWindow):
    def __init__(self):
        super().__init__()
        self.results = []  # Initialize the results attribute
        self.initUI()


    def initUI(self):
        self.setWindowTitle('YouTube Search Results')
        self.setGeometry(300, 300, 800, 600)

        self.search_field = QLineEdit(self)
        self.search_field.setGeometry(20, 20, 640, 40)

        self.search_button = QPushButton('Search', self)
        self.search_button.setGeometry(680, 20, 100, 40)
        self.search_button.clicked.connect(self.search_youtube)

        self.listbox = QListWidget(self)
        self.listbox.setGeometry(20, 80, 760, 400)

        self.progress = QProgressBar(self)
        self.progress.setGeometry(20, 500, 760, 30)

        self.download_button = QPushButton('Download', self)
        self.download_button.setGeometry(20, 550, 760, 40)
        self.download_button.clicked.connect(self.download_selected)

        self.results = []

    def search_youtube(self):
        query = self.search_field.text()
        s = Search(query)
        self.results = s.results[:10]  # Limiting to 10 results
        self.listbox.clear()
        for result in self.results:
            self.listbox.addItem(result.title)

    def download_selected(self):
        selected_index = self.listbox.currentRow()
        if selected_index >= 0:
            selected_result = self.results[selected_index]
            QMessageBox.information(self, "Download", f"Downloading: {selected_result.title}")
            yt = YouTube(selected_result.watch_url)
            yt.register_on_progress_callback(self.on_progress)

            # Download the highest resolution video
            video_stream = yt.streams.get_highest_resolution()
            video_stream.download()

            # Download only audio
            audio_stream = yt.streams.filter(only_audio=True).first()
            audio_file_path = audio_stream.download()
            print(audio_file_path)

            summary = transcribe_audio_mp4(audio_file_path)
            
            # Summarize transcript using Ollama API
          
            # Display summary in a message box
            QMessageBox.information(self, "Summary", summary)

            # Clean up audio file after processing
            os.remove(audio_file_path)

    def on_progress(self, stream, _, bytes_remaining):
        # Update the progress bar based on download progress
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_of_completion = int(bytes_downloaded / total_size * 100)
        self.progress.setValue(percentage_of_completion)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YouTubeDownloader()
    ex.show()
    sys.exit(app.exec_())
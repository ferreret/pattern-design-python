import zipfile
import os
from datetime import datetime
import shutil


class FileCompressor:
    def compress(self, file_path):
        output_path = file_path + ".zip"
        with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(file_path, os.path.basename(file_path))
        return output_path


class FileBackup:
    def __init__(self, backup_dir="backups") -> None:
        self.backup_dir = backup_dir
        os.makedirs(backup_dir, exist_ok=True)

    def copy(self, file_path):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = os.path.basename(file_path)
        backup_path = os.path.join(self.backup_dir, f"{filename}.{timestamp}.bak")
        shutil.copy2(file_path, backup_path)
        return backup_path


class FileFacade:
    def __init__(self) -> None:
        self.__compressor = FileCompressor()
        self.__backup = FileBackup()

    def process(self, file_path):
        backup_path = self.__backup.copy(file_path)
        print(f"Archivo copiado a {backup_path}")

        compressed_path = self.__compressor.compress(file_path)
        print(f"Archivo comprimido a {compressed_path}")


script_dir = os.path.dirname(os.path.abspath(__file__))
facade = FileFacade()
facade.process(os.path.join(script_dir, "doc.txt"))

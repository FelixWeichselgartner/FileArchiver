import os
from FileDownloader import FileDownloader
from datetime import date
import shutil


class FileArchiver:

    def __init__(self):
        today = date.today()
        self.today_str = today.strftime("%Y%m%d")

        if not os.path.exists(self.today_str):
            os.mkdir(self.today_str)
            self.archive()

    def archive(self):
        with open('files2.txt', 'r') as file:
            for line in file.readlines():
                # only allow certain top level sub domains
                if '.de' in line or '.online' in line or '.org' in line or '.com' in line:
                    link = line.replace('\n', '')
                    fd = FileDownloader(link)
                    fd.download(self.today_str)
        
        shutil.make_archive(self.today_str, "zip", self.today_str)

    def today(self):
        return self.today_str + '.zip'


if __name__ == '__main__':
    fa = FileArchiver()
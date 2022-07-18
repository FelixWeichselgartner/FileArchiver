import requests
import re
from requests.exceptions import RequestException


class FileDownloader:

    def __init__(self, url):
        self.url = url
    
    def download(self, folder='', ntry=0):
        if ntry < 3:
            try:
                with requests.get(self.url) as r:
                    fname = ''
                    if "Content-Disposition" in r.headers.keys():
                        fname = re.findall("filename=(.+)", r.headers["Content-Disposition"])[0]
                    else:
                        fname = self.url.split("/")[-1]
                        fname = fname.split('.pdf')[0] + '.pdf'
                    if b'%PDF' == r.content[0:4]:
                        with open(folder + '/' + fname, 'wb') as f:
                            f.write(r.content) 
            except ConnectionAbortedError:
                self.download(ntry=ntry + 1)
            except RequestException as e:
                print(e)


from urllib.request import urlopen
from bs4 import BeautifulSoup

url_global="https://edition.cnn.com/"
filepath="page.html"

class Scrapper:
    __url=''
    __data=''
    __wlog=None
    __soup=None

    def __init__(self,url,wlog):
        self.__url=url
        self.wlog=wlog

    def retrieve_webpage(self):
        try:
            html=urlopen(self.__url)
        except Exception as e:
            print(e)
            self.__wlog.report(str(e))
        else:
            self.__data=html.read()
            if len(self.__data)>0:
                print("Retrieved successfully")

    def write_webpage_as_html(self,filepath=filepath,data=''):
        try:
            with open(filepath,'wb') as fobj:
                if data:
                    fobj.write(data)
                else:
                    fobj.write(self.__data)
        except Exception as e:
            print(e)
            self.__wlog.report(str(e))

    def read_webpage_from_html(self,filepath=filepath):
        try:
            with open(filepath) as fobj:
                self.__dta=fobj.read()
        except Exception as e:
            print(e)
            self.__wlog.report(str(e))

    def change_url(self,url):
        self.__url=url

    def print_data(self):
        print(self.__data)

    def convert_data_to_bs4(self):
        self.__soup=BeautifulSoup(self.__data,"html.parser")

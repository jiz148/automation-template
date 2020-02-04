"""
Downloader class to download file
"""
import requests


class Downloader:

    def __init__(self, url: str, file_path: str):
        self.url = url
        self.file_name = file_path

    def download(self, auth=None):
        """
        Downloads file, with provided authorization info
        @param auth: <Tuple> authorization information as (user_name, password)
        @return: 1 if succeeded, 0 if not succeeded
        """
        if auth:
            r = requests.get(self.url, auth=(auth[0], auth[1]))
        else:
            r = requests.get(self.url)

        if r.status_code == 200:
            with open(self.file_name, 'wb') as f:
                f.write(r.content)
            return 1
        else:
            print('Error while downloading! Status Code: {}'.format(r.status_code))
            return 0

import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Test")

class Searcher():
    def __init__(self,params):

        self.params = params
    def getPost(self):
        response = requests.get("https://api.top-rule34.com/getPost", params=self.params)

        try:
            if response.status_code == 200:  # Проверяем успешность запроса
                data = response.json()
                main_file_url = data.get('main', {}).get('file')
                tags = data.get("tags")

                return response.json(), main_file_url, tags
            else:
                return "Unknown error"
        except ValueError:
            return ValueError





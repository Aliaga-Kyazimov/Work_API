import requests
from settings_for_yandex import token

class YaUpLoader:

    base_host = 'https://cloud-api.yandex.net:443/'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            "Content-Type":'application/json',
            'Authorization':f'OAuth {self.token}'
        }


    def get_upload_link(self, path):
        uri = 'v1/disk/resources/upload'
        request_url = self.base_host + uri
        params = {'path': path}
        response = requests.get(request_url, headers=self.get_headers(), params=params)
        print(response.json())
        return response.json()['href']

    def upload_to_disk(self, local_path, yandex_path):
        upload_url = self.get_upload_link(yandex_path)
        response = requests.put(upload_url, data=open(local_path, 'rb'), headers=self.get_headers())

if __name__ == '__main__':
    ya = YaUpLoader(token)
    ya.upload_to_disk("hello_world.txt", '/hello_world.txt')


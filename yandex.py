import requests

Token = ''


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_upload_link(self, file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': file_path, 'overwrite': 'True'}
        answer = requests.get(upload_url, headers=headers, params=params)
        return answer.json()

    def upload(self, file_path, file_name):
        href = self.get_upload_link(file_path=file_path)
        link = href.get('href')
        ans = requests.put(link, data=open(file_name, 'rb'))
        ans.raise_for_status()


if __name__ == '__main__':
    path_to_file = 'requests/rewrite123.txt'
    token = Token
    uploader = YaUploader(token)
    uploader.upload(path_to_file, 'rewrite123.txt')

from aip import AipOcr
from functools import partial
class BaiduApi():
    def __init__(self,APP_ID,API_KEY,SECRET_KEY,block_size=1024 * 8):
        self.client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        self.block_size=block_size


    def chunked_file_reader(self,file):
        for chunk in iter(partial(file.read, self.block_size), b''):
            yield chunk

    def get_filedata(self,imagepath):
        data = b''
        with open(imagepath,'rb') as f:
            for chunk in self.chunked_file_reader(f):
                data += chunk
            return data

    def get_text(self,imagepath):
        file_data = self.get_filedata(imagepath)
        res = self.client.basicGeneral(file_data)
        return '\n'.join([words.get('words') for words in res.get('words_result')])

    def write_file(self,imagepath,filepath):
        with open(filepath,'w',encoding='utf-8') as f:
            text = api.get_text(imagepath)
            f.write(text)
if __name__ == '__main__':
    api = BaiduApi('16611607','wAIXfXOUS8ztLa4FrK3rZex1','3b8nvjSGUZq0LPC18VVAizKYRBbny6Mq')
    path = 'imag2.png'
    text = api.get_text(path)
    print(text)
    # api.write_file(path,'xx.txt')
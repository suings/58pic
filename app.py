import mimetypes
import re
from io import BytesIO

import requests
from bs4 import BeautifulSoup
from flask import Flask, send_file, request

pattern = re.compile('(https:\/\/[a-zA-Z0-9\/\._]+)!\/')


def download(url):
    s = requests.session()
    page = s.get(url).text
    soup = BeautifulSoup(page)
    url_img = "https:" + soup.find(class_='pic-box').find('img')['data-src']
    url_img = pattern.search(url_img)[1]
    mime = mimetypes.guess_type(url_img)[0]
    img = s.get(url_img, headers={'referer': url})
    return (BytesIO(img.content), mime)


app = Flask(__name__)


@app.route('/58pic')
def qiantudownload():
    url = request.args.get('url', '')
    if url:
        file, mime = download(url)
        return send_file(file, mimetype=mime)


if __name__ == '__main__':
    app.run()

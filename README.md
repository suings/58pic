# 项目介绍

一段可以去除千图网图片水印的js代码。

# 使用

## 控制台临时使用

按F12打开控制台，输入以下代码即可

```js
const pattern = /(^(https:)?\/\/[a-zA-Z0-9\/\._]+)!\//;

const change_true_img = () => {
    let bigpic = document.getElementsByClassName('pic-box')[0].childNodes[0];// img所在元素	
    let data_src = bigpic.getAttribute('data-src');

    data_src = pattern.exec(data_src)[1];
    bigpic.setAttribute('data-src', data_src);
    bigpic.setAttribute('src', data_src);
}

const change_preview_img = () => {
    const pics = document.getElementsByClassName('show-area-pic');

    for (let index = 0; index < pics.length; index++) {
        let pic = pics[index];
        pic.src = pattern.exec(pic.src)[1];
    }
}
change_preview_img();
change_true_img();
```

源文件: [console.js](console.js)

## 油猴脚本

```javascript
// ==UserScript==
// @name         千图网去水印
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  try to take over the world!
// @author       SU
// @match        https://www.58pic.com/newpic/*.html
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // Your code here...
    const pattern = /(^(https:)?\/\/[a-zA-Z0-9\/\._]+)!\//;

const change_true_img = () => {
    let bigpic = document.getElementsByClassName('pic-box')[0].childNodes[0];// img所在元素
    let data_src = bigpic.getAttribute('data-src');

    data_src = pattern.exec(data_src)[1];
    bigpic.setAttribute('data-src', data_src);
    //bigpic.setAttribute('src', data_src); //油猴中不需要此行
}

const change_preview_img = () => {
    const pics = document.getElementsByClassName('show-area-pic');

    for (let index = 0; index < pics.length; index++) {
        let pic = pics[index];
        pic.src = pattern.exec(pic.src)[1];
    }
}
change_preview_img();
change_true_img();
})();
```

源文件: [tampermonkey.user.js](tampermonkey.user.js)

## python实现一个接口

通过网页请求[http://127.0.0.1:5000/58pic?url=]()即可获取到无水印的图片

```python
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
```

源文件: [app.py](app.py)

# 更新时间

2019.5.13
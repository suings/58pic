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
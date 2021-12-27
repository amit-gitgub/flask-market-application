from pyqrcode import create

s = "https://www.youtube.com/channel/UCeO9hPCfRzqb2yTuAn713Mg"
url = create(s)
url.svg("test.png", scale=8)

from lxml import etree
import requests
import subprocess
import time

def download(url_format):
    try:
        fetched_data = requests.request('GET', url_format)
    except:
        return False
    htmlelem = etree.fromstring(fetched_data.content, etree.HTMLParser())
    title = htmlelem.find(".//h1").text
    link = htmlelem.find(".//link[@rel='preload'][@as='fetch']").attrib['href']
    link = (str(link).replace('_TPL_','480p'))

    subprocess.run(["ffmpeg", "-protocol_whitelist", "file,http,https,tcp,tls,crypto", "-i", link, "-c", "copy", title+".mp4"])

if __name__ == "__main__":
    links = [
    ]
    for i in links:
        xht(i)

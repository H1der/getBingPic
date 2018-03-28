import urllib.request
import time


def get_html(url):
    req = urllib.request.Request(url)
    web = urllib.request.urlopen(req)
    content = str(web.read())
    return content


def get_url(con):
    json_list = con.split(',')
    json_url = ''
    json_url = json_url.join(json_list[3])
    url = 'http://cn.bing.com' + json_url[7:-1]
    return url


def main():
    url = 'http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
    content = get_html(url)
    file_name = str(time.strftime('%Y-%m-%d', time.localtime(time.time()))) + '.jpg'
    if urllib.request.urlretrieve(get_url(content), file_name):
        print('获取成功')
    else:
        print('获取失败')


if __name__ == '__main__':
    main()




'''
目标：
    使用分布式爬虫，去爬取所有页
    http://www.btbtdy.net/btfl/dy30.html
'''
from redis import Redis
import requests

# 存储urls

REDIS_KEY = "btdy:urls"

# rds = Redis('10.8.151.21',6379)
rds = Redis('192.168.56.1',6379)

def fetch(url):

    """
    下载页面，如果下载成功，返回response对象，否则返回None
    :param url:  你爬取的url
    :return: 返回response对象或者None
    """

    r = requests.get(url)
    if r.status_code == 200 :
        return r
    return None

def parse(response):
    rds.lpush('btdy:items','')
    pass



def start_request():
    '''
    获取地市局所有页的地址，并把地址push到REDIS_KEY中
    '''
    start_url = 'http://www.btbtdy.net/btfl/dy30.html'
    urls = ['http://www.btbtdy.net/btfl/dy30-{}.html'.format(str(page+1) ) for page in range(62)]
    rds.lpush(REDIS_KEY,*urls)

if __name__ == '__main__':
    #  从redis中的REDIS_URLS中获取url
    start_request()
    # while True:
    #     _,url = rds.blpop(REDIS_KEY)
    #     print(url)
    #     fetch(url)

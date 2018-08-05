'''
把redis缓存中的数据，转存到mongodb或mysql中
'''

import pymysql
import pymongo
import  json
from redis import Redis
from BtdyRedisCrawl import settings

# 1 从redis中取数据
rds = Redis(settings.REDIS_HOST,settings.REDIS_PORT)
client = pymongo.MongoClient(host='10.8.151.73',port=27017)
db = client['btdy']
collection = db['movies']

while True:
    _,item = rds.blpop(settings.REDIS_ITEMS_KEY)
    dict_item = json.loads(item.decode('utf-8'))

    print(dict_item)

    # 2 把取出的数据存储到数据库中
    collection.insert(dict_item)
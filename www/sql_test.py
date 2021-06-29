import asyncio

import orm
import asyncio
from models import User, Blog, Comment

async def test(loop):

    # 创建链接池
    await orm.create_pool(loop=loop, user='root', password='Pass@19970918', db='awesome')

    # 创建User对象 (对标数据库中的User table)
    u = User(name='Test', email='test@example.com', passwd='xxxlxl123', image='about:blank')
    
    # 把对象存入数据库
    await u.save()

    # 不加这几句的话会导致RuntimeError: Event loop is closed. （关闭连接池，等待关闭完成）
    orm.__pool.close()
    await orm.__pool.wait_closed()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()
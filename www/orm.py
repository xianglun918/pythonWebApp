#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   orm.py
@Time    :   2021/06/11 16:58:09
@Author  :   xianglun xu 
@Contact :   xianglun918@qq.com
'''

import asyncio, logging
import aiomysql

def log(sql, args=()):
    logging.info('SQL: %s' % sql)


# 连接池 - 每个HTTP请求都可以从连接池中直接获取数据库连接
# 不必频繁的打开和关闭数据库连接。
async def create_pool(loop, **kw):
    logging.info('Create database connection pool...')
    global __pool
    __pool = await aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset', 'utf-8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 10), 
        loop=loop,
    )


# SELECT 语句 - 需要传入SQL语句和SQL参数
async def select(sql, args, size=None):
    log(sql, args)
    global __pool
    with (await  __pool) as conn:
        cur = await conn.cursor(aiomysql.DictCursor)
        # 注意?是SQL的占位符而%s是MySQL的占位符
        # 在select内部自动替换可以防止SQL注入攻击 (坚持使用带参数的SQL)
        await cur.execute(sql.replace('?', '%s'), args or ())
        # 指定数量的记录，如无获取全部记录
        if size:
            rs = await cur.fetchmany(size)
        else:
            rs = await cur.fetchall()
        await cur.close()
        logging.info('Rows returned: %s' % len(rs))
        return rs

# 因为Inser, Update, Delete均需要相同的参数，以及返回一个整数表示
# 影响的行数，所以我们可以定义一个通用的execute函数
async def execute(sql, args):
    log(sql)
    with (await __pool) as conn:
        try:
            cur = await conn.cursor()
            await cur.execute(sql.replace('?', '%s'), args)
            affected = cur.rowcount
            await cur.close()
        except BaseException as e:
            raise 
        # 这里返回的是结果数，而不是结果集
        return affected

# # 编写简单的ORM，首先考虑如何定义一个User对象
# # 然后把数据库表users和它关联起来
# from orm import Model, StringField, IntegerField

# class User(Model):
#     __table__ = 'users'

#     id = IntegerField(primary_key=True)
#     name = StringField()
    


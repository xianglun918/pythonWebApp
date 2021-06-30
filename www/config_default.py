#  config_default.py

# 通常一个Web App在运行时都需要读取配置文件，比如数据库的用户名和口令之类的。
# 由于python语法简单，我们可以无需解析一个.properties或.yaml等配置文件，
# 直接使用python源代码。
# 默认的配置文件应该完全符合本地开发环境，这样，无需任何设置就可以立刻启动服务器。

configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': 'Pass@19970918',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }
}


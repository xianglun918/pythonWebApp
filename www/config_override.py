# config_override.py

# config_defaults.py的内容简单明了，但是，
# 如果要部署到服务器时，我们通常需要修改数据库的'host'等信息
# 可以由config_override.py来间接更改、覆盖某些默认设置。

configs = {
    'db': {
        'host': '127.0.0.1'
    }
}

# 这样，
# config_default.py作为开发环境的标准配置，
# 把config_override.py作为生产环境的标准配置
# 我们就可以既方便的在本地开发，又随时可以把应用
# 部署到服务器上。
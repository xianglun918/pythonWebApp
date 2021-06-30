# MVC(Model-View-Controller)是软件工程中的一种软件架构模式
# 把系统分为：Model, View, Controller三个部分，现在我们ORM框架
# Web框架和配置都已经就绪，编写一个简单的MVC就可以把它们全部启动起来

from models import User
from coroweb import get
import asyncio

@get('/')
async def index(request):
    users = await User.findAll()
    return {
        '__template__': 'test.html',
        'users': users
    }

# ‘__template__'指定的模版文件是test.html，其他参数是传递给模版的数据，
# 所以我们在模版的根目录templates下创建test.html



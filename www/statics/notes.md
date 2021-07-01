## 构建前端

至此，后端工作基本构建完成。接下要开始设计和编程前端页面了。
为了更容易构建出复杂的HTML前端页面，我们需要一套基础的CSS框架和jQuery作为操作DOM的JavaScript库。

如今好用流行的CSS框架有很多例如：Bootstrap, Pure CSS, Bulma, Semantic UI 等。
此教程会使用UIkit 作为网站的CSS 框架，具体的教程请参考官方Documentation。
请下载UIkit的最新版本(3.0.0或以上，廖大用的UIkit 2.0 将不适用)，将js和css文件放入www/static相应的文件目录中：

```python
static/
+- css/
|  +- awesome.css ## 自定义的css
|  +- uikit.min.css
+- js/
   +- awesome.js ## 自定义的script
   +- jquery.min.js
   +- uikit.min.js
   +- uikit-icons.min.js
   +- sha1.min.js ## 计算HASH值
   +- vue.min.js ## Vue是一种MVVM前端框架, 我们会用它将数据及数据操作与HTML页面显示联系起来
   +- sticky.min.js ## 实现黏性布局
```

由于前端包含很多页面，而每个页面都会有相同的页眉和页脚，最有效率的方法就是构建可以继承的父模板, 
jinja2提供了很便捷方法用可替换的block来建立模板。例如最简单的父模板base.html

```html
<!-- base.html -->
<html>
    <head>
        <title>{% block title%} 子模板可替换title内容 {% endblock %}</title>
    </head>
    <body>
        {% block content %} 子模板可替换content内容 {% endblock %}
    </body>
</html>
```

对于子模版a.html, b.html, c.html,只需要把父模版的title和content替换掉：

```html
{% extends 'base.html' %}

{% block title %} A or B or C {% endblock %}

{% block content %}
    <h1>Chapter A or B or C</h1>
    <p>blablabla...</p>
{% endblock %}
```

知道了如何用jinja2, 我们就可以用UIkit框架来完成网站父模板__base__.html的编写了
（请将所有的html文件存放在www/templates目录下）。
代码已加入屏幕自适应，可以在移动端上凹大卜查看效果。

# Scrapy练习项目

### 1.使用scrapy开始一个项目
- spiders/quotes_spider.py
    + 在spiders下创建类继承scrapy.Spider
    + 写属性start_urls 链接将从这里生成
    + 配置middleware 
    + 配置item
    + 回调函数parse 处理得到的response
        + 因为使用的yield，而不是return。parse函数将会被当做一个生成器使用。scrapy会逐一获取parse方法中生成的结果，并判断该结果是一个什么样的类型；
        + yield scrapy.Request(url = 'zarten.com')
        + yield item # 生成item
        + [scrapy中yield详细解释](https://www.jianshu.com/p/7c1a084853d8)
    + 生成的item会被pipline处理，pipline配置值越低越靠前
    + 生成的Request会被爬虫中间件处理、添加UA、添加代理
- 运行项目
    + scrapy crawl IPSpider
### 附录 相关知识
- css和xpath区别
    + https://www.cnblogs.com/themost/p/7069513.html
- scray中的request和response
    + https://www.jianshu.com/p/1b4c133296c1
- scrapy 如何调试
    + 新建一个main函数添加如下代码
```buildoutcfg
    #!/usr/bin/env python
    #-*- coding:utf-8 -*-
    
    from scrapy.cmdline import execute
    import os
    import sys
    
    #添加当前项目的绝对地址
    sys.path.append(os.path.dirname(os.path.abspath(__file__))) 
    #执行 scrapy 内置的函数方法execute，  使用 crawl 爬取并调试，最后一个参数jobbole 是我的爬虫文件名
    execute(['scrapy', 'crawl', 'jobbole'])
```

### 附录2 scrapy调度流程
![Scrapy](/readmeImage/20180720100328504[1].jpg)

### 附录3 python技巧
```buildoutcfg
#!/usr/bin/env python
#-*- coding:utf-8 -*-
print('\033[0m这是显示方式0')
print('\033[1m这是显示方式1')
print('\033[4m这是显示方式4')
print('\033[5m这是显示方式5')
print('\033[7m这是显示方式7')
print('\033[8m这是显示方式8')
print('\033[30m这是前景色0')
print('\033[31m这是前景色1')
print('\033[32m这是前景色2')
print('\033[33m这是前景色3')
print('\033[34m这是前景色4')
print('\033[35m这是前景色5')
print('\033[36m这是前景色6')
print('\033[37m这是前景色7')
print('\033[40m这是背景色0')
print('\033[41m这是背景色1')
print('\033[42m这是背景色2')
print('\033[43m这是背景色3')
print('\033[44m这是背景色4')
print('\033[45m这是背景色5')
print('\033[46m这是背景色6')
print('\033[47m这是背景色7')
```
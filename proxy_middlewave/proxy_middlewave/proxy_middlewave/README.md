
# 
## 本项目内容
### 1.添加proxy中间件
### 2.scrapy 中的request对象
```buildoutcfg
1,Request objects

class scrapy.http.Request(url[, callback, method='GET', headers, body, cookies, meta, encoding='utf-8', priority=0, dont_filter=False, errback])

一个request对象代表一个HTTP请求，通常有Spider产生，经Downloader执行从而产生一个Response。

Paremeters:     url(string): 用于请求的URL

callback(callable):指定一个回调函数，该回调函数以这个request是的response作为第一个参数。如果未指定callback，

则默认使用spider的parse()方法。

method(string):HTTP请求的方法，默认为GET（看到GET你应该明白了，过不不明白建议先学习urllib或者requets模块）

meta(dict):指定Request.meta属性的初始值。如果给了该参数，dict将会浅拷贝。(浅拷贝不懂的赶紧回炉)

body(str):the request body.(这个没有理解，若有哪位大神明白，请指教，谢谢）

headers(dict):request的头信息。

cookies(dict or list):cookie有两种格式。

1、使用dict:

request_with_cookies = Request(url="http://www.example.com", cookies={'currency': 'USD', 'country': 'UY'})
2、使用字典的list

request_with_cookies = Request(url="http://www.example.com",
                               cookies=[{'name': 'currency',
                                        'value': 'USD',
                                        'domain': 'example.com',
                                        'path': '/currency'}])
后面这种形式可以定制cookie的domain和path属性，只有cookies为接下来的请求保存的时候才有用。

 

当网站在response中返回cookie时，这些cookie将被保存以便未来的访问请求。这是常规浏览器的行为。如果你想避免修改当前

正在使用的cookie,你可以通过设置Request.meta中的dont_merge_cookies为True来实现。

request_with_cookies = Request(url="http://www.example.com",
                               cookies={'currency': 'USD', 'country': 'UY'},
                               meta={'dont_merge_cookies': True})
 

encoding(string):请求的编码， 默认为utf-8

priority(int):请求的优先级

dont_filter(boolean):指定该请求是否被 Scheduler过滤。该参数可以是request重复使用（Scheduler默认过滤重复请求）。谨慎使用！！

errback(callable):处理异常的回调函数。

属性和方法：

url: 包含request的URL的字符串

method: 代表HTTP的请求方法的字符串，例如'GET', 'POST'...

headers: request的头信息

body: 请求体

meta: 一个dict，包含request的任意元数据。该dict在新Requests中为空，当Scrapy的其他扩展启用的时候填充数据。dict在传输是浅拷贝。

copy(): 拷贝当前Request 

replace([url, method, headers, body, cookies, meta, encoding, dont_filter, callback, errback]): 返回一个参数相同的Request，

可以为参数指定新数据。

 给回调函数传递数据
当request的response被下载是，就会调用回调函数，并以response对象为第一个参数


复制代码
def parse_page1(self, response):
    return scrapy.Request("http://www.example.com/some_page.html",
                          callback=self.parse_page2)

def parse_page2(self, response):
    # this would log http://www.example.com/some_page.html
    self.logger.info("Visited %s", response.url)
复制代码
 

在某些情况下，你希望在回调函数们之间传递参数，可以使用Request.meta。（其实有点类似全局变量的赶脚）

 View Code
 

使用errback来捕获请求执行中的异常
当request执行时有异常抛出将会调用errback回调函数。

它接收一个Twisted Failure实例作为第一个参数，并被用来回溯连接超时或DNS错误等。

 example
 

Request.meta的特殊关键字
Request.meta可以包含任意的数据，但Scrapy和内置扩展提供了一些特殊的关键字

dont_redirect             （其实dont就是don't,嗯哼~）
dont_retry
handle_httpstatus_list
handle_httpstatus_all
dont_merge_cookies (see cookies parameter of Request constructor)
cookiejar
dont_cache
redirect_urls
bindaddress
dont_obey_robotstxt
download_timeout(下载超时)
download_maxsize
download_latency(下载延时)
proxy
```
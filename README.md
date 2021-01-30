# L_SPIDER
****
A spider with some methods that been used to crawling data like news and title or pic ,and another things which not encode in  Complex algorithm（well,the truth is i do not learn about it ,if someday i got it ,a new spider will been creat ,i promise.）<br>
At very first i code this just for help my friend to finish thier subject , and by the way training my programing capacity<br>.
But more i try to improve and perfect ,more i astounded about pentent ablity of SPIDER.<br>
_Excellent data killer，you can analyse anything by useing magic algorithm and your favourite programing language with the huge data you crawled by spider if web server allow.😈_<br>
Why i don't use scrapy or another frame? very simple,caused easy task need no Rocket Launcher，isn't it? <br>
In other words, I want to make a wheel to play by myself.<br>
Wish my code would help you to save some worry like i assisted my friends,good luck with you,guy.😇<br>
                                                                                                                                            __LOVEMOSTISBUG__<br>
这是一个用来抓取数据，比如新闻、标题或图片，还有一些没有用复杂的算法进行编码的数据的***小爬虫***（好吧，其实是小弟**学业不精**，哪天我懂了，会把该有的都加上去的，保证）。<br>
一开始我编写这个代码只是为了帮我的朋友完成他们的课题，顺便训练我自己的编程能力。<br>
但越是加油改进和完善，就越惊讶于爬虫的潜能。<br>
_牛X的数据杀手，你可以分析任何事物通过使用魔术算法和你最喜欢的编程语言与你爬下来的巨大数据，**如果网络服务器允许**。😈_<br>
为毛我不用Scrapy这样的框架去爬？杀鸡焉用牛刀，你说是吧~<br>
还有的话其实是我也想造个轮子自己玩（小声bb）<br>
希望我的代码能帮你省去一些烦恼，就像我帮助我的朋友一样，祝你好运，伙计。😇<br>
                                                                                                                                           __LOVEMOSTISBUG__  <br>
# 在教程开始前有件事必须得告诉你
****
**高强度和没有得到允许的脚本访问是所有服务器君和网站管理员都不想接待的。《从入门到入狱》。**<br>
**高强度和没有得到允许的脚本访问是所有服务器君和网站管理员都不想接待的。《从入门到入狱》。**<br>
**高强度和没有得到允许的脚本访问是所有服务器君和网站管理员都不想接待的。《从入门到入狱》。**<br>
**仅供学习参考。**<br>
****

# How to crawl 游戏开始
****
SPIDER这个类里的函数我来解释一下吧。<br>
初始定义时需要两个参数，一个是目标url还有便是目标的正则。<br>
url_open就是伪造报头和代理IP访问URL并返回值(默认二进制)<br>
get_html访问本身地址并返回且保存URL<br>
show_html输出本身地址HTML<br>
get_aim_list访问本身地址并返回且保存目标URL列表<br>
show_aim_list逐个输出目标的URL<br>
一般是先用crawl初始化基本的HTML和目标URL列表当然看你具体需求，代码已经尽量简略好不损失自由度了个人觉得。<br>
L_print是因为某些字符无法打印出来又不想报错写的类似print函数<br>
download就是download 参数有目标url和保存到文件夹，默认是根目录<br>
keep_data_one_page只保存一页的数据 参数为url和爬取一次得到的是元组时的分隔符号<br>
keep_data_by_pages参数为爬取页数 前段url和后段url（中间夹着页数） 还有分隔符号 以及页数跨度<br>
deep_crawl 首先是深入爬的正则 还有就是前段url和后段url<br>
deep_crawl_and_save 深入爬的正则 保存文件夹 还有就是前段url和后段url<br>

## TASK 0 如果你只是轻量级的爬取 <br>比如接下来的爬取新闻网站带有Chinese的所有新闻标题<br> 你甚至不需要用到我写的类<br>直接这样就行<br>当然 用我的也能很不错的完成任务 ~能帮你剩下些时间去干其他事情
```python
import urllib.request
import urllib.parse
import random
import re
import time

def url_open(url):
    my_headers = list(set(open('user_agent.txt','r').read().split('\n')))
    iplist = list(set(open('ip.txt','r').read().split('\n')))
    my_ip = random.choice(iplist)
    my_head = random.choice(my_headers)
    print (my_ip+'\n'+my_head+'\n')
    iplist =list(set(open('ip.txt','r').read().split('\n')))
    proxy_support = urllib.request.ProxyHandler({'http':my_ip})
    opener = urllib.request.build_opener(proxy_support)
    opener.addheaders = [('User-Agent',my_head)]
    urllib.request.install_opener(opener)
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    html1 = response.read()
    return html1

def gkd(url,k):
    c = re.findall(k,url_open(url).decode('utf-8'))
    c=list(set(c))
    return c

k1 = re.compile(r'class="story-txt">\r\n\t\t\t\t\t\t((?:.).*?)\t\t\t\t\t</div>')
for i in range(1,200):
    url2 = 'https://globalnews.ca/gnca-ajax/search-results/%7B%22term%22:%22china%22,%22type%22:%22news%22,%22page%22:'+str(i)+'%7D/'
    t = gkd(url2,k1)
    for i in t:
        b = str(i).replace('&#039;','\'')
        b = b.replace('&quot;',' ')
        print(b)
        with open ('T.txt','a',encoding="utf-8")as f:
            f.write(b+'\n')
    
print('ok done')

```
****

****
## TASK 1 百度贴吧：某吧首推前几十页的帖子标题及回复 命名为标题.txt 写入内容为一回复加一换行 保存到原目录data文件夹内 代码量：23行
```python
from L_SPIDER import SPIDER
import re
import urllib.parse
import multiprocessing as mp

k_aim = re.compile('''errer" href="((?:(?:.).*?))" title="(?:(?:.).*?)"''')
k_aim_deep= r'''j_d_post_content " style="display:;">((?:(?:.).*?))<'''
k_aim_deep_file_name =re.compile(r'''<title>((?:(?:.).*?))</title>''')
tieba = urllib.parse.quote('抗压背锅')
page = 50
b = SPIDER(f'https://tieba.baidu.com/f?kw={tieba}&ie=utf-8&pn={str(page)}',k_aim)
b.get_html()
ls = b.get_aim_list()
b.show_aim_list()
def run(urls):
    b.deep_crawl_and_save(k_aim_deep,k_aim_deep_file_name,f_url='https://tieba.baidu.com')

if __name__ == '__main__':
    p = mp.Pool(10)
    rel = p.map(run,ls)
    p.close()
    p.join()
```
****
多线程下，爬取非常迅速，5s内3000数据应该问题不大，对课题或者建立什么模型基本就能够开始了。<br>
正则表达式如果不会写可以用这招。把前面的特征和后面的特征换成你对应的内容前后特征便是。<br>
```python
k_aim = re.compile('''前面的特征((?:(?:.).*?))后面的特征''')
```
emmm我觉得都来爬虫了文本操作什么的应该都会了吧所以不多说了。<br>
其中效果如下：
****
![hope_you_luck](https://github.com/LOVEMOSTISBUG/another_files/blob/main/tieba0.PNG)  
****

****

# Some things you maybe want know
****
**you are been ban.respect~**<br>
****
![hope_you_luck](https://github.com/LOVEMOSTISBUG/another_files/blob/main/hope_you_luck.png)  
****
**web server was boom.respect~**<br>
****
![bad news](https://github.com/LOVEMOSTISBUG/another_files/blob/main/bad_news.png)  
****

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
skip 跳过教程 我们搞快点
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

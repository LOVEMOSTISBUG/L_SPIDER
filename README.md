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
# How to crawl 游戏开始
****
skip 跳过教程 
****
## TASK 1 爬取百度贴吧某个吧的前几十页的帖子标题及回复命名为标题.txt 保存内容为一回复加一个换行  代码量：23行
```python
from L_SPIDER import SPIDER
import re
import urllib.parse
import multiprocessing as mp

k_aim = re.compile('''errer" href="((?:(?:.).*?))" title="(?:(?:.).*?)"''')
k_aim_deep= r'''j_d_post_content " style="display:;">((?:(?:.).*?))<'''
k_aim_deep_file_name =re.compile(r'''<title>((?:(?:.).*?))</title>''')
tieba = urllib.parse.quote('抗压背锅')

def run(page):
    b = SPIDER(f'https://tieba.baidu.com/f?kw={tieba}&ie=utf-8&pn={page}',k_aim)
    b.get_html()
    ls = b.get_aim_list()
    b.show_aim_list()
    b.deep_crawl_and_save(k_aim_deep,k_aim_deep_file_name,f_url='https://tieba.baidu.com')

pages = [i for i in range(50,201,50)]
if __name__ == '__main__':
    p = mp.Pool(10)
    rel = p.map(run,pages)
    p.close()
    p.join()
```
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

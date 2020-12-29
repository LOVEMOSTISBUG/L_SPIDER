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
一个有一些方法可以用来抓取数据，比如新闻、标题或图片，还有一些没有用复杂的算法进行编码的数据的***小爬虫***（好吧，其实是小弟**学业不精**，哪天我懂了，我会把该有的都加上去的，我保证）。<br>
一开始我编写这个代码只是为了帮我的朋友完成他们的课题，顺便训练我自己的编程能力。<br>
但我越是加油改进和完善，我就越惊讶于爬虫的潜能。<br>
_牛X的数据杀手，你可以分析任何事物通过使用魔术算法和你最喜欢的编程语言与你爬下来的巨大数据，**如果网络服务器允许**。😈_<br>
为毛我不用Scrapy这样的框架去爬？杀鸡焉用牛刀，你说是吧~<br>
还有的话其实是我也想造个轮子自己玩（小声bb）<br>
希望我的代码能帮你省去一些烦恼，就像我帮助我的朋友一样，祝你好运，伙计。😇<br>
                                                                                                                                            __LOVEMOSTISBUG__  <br>
****
# Some things you maybe want know
****
**you are been ban.respect~**<br>
****
![bad news](https://github.com/LOVEMOSTISBUG/L_SPIDER/blob/main/Test_pic/hope_you_luck.png)  
****
**web server was boom.respect~**<br>
****
![bad news](https://github.com/LOVEMOSTISBUG/L_SPIDER/blob/main/Test_pic/bad_news.png)  
****
# How to crawl
****
crawl by pages 一页一页爬
****
```python
from L_SPIDER import SPIDER
import re
import urllib.parse

k_aim = re.compile('''((?:(?:.).*?)) 
        </div>''')        
#爬一页的帖的标题  Title of 1 pages's post 
tieba = urllib.parse.quote('钓鱼')
b = SPIDER(f'https://tieba.baidu.com/f?kw={tieba}&ie=utf-8',k_aim)
print(b.get_html())
#ls = b.get_aim_list()
b.show_aim_list()

#爬50页的帖的标题并保存为data.txt  Title of 50 pages's post and save as data.txt
b.keep_data_by_pages(50,f'https://tieba.baidu.com/f?kw={tieba}&ie=utf-8&pn=',page_wd=50)
```
****

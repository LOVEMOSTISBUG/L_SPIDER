from L_SPIDER import SPIDER
import re
import urllib.parse

k_aim = re.compile('''((?:(?:.).*?)) 
        </div>''')
        
#爬一页的帖的标题
tieba = urllib.parse.quote('钓鱼')
b = SPIDER(f'https://tieba.baidu.com/f?kw={tieba}&ie=utf-8',k_aim)
print(b.get_html())
#ls = b.get_aim_list()
b.show_aim_list()

#爬50页的帖的标题并保存为data.txt
b.keep_data_by_pages(50,f'https://tieba.baidu.com/f?kw={tieba}&ie=utf-8&pn=',page_wd=50)


import urllib.request
import urllib.parse
import random
import re
import time
import gzip
from io import StringIO

class SPIDER():
    def __init__(self,aim_url,k):
        """初始化"""
        self.aim_url = aim_url
        self.k = k
        self.html = ''
        self.aim_list = []
        self.deep_list = []
    def url_open(self,url):
        '''伪造报头和代理IP访问URL并返回值(默认二进制)'''
        ip_list = list(set(open('ip.txt','r').read().split('\n')))
        my_ip = random.choice(ip_list)
        user_agents = list(set(open('user_agent.txt','r').read().split('\n')))
        user_agent = random.choice(user_agents)
        proxy_support = urllib.request.ProxyHandler({'http':my_ip})
        opener = urllib.request.build_opener(proxy_support)
        opener.addheaders = [('User-Agent',user_agent)]
        opener.addheaders = [('Accept','*/*')]
        opener.addheaders = [('Referer',url)]
        urllib.request.install_opener(opener)
        print (my_ip+'\n'+user_agent)
        try:
            req = urllib.request.Request(url)
            response = urllib.request.urlopen(req)
            result = response.read()
            return result
        except urllib.error.HTTPError as e:
            if str(e.code)[0]=='4':
                print(e,'\n你被ban了,老弟。')
            if str(e.code)[0]=='5':
                print(e,'\n服务器炸了！哇靠！')
            return ''
        
    def get_html_gzip(self):
        """访问本身地址并用gzip解压后返回且保存URL"""
        try:
            result = self.url_open(self.aim_url)
            buf = StringIO(result)
            f = gzip.GzipFile(fileobj=buf)
            html =  f.read()
            self.html = html
            print('用gzip解压得到HTML')
            return self.html
        except Exception as e:
            print('gzip解压缩获取HTML也失败了。原因如下：',e)
                
    def get_html(self):
        """访问本身地址并返回且保存URL"""
        if self.html=='':
            try:
                result = self.url_open(self.aim_url)
                if result != '':
                    self.html = result.decode('utf-8')
                    print('得到HTML')
                if result == '':
                    print('啥都没摸到。。')
                    self.html = ''
                return self.html
            except Exception as e:
                print('获取HTML失败了。失败原因如下：',str(e))
                return self.get_html_gzip()
                
        else:
            return self.html
    def show_html(self):
        """输出本身地址HTML"""
        if self.html!='':
            print(self.html)
        else:
            print('请先运行get_html函数。')
    def get_aim_list(self):
        """访问本身地址并返回且保存目标URL列表"""
        try:
            self.aim_list = list(set(re.findall(self.k,self.html)))
            if self.aim_list == []:
                print('得到了空空如也的AIM_LIST')
            else:
                print('得到了想要的AIM_LIST')
            return self.aim_list
        except Exception as e:
            print('查找目标出错：',e)

    def show_aim_list(self):
        """逐个输出目标的URL"""
        if type(self.aim_list) == list:
            for url in self.aim_list:
                try:
                    print(url)
                except UnicodeEncodeError:
                    print('MD又是编码错误')
        else :
            print('居然不是列表？')
    def crawl(self):
        '''初始化基本的HTML和目标URL列表'''
        self.html = self.get_html()
        self.aim_list = self.get_aim_list()
        
    def download_aim_list(self,aim_dir='',aim_list=[]):
        """按查找到的aim_list逐个下载"""
        if aim_list == []:
            aim_list = self.aim_list
        total_len = len(aim_list)
        for i in range(1,total_len+1):
            url = aim_list.pop()
            print('目前下载文件URL：'+url)
            try:
                file_name = url.split('/')[-1]
                print('保存文件名为'+file_name)
                response = self.url_open(url)
                with open (aim_dir + file_name,'wb') as file:
                    file.write(response)
                print(f'已完成{i/total_len:.2%}')
            except Exception as e:
                aim_list.append(url)
                print('下载出现问题。问题原因如下：',e)
    
    def keep_data_by_pages(self,page=1,f_url='',b_url='',separator=','):
        '''分页爬取并保存数据'''
        for n in range(1,page+1):
            self.aim_url = f_url + str(n) +b_url
            self.html = self.url_open(self.aim_url).decode('utf-8')
            print(f'得到第{n}页的HTML')
            self.get_aim_list()
            with open('data.txt','a+')as f:
                for i in self.aim_list:
                    if type(i) == str:
                        f.write(i+'\n')
                        print('写入数据：',i)
                    elif type(i) == tuple:
                        f.write(separator.join(list(i))+'\n')
                        print('写入数据：'+separator.join(list(i)))
    def deep_crawl(self,k_deep):
        for url in self.aim_list:
            deep_html = self.url_open(url).decode('utf-8')
            ls =list(set(re.findall(k_deep,deep_html)))
            print(ls)
            self.deep_list.extend(ls)
        print(self.deep_list)
if __name__ == "__main__":
    print('ssln . i am just a spider object.')

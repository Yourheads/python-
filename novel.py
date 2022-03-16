from bs4 import BeautifulSoup
import requests



url1 = input("请输入要爬取的书籍详情页网址:")
path = r'C:\Users\12980\Desktop\小说\ '

def get_text(url):
    try:
        headers ={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
            'cookie': 'e1=%7B%22pid%22%3A%22qd_P_rank_19%22%2C%22eid%22%3A%22qd_C40%22%2C%22l1%22%3A5%7D; e2=%7B%22pid%22%3A%22qd_P_rank_19%22%2C%22eid%22%3A%22%22%2C%22l1%22%3A4%7D; _csrfToken=27b3ASUrbe2oiU5tl3OL1XUqq3X8qN23LFbMpB3k; newstatisticUUID=1623637298_560270187; _yep_uuid=cce8cf26-f08a-ee7d-8cad-433a856b86d1; e1=%7B%22pid%22%3A%22qd_P_rank_01%22%2C%22eid%22%3A%22qd_C19%22%2C%22l1%22%3A4%7D; e2=%7B%22pid%22%3A%22qd_P_rank_19%22%2C%22eid%22%3A%22%22%7D; qdrs=0%7C3%7C0%7C0%7C1; showSectionCommentGuide=1; qdgd=1; lrbc=1021617576%7C626160000%7C0; rcr=1021617576; bc=1021617576',
            'referer': 'https://www.qidian.com/rank'
        }
        resporse = requests.get(url,headers=headers)
        content = resporse.content.decode()
        soup = BeautifulSoup(content,'lxml')
        date_list = soup.find('ul',{'class':'cf'})
        for book in date_list.find_all('a'):
            print(book.text)
            book_url = 'https:'+book['href']
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
                'cookie': 'e1=%7B%22pid%22%3A%22qd_P_rank_19%22%2C%22eid%22%3A%22qd_C40%22%2C%22l1%22%3A5%7D; e2=%7B%22pid%22%3A%22qd_P_rank_19%22%2C%22eid%22%3A%22%22%2C%22l1%22%3A4%7D; _csrfToken=27b3ASUrbe2oiU5tl3OL1XUqq3X8qN23LFbMpB3k; newstatisticUUID=1623637298_560270187; _yep_uuid=cce8cf26-f08a-ee7d-8cad-433a856b86d1; e1=%7B%22pid%22%3A%22qd_P_rank_01%22%2C%22eid%22%3A%22qd_C19%22%2C%22l1%22%3A4%7D; e2=%7B%22pid%22%3A%22qd_P_rank_19%22%2C%22eid%22%3A%22%22%7D; qdrs=0%7C3%7C0%7C0%7C1; showSectionCommentGuide=1; qdgd=1; lrbc=1021617576%7C626160000%7C0; rcr=1021617576; bc=1021617576',
                'referer': 'https://www.qidian.com/rank'
            }
            date = requests.get(book_url,headers=headers)
            content_l = date.content.decode()
            soup = BeautifulSoup(content_l,'lxml')
            book_soup = soup.find('div',{'class':'read-content j_readContent'}).text

            with open(path+book.text+'.txt','w',encoding='UTF-8') as f:
                f.write(book_soup)
        print('下载完成')
    except Exception:
        print("网络未连接，下载失败")

if __name__ =='__main__':
    get_text(url1)






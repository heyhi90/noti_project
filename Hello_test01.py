import telegram
import time
import requests
from bs4 import BeautifulSoup


def ppomppu():
    # 텔레그램 세팅
    bot = telegram.Bot(token='1737174063:AAFGy4F-UWy667u3ycOQaE2fTEg3FSKv6Ek')
    testbot = telegram.Bot(token='1902707442:AAHcK9oumcVMWUWJMAhk0JFj-aH-Gxp6e48')

    # 스위치 변수
    n = 0
    t = 0

    # 오래된 게시글, 이름 끌어오기
    post_oldNum = 0
    post_oldName = 0
    post_oldReply = 0
    post_oldName1 = 0

    # 게시글 정보 저장하는 변수
    post_Num = []
    post_Cate = []
    post_Name = []
    post_Address = []
    post_Adnum = []

    post_Hit = []
    post_Down = []
    post_Date = []

    post_Reply = []

    while True:

        # 웹 연결
        url = 'https://newtoki97.com/toki_bl'
        req = requests.get(url)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')

        # 게시글 끌어오기
        post = soup.select_one('ul#list-body')
        post_list = post.select('.list-item')

        for i in post_list:
            postNum = i.select_one(".list-item > div.wr-num.hidden-xs").text
            postCate = i.select_one(".list-item > div.wr-subject > a > span.tack-icon").text
            postName = i.select_one(".list-item > div.wr-name.hidden-xs > a > span").text.lstrip()
            postAddress = i.select_one(".list-item > div.wr-subject > a")['href']

            postReply = i.select_one(".list-item > div.wr-subject > a > .icon_reply")

            postHit = i.select_one(".list-item > div.wr-hit").text.lstrip()
            postDown = i.select_one(".list-item > div.wr-down").text.lstrip()
            postDate = i.select_one(".list-item > div.wr-date").text.lstrip()

            postAdnum = postAddress[-7:]

            if postNum != '*':
                if postNum != '':
                    post_Num.append(postNum)
                    post_Cate.append(postCate)
                    post_Name.append(postName)
                    post_Address.append(postAddress)
                    post_Adnum.append(postAdnum)
                    post_Hit.append(postHit)
                    post_Down.append(postDown)
                    post_Date.append(postDate)
                    post_Reply.append(postReply)

        # 공유글 확인 함수
        for j in range(len(post_Num)):
            if j == 0:
                if post_Cate[j] == '공유':
                    if post_oldNum != post_Num[j]:
                        if int(post_Down[j]) < 30:
                            post_oldNum = post_Num[j]
                            post_oldName = post_Name[j]
                            text = '1-1) 공유: ' + post_Num[j] + ', 작성자: ' + post_Name[j] + '\n다운수: ' + post_Down[j] + ', ' + post_Date[j]
                            print(text)
                            bot.sendMessage(chat_id=-1001186655463, text=text)

                    elif post_oldNum == post_Num[j]:
                        if post_Name[j] != post_oldName:
                            post_oldName = post_Name[j]
                            text = '1-2) 공유: ' + post_Num[j] + ', 작성자: ' + post_Name[j] + '\n다운수: ' + post_Down[j] + ', ' + post_Date[j]
                            print(text)
                            bot.sendMessage(chat_id=-1001186655463, text=text)
                else:
                    print('공유없음')

            if post_Cate[j] == '공유' and j > 0:
                if post_Reply[j]:
                    print('')
                else: #답글 아닌 공유글만 보여지기
                    if int(post_Down[j]) < 30 and int(post_Down[j]) > 0:
                        if post_oldName == post_Name[j] and j == 1 :
                            print('no')
                        else:
                            if post_oldName1 != post_Num[j]:
                                post_oldName1 = post_Num[j]
                                text = '2) 공유 새글: ' + post_Num[j] + ', 작성자: ' + post_Name[j] + '\n다운수: ' + post_Down[j] + ', ' + post_Date[j]
                                print('공유 새글(다른글)')
                                bot.sendMessage(chat_id=-1001186655463, text=text)

        for j in range(len(post_Reply)):
            if post_Reply[j]:
                if int(post_Down[j]) > 0 and int(post_Down[j]) < 30:
                    if post_oldReply != post_Num[j]:
                        post_oldReply = post_Num[j]
                        if post_Cate[j] == '요청' or post_Cate[j] == '정보' or post_Cate[j] == '공유':
                            text = '3) 답글_' + post_Cate[j] + ': ' + post_Num[j] + ', 작성자: ' + post_Name[j] + '\n다운수: ' + post_Down[j] + ', ' + post_Date[j]
                            bot.sendMessage(chat_id=-1001186655463, text=text)
                            print('요청 정보 공유 답글')
                else:
                    print('답글 있으나 다운로드가 높음, 다운로드가 없음')
            else:
                print('답글 없음')

        # 게시글 정보 초기화 하는 변수
        post_Num = []
        post_Cate = []
        post_Name = []
        post_Address = []
        post_Adnum = []

        post_Hit = []
        post_Down = []
        post_Date = []

        post_Reply = []

        n = n + 1
        text01 = ' 테스트 '+str(n)
        if n%100 == 0:
            testbot.sendMessage(1840767554, text01)
            #bot.sendMessage(chat_id=-1001186655463, text=text01)
        time.sleep(8)

if __name__ == '__main__':

    try:
        ppomppu()
    except AttributeError as e:
        print(e)
# 2018 прототип для проекта парсинга данных с M-Link ABB и выгрузки в ПТК Энергосферу. Готовый проект mlink-parser на bitbucket.
import re

import requests
from robobrowser import RoboBrowser


def btnBr(br, link):
    br.follow_link(link)
    for s in br.parsed:
        if "pv_" in s:
            print(s)

s = requests.Session()
s.headers['User-Agent'] = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0'
br = RoboBrowser(parser="html.parser", history=True, session=s)
murl = 'http://192.168.200.100/modules/login.php'
br.open(murl)
f = br.get_form()
f["login"].value = "mview"
f["passwd"].value = "mview"
br.submit_form(f)

x = br.find_all("a", href=True)
for a in x:
    if ("cubicle.php?CU_index=0" in a["href"]):
        link = a
br.follow_link(link)
x = br.find_all("a", href=True)
for a in x:
    if ("Div7_a" in a):
        print(a)
x[16]['href'] = "http://192.168.200.100/modules/mc/operate.php?newDiv=7"
br.follow_link(x[16])
x = br.find_all("a", href=True)
for a in x:
    if ("down" in a["href"]):
        link = a

downlink = br.find(id="btn_down_a")
downlink['href'] = "http://192.168.200.100//modules/mc/operate_update.php?cmd=down"
uplink = br.find(id="btn_up_a")
uplink['href'] = "http://192.168.200.100//modules/mc/operate_update.php?cmd=up"

btnBr(br, downlink)
btnBr(br, downlink)
btnBr(br, downlink)
btnBr(br, downlink)
btnBr(br, downlink)

# btnBr(br,uplink)
# br.follow_link(a)
# in
# if a.find("cubicle.php?"):
#	print("True")
# x.find()
# print(x)

# print(x[0])
# <a href="cubicle.php?CU_index=0"><img src="/global/images/button.gif" alt="" width="100%" height="100%"></a>

# br.follow_link(x[0])
# #print(br.parsed)
# #x[0]['href']="http://192.168.200.100/modules/mc/operate.php?newDiv=7"


# x=br.find_all("a",href=True)
# #print(x)
# br.follow_link(x[0])
# print(br.parsed)

# x=br.find_all("a",href=True)


# br.open("http://192.168.200.100/modules/mc/operate.php?newDiv=7")
# print(br.parsed)

#! formSearch = browser.get_form(action=('liste.php'))


# print(br.parsed)
#f = br.get_form()
#assert_equal(link.get('href'), '/link1/')


# url=br.url
# <a id="Div7_a" href="javascript:Operate_direct(7)"><img src="/global/images/button.gif" alt="" width="100%" height="100%"></a>
# br.open("http://192.168.200.100/modules/mc/operate.php?newDiv=7")
# print(br.parsed)
#f1 = br.get_form(id="Div7_a")
# sbr.submit_form(f1)
# print(f1)


# b.submit_form


# import re
# from robobrowser import RoboBrowser
# browser = RoboBrowser(user_agent='a python robot',parser="html.parser")
# login_url = 'https://webbroker.td.com/waw/idp/login.htm?execution=e1s1'
# browser.open(login_url)
# form = browser.get_form(id="login")
# form["login:AccessCard"].value = "****"
# form["login:Webpassword"].value = "****"
# browser.submit_form(form)

# Inspect the browser session
# browser.session.cookies['_gh_sess']         # BAh7Bzo...
# browser.session.headers['User-Agent']       # a python robot

# browser.select('div.teaser-icon')       # [<div class="teaser-icon">
#                                         # <span class="mega-octicon octicon-checklist"></span>
#                                         # </div>,
#                                         # ...
# browser.find(class_=re.compile(r'column', re.I))

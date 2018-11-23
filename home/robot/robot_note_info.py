from pyquery import PyQuery as pq
from home.models import New

times=0
doc = pq("https://www.shmtu.edu.cn/events")
tbody = doc("tbody")
tr = tbody("tr").items()
for i in tr:
    temp = pq(i)
    i_url = temp("a").attr("href")
    lec_urls="https://www.shmtu.edu.cn/"+i_url
    i_time = temp(".date").text()
    i_title = temp(".title").text()
    i_department = temp(".department").text()
    doc = pq(lec_urls)
    title=doc(".title").text()
    cont = doc(".node-tong-zhi-gong-gao")
    cont("table").remove()
    items = cont("p").items()
    text = ""
    for i in items:
        text = text + i.text() + '\n\n'
    obj = New.objects.filter(source=lec_urls)
    if not obj:
        new = New(title=i_title, public=i_department, source=lec_urls, text=text, type='讲座通知', pub_date=i_time)
        new.save()
        times += 1
print("已更新"+str(times)+"条讲座通知。")
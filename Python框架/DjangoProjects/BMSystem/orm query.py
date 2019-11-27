import os


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BMSystem.settings")
    import django
    django.setup()
    from app01 import models
    from django.db.models import *

    # 1 查询每个作者的姓名以及出版的书的最高价格
    # ret = models.Author.objects.annotate(m=Max("book__price")).values("name","m")
    # print(ret)
    # 2查询作者id大于2作者的姓名以及出版的书的最高价格
    # ret = models.Author.objects.annotate(m=Max("book__price")).filter(id__gt=2).values("name","m")
    # print(ret)
    # 3查询作者id大于2或者作者年龄大于等于20岁的女作者的姓名以及出版的书的最高价格
    # ret = models.Author.objects.annotate(m=Max("book__price")).filter(Q(Q(id__gt=2)|Q(age__gte=20)),authordetail__sex="女").values("name", "m")
    # print(ret)
    # 4 查询每个作者出版的书的最高价格的平均值
    ret = models.Author.objects.annotate(max=Max("book__price")).aggregate(Avg("max"))
    print(ret)

    # 5每个作者出版的所有书的最高价格以及最高价格的那本书的名称
    # from django.db import connection, connections
    #
    # cursor = connection.cursor()  # cursor = connections['default'].cursor()
    # cursor.execute(""" select m.title,max(m.price) from (select title,price,author_id from app01_author a,app01_book b,app01_book_authors c where a.id=c.author_id and b.id=c.book_id order by price desc) m group by m.author_id""")
    # cursor.execute(""" select m.title,max(m.price) from (select title,price,author_id from app01_author a INNER JOIN app01_book b INNER JOIN app01_book_authors c ON a.id=c.author_id and b.id=c.book_id order by price desc) m group by m.author_id""")
    # ret = cursor.fetchall()
    # print(ret)









    # d = {'tname': 'haha'}
    # ret = models.Author.objects.raw(" select m.title,max(m.price) from (select title,price,author_id from app01_author a,app01_book b,app01_book_authors c where a.id=c.author_id and b.id=c.book_id order by price desc) m group by m.author_id",translations=d)
    # for i in ret:
    #     print(i.haha)
    #select title,price,author_id from app01_author a,app01_book b,app01_book_authors c where a.id=c.author_id and b.id=c.book_id order by price desc;

    #select k.title,max(k.price) from (select * from app01_author a,app01_book b,app01_book_authors c where a.id=c.author_id and b.id=c.book_id order by price desc) k group by k.author_id;
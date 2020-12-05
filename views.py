from models import ArticleList, SourceList


def show_titles(article_titles):
    for i in article_titles:
        print(i)


def show_article(article):
    print(article.title)
    print(article.publish_date)
    print(article.text)

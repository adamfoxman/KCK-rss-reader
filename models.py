import feedparser
from newspaper import Article as ArticleParser
from prompt_toolkit.shortcuts import ProgressBar


class Article:
    title = None
    text = None
    publish_date = None
    authors = None
    is_read = False

    def __init__(self, url):
        article = ArticleParser(url)
        article.download()
        article.parse()
        self.title = article.title
        self.text = article.text
        self.authors = article.authors
        self.publish_date = article.publish_date

    def set_as_read(self):
        self.is_read = True


class ArticleList:
    article_list = []

    def __init__(self, source_list):
        for source in source_list:
            title = "Fetching news from " + source
            source = feedparser.parse(source)
            with ProgressBar(title=title) as pb:
                for article in pb(source.entries):
                    new_article = Article(article.link)
                    new_article.publish_date = article.published
                    self.article_list.append(new_article)
        self.article_list.sort(key=lambda x: x.publish_date, reverse=True)

    def add_articles_from_source(self, url):
        source = feedparser.parse(url)
        for article in source.entries:
            new_article = Article(article.link)
            self.article_list.append(new_article)
        self.article_list.sort(key=lambda x: x.publish_date, reverse=True)

    def get_article_titles(self):
        article_titles = []
        for i in self.article_list:
            article_titles.append(i.title)
        return article_titles


class SourceList:
    source_list = []

    def __init__(self):
        pass

    def add_source(self, source_url):
        self.source_list.append(source_url)

    def delete_source(self, url):
        self.source_list.remove(url)

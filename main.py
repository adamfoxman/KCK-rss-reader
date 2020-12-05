import feedparser
from newspaper import Article
from controllers import ReaderController
import views
from models import SourceList, ArticleList


def main():
    reader = ReaderController()
    # for i in reader.article_list.article_list:
    #     views.show_article(i)
    views.run_tui(reader.article_list.article_list)

    # articles = feedparser.parse("https://www.polsatnews.pl/rss/wszystkie.xml")
    # for article in articles.entries:
    #     print(article.title)
    #     print(article.description)
    #     print(article.published)
    #     print(article.link)
    #     article_text = Article(article.link)
    #     article_text.download()
    #     article_text.parse()
    #     print(article_text.text)
    #     print()


if __name__ == '__main__':
    main()
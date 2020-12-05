from models import ArticleList, SourceList
import views


class ReaderController:
    src = SourceList()
    article_list = None

    def __init__(self):
        with open('sources.txt') as source_file:
            source_urls = source_file.readlines()
            for url in source_urls:
                self.src.add_source(source_url=url)

        self.article_list = ArticleList(self.src.source_list)

    def add_new_source(self, url):
        with open('sources.txt') as source_file:
            source_file.writelines(url)
        self.src.add_source(source_url=url)

import py_cui
import textwrap


class TUI:
    def __init__(self, master, article_list, width):
        self.master = master
        self.article_list = article_list
        self.width = width
        self.main_menu = self.master.add_scroll_menu("Articles", 0, 0, row_span=8, column_span=3)
        for i in self.article_list:
            self.main_menu.add_item(i.title)
        self.article_view = self.master.add_scroll_menu("", 0, 3, row_span=8, column_span=5)
        self.main_menu.add_key_command(py_cui.keys.KEY_ENTER, self.display_article)

    def display_article(self):
        title = self.main_menu.get()
        article_text = self.find_article(title=title)
        self.article_view.set_title(title=title)
        article_text = textwrap.wrap(text=article_text, width=((self.width*5)//8)-10)
        self.article_view.clear()
        for i in article_text:
            self.article_view.add_item(i)

    def find_article(self, title):
        for i in self.article_list:
            if i.title == title:
                return i.text


def run_tui(article_list):
    root = py_cui.PyCUI(8, 8)
    root.set_title("KCK RSS Reader")
    s = TUI(root, article_list, width=root._width)
    root.start()
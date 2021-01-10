import wx
import py_cui
import textwrap

class GUI(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent=parent, title=title, size=(800, 500))
        self.CreateStatusBar()
        self.SetMenuBar(self.create_menu())

        self.Show(True)

    def create_menu(self):
        def file_menu():
            filemenu = wx.Menu()

            about = filemenu.Append(wx.ID_ABOUT, "&About", "Information about KCK RSS Reader")
            self.Bind(wx.EVT_MENU, on_about, about)
            filemenu.AppendSeparator()
            filemenu.Append(wx.ID_EXIT, "E&xit", "Exit the program")

            return filemenu

        def on_about(e):
            messagetext = "Small RSS Reader made as a university project.\n\nMade by Adam Lisowski\n2021"

            message = wx.MessageDialog(self, messagetext, "About", wx.OK)
            message.ShowModal()
            message.Destroy()

        menu_bar = wx.MenuBar()
        menu_bar.Append(file_menu(), "&Menu")

        return menu_bar





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

def run_gui(article_list):
    app = wx.App(False)
    frame = GUI(None, "KCK RSS Reader")
    app.MainLoop()
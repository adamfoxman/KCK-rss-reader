import wx
import py_cui
import textwrap
import wx.lib.scrolledpanel



class Fonts:
    font = wx.NORMAL
    title_size = 24
    date_size = 8
    authors_size = 8
    text_size = 10
    def __init__(self):
        with open("settings.txt") as settings_file:
            settings = settings_file.readlines()
            self.font = self.get_font_from_file(settings[0])
            self.title_size, self.date_size, self.authors_size, self.text_size = self.get_size_from_file(settings[1])

    def get_font_from_file(self, settings):
        font = int(settings)
        if font == 0:
            return wx.NORMAL
        elif font == 1:
            return wx.DECORATIVE
        elif font == 2:
            return wx.ROMAN
        elif font == 3:
            return wx.SCRIPT
        elif font == 4:
            return wx.SWISS
        elif font == 5:
            return wx.MODERN
        else:
            return wx.NORMAL

    def get_size_from_file(self, size):
        size = int(size)
        return size + 14, size - 2, size - 2, size

    def set_font(self, font):
        self.font = font
        with open("settings.txt") as settings_file:
            if font == wx.NORMAL:
                settings_file.writelines("0")
            elif font == wx.DECORATIVE:
                settings_file.writelines("1")
            elif font == wx.ROMAN:
                settings_file.writelines("2")
            elif font == wx.SCRIPT:
                settings_file.writelines("3")
            elif font == wx.SWISS:
                settings_file.writelines("4")
            elif font == wx.MODERN:
                settings_file.writelines("5")
            else:
                settings_file.writelines("0")

    def set_size(self, size):
        self.title_size = size + 14
        self.date_size = size - 2
        self.authors_size = size - 2
        self.text_size = size
        with open("settings.txt") as settings_file:
            settings_file.readline()
            settings_file.writelines(str(size))


fonts = Fonts()


class GUI(wx.Frame):
    def __init__(self, parent, title, article_list):
        self.lst = []
        self.article_list = article_list
        super(GUI, self).__init__(parent=parent, title=title, size=(500, 800))
        self.CreateStatusBar()
        self.SetMenuBar(self.create_menu())

        for i in article_list:
            self.lst.append(i.title)

        artcl_list = wx.ListBox(self, choices=self.lst)
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.onListBox, )

        self.Show(True)

    def create_menu(self):
        def file_menu():
            filemenu = wx.Menu()

            about = filemenu.Append(wx.ID_ABOUT, "&About", "Information about KCK RSS Reader")
            self.Bind(wx.EVT_MENU, on_about, about)
            filemenu.AppendSeparator()
            exitbutton = filemenu.Append(wx.ID_EXIT, "E&xit", "Exit the program")
            self.Bind(wx.EVT_MENU, on_exit, exitbutton)

            return filemenu

        def font_menu():
            fontmenu = wx.Menu()
            normal = wx.MenuItem(fontmenu, 0, "Normal", "Normal system font", wx.ITEM_RADIO)
            decorative = wx.MenuItem(fontmenu, 1, "Decorative", "Decorative font", wx.ITEM_RADIO)
            roman = wx.MenuItem(fontmenu, 2, "Roman", "Roman font", wx.ITEM_RADIO)
            script = wx.MenuItem(fontmenu, 3, "Script", "Script font", wx.ITEM_RADIO)
            swiss = wx.MenuItem(fontmenu, 4, "Swiss", "Swiss font", wx.ITEM_RADIO)
            funky = wx.MenuItem(fontmenu, 5, "Funky", "Funky font", wx.ITEM_RADIO)

            fontmenu.AppendItem(normal)
            fontmenu.AppendItem(decorative)
            fontmenu.AppendItem(roman)
            fontmenu.AppendItem(script)
            fontmenu.AppendItem(swiss)
            fontmenu.AppendItem(funky)

            self.Bind(wx.EVT_MENU, on_font_change, normal)
            self.Bind(wx.EVT_MENU, on_font_change, decorative)
            self.Bind(wx.EVT_MENU, on_font_change, roman)
            self.Bind(wx.EVT_MENU, on_font_change, script)
            self.Bind(wx.EVT_MENU, on_font_change, swiss)
            self.Bind(wx.EVT_MENU, on_font_change, funky)

            fontmenu.AppendSeparator()

            small = wx.MenuItem(fontmenu, 7, "Small", "Change font to small", wx.ITEM_RADIO)
            medium = wx.MenuItem(fontmenu, 8, "Medium", "Change font to normal size", wx.ITEM_RADIO)
            big = wx.MenuItem(fontmenu, 9, "Big", "Change font to big", wx.ITEM_RADIO)

            fontmenu.AppendItem(small)
            fontmenu.AppendItem(medium)
            fontmenu.AppendItem(big)

            self.Bind(wx.EVT_MENU, on_size_changed, small)
            self.Bind(wx.EVT_MENU, on_size_changed, medium)
            self.Bind(wx.EVT_MENU, on_size_changed, big)

            return fontmenu

        def on_font_change(event):
            fontclicked = event.GetEventObject().GetItemLabelText()
            if fontclicked == "Normal":
                fonts.set_font(wx.NORMAL)
            elif fontclicked == "Decorative":
                fonts.set_font(wx.DECORATIVE)
            elif fontclicked == "Roman":
                fonts.set_font(wx.ROMAN)
            elif fontclicked == "Script":
                fonts.set_font(wx.SCRIPT)
            elif fontclicked == "Swiss":
                fonts.set_font(wx.SWISS)
            elif fontclicked == "Funky":
                fonts.set_font(wx.MODERN)

        def on_size_changed(event):
            sizeclicked = event.GetEventObject().GetItemLabelText()
            if sizeclicked == "Small":
                fonts.set_size(6)
            elif sizeclicked == "Medium":
                fonts.set_size(10)
            elif sizeclicked == "Big":
                fonts.set_size(14)

        def on_about(e):
            messagetext = "Small RSS Reader made as a university project.\n\nMade by Adam Lisowski\n2021"

            message = wx.MessageDialog(self, messagetext, "About", wx.OK)
            message.ShowModal()
            message.Destroy()

        def on_exit(e):
            self.Close(True)

        menu_bar = wx.MenuBar()
        menu_bar.Append(file_menu(), "&Menu")
        menu_bar.Append(font_menu(), "&Font")

        return menu_bar

    # def create_article_list(self):
    #     for i in self.article_list:
    #         self.lst.append(i.title)
    #     artcl_list = wx.ListBox(self.panel, choices=self.lst)
    #     # wx.CallAfter(self.Bind(wx.EVT_LISTBOX, self.onListBox, self.lst))
    #     return artcl_list
    #
    # def create_text_box(self):
    #     textbox = wx.StaticText(self.panel, label="test123")
    #     textbox.GetFont().PointSize = 14
    #     return textbox
    #
    # def find_article(self, title):
    #     for i in self.article_list:
    #         if i.title == title:
    #             return i.text
    #

    def get_article(self, title):
        for i in self.article_list:
            if i.title == title:
                return i.title, i.text, i.publish_date, i.authors

    class TextWindow(wx.Frame):
        def __init__(self, parent, title, article_title, text, publish_date, authors):
            super(GUI.TextWindow, self).__init__(parent=parent, title=title, size=(800, 500))
            articleframe = wx.Frame(self, title=title)
            # self.panel = wx.Panel(self)

            self.panel = wx.lib.scrolledpanel.ScrolledPanel(self)
            box = wx.BoxSizer(wx.VERTICAL)

            title_bar = wx.StaticText(self.panel, style=wx.ALIGN_CENTER_HORIZONTAL, label=article_title)
            title_bar.SetFont(wx.Font(fonts.title_size, fonts.font, wx.NORMAL, wx.BOLD))
            title_bar.Wrap(self.GetSize().width - 100)
            date_bar = wx.StaticText(self.panel, style=wx.ALIGN_CENTER_HORIZONTAL, label=publish_date)
            date_bar.SetFont(wx.Font(fonts.date_size, fonts.font, wx.NORMAL, wx.NORMAL))
            authors_bar = wx.StaticText(self.panel, style=wx.ALIGN_CENTER_HORIZONTAL, label=str(authors))
            authors_bar.SetFont(wx.Font(fonts.authors_size, fonts.font, wx.ITALIC, wx.LIGHT))
            text_box = wx.StaticText(self.panel, style=wx.SP_WRAP, label=text)
            text_box.SetFont(wx.Font(fonts.text_size, fonts.font, wx.NORMAL, wx.NORMAL))
            text_box.Wrap(self.GetSize().width - 100)

            box.Add(title_bar, 0, wx.ALL | wx.EXPAND)
            box.AddSpacer(0)
            box.Add(date_bar, 0, wx.ALL | wx.EXPAND)
            box.AddSpacer(0)
            box.Add(authors_bar, 0, wx.ALL | wx.EXPAND)
            box.AddSpacer(20)
            box.Add(text_box, 0, wx.ALL)
            self.panel.SetSizer(box)
            self.panel.SetupScrolling()

    def onListBox(self, event):
        title, text, publish_date, authors = self.get_article(event.GetEventObject().GetStringSelection())
        window = self.TextWindow(self, "Article", title, text, publish_date, authors)
        window.panel.GetSizer().Layout()
        window.Show()


# ----------------------------------------------------------------------------------------------------------------------
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
        article_text = textwrap.wrap(text=article_text, width=((self.width * 5) // 8) - 10)
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
    frame = GUI(None, "KCK RSS Reader", article_list)
    app.MainLoop()

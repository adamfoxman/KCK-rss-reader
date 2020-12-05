import urwid
from models import ArticleList, SourceList


def callback(key):
    raise urwid.ExitMainLoop()


def newspaper(articles):
    widget_title = "Your newspaper"
    body = [urwid.Text(widget_title), urwid.Divider()]
    for article in articles:
        button = urwid.Button(article.title)
        # urwid.connect_signal(button, 'click', item_chosen, title)
        body.append(urwid.AttrMap(button, None, focus_map='reversed'))
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))


def mainmenu(title, choices):
    body = [urwid.Text(title), urwid.Divider()]
    body.extend(choices)
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))


# def item_chosen(button, choice):
#     response = urwid.Text([u'You chose ', choice, u'\n'])
#     done = urwid.Button(u'Ok')
#     urwid.connect_signal(done, 'click', callback)
#     main.original_widget = urwid.Filler(urwid.Pile([response,
#                                                     urwid.AttrMap(done, None, focus_map='reversed')]))


def run_tui(article_list):
    main = urwid.Padding(newspaper('Articles from RSS feeds', article_list), align='center', width=('relative', 70))
    topw = urwid.Overlay(main, urwid.SolidFill(' '), align='center', width=('relative', 100),
                         valign='middle', height=('relative', 100), min_width=20, min_height=20)
    mainloop = urwid.MainLoop(topw, palette=[('reversed', 'standout', '')])
    mainloop.run()


def show_titles(article_titles):
    for i in article_titles:
        print(i)


def show_article(article):
    print(article.title)
    print(article.publish_date)
    print(article.text)

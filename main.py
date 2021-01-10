from controllers import ReaderController
import views


def main():
    # reader = ReaderController()
    # views.run_tui(reader.article_list.article_list)
    gui = views.run_gui(None)

if __name__ == '__main__':
    main()
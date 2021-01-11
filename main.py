from controllers import ReaderController
import views


def main():
    reader = ReaderController()

    # reader = ["test1", "test2", "test3"]

    # views.run_tui(reader.article_list.article_list)
    views.run_gui(reader.article_list.article_list)
    # views.run_gui([])

if __name__ == '__main__':
    main()
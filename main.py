from controllers import ReaderController
import views


def main():
    reader = ReaderController()
    views.run_tui(reader.article_list.article_list)


if __name__ == '__main__':
    main()
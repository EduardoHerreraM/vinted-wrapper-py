from vinted_wrapper import Vinted


def main():
    vinted = Vinted()

    products = vinted.items.search_items(search_text='bred')


if __name__ == "__main__":
    main()

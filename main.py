from open_site import open_sesame, get_browser


def main():
    # url = input("Deposit URL or website name (beta): ")
    # open_sesame(url)
    browser = input("Input preferred browser name or 'None' for default browser: ")
    get_browser(browser)


if __name__ == "__main__":
    main()
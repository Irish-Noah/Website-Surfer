import webbrowser as wb


def get_browser(preferred= None):
    browser = None
    try:
        if preferred is not None and preferred.lower() == "none":
            browser = wb.get(using="chrome")
        elif preferred is None:
            browser = wb.get(using="chrome")
        else:
            browser = wb.get(preferred)
    except wb.Error:
        browser = wb.get()
        print("Browser not found. Will use {:s} instead.".format(browser.name))
    if browser is not None:
        print("Browser Selected: {:s}".format(browser.name))
        url = input("\nInput URL or website name (beta): ")
        open_sesame(url)

"""
Function that opens a website given by website name or url
:parameter: a string of a url or website name
:return: None, but opens website
"""
def open_sesame(url):
    try:
        if url.lower() == "youtube":
            wb.open("https://www.youtube.com/channel/UCOyIIk-oDsmXs40hnano_Dw")
        elif url.lower() == "google":
            wb.open("https://www.google.com/")
        else:
            # gotta keep myself safe from opening shady websites on accident
            if "https" in url or "www" in url:
                wb.open(url)
            else:
                print("That shortcut is not supported. Please try again with a url")
    except wb.Error:
        url = " "
        raise ImportError("Website could not be found, try again")







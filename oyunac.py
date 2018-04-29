import webbrowser

def open_game(browser, url):
    return webbrowser.get(browser).open(url)

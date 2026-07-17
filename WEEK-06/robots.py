from urllib.robotparser import RobotFileParser

def allowed(url):

    rp = RobotFileParser()
    rp.set_url("https://books.toscrape.com/robots.txt")
    rp.read()

    return rp.can_fetch("*", url)
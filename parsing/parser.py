from aiohttp import ClientResponse
from bs4 import BeautifulSoup


def parse_responce(html):
    bs = BeautifulSoup(html, "html.parser")
    all_nums = bs.find("span", class_="page-title-count-wQ7pG").text
    all_nums = all_nums.replace(u'\xa0', u'')
    all_nums = int(all_nums)
    return all_nums






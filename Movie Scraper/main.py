import random
import requests  # pip install request
from bs4 import BeautifulSoup  # pip install bs4
url = 'https://www.imdb.com/chart/boxoffice'


def main():
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    movieTags = soup.select('td.titleColumn')
    movieTag0 = movieTags[0]
    movieSplit = movieTag0.text.split()

    print(movieSplit)


if __name__ == '__main__':
    main()

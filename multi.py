import requests
import csv
from multiprocessing import Pool


def write_csv(data):
    with open('multi_csv.csv', 'a') as f:
        order = ['name', 'url', 'desc', 'traf', 'percent']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)


def get_text(url):
    r = requests.get(url)
    return r.text


def get_data(html):
    for i in range(1, 6051):

        url = 'https://www.liveinternet.ru/rating/ru//today.tsv?page={}'.format(i)
        response = html.strip()
        d = response.split('\n')[1:]

        for row in d:
            colums = row.strip().split('\t')
            name = colums[0].strip()
            url = colums[1].strip()
            desc = colums[2].strip()
            traf = colums[3].strip()
            percent = colums[4].strip()

            data = {'name': name,
                    'url': url,
                    'desc': desc,
                    'traf': traf,
                    'percent': percent}
            write_csv(data)


def make_all(url):
    text = get_text(url)
    get_data(text)


def main():

    url = 'https://www.liveinternet.ru/rating/ru//today.tsv?page={}'
    urls = [url.format(str(i)) for i in range(1, 7134)]

    with Pool(20) as p:
        p.map(make_all, urls)


if __name__ == '__main__':
    main()

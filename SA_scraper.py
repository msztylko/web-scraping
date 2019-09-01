import requests, os, bs4

url = 'http://blog.samaltman.com'
os.makedirs('samaltman', exist_ok=True)

fav_urls = set()
with open('fav_blog_posts.txt') as file:
    lines = file.readlines()
    for line in lines:
        line = line.lower().replace('?', '').replace(',', '').replace('-', '').replace("'", "")
        line = line.split()
        fav_url = '-'.join(line)
        fav_urls.add(fav_url)


# for url in fav_urls:
#     print('Downloading webpage {}'.format(url))
#     res = requests.get(url)


# try:
#     res.raise_for_status()
# except Exception as exc:
#     print('Problem {}'.format(exc))
#
# resSoup = bs4.BeautifulSoup(res.text)
#
# file = open('Sam_Altman.txt', 'wb')
# for chunk in res.iter_content(100000):
#     file.write(chunk)
#
# file.close
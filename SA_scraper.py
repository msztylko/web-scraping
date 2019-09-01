import requests, os, bs4

url = 'http://blog.samaltman.com'
os.makedirs('samaltman', exist_ok=True)

fav_urls = set()
with open('fav_blog_posts.txt') as file:
    lines = file.readlines()
    for line in lines:
        line = line.lower().replace('?', '').replace(',', '').replace('-', '').replace("'", "").split()
        fav_url = '-'.join(line)
        fav_urls.add(fav_url)

error_count = 0
downloaded = 0
for fav_url in fav_urls:
    print('Downloading webpage {}'.format(url + '/' + fav_url))
    res = requests.get(url + '/' + fav_url)
    try:
        res.raise_for_status()
        downloaded += 1
    except Exception as exc:
        print('Problem {}'.format(exc))
        error_count += 1

print("Succesfully downloaded {} blog posts and "
      "encountered problems with {} blog posts.". format(downloaded, error_count))



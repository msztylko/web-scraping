import requests, os

url = 'http://blog.samaltman.com'
os.makedirs('sam-altman', exist_ok=True) #create directory for saving all fav blog posts
path = os.path.join(os.getcwd(), 'sam-altman')

fav_urls = set()
with open('fav_blog_posts.txt') as file:
    lines = file.readlines()
    for line in lines:
        #remove ? , - ' from url
        line = line.lower().replace('?', '').replace(',', '').replace('-', '').replace("'", "").split()
        fav_url = '-'.join(line)
        fav_urls.add(fav_url)

error_count = 0
downloaded = 0
for fav_url in fav_urls:
    full_url = url + '/' + fav_url
    print('Accessing webpage {}'.format(full_url))
    res = requests.get(full_url)
    try:
        res.raise_for_status()
        file_name = os.path.join(path, fav_url + ".html")
        with open(file_name, 'wb') as file:
            for chunk in res.iter_content(100000):
                file.write(chunk)
                print("Succesfully downloaded {}".format(fav_url))
        downloaded += 1
    except Exception as exc:
        print('Problem {}'.format(exc))
        error_count += 1
    print()

print("Succesfully downloaded {} blog posts and "
      "encountered problems with {} blog posts.". format(downloaded, error_count))
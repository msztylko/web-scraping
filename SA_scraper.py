import os
import requests
from selenium import webdriver

url = 'http://blog.samaltman.com'
dir_name = 'sam-altman'
os.makedirs(dir_name, exist_ok=True) #create directory for saving all fav blog posts
path = os.path.join(os.getcwd(), dir_name)

#I have a file fav_blog_posts.txt with the titles of my fav articles in each line
#Correct urls have no ? , - ' and are contected by - between each word
fav_urls = set()
with open('fav_blog_posts.txt') as file:
    lines = file.readlines()
    for line in lines:
        #remove ? , - ' from url
        line = line.lower().replace('?', ' ').replace(',', ' ').replace('-', ' ').replace("'", " ").split()
        fav_url = '-'.join(line)
        fav_urls.add(fav_url)

error_count = 0
downloaded = 0
incorrect_urls = []
for fav_url in fav_urls:
    full_url = url + '/' + fav_url
    print('Accessing webpage {}'.format(full_url))
    res = requests.get(full_url)
    try:
        res.raise_for_status()
        file_path = os.path.join(path, fav_url + ".html")
        with open(file_path, 'wb') as file:
            for chunk in res.iter_content(100000):
                file.write(chunk)
        print("Succesfully downloaded {}".format(fav_url))
        downloaded += 1
    except Exception as exc:
        print('Problem {}'.format(exc))
        error_count += 1
        incorrect_urls.append(fav_url)
    print()

print("Succesfully downloaded {} blog posts and "
      "encountered problems with {} blog posts, namely: {}."
      .format(downloaded, error_count, [x for x in incorrect_urls]))

browser = webdriver.Chrome()
browser.get(url)
try:
    elem = browser.find_element_by_class_name('search-archive')
    print("The {} element was found".format(elem.tag_name))
except:
    print("No element was found.")
elem.send_keys()


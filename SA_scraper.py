import os
import requests
from selenium import webdriver

url = 'http://blog.samaltman.com'
dir_name = 'sam-altman'
os.makedirs(dir_name, exist_ok=True) #create directory for saving all fav blog posts
path = os.path.join(os.getcwd(), dir_name)

#I have a file fav_blog_posts.txt with the titles of my fav articles in each line
#Correct urls have no ? , - ' and are connected by - between each word
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
      .format(downloaded, error_count, incorrect_urls))

browser = webdriver.Chrome()
for i in incorrect_urls:
    i = i.replace('-', '+')
    browser.get("https://www.google.com/search?q=" + i + " sam altman")
    matched_elements = browser.find_elements_by_xpath('//a[contains(@href, "samaltman.com")]')
    if matched_elements:
        i = i.replace('+', '-')
        matched_elements[0].click()
        file_path = os.path.join(path, i + ".html")
        with open(file_path, 'w') as file:
            file.write(browser.page_source)
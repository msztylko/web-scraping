# web-scraping

A short project for collecting my favourite blog posts from http://blog.samaltman.com/ and getting familiar with web scraping methods.
It is based on the list of my favourite blog posts that I keep as a text file. Each line of that file corresponds to the title of blog post and my goal was to download each blog post and save it as a html file.

Tasks involved:
* processing each blog post title to a valid url format
* accessing and downloading each webpage with requests library
* cretaion of a seperate directory to which the html files were saved
* use of Selenium module for 3 blog posts with urls that didn't follow standard pattern

There are probably better ways to achieve this task and I may try them in the future, but for now the real goal was to get familiar with requests and selenium modules and web scraping in general.

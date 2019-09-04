# web-scraping

A short project for collecting my favourite blog posts from http://blog.samaltman.com/ and getting familiar with web scraping methods.
It is based on the list of my favourite blog posts that I keep as a text file. Each line of that file corresponds to the title of the blog post and my goal was to download each blog post and save it as an html file.

Tasks involved:
* processing each blog post title to a valid URL format
* accessing and downloading each webpage with requests library
* cretaion of a separate directory to which the html files were saved
* use of the selenium module for 3 blog posts with URLs that didn't follow a standard pattern

There are probably better ways to accomplish this task and I may try them in the future, but for now the real goal was to get familiar with the requests and selenium modules and web scraping in general.

Possible next steps:
1. Take all html files and convert them into one PDF file to create a "book"

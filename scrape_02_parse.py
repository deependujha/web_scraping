import requests
from bs4 import BeautifulSoup   #   import beautifulsoup
'''
    A really nice thing about the BeautifulSoup library is that
    it is built on the top of the HTML parsing libraries like html5lib, 
    lxml, html.parser, etc. 
    So  BeautifulSoup object and specify the parser library can be created 
    at the same time.
'''
  
URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL)


'''
    We create a BeautifulSoup object by passing two arguments:
        1. r.content : It is the raw HTML content.
           (we can also pass r.text. But, generally people use r.content.)
        2. html5lib : Specifying the HTML parser we want to use.
'''

soup = BeautifulSoup(r.content,'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
'''
    We can also use 'html.parser' and 'lxml'. Just use:
    
        soup = BeautifulSoup(r.content,'html.parser')
        soup = BeautifulSoup(r.content,'lxml')  # If this line causes an error, run 'sudo apt-get install python3-lxml'


    So, what is the difference between them? 

    Ans->  visit these sites: 1. https://www.geeksforgeeks.org/html5lib-and-lxml-parsers-in-python/
                              2. https://stackoverflow.com/questions/45494505/beautifulsoup-whats-the-difference-between-lxml-and-html-parser-and-html5

        The basic reasoning why would you prefer one parser instead of others:

            -> html.parser- built-in - no extra dependencies needed
            -> html5lib - the most lenient - better use it if HTML is broken (tags not properly opened or closed)
            -> lxml - the fastest

'''
# Now print soup.prettify() , it gives the visual representation of the parse tree created from the raw HTML content.
# Printing soup will also print the html content. But, with prettify(), it will be more readable and easier to visualize.

print(soup)
print(soup.prettify())
print(type(soup))   #   <class 'bs4.BeautifulSoup'>. It is an object of class beautiful soup.
print(type(soup.prettify()))    #   <class 'str'>. It is a string containing html.
"""
# Steps involved in web scraping:

        1. Send an HTTP request to the URL of the webpage you want to access. 
       The server responds to the request by returning the HTML content of the webpage. 
       For this task, we will use a third-party HTTP library for python-requests.


        2. Once we have accessed the HTML content, we are left with the task of parsing the data. 
        Since most of the HTML data is nested, we cannot extract data simply through string processing. 
        One needs a parser which can create a nested/tree structure of the HTML data. 
        There are many HTML parser libraries available but the most advanced one is html5lib.


        3. Now, all we need to do is navigating and searching the parse tree that we created, i.e. tree traversal. 
        For this task, we will be using another third-party python library, Beautiful Soup. 
        It is a Python library for pulling data out of HTML and XML files.
"""

#   <---- INSTALL LIBRARIES  ---->
# pip install requests
# pip install html5lib
# pip install bs4
# sudo apt-get install python3-lxml  (if you want to use lxml for parsing html)

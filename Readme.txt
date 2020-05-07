Set up instructions:
1.  In the terminal, export the path to geckodriver that is attached in the zip folder.
    For example:
    If the path where I have extracted the zip is:
    /home/zeronp/Desktop/Zomato_Scraper
    In terminal:
    export PATH=$PATH:/home/zeronp/Desktop/Zomato_Scraper

2.  Run the ZomatoLinkScraper.py using the command: python ZomatoLinkScraper.py
    This will scrape and save the links to all the restaurants in a text file (pune_restaurant_list.txt)
    It will take some time to scrape all the data, since the list is huge (Depends on your network connectivity and speed).
    If you do not want to view the browser, uncomment the line: #options.add_argument('-headless').
    This scrape the data without opening the browser.

3.  Run the ZomatoRestaurantScraper.py using the command: python ZomatoRestaurantScraper.py
    This will scrape the restaurants one by one, and store it in a json file(zomato_pune.json)

4.  Run the Convertor.py using the command: python Convertor.py
    This will convert the json file to a csv file to improve readability.

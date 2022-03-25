# README

## Clogau Outlet Product Scraper
**Author:** Gareth Sion Jones
**Date:** 25/03/2022

This application scrapes the product pages from the Clogau Outlet website, and stores the data into a google sheet. This is run from a Flask application either locally, or integrated into a web server. 

### Configuration
In the source code folder, there is a folder named 'config'. In here are the service_account.json credentials from the google sheets API, and the email of the linked google sheets account. These can be changed in desired.

### To Run the App Locally
* You need to have python version 3.9 or higher installed on the computer. 
* You need to be able to access a command line terminal - either CMD in Windows, or Terminal in Mac OS/ Linux.

1. Open a command line terminal 
2. Navigate to the directory of this code
3. The code has been written in a virtual environment, so that a user can access all the required dependencies. To access this environment, run the following command in the terminal:


    `source venv/bin/activate`


4. Now the application can be launched. In the terminal, run the command 


    `flask run`


5. When the command executes, a message will appear in the terminal instructing which local address the app is running on (e.g. http://127.0.0.1:5000/). Open a browser, and enter this address into the address bar.

6. You should now see the running web application. To scrape, press the 'Scrape' button. This will take a while to complete, so don't close the window or let the computer sleep.

7. When the app has run, you will be directed to a new web page with the results listed. This can be downloaded as a csv file locally, and you can search through the results for specific entries. The data will have been automatically saved in the linked google drive account. 


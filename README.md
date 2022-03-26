# README

## Clogau Outlet Product Scraper
**Author:** Gareth Sion Jones
**Date:** 25/03/2022

This application scrapes the product pages from the Clogau Outlet website, and stores the data into a google sheet. This is run from a Flask application either locally, or integrated into a web server. 

## Configuration
In the source code folder, there is a folder named 'config'. In here are the service_account.json credentials from the google sheets API, and the email of the linked google sheets account. These can be changed in desired.

## Running the Application

The app can be run either in a browser on a local machine, or integrated into a web server. Details of how to achieve each are given below. Note, upon executing the app by selecting the 'Scrape' button in the browser window, the app will run, but will take quite a bit of time to complete. This is due to the inherent time overhead of scraping a webpage, and due to random time intervals encoded between each scrape to prevent overloading the website, and also triggering any anti-scraping policy. It is important therefore to not close/refresh the browser, or let the computer sleep. Just allow the app to run. An improvement to the app would be to incorporate a progress bar, however this is not so trivial due to the nature of how the Flask framework handles server requests. Hence it has not been included in this iteration of the app. 

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

### To Integrate App into Azure Server

1. Create a new Azure Web App. This can be done in the Azure portal, by entering "app services" in the search bar, and then selecting "Create" in the app services page.

2. In the create app page, fill out the form as below:
    * Create a new Resource Group
    * Name - give this an appropriate name of your choice.
    * Runtime Stack - Python 3.9
    * Region - UK South
    * App Service Plan - you can set this as desired. Basic is probably fine for the purposes of this project.
    * Select 'Apply', and then you can review and create the mew resource group.

3. Get credential for deploying the web application. The code is packaged as a zip file, so can be uploaded to Azure by an HTTP client such as 'Postman'. If you don't already have postman, this can be downloaded from 'https://www.postman.com/downloads/'.
    * To deploy the zip file to Azure, first you need to make sure that the file will be built upon deployment. To do this, navigate to the 'Configuration' tab in the portal, and under 'Application Settings', select 'New Setting'.
    * In the new dialogue box, create a new setting  with the name `SCM_DO_BUILD_DURING_DEPLOYMENT`, and the value as `true`.
    * Select save to save the settings.
    * Next, you need the FTPS credentials to upload the zip file via postman. These can be found by navigating to the 'Deployment Centre' tab, and subsequently the 'FTPS' tab. Here you are given a username and password. The required part of the username is only what follows the final '\' character, starting with a '$' symbol, e.g. $clogau_scraper.
    * Make a note of the email address of the application from the resource group.

4. Deploy the application with Postman. 
    * Create a new request.
    * Select **POST** as the request type. 
    * Enter the url https://\<app-name\>.scm.azurewebsites.net/api/zipdeploy where <app-name> is the name of the web app.
    * Navigate to the 'Authorization' tab, and enter the username and password from the FTPS credentials found previously. 
    * Navigate to the 'Body' tab. Set the content type as 'Binary', and select file to upload the zip file. 
    * Select Send. The file will upload to your Azure app. This may take a minute or two, depending on bandwidth. 

5. Open the web application.
    * Now the web app should have been deployed. To check, open a browser, and enter the url http://<app-name>.azurewebsites.net. The app should be here now. If the default Azure page shows, wait for a moment and refresh the browser.






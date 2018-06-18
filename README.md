# Project 4 - Full Stack Django App

## Overview

* Introduction
  - My application will allow users log in and build a personalized brewery brew trip. They will be able to search for cities that they are visiting and the application will give them the breweries in the area and a map to their location. They can then click on the brewery to get more information. I would also like for the user to build a list of "must have" beers at this individual brewhouses as well as a list of their favorite beers. For both, I will use external APIs to grab the information and then store it. The user's home page will list planned outings and favorite beers and breweries based on ratings. The user schema will have username, first name, then a related table with a list of breweries and their associated city.
* Technologies
  - Postgres SQL will be used to create the user profiles and store the information for favorite beers and breweries for their trip. When searching for cities to visit, I will use an external api to gather the breweries. The user can click to get more information. The user can then click on them to add them to their list. There will be a lot of use of templating html to display the information being grabbed from the api.
  - This will be a lot of grabbing brewery and beer ids that will then be hidden from the user but accessible in get requests.
* MVP
  - Aproximately 5-6 pages on top of the base template. The base template will have a nav bar. The home page will have the username, password and new user set up.
  - New User page will be user name, first name, and password.
  - User home page will have their planned breweries with a list and the brewery addresses, and websites.
  - A search page where the returned json will have a list of breweries and then add button and a more information button.
  - The more information button will take the user to a page specific for that brewery. Name, address and website will be listed here.
* Goals
  - In the detail page for the breweries, I would like to have a map, a website link, photos and their beers.
  - Breweries with icons that indicate features such as has food, main location, distributors.
* Stretch Goals
  - Once the brewery is added to their visit list, they can then search the breweries beers and add it to a "must have" list of beers.
  - A map that displays all the addresses on their planned brew trip.
* Timeline
  - _Monday_: application set up and running, SQL database setup in postgres. Authentication setup. Create/Read part of CRUD set up.
  - _Tuesday_: Be able to make an api call that lists the breweries from a given city.
  - _Wednesday_: Those breweries are clickable which then takes the user to a brewery detail page and map. From that page, user can add the brewery to their list of visits. Will have first test done here. Delete and Update will be added here.
  - _Thursday_: The app will be mostly finished, try to get map to load on individual brewery page. Work on getting the favorite beers to populate from an API instead of having user enter the beer name.

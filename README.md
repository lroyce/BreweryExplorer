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
  - Tell us what you would _like to have_ after you reach your MVP
  - In the detail page for the breweries, I would like to have a map, a website link, photos and their beers.
  - Breweries with icons that indicate features such as has food, main location, distributors.
* Stretch Goals
  - Tell us what you would like to get to, if time were no issue.  You should not expect to reach these.
  - Once the brewery is added to their visit list, they can then search the breweries beers and add it to a "must have" list of beers.
* Timeline
  - _Monday_: application set up and running, SQL database setup in postgres. Authentication setup. Create/Read part of CRUD set up.
  - _Tuesday_: Be able to make an api call that lists the breweries from a given city.
  - _Wednesday_: Those breweries are clickable which then takes the user to a brewery detail page and map. From that page, user can add the brewery to their list of visits. Will have first test done here. Delete and Update will be added here.
  - _Thursday_: The app will be mostly finished, try to get map to load on individual brewery page. Work on getting the favorite beers to populate from an API instead of having user enter the beer name.
* Wireframes
  - You can use whatever you want to make these (it can just be a drawing)
  - This must be checked into your repo and displayed in this section
  - If it's a drawing you can take a picture with your phone and upload it :)
* Crow's foot diagram of your schema.


## Technical Requirements

Everything is in the same repo you created for your proposal

### Due Thursday, June 21 at 11:00PM

Your project must:

* Be **Full CRUD**: `Create && Read && Update && Destroy`
* Have **authentication**.  Users can log in and out.  A user should not have the ability to see or update any data that you don't want them to
* **Tests**. You need to have at least a few tests per app.  All tests must pass.
* **Postgres database** with **multiple related database tables**.
* Do _something_ on the frontend (does not have to be as much as Project 1)
  - You are still using Django to serve up the pages
  - But the pages are not completely static - the user can interact with it
* Use **Vanilla Javascript or jQuery** for **DOM manipulation**
  - Do not have a heavy mix of both
  - If you are using Vanilla JS: we should see no `$` (unless it's used for AJAX)
  - If you are using jQuery: we should see no `document`
* Use at least one of the following (and your README should tell us what option(s) used)
  - **Ajax requests to your Django app**.  This means you have route that responds with JSON and your frontend makes an AJAX request to it.
  - [**`requests`**](http://docs.python-requests.org/en/master/). Make an HTTP from the backend to some API.
  - **Typescript**.  Use Typescript on your frontend instead of of Javascript.
  - **Full test coverage**.  At least one test per route per verb.  If the route does something different depending on whether or not someone is logged in. Test both cases.  All tests must pass.
  - **Something else** that will **blow us away**.  Talk to your squad leader if you can't make any of the above work.
* Be **deployed on Heroku**
  - Your app must work on Heroku, not just locally
* Have all your code on our **GitHub Enterprise**
  - We cannot see your code on Heroku, we can only see it on GitHub (the same repo where your proposal is)
  - This means you have two remotes, `heroku` and `origin`
* Use **CSS**.  You may use Bootstrap but you also need to have some of your own CSS.
* Have at least 40 commits. (You will likely have many more)
* Have code that we can read.  If the indentation is all over place, variable / function names that don't make sense, etc. then we cannot read your code.  We have to read your code in order to grade it.
* A `README.md` (see below)
* **Absolutely no Disney IP**.  If you have any doubts, do not use it
  - This is a reminder.  This goes for every assignment

### `README`

Your `README` (by Thursday night) should include

* (Every section from the proposal)
* Struggles
  - What were the challenging parts?  Tell us about it.  What did you learn?
* App
  - A link to the deployed app
  - Screen shots of the different pages of the app
  - Any other info we should know
* Future Goals
  - Tell us what would like to add/fix/remove/change with more time


## Suggested Ways to Get Unstuck

* **Break the project down into different components** (data, presentation, views, style, DOM manipulation) and brainstorm each component individually. Use whiteboards!
* **Use your Development Tools** (`console.log`, `debugger`, inspector, `alert` statements, etc) to debug and solve problems
* Work through the lessons in class & ask questions when you need to! Think about adding relevant code to your app each night, instead of, you know... _procrastinating_.
* **Commit early, commit often.** Don’t be afraid to break something because you can always go back in time to a previous version.
* Consult **documentation resources** (MDN, jQuery, etc.) at home to better understand what you’ll be getting into.
* Consult **previous lectures**
* **Don’t be afraid to write code that you know you will have to remove later.** Create temporary elements (buttons, links, etc) that trigger events if real data is not available.
* Read the error message.  Google the error message.


## Friendly reminder

Do not accidentally plagiarize. [Cite your sources](https://git.generalassemb.ly/code-rosie/student_resources/blob/master/plagiarism.md#how-to-get-around-plagiarism)

## Project Feedback + Evaluation

Refer to our [Project Rubric](https://git.generalassemb.ly/code-rosie/student_resources/blob/master/project-rubric.md)

## Asking for you help

Refer to [these instructions](https://git.generalassemb.ly/code-rosie/student_resources/blob/master/project-week-help.md)



## What happens during project week

* Like any other day, you must be here from 9 to 5
* You will meet with your squad for standup daily
* You are in charge of your own time management
  - We will help as needed but getting the job done is **your responsibility**
* You will present your project on Friday (more on this as the date gets closer)

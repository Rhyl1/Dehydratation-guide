## The Dehydratation guide. 
This site was put together for the Code Institue milestone project nr. 3.
It offers a reference for times and temperatures to dry food in food dehydrators.

### UX
The website is constructed with a minimal responsive grid and contains a basic navbar for navigation.
<![alt](https://github.com/Rhyl1/Dehydratation-guide/blob/5b92296606871c15af749687e66ca4aaf295ad30/static/img/responsive1.png)>

<![alt](https://github.com/Rhyl1/Dehydratation-guide/blob/5b92296606871c15af749687e66ca4aaf295ad30/static/img/responsive2.png)>
- See following link for wireframes (included in the root structure img folder): 
(https://github.com/Rhyl1/

#### Users
The users of the website include people looking for information about drying food in food hydrators and owners of home food hydrators looking for reference material.


#### Features
##### Existing Features
- Start button -- This button starts the game
- About button -- This button links to an info screen, explaining the game
- Score counter -- Appears after the game starts and shows the current score
- Random generated letter bubbles -- These are the main feature of the game and need to be matched by typing the corresponding key for them to disappear from the screen and gain points.

##### Features Left to Implement
- Filter function: to filter the list so it shows for instance only vegetables, or only a certain kind of temp. to prepare food. 
- Favourites functionality; items out of the list could be marked as favourite.
- Logging of the users so they can edit and store their favorite lists.


##### Technologies Used
This project uses:

- HTML - for structure
- CSS - for styling
- Flask
- Jinja for template logic
- Pyton for logical programming
- Materialize CDN for styling and icons
- MongoDB Atlas for database
- Heroku for site deployment
-flask_pymongo for ?
-ndspython for ?
- Google Chrome - for browser use and the use of development tools
- The Google search engine - was used for research.
- Links to Bootstrap CDN - for the Bootstrap and JavaScript functions
- Links to JQuery and JS scripts
- GitHub - repository hosted on Github -Gotpod: was used as cloud IDE solution
- Git Pages - Website is hosted on Github pages
- Am I responsive - was used for testing responsiveness of the website
- https://validator.w3.org - was used to validate the css and html code used
##Testing
While constructing the website, the initial responsiveness was tested within the Gitpod IDE, which links to the Google Chrome browser, where development tools were used.
After this, Am I responsive was used to test responsiveness.
Also the html and css code was validated using; https://validator.w3.org. 

## Deployment
The settings for the mongo DB are set in the env.py file. It contains a string with the username and password and a reference to the database name, used for the apps construction. This file is 
not uploaded to github, to keep the information secure after deployment. After finishing the pages in Gitpod, the project was deployed using Heroku. 
To make this deployment possible the following steps need to be followed:

The pages where deployed by activating the GitHub pages on GitHub. This process makes the website accessible for user via the internet
## Credits for Content & Acknowledgements
- All props go to the course material and in perticular the miniproject at the end of the ....module.


- CSS3 Patterns Gallery is used for background CSS styling:
https://leaverou.github.io/css3patterns/#cross-dots

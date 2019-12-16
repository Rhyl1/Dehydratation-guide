## Food Dehydration Guide
This site was put together for the Code Institue milestone project nr. 3.
It offers a reference for times and temperatures to dry food in food dehydrators.

### UX
The website is constructed with a minimal responsive grid and contains a basic navbar for navigation.
<![alt](https://github.com/Rhyl1/Dehydratation-guide/blob/5b92296606871c15af749687e66ca4aaf295ad30/static/img/responsive1.png)>

<![alt](https://github.com/Rhyl1/Dehydratation-guide/blob/5b92296606871c15af749687e66ca4aaf295ad30/static/img/responsive2.png)>

#### Users
The users of the website include people looking for information about drying food in food dehydrators 
and owners of home food dehydrators looking for reference material and a way to combine foods with the same dry time for drying together.


#### Features
##### Existing Features
- Navigation bar -- This bar is responsive and changes for smaller resolutions.
- Editable list of items with icon, corresponding to the chosen category.

##### Features Left to Implement
- Flask Pagination - to deal with a larger list
- Validation of input on fields and return messages for users
- Disabeling of duplicate records in types list
- Possibility to create a list of favorites (by clicking on the start in the right-hand corner of the list item)
- Filter function: to filter the list so it shows for instance only vegetables or only a certain kind of temp. to prepare food. 
- Logging of the users so they can edit and store their favorite lists.

##### Technologies Used
This project uses:

- HTML - for structure
- CSS - for styling
- Flask
- Jinja for template logic
- Python for logical programming
- Materialize CDN for styling and icons
- MongoDB Atlas for a cloud-based database service
- Google Chrome - for browser use and the use of development tools
- The Google search engine - was used for research.
- Links to JQuery and JS scripts
- GitHub - repository hosted on Github 
- GItpod: was used as a cloud IDE solution
- Heroku for site deployment & hosting
- Am I responsive - was used for testing responsiveness of the website
- https://validator.w3.org - was used to validate the CSS and HTML code used

##Testing
While constructing the website, the initial responsiveness was tested within the Gitpod IDE, which links to the Google Chrome browser, where development tools were used.
After this, Am I responsive was used to test responsiveness.
Also, the HTML and CSS code was validated using; https://validator.w3.org. 

## Deployment
The settings for the mongo DB are set in the env.py file. It contains a string with the username and password and a reference to the database name, used for the construction of the app. This file is not uploaded to GitHub, to keep the information secure after deployment. After finishing the pages in Gitpod, the project was deployed using Heroku. 
To make this deployment possible the following steps need to be followed:
- The Heroku account needs to be linked to the GitHub repository.
- The following 2 files need to be present in the Root structure before deployment action: 
1)requirements.txt (containing dependencies)
2)Procfile
- The Config Vars under settings need to be set with the following keys:
 IP (in this case 0.0.0.0)
 PORT (in this case 8080)
 MONGO_URI (the key needed to access the MongoDB Atlas service)
-- If the right files are present and the Config Vars are set the master branch can be successfully deployed.

## Credits for Content & Acknowledgements
- All inspirational credit go to the course material and in particular the mini-project at the end of the Data-Centric Development module.


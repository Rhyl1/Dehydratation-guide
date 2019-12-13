## The Dehydratation guide. 
This site was put together for the Code Institue milestone project nr. 3.
It offers a reference for times and temperatures to dry food in food dehydrators.

### UX
The game is made to be played in full-screen mode.
Start the game by clicking the <START> button in the screen.
After this random letters will appear; the user can score 20 points for each matched letter.
To stop the game the user can press the <ESC> button. After stopping the game the START menu will re-appear. 
The About button in the start menu links to an ABOUT info screen, explaining the working of the game.
<![alt](https://github.com/Rhyl1/projectII_game/blob/4b7e8865d7b586ac6ac11cce08ac2036256cbf0b/img/startscrn.png)>
- See following link for wireframes (included in the root structure img folder): 
(https://github.com/Rhyl1/projectII_game/blob/a336cc4f5f47e2d04dbcb2eeea74ff36ec1dabff/img/Wireframe_typegame.pdf)

#### Users
The users of the website include people looking for information about drying food in food hydrators.

#### Features
##### Existing Features
- Start button -- This button starts the game
- About button -- This button links to an info screen, explaining the game
- Score counter -- Appears after the game starts and shows the current score
- Random generated letter bubbles -- These are the main feature of the game and need to be matched by typing the corresponding key for them to disappear from the screen and gain points.

##### Features Left to Implement
- Logging of the user name.
- Logging of the user scores.
- Access to a high score list via the start menu.
- A level up function for increased difficulty.

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
The settings for the mongo DB are set in the app.py file. It contains a string with the username and password and a reference to the database name, used for the apps construction. This file is 
not uploaded to github, to keep the information secure after deployment.

The pages where deployed by activating the GitHub pages on GitHub. This process makes the website accessible for user via the internet
## Credits for Content & Acknowledgements
- All props go to Riva Tamada who got me started on this game, via his free tutorial (https://www.9lessons.info/2010/12/typing-game-with-jquery.html)

- Also Anathol for his inspiring game turoials.

- CSS3 Patterns Gallery is used for background CSS styling:
https://leaverou.github.io/css3patterns/#cross-dots
pattern startpage & game is Upholstry by Nate Eagle.
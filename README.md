# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)


## Cloud IDE Reminders

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In the terminal, run `heroku_config`
5. Paste in your API key when asked


You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.


## Dataset Content
* I borrow a data set from a Youtuber named Dataquest. Inside this dataset there was data about every country that took a part and competet in the Olympics games. 


## Business Requirements
* This year sweden want's to win as much medals as possible and with the data I have collected I am going to analys what the best strateige to get as much medals as possible. 


## Hypothesis and how to validate?
* So to get some type of understanding how we should strategies when we send athletes to OS, we need to look at numbers. One of my hypothesis is that people that are younger wins more medals, but the countrys that send most athletes win the most.  


## The rationale to map the business requirements to the Data Visualizations and ML tasks
* The first thing i need to do is to get the data to my workspace eather through kaggle or local from my computer. Then i need to clean the data and through away all columns with NAN. Then I can start to compare the amount of medals compared to for exampel what year the OS was held or where it was. For exampel if we see an increase of medals for france this year, what could that mean? 


## ML Business Case
* The goal with the ML is for Sweden to decide who they should send to OS, I am going to study further with this concept becuase I am intrested if ethnicity matter. For exampel if a half norwigen and half swedish have higher chanse of winning a medal in norway. 


## Dashboard Design
* For the user there is right now two input fields, one for country and one for year. With the help of that a user can search for USA or Afghanistan 2030 and the ml will predict the amount of medals they will get. 



## Unfixed Bugs
* I have a pretty difficult bug wich is no matter the country i input, if it is before 2016 I will only get this message "The predicted number of medals for Zimbabwe in 2016 is 142.4127678192977" 
* * And I have 0 clue where the machine get's those numbers from. 

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.


## Main Data Analysis and Machine Learning Libraries
* I downloaded a set from Kaggle. 


## Credits 

* I want to give a shoutout to the youtube channle Dataquest for the csv file and data set and tutorial how to create an LinnearRegression ML  

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site



## Acknowledgements (optional)
* I want to give a shoutout to the youtube channle Dataquest for the csv file and data set


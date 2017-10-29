# Specification Document - _xAI Vision_ #
<center>Yotam Salmon &amp; Shai Kimhi</center>

## Features and main processes ##

### Adding a category ###

**The GUI-demo version** of *xAI Vision* will provide a form to add a new category. The simple form will have a text-box, in which the user would enter a category id, and a second text-box in which the user would enter the category's preview name. Beneath that will be a button to add the category. The software will check that there the same category id does not exist yet, and if so - an error message will be shown. Otherwise, the system will add the category to the storage and redirect the user to the main form.

**On the API version**, a function will be specified to create a new category `classifier.add_category(id : string, name : string) : void`. The REST API would provide a `POST` request option to  `/categories/add` **internal*** endpoint to remotely add a category.

**The web interface** for the REST api would hold a form to enter a category, same UI as the demo version. Differene is that the web based version adds the category globally, and the demo version adds it locally.

*not accessible for developers to use. The public API would not provide a way to add a category for safety.

### Adding an image to a category ###

**The GUI demo-version** would provide a form to insert single/multiple images and classify them for a specific category. The form will contain a file input for an image.
If one image is selected, an autocompletion checkbox and a listbox will appear, allowing the user to enter multiple categories from the existing ones. If more than one image is selected,
the user will be able to select a common category to apply those images to. After clicking a "finish" button, the software will train the network using that image.

**The API version** will sign a function `classifier.sign_category(image : image, category : string) : void` and an overload `classifier.sign_category(image : image, categories: string[]) : void` that will take an image and category/ies and will train the network using the image.

**In the web version** there will be a form similar to the form of the local network to upload a single image or multiple images. Additionally, there will be a form with an option to receive a random image and apply tags to it. 

### Clasifying an image ###

**In the GUI demo-version**, there will be a form with an option to submit an image. Once an image is uploaded, a table will appear below it, stating the most relevant categories classified for it and the confidence about each of the categories (a number between 0 and 1 representing the possibility for a correct answer).

**The API version** will provide a function `classifier.classify(image : image) : dict`, that will return a dictionary with the categories as the keys and the confidence levels as the values.

**The web version** will be exactly like the GUI demo version.

### Mass classifying ###

_xAI Vision_ will have a little game, in the form of a mobile application. The purpose of the game is to create a rich set of categories and classifiers for the API. Multiple players will simultaneously be given images and would have to enter what they think the others are thinking about. The more categories they got in common, the more points they achieve. That will help us classify random images from the internet to categories we already know, and will create a rich metadata of classifiers. More information about the game's GUI in the UI visualization section.

Features it will have:
+ Login and registration system
+ Cash system with profile options
+ Random game
+ Cosmetic shop

### Login screen ###

A screen featuring a login form with a Facebook authentication logo. On the top, the logo of the application will appear. Below it, 2 text-boxes, `Username` and `Password` that will require the user's information. Below, a `Login` button. On correct login credentials, will be transferred to the main app form. On incorrect credentials, a notification will pop, announcing that an error occured. 

The login form will also feature a Facebook login button, that will automatically sign the user in using their Facebook credentials or account.

Below everything, there will be a Label titled _Don't have an account? Sign up!_ that on click will transfer the user to the sign up page.

### Registration screen ###

Will list textboxes as `Username`, `Password`, `Password confirmation`, `Email`, and a `Country` combobox. Below there will be a registration button. On incorrect information submission, will alert an error message. Otherwise, will add the user to the storage and redirect the user to the email verification process.

Information requirements: 
+ Username must be at least 8 characters
+ Username can be at max 30 characters
+ Password must be at least 8 characters
+ Password can be at max 50 characters
+ Password must contain a number
+ Password must contain an uppercase letter
+ Password must contain a lowercase letter
+ Password confirmation must be the same as the password
+ The email must be a valid email address
+ The Country combobox must hold an existing country

### Main Screen ###

The main screen will have 3 buttons: `Play`, `Store` and `Profile`. Play will redirect to the game screen, Store will show the store panel, and Profile will allow the user to edit their profile settings, chaning their profile picture, etc. (in the profile screen).

Below there will be the image of the player, and below it a red button titled 'Log out', that will sign the user out of the application and take the user back to the login screen.

### Play Screen ###

More to be detailed about that later. Can be seen in the UI visualisation section_


## User interface visualisation ##

### WF version ###

**Adding an image to a category**

![Uploading a picture](https://github.com/yotam180/xAI/blob/master/docs/xAI%20Vision/images/Uploading%20Picture.PNG?raw=true)


**Verifying images from the internet**

![Downloading a picture](https://github.com/yotam180/xAI/blob/master/docs/xAI%20Vision/images/Download1.PNG?raw=true)

![Downloading a picture](https://github.com/yotam180/xAI/blob/master/docs/xAI%20Vision/images/Download2.PNG?raw=true)

**Adding a category**

![Setting a Catagory](https://github.com/yotam180/xAI/blob/master/docs/xAI%20Vision/images/AddCatagory.PNG?raw=true)

**Clasifying an image**

![Testing](https://github.com/yotam180/xAI/blob/master/docs/xAI%20Vision/images/Test.PNG?raw=true)

### Application ###

**Login screen**

![Login screen](https://raw.githubusercontent.com/yotam180/xAI/master/docs/xAI%20Vision/images/first_form.png)

**Sign up process**

![Sign up](https://raw.githubusercontent.com/yotam180/xAI/master/docs/xAI%20Vision/images/signup.png)

**Main screen**

![Main screen](https://raw.githubusercontent.com/yotam180/xAI/master/docs/xAI%20Vision/images/main_form.png)

**Play screen**

![Play screen](https://raw.githubusercontent.com/yotam180/xAI/master/docs/xAI%20Vision/images/play.png)

## Non-functional requirements ##

### For using the GUI interface ###

1. .NET Framework (possible with .NET Core)
2. Internet Connection

### For using the API ###

1. Python 2.7/3 **OR** C++ **OR** .Net Framework
2. Internet Connection (for REST API calls)

### For the web interface ###

1. Browser (with HTML 5 and JavaScript support)
2. Internet Connection

### For the application ###

1. Android 4 or better* (TBD)
2. Some free space on the disc
3. Internet connection
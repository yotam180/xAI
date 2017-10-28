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

_More to be detailed about that later_


## User interface visualization ##

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

1. .NET Framework
2. Internet Connection

### For using the API ###

1. Python 2.7/3 **OR** C++ **OR** .Net Framework
2. Internet Connection (for REST API calls)
3. Windows OS (for C++ and .NET versions of the API)

### For the web interface ###

1. Browser
2. Internet Connection

### For the application ###

1. Android 4 or better* (TBD)
2. Some free space on the disc
3. Internet connection
# Specification Document - _xAI Vision_ #
<center>Yotam Salmon &amp; Shai Kimhi</center>

## Features and main processes ##

### Adding a category ###

**The GUI-demo version** of *xAI Vision* will provide a form to add a new category. The simple form will have a text-box, in which the user would enter a category id, and a second text-box in which the user would enter the category's preview name. Beneath that will be a button to add the category. The software will check that there the same category id does not exist yet, and if so - an error message will be shown. Otherwise, the system will add the category to the storage and redirect the user to the main form.

**On the API version**, a function will be specified to create a new category `classifier.add_category(id : string, name : string);`. The REST API would provide a `POST` request option to  `/categories/add` **internal*** endpoint to remotely add a category.

**The web interface** for the REST api would hold a form to enter a category, same UI as the demo version. Differene is that the web based version adds the category globally, and the demo version adds it locally.

*not accessible for developers to use. The public API would not provide a way to add a category for safety.

### Adding an image to a category ###

**The GUI demo-version** would provide a form to insert single/multiple images and classify them for a specific category. The form will contain a file input for an image.
If one image is selected, an autocompletion checkbox and a listbox will appear, allowing the user to enter multiple categories from the existing ones. If more than one image is selected,
the user will be able to select a common category to apply those images to. After clicking a "finish" button, the software will train the network using that image.

**The API version** will sign a function `classifier.sign_category(image : image, category : string)` and an overload `classifier.sign_category(image : image, categories: string[])` that will take an image and category/ies and will train the network using the image.

**In the web version** there will be a form similar to the form of the local network to upload a single image or multiple images. Additionally, there will be a form with an option to receive a random image and apply tags to it. 

### Clasifying an image ###

****

## User interface visualization ##

[ Enter GUI images and docs here ]

## Non-functional requirements ##

[ Enter here ]
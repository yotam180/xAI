# Specification Document - Part 1 #
<center>Yotam Salmon &amp; Shai Kimhi</center>

## Features and main processes ##

### Adding a category ###

**The GUI-demo version** of *xAI Vision* will provide a form to add a new category. The simple form will have a text-box, in which the user would enter a category id, and a second text-box in which the user would enter the category's preview name. Beneath that will be a button to add the category. The software will check that there the same category id does not exist yet, and if so - an error message will be shown. Otherwise, the system will add the category to the storage and redirect the user to the main form.

**On the API version**, a function will be specified to create a new category `add_category(id : string, name : string);`. The REST API would provide a `POST` request option to  `/categories/add` **internal*** endpoint to remotely add a category.

**The web interface** for the REST api would hold a form to enter a category, same UI as the demo version. Differene is that the web based version adds the category globally, and the demo version adds it locally.

*not accessible for developers to use. The public API would not provide a way to add a category for safety.

### Adding an image to a category ###

**The GUI demo-version** would provide a form to insert single/multiple images and classify them for a specific category. // Todo: finish this section

## User interface visualization ##

[ Enter GUI images and docs here ]

## Non-functional requirements ##

[ Enter here ]
# How to build a random website quickly

# The HTML + Python Life

## The Front End
This is the pretty part.

### Start with a static web template
* Look through the deck of free website templates at [HTML5 UP!](https://html5up.net) and find what you want.
* Download the one you want and edit the `index.html` look how you want.


#### Editing HTML, Javascript & CSS
This is scary and hard. 
Use the chrome inspector tool to find what parts of html to edit. 
Don't mess with the Javascript, it's making things interactive and reactive. 
Everything under the sun in CSS has been done. 
Always add CSS rather than take it away.


## The Back End
### Get a flask instance going

You can now replace stuff in the static html with `{{variable}}` which can then be passed into the route function call of Flask.
 
### Getting your domain
Email `help@media.m(...)` asking for your exact domain (e.g. example.media.mit.edu). 
Ask for a VM and ask to have it for 24 months (or however long you need).

 
### Removing the PORT (so that it looks legit)

Just follow exactly [this](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04). 
WSGI is a mystery and you don't need to perfectly understand it.


# The React Life
React, Solid, Svelte, and so many more. These are the modern javascript libraries that will serve as your full front end. 
They can be deployed in simmilar ways to python flask apps.


# Databases
You could have a backend SQL databased that you connect to with via Python or React (or whatever)
Or you could just use Google Sheets as your backend. There are python and react packages or 
you can sing JQuery you can change your html without messing too much.


# Other Stuff
* [TailwindCSS](https://tailwindcss.com) is a great way to add style without messing too much with html. This pairs really nice with any html. There are lot's of [templates and resources](https://www.tailwindtoolbox.com) you can use as well.
* Keep all your credentials in some `creds.?` file and put that in your `.gitignore`.
* You should think about the cyber security at some point. Maybe ask someone about that.


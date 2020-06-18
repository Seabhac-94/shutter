# Shutter

## Description
Shutter is an Irish company website and e-commerce store. It allows users to purchase products off of the online store,
as well as view and apply for job vacancies in the company.

## UX

#### Design Considerations
1. Images - The home image is chosen as it is a sterotypical representation of Ireland.
2. Font - Architects Daughter was chosen as the main font, as it strongly resembles fonts used in sterotypical Irish
tourist products, such as Wacky Woollies, a highly successful Irish merchandise company.
3. Careers Section font - Roboto is used as the font in the careers section. This is because the careers section is to have a more professional
feel, using a scribbled font seemed unprofessional, and could potentially steer applicants from th page.
4. Text transform - except in the case of the careers section, and for the same reasons, text-transform:lowercase was
used. It gives a more relaxed feel on the website, and once again, plays into the sterotypical Irish/casual personality of the company.
Cart/Checkout - Taking note from the standard e-commerce website, the cart and checkout pages layout were designed to be easily readable.

## Features

#### Existing Features
1. Register/Login/Logout Service - Allows user to have personal account on site and restricts checkout without one.
2. Products/Collections - All products are assigned a type, Still Life, Nature, etc.., this allows each type to be viewed individually, or as a whole, depending on what the user wants.
3. Careers - a fully functional careers section, where the company can post jobs through Django admin, and the are displayed on the site, where applicants can fill out a application form, and it will be viewed through Django admin.
4. Add to cart/checkout - Utilizing stripe(for checkout), the user can add products to a cart, amend the quantities and checkout using a standard payment form.
5. homepage messages indicating succesful registration/login/logout or purchasing information.

#### Possible Future Features
1. Reviews section - Allow users to post reviews on the company
2. Booking service. Allow users to book the company for product photography shoots.

## Technologies/Frameworks
1. HTML5 
2. CSS3
3. JavaScript
4. <a target="_blank" href='https://www.python.org/'>Python</a>
5. <a href="https://www.djangoproject.com/">Django Frameworks</a>
6. Postgres SQL
7. <a target="_blank" href='https://getbootstrap.com/'>Bootstrap</a>
8. <a target="_blank" href='https://fontawesome.com/'>Font Awesome</a>


## Testing
This site was developed through constant testing of functionality. The below tests are a record of the process from initial code, to testing, debugging, to retesting.

##### Register function
No issues were found intitally.

##### Login/Logout function
No issues were found intitally.

#####  Reset password
Throws an error ifemail domain is not gmail. Removed fform site until the problem is fully recitfied.

##### Product App
Initial problems, tables were not showing in django-admin. Problem - model wasn't registered in admin.py.

##### Add to cart
Initial problems, thorwing int() error when adding to cart. Problem - method on form wasn't set to POST.

##### Careers App
Initial problems - Forms were not being sent to django-admin. On inspection, method and action were not defined in the form. Once the issue was fixed, the form was tested and found working.

##### Testing Procedure for Responsiveness

1. Developer tools was opened and the above tests were completed on a number of different platforms including iPhone 5/SE, iPhone 6/7/8, iPAd, iPad Pro, iPad Mini, Galaxy S5, Pixel 2, Pixel 2XL. Along with this, standard settings form the size bar were selcted, i.e; Mobile S/M/L, Tablet, Laptop & Laptop L.
2. For each device, the site was checked to enure there was no overlap of information and that the presentation looked well.

#

## Deployment

#### Libraries to be installed
- Refer to requirements.txt

#### Creating a requirements.txt and Procfile

1. In CLI input pip3 freeze --local > requirements.txt . This should generate a file with all tools listed and they're version number.
2. Procfile - in CLI input echo web: python app.py > Procfile

#### Creating an app on Heroku
1. Create account with Heroku.
2. Select "New" then "Create new app"
3. Input app-name and region (Europe in this case)
4. Follow steps for "Deploy using Heroku Git" (push from CLI, described below)
5. Set Config vars (described below)

#### Creating a databse on Heroku
1. Heroku > Resources > New add on
2. type postgres and select Heroku Postgres
3. take url from config
4. env
5. 

ISSUES
<br>
issue - a previous migration in products was throwing an error for maximum value allowed, this was fixed by destroying old migrations, this then threw a django error for django.migrations module not being available, django was reinstalled, migrations worked on local server, however on the Postgres, it was still throwing an error, the old Postgres databse was deleted and a new one installed, after this the issue was fixed.


##### Push to Heroku
1. First, ensure requirements.txt and Procfile are configured.
2. In temrinal window, run "heroku login"
3. Press and key to be redirected to Heroku Login page, select "Login in to Heroku CLI"
4. Return back to Terminal, Herok ushould be logged in, run the command "git push heroku master".
5. Once successfully completed, " https://APPNAME.herokuapp.com/ deployed to Heroku" will be available in terminal window, you can follow this link to view your application.

##### Set config vars on Heroku
1. From your app dashboard, select settings.
2. In settings, select "Reveal config vars"
3. The following need to be configured;


##### Final steps

## Credits

#### Sources
All photos were taken by Zac Allen and Aoife Higgins. All site copy was written by Zac Allen.
[![Build Status](https://travis-ci.org/Seabhac-94/shutter.svg?branch=master)](https://travis-ci.org/Seabhac-94/shutter)

# Shutter

## Description
Shutter is an Irish company website and e-commerce store. It allows users to purchase products off of the online store,
as well as view and apply for job vacancies in the company.
<br>
The full site is deployed at <a href="https://shutter-ecommerce.herokuapp.com/">Shutter</a>

### Using the site

1. Create Account
2. Navigate to products, add product to cart
3. When in checkout use the following card details to simulate purchase:
- Card Number : 4242424242424242  Exp: 01/2021 CCV: 100
4. Navigate to careers section - click apply
5. Fill out form to apply for position 

## UX

#### Design Considerations
1. Images - The home image is chosen as it is a sterotypical representation of Ireland.
2. Font - Architects Daughter was chosen as the main font, as it strongly resembles fonts used in sterotypical Irish
tourist products, such as Wacky Woollies, a highly successful Irish merchandise company.
3. Careers Section font - Roboto is used as the font in the careers section. This is because the careers section is to
have a more professional
feel, using a scribbled font seemed unprofessional, and could potentially steer applicants from th page.
4. Text transform - except in the case of the careers section, and for the same reasons, text-transform:lowercase was
used. It gives a more relaxed feel on the website, and once again, plays into the sterotypical Irish/casual personality
of the company.
Cart/Checkout - Taking note from the standard e-commerce website, the cart and checkout pages layout were designed to be
easily readable.

## Features

#### Existing Features
1. Register/Login/Logout Service - Allows user to have personal account on site and restricts checkout without one.
2. Products/Collections - All products are assigned a type, Still Life, Nature, etc.., this allows each type to be
viewed individually, or as a whole, depending on what the user wants.
3. Careers - a fully functional careers section, where the company can post jobs through Django admin, and the are
displayed on the site, where applicants can fill out a application form, and it will be viewed through Django admin.
4. Add to cart/checkout - Utilizing stripe(for checkout), the user can add products to a cart, amend the quantities and
checkout using a standard payment form.
5. Homepage messages indicating succesful registration/login/logout or purchasing information.

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
This site was developed through constant testing of functionality. The below tests are a record of the process from
initial code, to testing, debugging, to retesting.

##### Register function
No issues were found intitally.

##### Login/Logout function
No issues were found intitally.

##### Reset password
Throws an error ifemail domain is not gmail. Removed fform site until the problem is fully recitfied.

##### Product App
Initial problems, tables were not showing in django-admin. Problem - model wasn't registered in admin.py.

##### Add to cart
Initial problems, thorwing int() error when adding to cart. Problem - method on form wasn't set to POST.

##### Checkout
No issues initally - the stripe test card was used to simulate payment.

##### Careers App
Initial problems - Forms were not being sent to django-admin. On inspection, method and action were not defined in the
form. Once the issue was fixed, the form was tested and found working.

##### Testing Procedure for Responsiveness

1. Developer tools was opened and the above tests were completed on a number of different platforms including iPhone
5/SE, iPhone 6/7/8, iPAd, iPad Pro, iPad Mini, Galaxy S5, Pixel 2, Pixel 2XL. Along with this, standard settings form
the size bar were selcted, i.e; Mobile S/M/L, Tablet, Laptop & Laptop L.
2. For each device, the site was checked to enure there was no overlap of information and that the presentation looked
well.

#

## Deployment

#### Libraries to be installed
- Refer to requirements.txt

#### Creating a requirements.txt and Procfile

1. In CLI input pip3 freeze --local > requirements.txt . This should generate a file with all tools listed and they're
version number.
2. Procfile - in CLI input echo web: python app.py > Procfile

#### Creating an app on Heroku
1. Create account with Heroku.
2. Select "New" then "Create new app"
3. Input app-name and region (Europe in this case)
4. Set up Postgres DB (detailed below)
4. Follow steps for "Deploy using Heroku Git" (push from CLI, described below)
5. Set Config vars (described below)

#### Creating a databse on Heroku
1. In Heroku, select "Resources"
2. Select New Addon, type postgres and select Heroku Postgres
3. Navigate to Settings, reveal ConfigVars, and copy the DATABASE_URL
4. In your IDE, navigate to your env file and insert os.environ.setdefault("DATABASE_URL", "database url inserted here")
5. Navigate to settings.py, comment out current DATABASES, and replace with DATABASES = {'default':
dj_database_url.parse(os.environ.get('DATABASE_URL'))}, later this is changed to select the .sqlite db if DATABSE_URL
isn't available.
6. Run python3 mange.py make migrations
7. Run python3 manage.py migrate
8. Issues (see below)
9. Create superuser for new db
##### Issues that arose with migration to postgres db
- On running the migration the the postgres db, an error was thrown for a previous migration in products was throwing an
error for maximum value allowed
- The error indicated there had been a problem with a specific migration, namely, the product_id model.
- Attempted to remove the product_id from the product, but the error was still showing.
- Deleted all migrations, and .sqlite, except __init__.py files in the migtations folder and the error changed to a
dependency error.
- Deleted the __pycache__ and attempted again, this time a django error was thrown for django.migrations module not
being available.
- Django was uninstalled from virtualenv and reinstalled - migrations now worked on local db.
- Migrations were not working on postgres db, on inspection, it was because there was already tables created in the
postgres db, that interfered with the current migrations.
- The postgres db was deleted, as it had not been used yet, and recreated.
- On recreation, the migrations ran smoothly and everything was aligned.

#### Creating a S3 bucket on AWS
1. Navigate to amazon web services, and create new account or log in.
2. Create new S3 bucket - give public access
3. Set CORS Configuration and bucket policy
4. In AWS IAM, create a new group, and then create a new policy
5. Policy should be S3 Full Access
6. Add this policy to the group
7. Create a new user, and allow programatic access
8. **IMPORTANT** - download csv file and store it.
9. In S3, test by uploading file.

#### Add S3 to Django
1. Install django-storages and boto3
2. Set AWS parameters in settings.py
3. Run python3 manage.py collectstatic -> yes.
4. Open app and refresh, the static images/css should load.
5. On AWS - the static files and folders will be available.

#### Travis CI
1. Open travis, select project from Github
2. In project, set up travis.yml
3. Take link from 'markdown' in travis and paste it into README.md
4. Build should begin.

##### Issues

1. Module not found 'env'
 - commented out import env file as it is not used once app is on web
2. Module not found 'storages'
- Checked the INSTALLED_APPS, storages was present, so pip3 install django-storages was run, ensuring it was inside the virtualenv, requirements.txt updated. Build now passed.

#### Push to Heroku
1. First, ensure requirements.txt and Procfile are configured.
2. In Heroku, in Deploy tab, select your app to deploy from Github.
3. Add shutter-ecommerce.herokuapp.com/ to ALLOWED_HOSTS
4. Once successfully completed, "https://shutter-ecommerce.herokuapp.com/" deployed to Heroku" will be available in terminal
window, you can follow this link to view your application.

##### Set config vars on Heroku
1. From your app dashboard, select settings.
2. In settings, select "Reveal config vars"
3. The following need to be configured;

<table style="width=100%">
    <tr style="border:solid 1px">
        <th>Config Vars</th>
        <th>Key</th>
    </tr>
    <tr>
        <td style="border:solid 1px">SECRET KEY</td>
        <td style="border:solid 1px"> Defined when Django project is started</td> 
    </tr>
    <tr>       
        <td style="border:solid 1px">STRIPE PUBLISHABLE</td>
        <td style="border:solid 1px"> Defined when Stripe is configured</td>
    </tr>
    <tr>       
        <td style="border:solid 1px">STRIPE SECRET</td>
        <td style="border:solid 1px"> Defined when Stripe is configured</td>
    </tr>
    <tr>       
        <td style="border:solid 1px">DATABASE URL</td>
        <td style="border:solid 1px"> Defined when Postgres SQL is added to app</td>
    </tr>
    <tr>       
        <td style="border:solid 1px">AWS ACCESS KEY ID</td>
        <td style="border:solid 1px"> Defined in new_credentials.csv file</td>
    </tr>
    <tr>       
        <td style="border:solid 1px">AWS SECRET ACCESS KEY</td>
        <td style="border:solid 1px"> Defined in .csv file downloaded AWS</td>
    </tr>
</table>


##### Final steps

1. Set Debug = False in settings.py
2. Repeat all tests done on development server on Heroku platform

## Credits

#### Sources
All photos were taken by Zac Allen and Aoife Higgins. All site copy was written by Zac Allen.
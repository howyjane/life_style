# Yogalifestyle

# 4th Coding Project:  Code Institute Full Stack Project

This is my 4th coding project. In this project I created a YOGA website applying the CRUD principles. The website offers users a platform to browse suitable yoga classes and make immediate purchase of the classes that interest them.
We are currently offering 6 different yoga programs and 3 class passes. Users can either purchase class passes or individual classes based on their needs.
A search tool is created for users to filter by class title, schedule and instructor. The classes are conducted by 3 instructors who are the owners of the yoga studio. Users can read more about their profiles and choose the classes based on their own preference.
The classes are conducted in small groups and the instructors pace the classes based on each individual's core strengths and weaknesses.
This is a responsive website and the design is simple and easy to use. At the same time, the tools that I have created will respond to the user’s actions and displays information based on users’ requests.


## Project Strategy and Scope
The key intention of this project is to create a website to showcase our instructors and yoga classes whereby users can easily access the website for class details and schedule and register for a class instantly. 
The website is designed in a way that users have to register and login before they can purchase classes. Based on the CRUD principles, our instructors/owners of the studio who can login as superusers to create, read, update and delete records on the website.
Students and other users are not allowed to edit in the website except for changing their user profile details i.e. first name, last name, email address, password. In this project, i use django to store the class data and user records.
As part of the design process, I have saved the wireframes in folder: /static/imagewireframes. To view the jpg images, please change size view to 20%.

### User Stories

| User Stories        | Description           | Features to implement  |
| :------------- |:-------------| :-----|
| 1      | Public User would like an easy to navigate yoga website. | To include a simple navigation bar on website.  |
| 2      | Public User would like to find out about the yoga class details, schedule and prices and schedule on a single page . | To include a page that provides all information about the classes.  |
| 3      | Public User would like to know who are the yoga instructors . | To include a brief description of the instructors on a single page.  |
| 4      | Public User would like to know to allow members to sign up and purchase for the classes. | To include user authentication for purchase of class.  |
| 5      | Public User would like to edit their purchases of a class before confirming purchase. | To include an order summary page where users can remove or edit their quantity purchase.  |
| 6      | Public User would like to read reviews of the yoga studio and instructors| To include a section for user reviews.  |
| 7      | Public User would like to know what are the payment modes available. | To link stripe at checkout page for credit card purchases.  |
| 8      | Public User would like to change their profile, reset and change password. | To include a page to edit user profile, change and reset of password.  |
| 9      | Instructors would like to update and remove class details and instructor profile. | To include a page where instructors as superusers can edit their profile and class details.  |

###(i)Overview

Based on above project strategy, I identified the following requirements:
1) The website must provide users with ease of navigation and displays information that is clear and easy to read.

2) Content Requirements

The website includes a simple landing page that displays the introducton of the yoga studio, yoga studio main features and yoga reviews. Users can either scroll down the landing page for all the reviews.

The website pages included:

## Navigation Bar (Public view)

1)Home
This is the landing page which contains 3 sections. 
First Section: An introduction of the yoga studio , core features of our yoga studio and student reviews.

2)Classes
This features a dropdown list for users to buy classes, list of class passes, search of classes.
Purpose is for easy access where users can filter and browse for classes that are offered by the yoga studio.

3)Instructors
This page contains instructors profile where users can read about our instructors background and experiences.

4)Register
This is a link to new users registration where users creates an account by completing the form with personal details:
(first name, last name, email address). Using the form to create a new username and password to access our website to purchase yoga classes.

5)Login
This is a link user login menu where user enters their username and password. There is a link below the login placeholders where users can click on for password resets if required.

5)Admin
This is for purpose of admin use where superusers can access this link to create new class/class passes and perform edits/deletes of classes/class passses.

## Navigation Bar (Login as a registered user excludes superuser login)

Ther navigation bar is similar to public view except that the register link will be hidden and the naviagation will show the 'car't link and the 'login' link will change to show the login username and a dropdown list for users to edit their profile, view account details, change password and logout.

To test if the function works, please use:

Eg. User Account 
Username: mary123
First Name:mary
Last Name:lee
Email Address:howyjane@gmail.com
Password:test12345

6) Cart
This is where users can click to view their order summary of classes that they purchased.
In the cart, users can select the number of quantity that they wish to purchase for each class enrolled and if they wish to remove the classes, they may do so by clicking the 'Remove class' button.
Once users decides to puchase the classes, they may click on 'checkout' button. At checkout, users will make payment on Stride checkout page using credit card or google pay .
At the moment, this is a test account and has yet to be implemented. 

To test if stride payment is working, please use :
Card: 4242 4242 4242
Exp date: 12/23
CCV: 123

## Navigation Bar (Login as a superuser only)

Ther navigation bar is similar to public and registered users view except that the register link will be hidden and the naviagation will show the 'car't link and the 'login' link will change to show the login username and a dropdown list for users to edit their profile, view account details, change password and logout.

7) Admin (dropdown list)

This link is dedicated for superusers to create, edit/delete class/class passes. 

To test if the function works, please use:

Eg. SuperUser Account 
Username: admin123
First Name:Leigh
Last Name:Hoover
Email Address:howyjane@hotmail.com
Password:micro123457

## Create

1. Create New Class - A page that contains an “create new class” form where superusers can input class details  according to each field and add the class to the platform.

## Read

1. Buy Classes and Class Pass Link under 'Classes' on the nav menu bar – shows all yoga classes that are availabe for purchase.

2. Search Classes - A page that contains 3 search dropdowns where users can search through the website for class , schedule and instructor information.

## Update

1. Superusers can access the 'admin' link to locate the dropdown list for edit of classes/passes.
2. Registered users can update their account profiles, change password, reset password under 'login (username)'dropdown.


## Delete

1. Superusers can access the 'admin' link to locate the dropdown list for delete of classes/passes.

## Skeleton

As part of the design process, I saved the wireframes in folder/static/imagewireframes. To view the jpg images, please change size view to 20%.

## Surface

1. Colors:

I used the colorlib template. The main colors used are white, black , turquoise since it is a yoga website.

2. Background Images / Images

I used website: unsplash.com to perform a search 'yoga' for images in my website.
'Our Yoga Feature' icons are taken from colorlib template.

3. Typeface

Throughout the site, i used the colorlib template. Please refer to style.css for the different fonts used.

4. Interactions

Created several forms i.e. create class, class pass forms and edit / delete forms for superusers to create, update class information and upload images that are advertised on the website.
Created user profile form for all registered user to update their account profile, change and reset password.
Created dynamic authentication navigation menu where registered users can't view the admin dashboard and only registered user can purhcase classes on the website.

###(ii) Wireframes

As part of the design process, I saved the wireframes in folder/static/imagewireframes. To view the jpg images, please change size view to 20%.

## Project Skeleton
### (i) Existing Features

1. Created a simple homepage layout to introduce our yoga studio , core features and student reviews.
2. Public Users can easily access yoga classes / passes that are available for purchase on 1 single page.
3. Created search dropdown list for public and registered users to locate classes, class schedule and instructors.
4. Registered users can update their account profie, change and reset password according to their needs.
5. Registered Users can refer to the 'cart' page where they can review their registered class titles, class cost and grand total before checkout.
6. Registered Users can select the quantity of classes that they wish to purchase on the cart summary page before checkout.
7. Registered Users can find out more about the instructors from the instructors page.
8. Created easy navigation for superusers to locate each record and link the edit and delete function on each class record page.
9. Superusers can upload a new class image that best represents each class conducted. 
10. Superusers can create a new record or edit an existing by completing a simple to use form. 
11. All pages have been written with semantic HTML in mind.
12. Fixed Scroll to Top: Each page has a fixed scroll to top, for ease of navigation.
13. Responsive nav bar menu bar is created for mobile users.
14. Responsive Design: Site pages are designed to work on all sizes of device.

### (ii) Features to implement in the future

1. To implement a function for registsered users to purchase class pass directly from the class pass page.
2. To implement and create a form for superusers to create instructor profie.
3. To implement and create a form for registered users to create student reviews.
4. To implement and create form for registered users to create/edit/delete student reviews.
5. To improve on the stride checkout payment page.
6. To include quantity selection on "buy classes" page instead of cart summary page.
7. To implement and include order history in registered user account.
8. To improve on the cart summary mobile responsive layout.

I would also like to include more interactive elements in studio introduction page to include a video introduction and include a date picker and calender for users to locate when are the classes being conducted.

### (iii) Limitations
Several information on the website are hardcoded which i wish to implement in future using multiple django models to display 
the information in html. 

Challenges for reset password function.i managed to perform a few password resets to my hotmail account and it was working. But a few days before project submission, my sendgrid account has been deactivated. 
Please use the backend email in settings.py if you wish to test the password reset login.

There isn't an account folder in my project. I saved the account registration templates (logged_out.html, login.html, password resets htmls) in the core Django Project 4 Lifestyle path under templates/registration.

The change_password.html is saved in home/templates/home/change_password.html.

## Project Surface
### Design Choices
(i) I chose a yoga theme template from colorlib for my website . This reflects our yoga studio core features.
(ii) The colors, fonts and layout from the template best represents my yoga website. It is simple, calming and modern for a yoga website.

## Technologies


In this project the following technologies have been used:

1.  Bootstrap 4
2.  HTML
3.  CSS
4.  Inline html styling
5.  Python
6.  Django
7.  jQuery

## Testing
(i) Mobile Responsiveness

This site was tested across several mobile devices (Samsung, Huawei and Iphones) to ensure compatibility and responsiveness.

(ii) Browser Compatability

This site was tested using google chrome to ensure compatibility and responsiveness.

(v) Test Cases 

Throughout this project I have done regular testing and reloaded the pages many times after each addition and modification on cloud 9 and Heroku.

| Test Case(s)        | Description           | Outcome |
| :------------- |:-------------| :-----|
| 1      | When user clicks on home link on the top-right navigation bar, the website redirects to the home page. | Pass  |
| 2      | When user clicks on class link and buy classes, class pass, search classes by class, instructors and days on the top-right navigation bar, the website redirects to each page. | Pass  |
| 3      | When user clicks on instructors link on the top-right navigation bar, the website redirects to the instructor profile page. | Pass  |
| 4      | When user clicks on registration and login link on the top-right navigation bar, the website redirects to the registration and login form. | Pass  |
| 5      | When user clicks on buy class page and select a class to purchase , the website does not redirects to the cart but redirects back to buy class page. User clicks on cart to see the items selected| Pass  |
| 6      | When user logins to the website, the navigation bar hides registration and shows cart on the menu. | Pass  |
| 7      | When superuser logins to the website, the navigation bar will show the admin dropdown list. | Pass  |
| 8      | When registered user reviews the cart items, they can select the quantity that they wish to purchase and the order summary will show the correct subtotal of each item and grand total. | Pass  |
| 9      | When user register an account on the wesbite, it redirects them buy classes. | Pass  |
| 10     | When user login to an account on the wesbite, it redirects them buy classes. | Pass  |
| 11     | When user change their password , it redirects does not redirect them to any page but shows a message that password changed successfully.| Pass  |
| 12     | When user updates their user profile, it redirects them to the login page. | Pass  |
| 13     | The shopping cart on the righ side of the navigation bar updates the correct item count after users add their purchases. | Pass  |
| 14     | When user clicks on checkout in the cart, it redirects to the stride payment page | Pass  |
| 15     | After user clicks on payment in stride, it redirects to the website and shows checkout success | Pass  |


1. To test the functionality and usability of the site, I did a class presentation. 

Their feedback was the website was calming and the fonts on the button and links color need to change to a darker color. I change the fonts to black.

2. Testing the navigation links to ensure the pages are linked.

## Search function

Tests were carried out for each search tool ensuring that the search results display the correct results.


## Add/Update function

Created several dummy records to add/update via website and django admin. Ensuring that the records are created and updated correctly.

## Authentication function

Created several users and superusers accounts for login to my website and the navigation menu changes and hides the correct menu items correctly.
Superusers are able to view the admin create, edit/delete function.
Registered users are unable to view the admin dropdown list and after login, the cart menu appears.

## Password Reset function
Challenges for reset password function.i managed to perform a few password resets to my hotmail account and it was working. But a few days before project submission, my sendgrid account has been deactivated. 
Please use the backend email in settings.py if you wish to test the password reset login.

## Password Change function
Changed a few users password and it works.

## Bugs Discovered
CSRF token not working during user login. Need to clear cach and browing history to get it working again.

### Media 

Content & Media All content on this site is taken from through the use of cololib.

All copyrights of images and text belong to their respective owners.

1. Website layout:
https://colorlib.com/wp/template/yogalife/

2. Background and Class Image:
https://unsplash.com/


## Deployment

The site has been deployed using github and Heroku:

The app live at :

https://howyjane.github.io/life_style

https://yogalifestyle.herokuapp.com/

### Acknowledgements and Credits

Template used was desgined by Colorlib  https://colorlib.com/wp/template/yogalife/
Paul, code institue trainer for the django template walkthrough.
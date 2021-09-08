<div align="center">
<img src="static/img/logos/logo_readme.png" alt="T4H Metallica Tribute Band"/>
<br>
Brazilian METALLICA tribute band
</div>

# Overview

This is the virtual HQ of one of the most important Metallica tribute bands from South America, called THE FOUR HORSEMEN. A responsive website for those interested in finding out more about the band's history and activities, our members, merchandising, upcoming shows and taking the band to their city/country.

tribute band born in 2003, aiming to reproduce the spirit and presence of the most extraordinary band in the world, METALLICA. Underneath the passion for their style and sound, our band's restless motivation is to bring the audience the feeling of being in an authentic Metallica concert.

The aim of this web application is to strengthen our online presence, gathering all the information spread over other social media platforms and have the chance to sell band merchandising products, as well as increase show business managers interactions, offering a proper communication channel.

---
![App ScreenShot](static/img/docs/preview.png)

[Access the App here](https://t4h-portal-app.herokuapp.com/)

**Please note**: To open any links in this document in a new browser tab, please press `CTRL + Click`.

---

# Table of Contents

- [User experience](#user-experience)
  * [User Stories](#user-stories)
- [Strategy](#strategy)
- [Scope](#scope)
  * [Existing Features](#existing-features)
- [Structure](#structure)  
  * [Databases](#databases)
- [Skeleton](#skeleton)
  * [WireFrames](#wireframes)    
- [Surface](#surface)   
- [Technologies Used](#technologies-used)

### Structure

## User experience

### User Stories

- Anonymous user

  - As an anonymous user, I want to easily navigate the site and quickly find info about the band;
  - As an anonymous user, I want to navigate through a responsive app and be able to access it by mobile, tablet or desktop device nicely;
  - As an anonymous user, I want to get more details about the band, its media sources and history and consider booking the band;
  - As an anonymous user, I want to check the upcoming concert dates quickly browsing the band tour calendar;
  - As an anonymous user, I want to find the band's social media channels, so that I can start following them;
  - As an anonymous user, I want to see videos and photos and check their live performances;
  - As an anonymous user, I want to check the merchandising items and their prices, so that I can place an order and support the band;
  - As an anonymous user, I want to access contact details, so that I can get in touch to book the band;
  - As an anonymous user, I want to register for a user profile account by email and password and store details of orders history;

- Registered user

  - As a registered user, I want to log in and log out of my profile account and keep my information safe for future accesses;
  - As a registered user, I want to update my details, so that I can change my delivery address for future purchases;
  - As a registered user, I want to store my details for later use, avoiding to retype it on the next purchase;
  - As a registered user, I want to store my purchase history and check the goods delivery status;
  - As a registered user, I want to select the quantity of each product I want to order, entering the quantity of each I want to purchase;
  - As a registered user, I want to review my purchase choices at checkout, so that I can decide to add or remove products before confirming;
  - As a registered user, I want to store my choices in checkout and go back to the site in case I wish to change the options;
  - As a registered user, I want to make secure payments and ensure my payments are securely handled;
  - As a registered user, I want to receive an email confirmation of my order, so that I can confirm that my order was confirmed;
  - As a registered user, I want to log in to my profile account and keep track of my order's delivery status;

-  Site admin user.

   - As an admin user, I want to add new concert dates, so that I can keep fans updated on upcoming dates;
   - As an admin user, I want to update concert dates, so that I can update fans on existing concert dates;
   - As an admin user, I want to delete concert dates, so that I can remove concert dates cancelled;
   - As an admin user, I want to update merchandising products listing and update new items info;
   - As an admin user, I want to delete existing merchandising products listing, so that I can avoid out of stock items for customers;
   - As an admin user, I want to add new merchandising products and category listings, so that I can make new items available for purchasing;
   - As an admin user, I want to update orders delivery status, so that I can keep customers updated on the delivery of their items;

### Strategy

With over 17 years of experience consistently touring Brazil, some gigs in Latin American countries and a tour in Portugal and Spain, THE FOUR HORSEMEN has become an increasingly strong and professional live music project.

This website project comes to show we take work behind the scenes as seriously as being on the road and performing live.

The strategy of this website is to translate our stage presence, giving us a boost in the right direction by selling merch, booking concerts amd bringing potential fans and the live music industry closer to us.

#### Project Goals

Increase internet presence presenting relevant content about the band and improving its positioning in the main internet search engines. Increasing number of fans, increasing concert bookings and merchandising sales.

#### User Goals

Users can easily find info about the band, see photos and videos, purchase merch or book concerts.

### Scope

Built based on technologies such: HTML, CSS, JavaScript, Python and Django.

#### Existing Features

- Fully responsive website across all popular devices, using Bootstrap Grid and custom media queries
- Intuitive and responsive Navigation menu
- About section on Home page to read the band concept
- Shows section on Home page to read the upcoming concert dates
- Media section with an interactive lightbox with images and Youtube embedded live performance videos  
- Merch page with available band merchandise 
- Login page with form
- Profile/account page
- Checkout page
- Order history and status page
- Footer element with social media links.
- Ability for admin user to add, update and delete concert date entries.
- Ability for admin to add, update and delete stock merch entries.
- Ability for admin to update orders delivery status.


#### Future Features to Implement

- Login with other Social Media options
- Share content with other Social Media apps
- Media content manageable by Admin system
- Forgot Password feature
- Past Dates on Shows section.
- Implement further communication to the user via email for order invoices & confirmation.

### Structure

The structure is a mix of a single page application, easing the navigation to each content with section hinting for quick impact, and a multiple page application with progressive steps along the purchase process, making it easier.

#### Interaction Design and Architecture

A template with a full-width content area to layout texts, images and photos aiming straightforward navigation supported by Django apps built using bootstrap 5 Html elements
All the content is organized according to the main menu at the top, clearly presenting the user the sections sequence.

#### Databases

- [SQLite3](https://www.sqlite.org/index.html) used in Development, which comes as default with Django installation.

#### Apps and Models used

- Home App

  - The **Agenda model** stores information about the tour dates.

  - The **Product model** stores information about the band's merch.

  - The **Category model** stores information about the band's merch categories and is used in the Product model as a specific category.

- Profiles App

  - The **UserProfile** model stores information about registered users, including order history and delivery statuses.

- Checkout App

  - The **Order** model stores information about each order placed.

  - The **OrderLineItem** model stores information from the order, used in calculation in the Order model.

#### Model Relationship Data Schema

![DB Schema](docs/)

### Skeleton
  
### WireFrames

#### Anonymous Users

- [Anonymous Users Perspective](static/docs/CI_MS4_WF_AnonUser.pdf)

#### Registered Users

- [Registered Users Perspective](static/docs/CI_MS4_WF_RegUser.pdf)

#### AdminUser

- [Admin User Perspective](static/docs/CI_MS4_WF_AdminUser.pdf)

The idea is to keep it simple and straightforward, gathering info in sections on home pages and separate "stepped" pages for the purchasing process.

- Menu bar pointing to each section on home page:
  - Shows
  - Media
  - About
  - Contact
- Menu bar pointing to separate page:
  - Merch
  - My Account
  - Cart items count
  - Product admin feature
  - Shows dates admin feature

### Surface  

For clean code purposes, I chose a Bootstrap template that perfectly matches the objectives of this website idea, taking leverage of the boilerplate pre-built by [StartBootstrap](https://github.com/startbootstrap/startbootstrap-creative).

#### Colours

A colour palette tending to hot colours, favouring reading and a bold yet professional contrast.
![Colour palette](static/img/palette.png)

#### Typography

- Headings - "Merriweather Sans" font (with fall-back font of Serif). 
- Content - "Merriweather.

#### Images

All band, members, live performance images and logos are band's property represented by myself, developer responsible as well as merch images.

## Technologies Used

Designed with HTML5, CSS3, JavaScript, Python3 with the Django Framework

### Languages

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Integration

- [StartBootstrap](https://startbootstrap.com/) - Clone the repo: [git clone](https://github.com/StartBootstrap/startbootstrap-creative.git)
- [Bootstrap Icons](https://icons.getbootstrap.com/) Icons for Social Media links
- [Google Fonts](https://fonts.google.com/) - Overall Typography import
- [jQuery](https://jquery.com/) - JavaScript library
- [Django](#) Micro web framework written in Python

### Dependencies
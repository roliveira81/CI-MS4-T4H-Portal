# Table of Contents

> - [User Stories](#user-stories)
> - [Responsive Tests](#responsive-tests)
> - [Code Validation](#code-validation)
> - [Manual Site Testing](#manual-site-testing)
> - [Deployment](#deployment)

## User Stories

### Anonymous user

#### easily navigate the site

- Responsive Bootstrap menu bar with easily identifiable icons allow the user to intuitively find what they need
- All the navigation happens on the top menu bar

#### view the site on all screen sizes

- Bootstrap Grid has been used to layout the main responsive design
- Custom media queries in external CSS files ensures fine responsive details
- Focussed responsive design on popular mobile, table and laptop/desktop dimensions:
  - Mobiles: iPhone5(320px) | Samsung S5 (360px) | iPhone 6/7/8/X (375px) | iPhone 6/7/8 Plus (414px)
  - Tablets: iPad (768px) | iPad Pro (1024px)
  - Desktops: Laptop (1200px) | Large Desktop screen (1920px)

#### read about the band details, goals and aims

- Incorporated a brief, yet descriptive 'About Us' section on the home page.

#### read details about products/band's merch

- On the Merch page, each product has its description, sizes and prices.

#### read details of products purchase

- On the checkout page, the total amount of the order is clearly displayed to the user before payment is made.

#### access contact details

- Contact number displayed on Contact section.
- Contact form on contact page allows user to get in touch.

#### register for a user profile account by choosing a username and password

- If user is not logged in, simple registration is available from the Profile icon on the navigation menu.
- User has the option to enter email address, username and password to register and is sent a confirmation email to confirm registration.

#### register for a user profile account using social media login details

- User has the option to sign into a choice of social media accounts on the Log in page.

### Registered user

#### log in and log out of my profile account

- The Profile icon in the navigation menu displays whether a user is logged in or not, and allows the user to easily log in and out of their account accordingly.

#### update my details

- The user's Profile page (accessed by the Profile icon in the navigation menu) allows the user to edit and save phone number and address details.

#### store my address for later use

- Details for the phone number and address fields on the Profile page persist, regardless of user logging off or clearing browser cache.

#### store my order history

- A order history list is visible on the user's Profile page. These details persist regardless of user logging off or clearing browser cache.
- The user can follow his delivery and payment statuses.

#### review my purchase choices at checkout

- Before confirming and paying for the purchase, user has the ability to review, add or delete any products added to their cart.

#### store my choices in checkout

- Whilst navigating the site, users (including anonymous users) can add multiple products as a wish list order cart, which are all stored in the checkout whilst browsing the site. The stored data is only accessible during hte session and clears if the user logs out.

#### Make secure payments

- Payment security is handled by Stripe implementation for the payment process.

#### Receive email confirmation of my purchase payment

- Emails are not being sent, and this has been added as a Known Issue to the README document.

### Site admin/superuser

When the Admin/Superuser account is logged into:

#### add new products and category listings

- A menu is accessible from the top menu bar in the navigation menu. Under Merch Management, products can be added.

#### update products listings

- On each product card on products page, additional button is visible to the Superuser to Update a Product.

#### delete existing products listings

- On each product card on products page, additional button is visible to the Superuser to Update a Product.

#### create, update and delete Shows dates

- Under App Management, on the top menu bar, is possible to add, update and delete Shows dates for the Shows sections on home page. 

## Responsive Tests

- DevTools - Devices tested across a range of widths:

  - Mobiles: iPhone5(320px) | Samsung S5 (360px) | iPhone 6/7/8/X (375px) | iPhone 6/7/8 Plus (414px)
  - Tablets: iPad (768px) | iPad Pro (1024px)
  - Desktops: Laptop (1200px) | Large Desktop screen (1920px)

- Viewed on physical devices:

  - Mobiles: small phone (320px) | large phone (414px)
  - Tablets: large tablet (768px)
  - Desktops: Medium laptop (1366px) | Large Desktop screen (1920px)

- Viewed site on above range (including Responsive mode) on various browsers: > - Google Chrome
  - Firefox
  - Opera
  - Safari

## Code Validation

### HTML and CSS

- **Warnings**: Loads of warnings were triggered regarding StartBoostrap bolierplate used which could not be fixed.

Parsed all css code through [Autoprefixer](https://autoprefixer.github.io/) and tested validation via [Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/validator)

`style.css`, `checkout.css`

- No errors found

### JAVASCRIPT

- The main script passed through [JShint](https://jshint.com/) with just an exceptions:
  - `stripe_elements.js` returned undefined variables `Stripe`and `$`, which can be ignored as these are built into Stripe.

### PYTHON

- Installed [flake8](https://flake8.pycqa.org/en/latest/) to check errors on all Python files.
- Passed all Python files through [pep8online](http://pep8online.com/) to check [PEP8](https://www.python.org/dev/peps/pep-0008/) compliance.
- All files passed, but the following ignored:
  - `.\env.py`:10:80: E501 line too long (144 > 79 characters)
  - `.\env.py`:11:80: E501 line too long (144 > 79 characters)
  - `.\env.py`:15:29: E225 missing whitespace around operator.\env.py:15:80: E501 line too long (191 > 79 characters)..\env.py:17:1: E265 block comment should start with '# '
  - `.\env.py`:19:80: E501 line too long (80 > 79 characters)
  - `.\env.py`:21:1: E265 block comment should start with '# '
  - `.\env.py`:24:51: W292 no newline at end of file
  - `.\checkout\apps.py`:10:9: F401 'checkout.signals' imported but unused
  - `.\checkout\webhooks.py`:28:5: F841 local variable 'e' is assigned to but never used
  - `.\checkout\webhooks.py`:31:5: F841 local variable 'e' is assigned to but never used
  - `.\home\views.py`:12:4: W291 trailing whitespace
  - `.\home\views.py`:14:25: W291 trailing whitespace
  - `.\home\views.py`:29:42: W291 trailing whitespace
  - `.\home\views.py`:38:25: E127 continuation line over-indented for visual indent
  - `.\home\views.py`:39:31: W291 trailing whitespace
  - `.\home\views.py`:42:13: F541 f-string is missing placeholders
  - `.\home\views.py`:49:46: W292 no newline at end of file
  - `.\T4H_Portal\settings.py`:18:5: F401 'env' imported but unused
  - `.\T4H_Portal\settings.py`:145:80: E501 line too long (83 > 79 characters)

## Manual Site Testing

### Navigation

- Clicked on all links in Navigation menu main headings and confirmed user is directed to the desired page.
- Clicked on Logo, and Home link in the menu, from all pages and reached expected result of user being returned to the home page.
- Clicked on each Social Media icon in the Media Section and each opens relevant external page in a new browser tab.
- Confirmed that the 'back to top' button returns user to the top of the page once clicked (on all pages).

### Register page

- Clicked on Account link in the navigation menu and selected Register option, which redirects to the Registration/Sign Up page.
- Link to Login page working correctly when clicking 'sign in here' link, redirecting to the Login/Sign In page.
- Clicked 'Sign Up' button with no details and correct error message is returned for required inputs.
- Filled in form correctly and clicked 'Sign Up' button. Received email with confirmation link.
- Once clicked, I was redirected to the 'Confirm Email' page.
- Clicked on 'Confirm' button and redirected to the Log In/Sign In page with Django success message informing confirmation of email address.

### Login page

- Clicked on Account link in the navigation menu and selected Login option, which redirects to the Login page.
- Clicked 'Log in with GitHub' button and user is prompted to log in with GitHub credentials. Tested with own account and working as expected.
- Clicked 'Log in with Google' button and user is prompted to log in with Google credentials. Tested with own account and working as expected.
- Clicked 'Sign Up' link and correctly redirected to Register/Sign Up page.
- Clicked 'Sign In' button with no details and correct error message is returned for required inputs.
- Entered correct, registered username and password, and clicked 'Sign In' button. Django success message returned, informing the user is logged in, and returned to the Home page.

### Logout page

- Clicked on Account link in the navigation menu and selected Logout option, which redirects to the Logout/Sign Out page.
- Clicked the 'Cancel' button and returned to the Home page, and not logged out.
- Clicked the 'Sign Out' button and returned to the Home page, with Django success message that user is logged/signed out of the profile account.

### Home page

- Clicked on 'find out more' button in all slideshow images and each takes user to the specified filtered section page.
- All tickets links open on another screen properly in the Shows list.
- Hovered over media lightboxes in 'Media' section and the content featured opened properly.

### Merch page

- Clicked on the image, which opens the image preview in new browser tab.
- Clicked on 'See Details' button on each product, which leads to product details page.

### Product Detail page

- Clicked on 'Add to cart' button on each product, it adds the products to the user's shopping bag.
- Clicked on 'plus/minus' buttons on each product, they increase or decrease products on the user's shopping bag.

### Add Product page

- Clicked on the top menu bar in the navigation menu and confirmed that the 'Product Management' option is only visible when logged in as a SuperUser.
- Clicked 'Add Product' from the dropdown and redirected to the Add Product page.
- Tested form by clicking the 'Add Product' button with no form entries, resulting in page refresh, correct error message for required fields and form is not submitted.
- Tested functionality of 'Select an Image' button, which opens up the file upload from local machine option.
- Filled in form correctly with all fields and clicked 'Add Product' button. Redirected to the new product page with success message.
- Confirmed that all details entered, including image, is displayed in the new product added.

### Edit Product page

- Clicked on the 'Update' button with all fields correctly filled in, page refreshes with updated entries and success message is returned.
- Tested the 'Remove' checkbox on the image field, which correctly updates the Product and removes the image.

### Bag page

- Clicked on 'Remove product' button and Django success message displayed:
  - Informing the user of cart item deletion.
  - Current cart info is updated in this message.
  - Cart icon number display updates correctly.
- Removed all items in cart and default image with message to user, informing nothing is in the car, is displayed.
- Re-added multiple products to the cart:
  - purchase amounts of each product display correctly.
  - Total of all products displays correctly.
  - Order summary number displays correct amount of items in the cart.
- Clicked 'Secure Payment' button, which redirects to the Checkout page.

### Checkout page

- Tested form validity, by clicking the 'Complete Payment' button and correct errors returned if all required fields are not correctly filled in.
- Clicked 'Adjust cart' button, which redirects back to the cart and retains items in the cart.
- Correctly filled in form (with test credit card details) and clicked 'Complete Payment' button:
  - Loading screen loads as expected.
  - Order confirmation (checkout success) page is displayed with correct information about the purchase.
  - Django success message displays success message, order number and that an email has been sent.
  - Email is not received by the user - Added to README under Known Issues.
- Tested 'save billing information to my profile' checkbox by changing information, selecting the box (confirming checked) and confirmed that this changes the amended information on the Profile page.

### Order Confirmation page

- Info correctly displayed about the transaction made.
- Clicked 'Keep shopping' button and redirects correctly to 'Merch' section

### Profile page

- Tested billing info form inputs and country dropdown and all working as expected.
- Changed info and clicked on 'Update' button and changes are correctly saved to the database and displayed to the user.
- Clicked on 'View purchase confirmation' links (in the list of saved previous purchases)
  - Correctly directs to the purchase Confirmation page for each item.
  - Displays Django info message with order details.

### Contact page

- Tested form by clicking the 'Submit' button with no form entries, resulting in page refresh, correct error message for required fields and form is not submitted.
- Filled in form correctly with all fields and pressed 'Submit' button. Redirected to Home page with success message that email has been sent.
- Confirmed that email functionality is working and email is received by user.

## Deployment

- All tests above carried out on the [deployed url](https://t4h-portal-app.herokuapp.com/) to confirm the site is working as expected.
- Debug set to False in `settings.py` for final production push.
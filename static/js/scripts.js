/*!
* Start Bootstrap - Creative v7.0.4 (https://startbootstrap.com/theme/creative)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-creative/blob/master/LICENSE)
*/

window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }

        //changing to on the original script to keep navbar shrinked just at home page
        if (window.scrollY === 0 && window.location.pathname === '/') {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }
    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            offset: 74,
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });
});

//https://www.w3schools.com/howto/howto_js_scroll_to_top.asp
//Get the button:
mybutton = document.getElementById("topBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () { scrollFunction() };

function scrollFunction() {
   if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
       mybutton.style.display = "block";
   } else {
       mybutton.style.display = "none";
   }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
   document.body.scrollTop = 0; // For Safari
   document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

/*Change the nav-bar behavior to autoclose for specific <a> elements
and keep it open for dropdown menu items, triggering the jquery function
below when the element has the css class auto-hide*/
$(function(){ 
    var navMain = $(".navbar-collapse");
    navMain.on("click", "a.auto-hide:not([data-toggle])", null, function () {
        navMain.collapse('hide');
    });
});


//function to make the menu links work out of single page
if (window.location.pathname !== '/')
{
    $(document).on('click', '#navbarSupportedContent a', function(e) {
        let target = $(this).attr('href');
    
        if (target.indexOf('#home_') > -1)
        {
            target = "/" + target
            window.location.href = target;
        }
    });
}         

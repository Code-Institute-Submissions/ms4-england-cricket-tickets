## Validation

The W3C Markup and CSS Validator Services, JSHint and Python Validator were used to validate every page of the project 
to ensure there were no syntax errors in the project.

-   [W3C Markup Validator](https://validator.w3.org/) - [Results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fengland-cricket-tickets.herokuapp.com%2F)
    This same result appears across every page of the site, and the error that shows is due to the base.html template being used across the site.
    <p> <img src="html-checker.jpg">  </p> 
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - [Results](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2F8000-ed7f6852-bcc5-4712-9035-464423e5cab7.ws-eu03.gitpod.io%2Ftours%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) -  
    There is 1 property issue found when checking the site. However, these are being validated from the Materialize 
    link and therefore out of my control.
    <p> <img src="documentation/screenshots/css-validator.jpg">  </p> 
-   [JSHint](https://jshint.com/) - 
    No issues were found on this check.
    <p> <img src="documentation/screenshots/jshint.jpg"></p>      
-   [Python Validator](http://pep8online.com/)
    No issues were found on this check.
    <p> <img src="documentation/screenshots/pep8.jpg"></p>   
    

## Autoprefixer CSS Online

This was used to parse CSS and add vendor prefixes in order to ensure that the CSS styling works properly across all 
browsers. I have added the below header to my CSS styles sheet in order to show this:
<p> <img src="documentation/screenshots/css-prefixer.jpg">  </p>

## Lighthouse

<p >Desktop<img src="documentation/screenshots/lighthouse.jpg">
Mobile<img src="documentation/screenshots/lighthouse-mobile.jpg"></p>

From Chrome Developer Tools, this Lighthouse score is based on the homepage while being viewed on desktop and mobile. The 
biggest variant throughout the site is the performance score, which is predominantly due to the image link added by users 
to the site for each individual Tip, making it quite hard to control. 


## Testing User Stories from User Experience Section

-   #### First Time Visitor Goals - I want to:

    1. Quickly understand the service being provided by England Cricket Tickets and how I can interact with the service.
        - *###*
    2. Be able to easily browse the various Tours and select which match I am interested in
        - *###*
    3. Having selected match, I want to choose where I want to sit and which days I would like to attend, as well as the number of tickets.
        - *###*
    4. Use my credit card to make an online payment, and receive an email to let me know that my payment has gone through.
        - *###*
    5. Register to the website to receive any offers
        - *###*
    6. Find the answers to any questions that I may have, and contact the company if I can't find them online.
        - *###*

    
-   #### Frequent User Goals - I want to:

    As a Frequent User, I want to:
    1. Easily be able to check if any new tours have been added that may interest me.
        - *###*
    2. Login to the account that I have previously set up and see the information of the tickets I have purchased.
        - *###*
    3. Change my saved details, for example I have moved address or changed phone number.
        - *###*
    4. Buy additional tickets to the matches where I have previously bought tickets.
        - *###*
    5. Contact the company to ask any further questions.
        - *###*


-   #### Admin Goals - I want to:
   
    1. Be able to create, read, update and delete all tours, tickets and FAQs on the website.
        - *###*



## Fixed Bugs
After deployment, I found multiple bugs that needed addressing:

1. Bug 1...
    - *###*
2.  Bug 2
    - *###*  
2.  Bug 3...
    - *###*  


## Further Testing

- ###
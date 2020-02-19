# adventureBuddy

AdventureBUDDY is a service that connects adventurers with adventures. Users can search and sign up for adventures with a new buddy. Buddies can monetize their adventure knowledge by creating events for other users to join.

LANDING - on landing, users are greeted with a splash header with the site title and a simple blurb about the site’s purpose. Signup / Login prompts are displayed on the header if no session is present. Under the header is a main gallery, populated with cards depicting ‘adventures’ other users have posted. This gallery can be browsed without the user being logged in, but if the user attempts to book an adventure, they will be prompted to sign up / in.

SIGNUP - users will register with a unique username and email address, a password, and first and last names. 

LOGIN - users sign in using their username and password - logging in returns the user to the main gallery

LANDING  (when logged in) - the header is populated with links to view the user’s profile or logout. Users are now able to fully interact with adventures.

USER PROFILE - the user profile contains multiple tabs that provide different information when selected. 
 - Posts - all posts created by the user, with posts booked by other users displayed at the top, with styling that clearly indicates their booked status
 - Booked - all posts the user themself has signed up for
 - User info - contains all information regarding the current session user as well as an edit button to update the info or change their password.
 - Create post - A signed in user can create a new experience that other users can book.
 
## ADVENTURE DETAIL
An expanded view of the adventure cards, featuring more details about the event and the ability to book it. Booking an adventure takes the user to their profile’s Booked gallery. When the user clicks on a booked adventure, the ability to cancel replaces the Book option. 

## TECHNICAL REQUIREMENTS

## CRUD
C - CREATE users, experiences, and bookings
R - READ users, experiences, and bookings
U - UPDATE users, experiences, and bookings
D - DESTROY users, experiences, and bookings

## TECHNOLOGIES
- Python/Django
- Postgres SQL
- 4 data models
- User login and authentication
    - with data validation and error handling
- Views
- Semantic UI
- Responsive UI optimized for phone/tablet


## STRETCH GOALS

- Use Stripe API for payments
- Email notifications

## MILESTONES
Tuesday - Set up Django/SQL/base template (E/M)
Tuesday - Build seed file for DB. (R)
Wednesday - User & Experience Model, and Routes (M)
Wednesday - Login/signup/logout w/ authentication (E)
Thursday - Fully functioning landing page with experience rendering and search* functionality (R/M)
Friday - Fully functioning profile page (see your bookings, your offered experiences) (E/R)
Full CRUD MVP by Friday (E/M/R)

*stretchy


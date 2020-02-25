# adventureBuddy

adventureBUDDY is a service that connects adventurers with adventures. Users can search and sign up for adventures with a new buddy. Buddies can monetize their adventure knowledge by creating events for other users to join.

[adventureBUDDY on Heroku](https://adventurebuddy.herokuapp.com)


adventureBUDDY is created by

[Eric Laitala](https://github.com/elaitala) |
[Randy Rueter](https://github.com/rerueter) |
[Marco Salcedo](https://github.com/msalcedo88)

## User Story

![wireframes](/assets/wireframes.jpg)

LANDING - on landing, users are greeted with a splash header with the site title and a simple blurb about the site’s purpose. Signup / Login prompts are displayed on the header if no session is present. Under the header is a main gallery, populated with cards depicting ‘adventures’ other users have posted. This gallery can be browsed without the user being logged in, but if the user attempts to book an adventure, they will be prompted to sign up / in.

SIGNUP - users will register with a unique username and email address, a password, and first and last names.

LOGIN - users sign in using their username and password - logging in returns the user to the main gallery

LANDING (when logged in) - the header is populated with links to view the user’s profile or logout. Users are now able to fully interact with adventures.

USER PROFILE - the user profile contains multiple tabs that provide different information when selected.

- Posts - all posts created by the user, with posts booked by other users displayed at the top, with styling that clearly indicates their booked status
- Booked - all posts the user themself has signed up for
- User info - contains all information regarding the current session user as well as an edit button to update the info or change their password.
- Create post - A signed in user can create a new experience that other users can book.

### ADVENTURE DETAIL

An expanded view of the adventure cards, featuring more details about the event and the ability to book it. Booking an adventure takes the user to their profile’s Booked gallery. When the user clicks on a booked adventure, the ability to cancel replaces the Book option.

## TECHNICAL REQUIREMENTS

## CRUD

CREATE users, profiles, experiences, and bookings

READ users, profiles, experiences, and bookings

UPDATE users, profiles, experiences, and bookings

DESTROY experiences, and bookings

## TECHNOLOGIES

- Python/Django
- Postgres SQL
- JavaScript
- jQuery
- Semantic UI
- Pillow

## TODO

- integrate the Stripe payment API
- adventure.creator == request.user on adventure delete for db security

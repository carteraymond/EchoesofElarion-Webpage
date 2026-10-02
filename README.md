# Overview

Echoes of Elarion is an interactive web application built with Django and Python. The application allows users to enter an adventurer name and explore the lore of the fictional world of Elarion. As users discover new pieces of lore, they earn experience points and can eventually level up to unlock additional content.

To start the test server on a local computer, activate the Python virtual environment and run the Django development server:

```powershell
.\echoes\Scripts\Activate.ps1
python manage.py runserver
```

After starting the server, open the following website in a web browser:

```text
http://127.0.0.1:8000/
```

The application begins on the Welcome page, where the user enters their adventurer name before beginning their journey.

The purpose of writing this software is to gain practical experience developing web applications with Python and Django. This project allowed me to learn how Django handles web pages, URL routing, templates, user input, sessions, and dynamically generated content. I also wanted to build an application that could be expanded into a larger interactive experience in the future.

[Software Demo Video](http://youtube.link.goes.here)

# Web Pages

**Welcome Page**

The Welcome page is the starting point of the application. The user enters an adventurer name and submits the form. Django stores the player's name, experience points, level, and discovered lore in the user's session before sending them to the Home page.

**Home Page**

The Home page displays the player's name, current level, and experience points. It also provides an introduction to the world of Elarion and gives the player access to the Lore page.

When the player reaches Level 2, the Home page dynamically displays a new Path of History that was previously unavailable.

**Lore Page**

The Lore page allows the player to choose from several topics about the world of Elarion. The available topics include the Wells of Elarion, the War of Sundering, Nytherael, the Concordance, and the Strange Observer.

When a player selects a topic, Django dynamically displays the selected lore entry. The first time a player discovers a topic, they receive 1 XP. Discovering the same topic again does not award additional XP.

After discovering all five unique lore entries, the player reaches 5 XP and advances to Level 2.

**Path of History**

The Path of History is unlocked when the player reaches Level 2. This page provides additional historical information about Elarion and expands upon the mystery of the Strange Observer.

The page is protected by Django so that players below Level 2 cannot access it directly. Players who have not reached the required level are redirected back to the Home page.

# Development Environment

The software was developed using Visual Studio Code, Python, Django, HTML, CSS, Git, GitHub, and SQLite.

The primary programming language used was Python. Django 5.2.17 was used as the web framework for handling URL routing, views, sessions, and server-side template rendering.

HTML was used to create the structure and content of the web pages. CSS was used to style the application and provide a consistent visual design.

The application uses Django's built-in session system to store player information such as the player's name, XP, level, and discovered lore.

# Useful Websites

* [Django Documentation](https://docs.djangoproject.com/)
* [Django Templates Documentation](https://docs.djangoproject.com/en/5.2/topics/templates/)
* [Django Sessions Documentation](https://docs.djangoproject.com/en/5.2/topics/http/sessions/)
* [Django Static Files Documentation](https://docs.djangoproject.com/en/5.2/howto/static-files/)
* [Python Documentation](https://docs.python.org/3/)

# Future Work

* Add additional levels and unlockable paths.
* Add more lore entries, characters, locations, and historical events.
* Expand the Path of History into a larger interactive progression system.
* Add a database to permanently store player progression.
* Add additional interactive choices and player decisions.
* Improve the visual design with additional artwork and themed elements.
* Expand the application into a larger interactive experience based on the world of Elarion.

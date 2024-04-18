# Architecture
Django is indeed based on the MVT (Model-View-Template) architecture by default. This architecture is a software design pattern for developing web applications, where:

- Model acts as the interface of your data, maintaining data and represented by a database (generally relational databases such as MySQL, PostgreSQL).
- View is the user interface, what you see in your browser when you render a website, represented by HTML/CSS/Javascript and Jinja files.
- Template consists of static parts of the desired HTML output as well as some special syntax describing how dynamic content will be inserted.

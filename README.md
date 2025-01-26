Random Quote Generator Web App
This is a simple Flask-based web application that generates random motivational quotes using Google Generative API. Every time the user clicks the "Get New Quote" button, a new quote is fetched and displayed on the webpage.

Features
Generates new motivational quotes with every button click.
Uses Flask for backend and Google Generative API for generating content.
Simple and interactive user interface.
Requirements
Before running the app, make sure you have the following installed:

Python 3.x
pip (Python package installer)


Setup and Installation

git clone https://github.com/yourusername/random-quote-generator.git
cd random-quote-generator

How It Works
Frontend (HTML): The HTML page displays the quote and includes a button that triggers a JavaScript function. This function makes a GET request to the backend Flask API.
Backend (Flask): The Flask app handles the request for a new quote, generates the content using the Google Generative AI API, and sends the response back to the frontend.
Google Generative API: The backend uses Google's Generative AI API to fetch a new quote based on a pre-defined prompt.
Contributing
If you'd like to contribute to the project, feel free to fork the repository and make your changes. You can create a pull request once you're done.

License
This project is licensed under the MIT License - see the LICENSE file for details.
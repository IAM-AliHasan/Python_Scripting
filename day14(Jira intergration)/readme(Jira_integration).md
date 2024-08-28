Project Overview
This project is a Flask-based web application designed to automate the creation of Jira issues based on specific comments made on GitHub issues. The application listens for webhook events from GitHub and creates a Jira issue only when a comment starts with the command /jira. This ensures that only relevant comments trigger the creation of Jira issues, streamlining the workflow for development teams.

Key Features
Webhook Integration: Listens for issue comment events from GitHub using webhooks.
Conditional Issue Creation: Creates a Jira issue only when the comment starts with /jira.
REST API Interaction: Utilizes the Jira REST API to create issues programmatically.
Authentication: Secures API requests using HTTP Basic Authentication with an API token.
Flask Framework: Built using the Flask web framework for simplicity and ease of deployment.
How It Works
Webhook Setup: Configure a webhook in your GitHub repository to send issue comment events to the Flask application.
Comment Parsing: The application receives the webhook payload and extracts the comment text.
Command Check: If the comment starts with /jira, the application proceeds to create a Jira issue.
Jira Issue Creation: The application sends a POST request to the Jira REST API with the necessary issue details.
Response Handling: The application returns a success message if the issue is created, or a command not recognized message otherwise.
Technologies Used
Python: The core programming language.
Flask: A lightweight web framework for handling HTTP requests.
Requests: A simple HTTP library for making API calls.
Jira REST API: For creating issues in Jira.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.


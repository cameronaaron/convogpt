ChatApp
ChatApp is a Python application that generates responses to social interactions using OpenAI's GPT-3.5-turbo model. The application prompts the user to enter a message they received and the type of message (e.g. flirty, professional, friendly), and generates a response based on the input.

Installation
Clone the repository: git clone https://github.com/username/ChatApp.git
Install the required packages: pip install -r requirements.txt
Set the OPENAI_API_KEY environment variable to your OpenAI API key.
Usage
Run the application: python chatapp.py
Enter your user ID when prompted.
Enter the message you received when prompted.
Enter the type of message (e.g. flirty, professional, friendly) when prompted.
The application will generate a response based on the input and display it on the console.
Data Storage
The application uses a JSON file to store user data, including user profiles and conversation history. The JsonDataStore class provides methods for loading and saving data to the JSON file.

Disclaimer
This application is designed to help generate responses for social interactions. It should not be used to deceive or mislead others. Always be honest and respectful in your communications.

License
This project is licensed under the MIT License - see the LICENSE file for details.
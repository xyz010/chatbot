# SalesmanBot
This is a chatbot designed to make an inexperienced door-to-door salesman to an expert-level salesperson. User can insert their field of work (e.g. plumbing, heating and cooling) and their years of experience (e.g. 3) and get personalized feedback.

## Project Requirements

1. The chatbot needs to run in a terminal.
2. The chatbot should have simple memory capabilities so that it can recall previous messages.

## System Requirements
1. Developed and tested in Python `3.9.7`. Also compatible with newer versions.
1. Requires an OpenAI API key as an env variable. 
    > `export OPENAPI_API_KEY=<your_key_here>`


## Installation
1. Install `pdm` with 
    > `pip install pdm`
2. Clone this repository
3. `cd` into the repository
4. Install dependencies with
    >  `pdm install`
5. Run the SalesmanBot with
    > `pdm run chatbot/chatbot.py `

## Instructions
1. Insert your field of work
    > Please enter your field of work: plumbing
2. Insert your exeperience in years
    > Please enter your years of experience: 3
3. Ask any question on how to become a better salesperson
    > Help me become a better salesperson
4. Bot responds
    > Of course! I'm happy to help you become a more effective door-to-door salesperson. Here are some tips and strategies to improve your sales techniques:
    Be prepared: Before you start your day, make sure you have all the necessary tools and materials with you, such as brochures, product samples, and business cards. Familiarize yourself with the products or services you are selling so that you can confidently answer any questions.
    Dress professionally: Your appearance matters when making a first impression. Dress in business attire to convey trust and professionalism. It helps build credibility and makes potential customers more willing to listen to what you have to say.
    Plan your route: Before heading out, plan your route strategically. Research the neighborhoods

5. Type "history" to get the previous messages

6. Press Ctrl + C or Ctrl + D to exit


## Testing
You can run the tests with `pdm run pytest`

## Future Extensions
- can be extended to consult blogpost or other websites regarding door-to-door best practices
- can be also extended for a company-specific database of internal documents
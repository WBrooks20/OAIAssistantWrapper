from gpt import GPTBot  # Importing the GPTBot class from the gpt module

def main():
    # Flag to control the conversation loop
    continue_talking = True

    # Prompt the user to input their OpenAI API key and Assistant ID
    openAI_key = input("Insert OpenAI Key: ")
    openAI_Assistant_ID = input("Insert OpenAI Assistant ID: ")

    # Initialize the gpt_bot instance with the provided credentials
    bot = GPTBot(openAI_key, openAI_Assistant_ID)
    bot.InitOpenai()  # Initialize the OpenAI API connection

    print("\n--- Conversation Started ---\n")
    
    # Start a loop to interact with the bot
    while continue_talking:
        # Get the user's message for the bot
        message = str(input("Your message to GPT: "))
        print("------------------------------")

        # Send the message to the bot and get the response
        response = bot.PromtBot(message)

        # Print the bot's response in a formatted way
        print(f"{response[0]}\n++++++++++++++++++++++++++++++\n{response[1]}")

if __name__ == "__main__":
    # Entry point of the script
    main()
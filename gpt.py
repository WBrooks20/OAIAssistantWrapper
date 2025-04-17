from openai import OpenAI
from termcolor import colored
from enum import Enum
import datetime

class Type(Enum):
    USER = 0
    BOT = 1
    ERROR = 2

class GPTBot():
    def __init__(self, key: str, assist_ID: str):
        self.key = key
        self.assist_ID = assist_ID
        self.client = None
        self.thread = None
        self.thread_id = None

    def formatter(self, message: str, speakertype: Type) -> str:
        match speakertype:
            case Type.USER:
                return f"{colored(datetime.datetime.now(), 'yellow')}: Your message: {colored(message, 'yellow')}"
            case Type.BOT:
                return f"{colored(datetime.datetime.now(), 'green')}: Assistant Response: {colored(message, 'green')}"
            case Type.ERROR:
                return f"{colored(message, 'red')}"

    def InitOpenai(self):
        try:
            self.client = OpenAI(api_key=self.key)
            self.thread = self.client.beta.threads.create()
            self.thread_id = self.thread.id
        except Exception as e:
            print(self.formatter(f"Failed to initialize OpenAI client: {str(e)}", Type.ERROR))
            raise

    def PromtBot(self, message: str) -> str:
        try:
            # Send the user's message to the assistant
            user_message = self.client.beta.threads.messages.create(
                thread_id=self.thread_id,
                role="user",
                content=message
            )
        except Exception as e:
            return self.formatter(f"Failed to send message to assistant: {str(e)}", Type.ERROR), ""

        try:
            # Start and poll the assistant's response
            run = self.client.beta.threads.runs.create_and_poll(
                thread_id=self.thread_id,
                assistant_id=self.assist_ID
            )
        except Exception as e:
            return self.formatter(f"Failed to process assistant response: {str(e)}", Type.ERROR), ""

        if run.status == 'completed':
            try:
                # Retrieve the latest message from the assistant
                thread_messages = self.client.beta.threads.messages.list(
                    thread_id=self.thread_id,
                    order="desc",
                    limit=1
                )
                assistant_response = thread_messages.data[0].content[0].text.value
            except Exception as e:
                return self.formatter(f"Failed to retrieve assistant response: {str(e)}", Type.ERROR), ""
        else:
            return self.formatter("Assistant response not completed successfully.", Type.ERROR), ""

        # Format and return the user message and assistant response
        return self.formatter(message, Type.USER), self.formatter(assistant_response, Type.BOT)
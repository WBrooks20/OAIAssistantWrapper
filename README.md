# OAIAssistantWrapper 🚀

OAIAssistantWrapper is a simple Python package that allows you to interact with an OpenAI assistant in a single thread. It provides a streamlined interface for sending messages to the assistant and receiving responses.

![image](https://github.com/user-attachments/assets/aeb16195-35e7-41bd-a9fe-7b12c72de432)



## Features ✨

- Easy-to-use interface for interacting with OpenAI's API.
- Supports single-threaded conversations.
- Provides formatted output for user and bot messages.
- Built-in error handling for API interactions.

## Installation 🛠️

1. Clone the repository:
   ```bash
   git clone https://github.com/wbrooks20/OAIAssistantWrapper.git
   cd OAIAssistantWrapper
2. Install the required dependencies:
   ```
    pip install -r requirements.txt
   ```

## Usage 💻

1. Run the main.py script:
```
python3 main.py
```
3. Enter your OpenAI API key and Assistant ID when prompted.
4. Start interacting with the assistant by typing your messages.

## Example 📝
```
Insert OpenAI Key: <your-api-key>
Insert OpenAI Assistant ID: <your-assistant-id>
Your message to GPT: Hello!
2025-01-01 12:00:00: Your message: Hello!
--------------------
2025-01-01 12:00:01: Assistant: Hi there! How can I assist you today?
```
## Project Structure 📂
```
OAIAssistantWrapper/
├── [gpt.py]                                          # Core logic for interacting with OpenAI API
├── [main.py]                                         # Entry point for the application
├── [requirements.txt]                                # List of dependencies
├── [README.md]                                       # Project documentation
├── LICENSE            # License information
└── .gitignore         # Git ignore rules
```
## Requirements 📋

- 🐍 Python 3.10 or higher
- 🔑 OpenAI API key
- 🆔 OpenAI Assistant ID

## Dependencies 📦
The project uses the following Python libraries:

- openai
- termcolor
- httpx
- pydantic
- And others listed in requirements.txt.

## Contributing 🤝
Contributions are welcome! Feel free to open an issue or submit a pull request.

## License 📜
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments 🙌

- 🌟 OpenAI for their API.
- 🐍 The Python community for the amazing libraries used in this project.

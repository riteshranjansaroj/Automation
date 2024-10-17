# Automation Scripts

This repository contains Python automation scripts for various tasks, including automating **YouTube song searches** and **automatically sending messages** on social media platforms. The scripts use libraries like `pyautogui`, `speech_recognition`, and `pyttsx3` to control the mouse, keyboard, and perform voice recognition tasks.

## Features

1. **YouTube Song Search Automation**: 
   - Uses voice input to search and play songs on YouTube.
   - Opens Chrome, navigates to YouTube, and plays the requested song.
   
2. **Automated Message Sending**:
   - Sends random messages continuously on social media platforms.
   - You can configure the number of messages and the content of the messages.

## Technologies Used

- **Python**: The main programming language for writing these scripts.
- **PyAutoGUI**: A Python library used for automating mouse and keyboard control.
- **SpeechRecognition**: Used for recognizing voice commands from the user.
- **pyttsx3**: A Python library for text-to-speech conversion.

## Installation

### Prerequisites

- **Python**: Ensure Python 3.x is installed. You can download it from [python.org](https://www.python.org/downloads/).
- **Required Libraries**: You can install the necessary Python libraries using pip. Run the following commands:

```bash
pip install pyautogui pyttsx3 speechrecognition
```

## Scripts

### 1. **YouTube Song Search Automation** (`youtube.py`)

This script allows you to automate the process of opening Chrome, navigating to YouTube, and playing a song using voice commands.

#### How it works:
1. The script uses text-to-speech (`pyttsx3`) to ask if you want to continue.
2. If the response is affirmative, the script listens for a song name or any text (through voice recognition).
3. It opens Chrome, goes to YouTube, and plays the song of your choice.
4. If no song is specified, it will play the generic input text.

#### How to use:
1. Run the script:

```bash
python youtube.py
```

2. The script will prompt you to confirm if your browser is full-screen. Respond with **yes** or **no**.
3. If you say **yes**, it will prompt you to say a song name.
4. Once the song name is spoken, the script will automatically open Chrome and search YouTube for the song.
5. The script will click on the first video to play it.

#### Code Explanation:

- Uses `pyttsx3` for text-to-speech.
- Uses `speech_recognition` to listen for the user’s input.
- Uses `pyautogui` to automate mouse and keyboard actions (opening Chrome, typing the URL, clicking on search results, etc.).

### 2. **Automated Message Sender** (`autoMsgSend.py`)

This script allows you to send random messages continuously on any social media platform by simulating keyboard input. You can automate the process of sending messages a number of times.

#### How it works:
1. The script asks for the number of messages to send and then waits for 10 seconds.
2. Once ready, it types random messages from a pre-defined list and sends them by simulating the press of the **Enter** key.

#### How to use:
1. Run the script:

```bash
python autoMsgSend.py
```

2. The script will ask for the number of times to send the message. Enter a number (e.g., `5`).
3. After 10 seconds of delay, the script will start sending messages continuously.

#### Customization:
- You can customize the `msg_list` with any messages you want to send.
- If you're unsure about the exact position of the message input box, you can un-comment the lines that print the mouse position.

#### Code Explanation:

- Uses `pyautogui` to simulate typing messages and pressing the **Enter** key.
- The `random.choice()` function picks a random message from the `msg_list` for each iteration.

---

## How to Use the Scripts Together

1. **Run the YouTube Automation Script** (`youtube.py`) to play songs automatically by voice command. 
2. **Run the Message Automation Script** (`autoMsgSend.py`) to send multiple messages automatically on any social platform (e.g., WhatsApp, Telegram, etc.).

These scripts are useful for automating routine tasks like searching for songs and sending repeated messages with minimal interaction.

## Limitations

- The automation scripts assume that the Chrome browser is already installed and accessible from the **Windows Start Menu** (for YouTube automation).
- Ensure your screen resolution and browser window positions are consistent with the coordinates specified in the scripts (`pg.click(x, y)`). You can use the `pg.position()` function to identify the exact mouse position.

## License

This project is open-source and available for personal use and modification. No formal license has been applied, so feel free to use or modify the code as per your needs.

# Asur v1.0.1 
The above code is designed to process speech input, extract movie keywords, and open corresponding Google Drive search links for each keyword. It utilizes various libraries and APIs to achieve this functionality.

Here's a short description of the code:

1. The code uses the `speech_recognition` library to capture speech input from the user via a microphone.
2. The captured speech is then processed using the Google Cloud Speech-to-Text API for speech recognition.
3. The recognized speech is combined with a predefined message and passed to the Bard API, which returns an answer based on the provided input.
4. The answer is analyzed, and movie keywords are extracted using regular expressions.
5. Duplicate movie keywords are removed from the extracted list.
6. The extracted movie keywords are used to generate corresponding Google Drive search links.
7. The code opens each Google Drive search link in separate Chrome tabs using the `undetected_chromedriver` library.
8. The answer from Bard API, along with the extracted movie keywords, is converted to speech using the `pyttsx3` library and played back to the user.
9. The code includes error handling and waits for a certain amount of time before exiting.

Overall, this code combines speech recognition, natural language processing, web scraping, and text-to-speech conversion to create an interactive experience where users can provide speech input, receive answers based on that input, and explore movie-related content through Google Drive search links.


To create an installation script for the requirements of your Python code, you can follow these steps:

```
pip install -r requirements.txt
```

This command will install all the listed dependencies from the requirements.txt file automatically.


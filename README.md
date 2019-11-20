# SentimentAnalyzerWithRealtimeVoice :loudspeaker:
This is Simple Python project to acknowledge the voice and convert voice to text and analysis that converted text using Text-Blob


## Table of Contents

- [Prerequisite](#Prerequisite)
- [Install](#install)
- [Download](#Error_Solution)
- [Contributors](#Contributors)
- [Help](#Help)
- [License](#license)


## Prerequisite
SentimentAnalyzerWithRealtimeVoice Requires
```
Modules :
1)speech_recognition- For Realtime Speech Recognizer
2)textblob - Sentimental analysis
3)pyttsx3 - Text-to-speech conversion library
```

## Install
First install required Modules

**speech_recognition**
```
pip install SpeechRecognition
```
**textblob**
```
pip install textblob
```
**pyttsx3**
```
pip install pyttsx3
```
Clone this https://github.com/chavarera/SentimentAnalyzerWithRealtimeVoice repository at local.
Extract on your system.
After Cloning repository  go to root directory and run following command in command prompt.
```
python SentimentAnalyzerWithRealtimeVoice.py
```
Now Just  speak any Sentences to test Application.
After running above statement you will get following result.
![sentimental](https://raw.githubusercontent.com/chavarera/SentimentAnalyzerWithRealtimeVoice/master/screenshots/RealTimeWOrdSentimentanalaysisy.png)

## Error_Solution
**Error 1:win32api module not found**
Install Following Libraries and Restart Your machine
```
pip install pywin32
pip install pypiwin32
```

**Error 2:Pyaudio Module Not Found(Or Error While Installation)**
find your Python version First
```
python --version
```
find the appropriate .whl file from here,
https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

For Example(mine 64 bit 3.7.4 python ):
The Download
```
PyAudio‑0.2.11‑cp37‑cp37m‑win_amd64.whl file
```
Go to that directory where you have saved that file and running
```
pip install PyAudio-0.2.11-cp37-cp37m-win_amd64.whl
```
Hit enter and after successful installation close the Terminal


## Contributors
- :octocat: [Ravishankar Chavare](https://github.com/chavarera)

## Help
If Any issue arise contact me at
```
chavare.ravi123@gmail.com
```
## License

[MIT © Ravishankar Chavare.](LICENSE)

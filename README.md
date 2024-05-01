# Speech-to-Sign-Language-Translator

<b>Instructions</b>
1. Install blender 2.79.
2. Set Path variable for python distribution present inside blender (\Your installation directory\Blender Foundation\Blender\2.79\python\bin). Pip will be present with python. If not, then install from <a href="https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation#pip-install"> here </a> and set path variable.
3. Install and setup ffmpeg. Required while importing pydub as well.
4. Install python dependecies using pip: pydub, pyaudio, google-cloud-speech, google-cloud-language etc.
5. Congifure API Key for google cloud services. You might have to create a new project and enable google speech and language api in googlecloud console, then create and download a json credential file and place the file in model directory. Detailed instructions <a href="https://cloud.google.com/speech-to-text/docs/quickstart-client-libraries#client-libraries-install-python"> here.</a>
6. Run animationData.py as script inside blender. It generates some meta-data used in animating sign glosses.
7. Run .blend file inside model folder.


#### Additional
1. Python 3.5.3 is already included with blender 2.79.
2. ffmpeg required for converting wav to flac. Install ffmpeg first and add it to environment variables else errors will occur.
3. .raw & .flac are the only audio file accepted for text transalation by the API.
4. Works correctly for first time in game engine after that errors occur because python cahces imported modules. Hence we need to restart blender everytime to delete cached imports.


#### Detailed Steps
1. Download Blender 2.79 and install it.
2. After installation goto installation directory and find python distribution of your blender. This will be present in "/blender_installation_dir/Blender/2.79/python/bin".
3. Add the above path to the "Path" environment variable. We need this because we will need to install some libraries in this python distribution. We do not want these libraries to get installed in some wrong python distribution that might be present in your pc.
4. Check in cmd if python is accessible. Enter python in cmd and press enter.Version info will be displayed. It should be 3.5.3.
5. Exit from python and enter 'python -m pip install -U pip' to upgrade pip.
6. Install ffmpeg from <a href="http://ffmpeg.zeranoe.com/builds/">here</a>. Extract it in your system. There will be a bin folder present. Add the path of the bin folder (including bin folder) to your System "Path" variable.
7. Enter following commands in cmd and install libraries.

    python -m pip install pydub\
    python -m pip install pyaudio\
    python -m pip install google-cloud-speech\
    python -m pip install google-cloud-language

8. Login to google cloud console. Create a new project there. Goto "API and Services" and click on "enable API and services". Search for "speech to text" and "natural language" APIs. Enable them and also enable billing for them as well. If it asks for payment information provide a VISA or MasterCard details. These APIs are free but you will need to enable billing to access them.
9. Goto "Credentials" tabs under "API and services". Click on manage service account and create a new service account. Add details. Select "owner" under roles.
10. Again goto "Credentials" tabs under "API and services". Click on your newly created service account. On the next page click on "Add key" -> "Create New Key" -> "Json" -> "Create". A json file will be downloaded. **Put this file in the model directory.** Uncomment the code if commented.
11. Open project .blend file. Click on "Default" and select "scripting". The code will be visible now. Select AnimationData.py. Right Click on it and select run. **AnimationData.txt will be generated in the model directory.**
12. Again select "Default" view and press key P. You will enter the game engine. Make sure to open the Windows console before pressing P for debugging.
13. Press R to record and S to stop. After recording APIs will be called. If any error occurs, see the error dump in the console.


#### Screen Shots
Recording Speech: 

![image](https://github.com/anuragk240/Speech-to-Sign-Language-Translator/assets/17070972/1758bfd7-fe1a-4f45-bf4c-6ae6745ef2aa)

Converting Speech to text:

![image](https://github.com/anuragk240/Speech-to-Sign-Language-Translator/assets/17070972/7cd53eea-6f09-4bc6-bcd0-b11891afa600)

Analyzing input text:

![image](https://github.com/anuragk240/Speech-to-Sign-Language-Translator/assets/17070972/2e862044-8179-4618-8a58-7f578f2e81f9)

Animation of Model:

![image](https://github.com/anuragk240/Speech-to-Sign-Language-Translator/assets/17070972/82834fb9-036f-42b6-a259-8d59b1eca501)





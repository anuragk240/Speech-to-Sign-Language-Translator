# Speech-to-Sign-Language-Translator

<b>Instructions</b>
1. Install blender 2.79.
2. Set Path variable for python distribution present inside blender (\Your installation directory\Blender Foundation\Blender\2.79\python\bin). Install pip for this python distribution from <a href="https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation#pip-install"> here </a> and set path variable also.
3. ~~Install and setup ffmpeg from <a href="https://github.com/adaptlearning/adapt_authoring/wiki/Installing-FFmpeg">here</a>.~~ Not required now, instead importing pydub.
4. Install python dependecies using pip: pydub, pyaudio, google-cloud-speech, google-cloud-language etc.
5. Congifure API Key for google cloud services. You might have to create a new project and enable google speech and language api in googlecloud console, then create and download a json credential file and set "json_key_file" in startup.py to the path to json credential file. Detailed instructions <a href="https://cloud.google.com/speech-to-text/docs/quickstart-client-libraries#client-libraries-install-python"> here.</a>
6. Run animationData.py as script inside blender. It generates some meta-data used in animating sign glosses.
7. Run .blend file inside model folder.


#### Additional
1. Use python 3.5.3 so that code is compatible with blender 2.79.
2. ~~fmpeg required for converting wav to flac. Install ffmpeg first and add it to environment variables else errors will occur.~~
3. .raw & .flac are the only audio file accepted for text transalation by the API.
4. Works correctly for first time in game engine after that errors occur because python cahces imported modules. Hence we need to restart blender everytime to delete cached imports.

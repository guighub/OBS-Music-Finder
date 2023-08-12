# OBS-Music-Finder
Find songs using shazamio and output it to OBS!

## How To Use
[Install the latest release of Python](https://www.python.org/downloads/)

To use this in OBS, you will need to install `shazamio` and `pyaudio` with pip:
```
pip install shazamio
pip install pyaudio
```
After doing this, download this repository and put it somewhere easily accessible.

You'll now need to find the device ID that your music is playing from. Currently this code only supports audio inputs (Line in, Microphones, etc.) To find the device ID, run `list_devices.py` in a terminal. You should see a list of your devices and their associated ID's. Once you find your device, remember it's ID and change the value of `input_device_index` in the file `obs-shazam.py` to that ID. (By default it is set to 5 which is "Line In (Realtek(R) Audio)" for me)

You can now run `obs-shazam.py` in the background, and it should start writing to the .wav and .txt files.

Almost done! Now you need to create a "Text (GDI+)" object in your OBS scene, check "Read from file", and select the text file. The text should now automatically update to display the song info.

## Information
I originally made this for use in Discord streaming, as I occasionally stream my vinyl record collection in voice chats. It gets a little hard to manage when someone asks what song is playing, as I would have to get the record jacket and look at the track list each time if I didn't know the song name from memory. I tried manually changing the text each time I play a new album, but it's a little inconveniant and I often forgot to change the text. I eventually found the shazamio Python library and decided it would be a perfect way to automate the process.

I might eventually make this an OBS script that can run directly in OBS, but I've had trouble trying to install and use their library.

## Known Issues
It will occasionally get the song completely wrong, which happens most likely because there isn't enough audio to determine the correct song. You can try increasing the `record_length` variable in `obs-shazam.py` to fix it, however it will take longer to recognize the song.
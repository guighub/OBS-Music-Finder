# Records audio and recognizes track using shazamio!
# Run this code, the song info will be saved to the file "song_name.txt" which you can then use in a Text (GDI+) set to read from the file.

import asyncio
from time import sleep
from shazamio import Shazam
from record import record_clip

record_length = 5
cooldown_length = 5
record_path = 'song_sample.wav'
input_device_index = 5 # The index of the device to record from. To find yours, run list_devices.py in a terminal.

# Main code loop
while True:
    # Record sample to recognize
    record_clip(record_length, record_path, input_device_index)

    async def main():
        shazam = Shazam()
        # Recognize from recorded audio file
        out = await shazam.recognize_song(record_path)
        if 'track' in out:
            track_data = out['track']
            if 'subtitle' in track_data and 'title' in track_data:
                # Return song info (and repair a strange unicode issue)
                return (track_data['subtitle'] + ' - ' + track_data['title']).replace('’', '\'')
        else:
            # No song info was found, so return nothing
            return None
    loop = asyncio.get_event_loop()
            
    song = loop.run_until_complete(main())
    if song is not None:
        # Song recognized!
        print('Matched: ' + song)
        
        # Output to text file
        txt = open('song_name.txt', 'wt')
        txt.write(song)
        txt.close()
        
        # Wait for set amount before starting over
        print('Sleeping')
        sleep(cooldown_length)
    else:
        # Song was not found, restart the loop immediately
        print('Song not found, trying again.')
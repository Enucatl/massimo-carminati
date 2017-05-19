import pyaudio
import os
import wave
from curses import wrapper
from glob import glob
import pulsectl


def main(stdscr):
    #define stream chunk   
    chunk = 1024  
    files = sorted(glob("16bit/*.wav"))
    pulse = pulsectl.Pulse("massimo-carminati")
    sink = pulse.sink_list()[5]
    pulse.default_set(sink)

    p = pyaudio.PyAudio()  
    # open stream  
    stream = p.open(
        format=2,  
        channels=2,  
        rate=22000,  
        output=True)  

    try:
        while True:
            stdscr.clear()
            for i, filename in enumerate(files):
                display_name = os.path.splitext(os.path.basename(filename))[0].replace("-", " ")
                stdscr.addstr(i, 0, "({0}): {1}".format(i + 1, display_name))
            selected = int(stdscr.getkey())
            f = wave.open(files[selected - 1], "rb")  
            data = f.readframes(chunk)  

            while data:  
                stream.write(data)  
                data = f.readframes(chunk)  

    finally:
        stream.stop_stream()  
        stream.close()  

        p.terminate()
        pulse.default_set(pulse.sink_list()[4])
        pulse.close()

wrapper(main)

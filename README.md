# piClaptest
Python script that automates the 'clap' test for determining latency of audio processing. This is being used alongside a InnoMaker Audio DAC (BossDac) and two speakers playing noise generated via ffmpeg, I wanted to take the setup further to dynamically change the noise based on live conditions.

### Usage
1) Change option for your audio recording device; show available recording interfaces with command `arecord -l`
2) Launch the script, have your pi with sense hat handy, press the button, wait for the countdown, clap, will show a green ! when it successfully records and writes to the file system.

Note: I used google/gemma-4-26b-a4b running locally to ask it about my specific audio needs; and we eventually decided a clap test was in order before we continued to determine if the latency was appropriate before going full AI (RNNoise). The code that it spat out was fairly terrible, I spent about two hours troubleshooting basic api calls that were 'wrong'; but not by a lot. By the end it was repeating its thoughts in loops concerning its quotes spacing. Some of the errors were basic typos; while others got the api calls wrong; in proper logical flow loop; but it did give me a code base to start on! I'm by no means a python expert, but I did not expect the AI to be so bad at performing a basic task on a device that's over a decade old; doing online searches produced the same wrong code (ms co pilot)

## Recommended Equipment

1) **Rasperry pi 2 Model B** (what I'm using; its not super fast but I have thermal pads and a heatsink, you probably can't use anything older than this)
2) **External Audio Playback device** preferrably not usb (I'm using the Boss DAC, by innomaker)
3) **External Audio Input device** (I'm using a logitec webcam; but a audio DAC with line in will have less latency)

You can use the internal audio 3.5mm audio out device (not recommended) or the hmdi audio out; I haven't tried these methods but your mileage my vary; pi 3.5mm audio out has never known to be rhobust; and it has issues when using ethernet AND built in audio, I have a dac, but yes its not a requirement but you may not have anything usable due to latency constraints for the purposes of active noise canceling.

Eventually I plan to expand this to dynamically change noise color/amplitude based on microphone input.

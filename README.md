# ChordGenPlay

> Proper documentation in progress. Stick around if you want xD

- Take an arbitrary combination of audio files (eg: chords)
- Write down a simple line defining it (eg: "g\*3;a\*4;am")
- Have generated audio :)
  
## Why?

- Experiment with audio
- Use it if you want to fast track your creative process
- Interested in **deep learning** with audio?? Generate infinite data (yayyy)
- Maybe make cool sound effects just by the power of script

## What can this bad boy do?

- Mini language of sorts to define any arbitrary audio pattern
- Repeat an many times as you want by adding a * (eg: g*3 will repeat g.wav 3 times)
- You get one track at the end with the entire combinations. Repeated or whatever you want
- Generate n clips

## How do I use this madness?

- Get python
- Install librosa, numpy, scipy, tqdm. (I will be adding a requirements.txt soon)
- Make a folder called music/ pass your folder as an argument
- Rename your audio files to usable ones. (eg: a.wav, g.wav). This is not required but it will save you typing
- python3 runner.py --dir "music/" --rate 22040 --order "g*3;a*2" --fname "outputs" --random 0 --n 10

## WIP

- Repeat entire sequences. (Code done. Have to think of a syntax)
- Batch generator / randomness (Cuz Deep Learning4life)
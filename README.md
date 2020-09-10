- [ChordGenPlay](#chordgenplay)
  - [Why?](#why)
  - [What can this bad boy do?](#what-can-this-bad-boy-do)
  - [How do I use this madness?](#how-do-i-use-this-madness)
  - [Supported parameters](#supported-parameters)
  - [Examples](#examples)
  - [Future plans (Contributions welcome :))](#future-plans-contributions-welcome-)

# ChordGenPlay

- Take an arbitrary combination of audio files (eg: chords)
- Write down a simple line defining it (eg: "g\*3;a\*4;am"). Or leave it blank if you want randomness.
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
- Generate n random clips from the audio. (customize the randomgen function if you need it)
- Batch generator / randomness (Cuz Deep Learning4life)

## How do I use this madness?

- Get python
- Install librosa, numpy, scipy, tqdm. (I will be adding a requirements.txt soon)
- Make a folder called music/ pass your folder as an argument
- Rename your audio files to usable ones. (eg: a.wav, g.wav). This is not required but it will save you typing
- python3 runner.py --dir "music/" --rate 22040 --order "g*3;a*2" --fname "outputs" --random 0 --n 10

## Supported parameters

```py
python3 runner.py --dir "music/" --rate 22040 --order "g*3;a*2;a+*5" --fname "outputs" --random 1 --n 20 --rep 3 --maxlen 10
```

1. "-d", "--dir" : Choose the folder to take the music from
2. "-r", "--rate" : Rate of audio generated
3. "-o", "--order" : File order and repetition
4. "-f", "--fname" : Output file name
5. "-ran", "--random" : 1 or 0 => Randomly pick audio/ shuffle given order or preserve order
6. "-n", "--number" : How many audio files you want
7. "-m", "--rep" : How many times should each file be repeated (maximum)
8. "-l", "--maxlen" : Maximum audio size . Aka max number of files picked 

## Examples

1. Generate 20 songs with random combinations from the file and repeat each audio a maximum of 3 times. Max length should be 10
```py
python3 runner.py --dir "music/" --rate 22040 --order "g*3;a*2;a+*5" --fname "outputs" --random 1 --n 20 --rep 3 --maxlen 10
```

## Future plans (Contributions welcome :)) 

- Repeat entire sequences. (Code done. Have to think of a syntax)

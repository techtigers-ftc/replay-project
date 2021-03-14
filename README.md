# Magik SDK

_SDK that will allow you to write a game for the [Tech Tigers](https://www.techtigers.team/home Magic Carpet game mat._
# Introduction
This was developed by the Tech Tigers FLL team as part of the Innovation Project for the 2020-2021 season -  Replay. As part of our competiton we had identify and popose an innovative solution. We chose the problem of there not being enough fun ways to stay active at home.

Our solution is the Magik Carpet - an interactive carpet that is easy to use, needs no setup, fits in with your home decor, and offers an endless variety of games and exercises for all ages.

It consists of:
- A controller: [ESP32](https://amzn.to/38eJIx1)
- The pressure sensing layer: [Velostat](https://amzn.to/3ehWQFK) and [copper tape](https://amzn.to/2OwDvWw)
- The LED layer: [LED strips](https://amzn.to/2O1q0OL)
- The cushion layer: [Interlocking, wood-patterned foamtiles](https://amzn.to/3rqJL0x)
- The facade layer: [Flex foam](https://bit.ly/38ioNcI)

For for info look [here](https://www.techtigers.team/replay/project)

# Motivation
During the pandemic, it was not safe to test our prototype with people
in person. We made an SDK so that:
- Less expirienced programmers on the team could still write games
- Teammates could write games without understanding or having acces to the hardware
- We could keep things interesting with more and more games

# Design

Our input adaptors take our inputs and convert them into a standard format. Then our gane interprets those inputs and returns a standard format of what to draw. The Output adaptors take that and then write it to the final display.

### Input
 - Keyboard
 - Pressure Sensor
### Output
- Ascii
- LEDs on mat

# Installation

Clone?

# Usage

1. Go into the games directory and create a new directory
2. Create __innit\_\_.py, main.py and {insert sprite}.py
3. look at /games/demo and copy much of the structure
4. replace the initialize sprites and other uniqe things
5. before you run, make sure to
`` export PYTHONPATH="~/replay-project/" ``

## Examples

- [demo](https://github.com/techtigers-fll/replay-project/tree/master/games/demo)
- [intro](https://github.com/techtigers-fll/replay-project/tree/master/games/intro)
- [football](https://github.com/techtigers-fll/replay-project/tree/master/games/football)
- [quadrant](https://github.com/techtigers-fll/replay-project/tree/master/games/quadrant)






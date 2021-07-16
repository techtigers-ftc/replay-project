# Magik SDK

_SDK that will allow you to write a game for the [Tech Tigers](https://www.techtigers.team/home) Magic Carpet game mat._
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

![Magik Demo](images/magik-demo.gif)

# Motivation
During the pandemic, it was not safe to test our prototype with people
in person. We made an SDK so that:
- Less expirienced programmers on the team could still write games
- Teammates could write games without understanding or having acces to the hardware
- We could keep things interesting with more and more games

# Design

Our design is in the picture below

![Magik SDK](images/magik-sdk.png)

All games have an input and an output. Ours does too. The difference is that we want our games to be able to interact with different inputs and outputs. 

To do this we use adaptors. The job of these adaptors is to convert a signal from a keyboard or pressure senson into a standard input that our game can read.

It is very similar to the output, our game sets the pixels in a standard format and out output adaptors convert it into something a display can show.

### Supported Input
 - Keyboard
 - Pressure Sensor
### Supported Output
- Ascii
- LEDs on mat

# Usage

Please fork our repository before making changes. After you fork, you will see 2 main folders, `magik` and `games`

`magik` is our sdk and `games` has games that we have written.

To write a game, you can copy a pre-existing game (See the examples below). Keep these points in mind:

**main.py**
1. Make sure the first import is importing `launch_module`, and not `launch_single_tile`
2. Make sure to adapt the sprite import line and sprites array to your sprites and directories
3. To run the program, write `python3 main.py` in the directory

**Sprite programs**
1. Change the code in the update section to change the sprite's properties, and the draw section to change how it draws
2. Don't keep any unnecessary sprites in the directory
3. Check the sprites import statements to make sure you are not importing deleted sprites


You can check [sprite.py](https://github.com/techtigers-fll/replay-project/blob/master/magik/sprite.py) for information on how to use the properties of the sprite.

Do not change the code in any of the existing code, espicially in the `magik` directory, as it will cause the code to not work.

After completing a game, please share your repository with us so we can try it out on our actual mat!

Any questions can be can be asked on our [discord server](https://discord.gg/2ak6YbZjVR), or emailed to techtigers33958@gmail.com

## Examples

- [big_intro](https://github.com/techtigers-fll/replay-project/tree/master/games/big_intro)
- [big_whackamole](https://github.com/techtigers-fll/replay-project/tree/master/games/big_whackamole)
- [football](https://github.com/techtigers-fll/replay-project/tree/master/games/football)
- [plank](https://github.com/techtigers-fll/replay-project/tree/master/games/plank)

 **NOTE**: Some of our programs were originally built for our smaller mat, like `intro` and `whackamole`. We now have a larger scaled mat that is being used. Due to this, some of out programs have an import statement with `launch_single_tile`, which should not be used anymore, and newer versions of the old programs are named with a *big* prefix, like `big_intro` and `big_whackamole`.

## Testing Pull Requests

I've made some changes to this doc.


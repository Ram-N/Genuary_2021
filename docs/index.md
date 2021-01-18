## Genuary 2021 - Daily Prompts for Generative Art

Generative Art that is based on daily prompts for the month of January 2021. Genuary 2021 was a collective project in which 100s of generative artists created art daily based on prompts that were given to them ahead of time. Below are my entries for this project.

***** 
## Prompts

A group of generative artists have collaborated and created a "prompt" for each day.
Click for the prompts for each day. [Here](https://genuary2021.github.io/prompts) are the actual prompts, but you’re only supposed to do them on that particular day.

*****

## Jan 17 
### Prompt: Draw a line, pick a new color, move a bit. 
[Code](https://github.com/Ram-N/Genuary_2021/tree/main/Jan17_Line_Color_Move/)
![with size](https://raw.githubusercontent.com/Ram-N/Genuary_2021/main/Jan17_Line_Color_Move/images/keep0.png?s=400)

**Description** I constrained the lines to stay within one of 36 (6x6) panels. The colors rotate through a palette of colors. Each line (within a panel) is slightly longer that its previous one. Once the line length reaches the panel's dimension, it gets reset. Alternate the orientations to be vertical and horizontal in subsequent panels.

*****

## Jan 16: Circles Only [Code](https://github.com/Ram-N/Genuary_2021/tree/main/Jan16_Circles_Only)
### Prompt: Circles Only
![with size](https://raw.githubusercontent.com/Ram-N/Genuary_2021/main/Jan16_Circles_Only/images/keep0.png?s=400)

*****

## Jan 15: Rules by Someone Else [Code](https://github.com/Ram-N/Genuary_2021/tree/main/Jan15_Rules_By_Someone_Else)
### Prompt: Let someone else decide the general rules of your piece.
![with size](https://raw.githubusercontent.com/Ram-N/Genuary_2021/main/Jan15_Rules_By_Someone_Else/images/keep0.png?s=400)

*****

## Jan 14: Subdivision [Code](https://github.com/Ram-N/Genuary_2021/tree/main/Jan14_Subdivision)
### Prompt: // SUBDIVISION 
![with size](https://raw.githubusercontent.com/Ram-N/Genuary_2021/main/Jan14_Subdivision/images/keep0.png?s=400)

*****

## Jan 13: Do Not Repeat [Code](https://github.com/Ram-N/Genuary_2021/tree/main/Jan13_Do_Not_Repeat)
### Prompt: Do not repeat.
![with size](https://raw.githubusercontent.com/Ram-N/Genuary_2021/main/Jan13_Do_Not_Repeat/images/keep0.png?s=400)

*****

## Jan 12: Public API to create Art [Code](../Jan12_Use_API)
### Prompt: Use an API (e.g. the weather).
![with size](https://raw.githubusercontent.com/Ram-N/Genuary_2021/main/Jan12_Use_API/images/hours_daylight.png?s=400)

*****
## Jan 11: Non-computer Autonomous Process [Code](https://github.com/Ram-N/Genuary_2021/tree/main/Jan11_Other_Autonomous)
### Prompt: Use something other than a computer as an autonomous process (or use a non-computer random source).
![with size](https://raw.githubusercontent.com/Ram-N/Genuary_2021/main/Jan11_Other_Autonomous/images/spiral_20210112_090340.png?s=400)

*****
## Jan 10: Tree [Code](https://github.com/Ram-N/Genuary_2021/tree/main/Jan10_Tree)
### Prompt: // TREE
![with size](https://raw.githubusercontent.com/Ram-N/Genuary_2021/main/Jan10_Tree/images/ev_60.png?s=400)

*****
## Jan 09: Interference Patterns [Code](https://github.com/Ram-N/Genuary_2021/tree/main/Jan09_Interference_Patterns)
### Prompt: Interference patterns.
![with size](https://raw.githubusercontent.com/Ram-N/Genuary_2021/main/Jan09_Interference_Patterns/images/interference_6784.png?s=400)

*****
## Jan 08 Curve Only [Code](https://github.com/Ram-N/Genuary_2021/tree/main/Jan08_Curve_Only)
### Prompt: Curve Only.
![with size](https://raw.githubusercontent.com/Ram-N/Genuary_2021/main/Jan08_Curve_Only/images/curves_4755.png?s=400)

*****
## Jan 07 Generate Rules - Hand Drawn [Code](https://github.com/Ram-N/Genuary_2021/tree/main/Jan07_Rules_and_Hand-drawn)
### Prompt: Generate some rules, then follow them by hand on paper.
![with size](https://raw.githubusercontent.com/Ram-N/Genuary_2021/main/Jan07_Rules_and_Hand-drawn/images/attempt1.JPEG?s=400)

*****
## Jan 06 Triangle Subdivision [Code](https://github.com/Ram-N/Genuary_2021/tree/main/Jan06_Triangle_Subdivision)
### Prompt: Triangle subdivision.
![with size](https://raw.githubusercontent.com/Ram-N/Genuary_2021/main/Jan06_Triangle_Subdivision/images/ico_anim.gif?s=400)

*****
## Jan 05 Code Golf [Code](https://github.com/Ram-N/Genuary_2021/tree/main/Jan05_Code_Golf)
### Prompt: Do some code golf! How little code can you write to make something interesting? Share the sketch and its code together if you can.
![with size](https://raw.githubusercontent.com/Ram-N/Genuary_2021/main/Jan05_Code_Golf/images/code_golf_251.png?s=400)

**Description** 
Randomly scatter colored balls, with increasing density closer to the "ground." Added connecting lines from the top to 3% of the balls, for a chandelier or suspended effect. The color of the balls is also dependent on their y-coordinate. Do the above, using 10 lines of code.

```
def setup():
    size(w, w)
    for _ in range(w):
        s, c = random(w), random(_)
        fill(c, c / 2, c / 4)
        flip = random(1)
        if flip > 0.97:
            line(w - s, 0, w - s, w - c)
        if flip > 0.8:
            ellipse(w - s, w - c - 20, r, r)
```
*****
## Jan 04 Small Areas of Symmetry [Code](https://github.com/Ram-N/Genuary_2021/tree/main/Jan04_Symmetry)
### Prompt: Small areas of symmetry.
![with size](https://raw.githubusercontent.com/Ram-N/Genuary_2021/main/Jan04_Symmetry/images/noise_symm_4209.png?s=400)

*****
## Jan 03 Something Human [Code](https://github.com/Ram-N/Genuary_2021/tree/main/Jan03_Something_Human)
### Prompt: Make something human.
![with size](https://raw.githubusercontent.com/Ram-N/Genuary_2021/main/Jan03_Something_Human/images/g25.gif?s=400)

*****
## Jan 02 Rule 30 [Code](https://github.com/Ram-N/Genuary_2021/tree/main/Jan02_Rule30)
### Prompt: Rule 30 (elementary cellular automaton)
![with size](https://raw.githubusercontent.com/Ram-N/Genuary_2021/main/Jan02_Rule30/images/tile_alt_rule_30_7324.png?s=400)

*****
## Jan 01 Triple Nested Loops [Code](https://github.com/Ram-N/Genuary_2021/tree/main/Jan01_Triple_Nested_Loops)
### Prompt: // TRIPLE NESTED LOOP
![with size](https://raw.githubusercontent.com/Ram-N/Genuary_2021/main/Jan01_Triple_Nested_Loops/images/triple_loop1.png?s=400)
*****

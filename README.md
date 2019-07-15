# Unique-Pairings
A simple script for generating rounds of pairs of people with no repeats for groups of an arbitrary size

### Motivation
My mother works with teams of people and sometimes needs to have the people work in pairs for several rounds until they've worked with everyone. The pairs should never repeat. She had figured out what do for smaller groups, but didn't know how to pair people up when she had an unusually large amount of people. I wrote this quick script to generate pairs for each round for whatever group size is input(some slight tweaking is needed for groups > 26 due to formatting decisions). 

### Example
Here is the output for a group of size 10. The people above/below each other are paired together for the round. So in this example for the first round A and J are working together. If there is an odd amount of people, an extra "dummy" person is added and the person matched with this dummy person each round just sits it out. The letters are lined up in Python's output, unfortunately they aren't in Markdown.

Round 1

A B C D E 

J  I  H G F 


Round 2

A C D E F 

B J I H G 


Round 3

A D E F G 

C B J I H 


Round 4

A E F G H 

D C B J I 


Round 5

A F G H I 

E D C B J 


Round 6

A G H I J 

F E D C B 


Round 7

A H I J B 

G F E D C 


Round 8

A I J B C 

H G F E D 


Round 9

A J B C D 

I H G F E 

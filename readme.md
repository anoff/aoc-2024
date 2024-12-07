# Advent Of Code 2024

## Time spent [min]

This year I was curious how much time I'm spending on each challenge, so keeping some record here.

- Setup: 20
- Day01: 15
- Day02: 50 + 
- Day03: 50
- Day04: 

## Thoughts

### Day4

At first I wanted to do a quick parse and eliminate all A's that did not have an adjacent M or S - regardless of their orientation.
Turns out this did hardly remove any characters from the board, so not making the further executions faster.

Next approach was just brute forcing, starting from each X and maintaing a small data structure for each potential word.

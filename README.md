# Advent-of-Code-2017
Solutions to [Advent of Code](https://adventofcode.com/2017) puzzles 2017.

## Naming convention:
Each script is named after the day and part number of the puzzle. First number is the day and second is the part. If part number is missing, that means that the script for that day will output result for all parts of the puzzle separated by a space.

### For eg: 

- Day 2 puzzle has 2 parts, so 2part1.py will solve the first part and 2part2.py will solve the second one.
- Day 6 has two parts too but only one file (6.py). So, 6.py will solve for both parts and output results separated by a space.

## Usage for each script:
Each script would be run as following:

```python <Script> [Input File] [Extras]```

Input file = The puzzle input saved as a file

Extras = Any extra arguments required for the script. Extras, if any required, are listed below.

### For eg:

- Day 1: python 1part1.py \<Input File\>
- Day 3: python 3part1.py \<Input File\>
- Day 6: python 6.py \<Input File\>
- Day 7: python 7part2.py \<Input File\> \<Extras\>

### Extras

The following are the required extras for the scripts:

- Day 7, Part 2: Output of 7part1.py

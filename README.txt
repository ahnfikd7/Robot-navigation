# Robot Navigation Challenge

To run in the terminal:
 python3 robot_navigation.py input_file.txt output_file.txt

If any avocado is unreachable in the provided input text file, the program outputs the following message to the terminal:
 Complete path to all avocados is not possible due to accessibility issues.

I spent approximately 5 hours on this challenge including coding, testing, and documenting.



I tested the program with couple of test cases:

Test case 1:
Input:
################
###..#@.....@#.#
##x....####..#.#
###.....#...##.#
#######.#.###..#
#@#...#..@....##
#...#...#.###.@#
################
Output:
42
1,6
1,12
6,14
5,9
5,1


Test case 2:
Input:
################
###...........##
##x.........@.##
###...........##
################
Output:
10
2,12

Test case 3:
Input:
################
###..#@.....@#.##
##x....####..#.##
###.....#...##.##
#######.#.###..##
################
Output:
11
1,6
1,12

Test case 4:
Input:
################
###..#@.....@#.##
##x.#.####..#.##
###.....#...##.##
#######.#.###..##
###@###.##@###.##
################
Output:
Complete path to all avocados is not possible due to accessibility issues.

Test case 5:
Input:
################
###...........##
##x...........##
###...........##
####.........###
#####.......####
######.....#####
#######...######
########.@#######
################
Output:
13
8,9

Test case 6:
Input:
################
####..####..####
##x..##.##..####
###..##.######.#
##.............##
######..######.##
#####...#####..##
####....####...##
#@##############
################
Output:
Complete path to all avocados is not possible due to accessibility issues.


Test case 7:
Input:
####
##x#
#@##
####
Output:
Complete path to all avocados is not possible due to accessibility issues.



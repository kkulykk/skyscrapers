# Skyscrapers
The program helps to find out whether there is a winning combination on a board.

There are 7 functions:
1. read_input - Read game board file from path.
2. left_to_right_check - Check row-wise visibility from left to right.
3. check_not_finished_board - Check if skyscraper board is not finished, i.e., '?' present on the game board.
4. check_uniqueness_in_rows - Check buildings of unique height in each row.
5. check_horizontal_visibility - Check row-wise visibility (left-right and vice versa)
6. check_columns - Check column-wise compliance of the board for uniqueness (buildings of unique height) and visibility (top-bottom and vice versa).
7. check_skyscrapers - Main function to check the status of skyscraper game board.

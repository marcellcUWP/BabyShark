"""----------------------------------------------------------------
Name:       Carson Marcell
Assignment: Lab - Baby Shark
Course:     CS 1430, Section X, Fall 2026
Purpose:    This program is designed to be practice for Python
            functions

Input: None

Output: The sound Baby Shark, with three verses:
        Baby Shark,
        doo-doo-doo-do-do-do-do *3
        Baby Shark!
        Mommy Shark,
        doo-doo-doo-do-do-do-do *3
        Mommy Shark!
        Daddy Shark,
        doo-doo-doo-do-do-do-do *3
        Daddy Shark!
----------------------------------------------------------------"""

##############
# CONSTANTS
##############
REPEAT = 3
repeat = 0

def verse_maker(family):
    for repeat in range(REPEAT):
        print(f"""{family} Shark,
doo-doo-doo-do-do-do-do""")
        repeat += 1
    print(f"{family} Shark!")

def main():
    verse_maker("Baby")
    verse_maker("Mommy")
    verse_maker("Daddy")


if __name__ == "__main__":
    main()

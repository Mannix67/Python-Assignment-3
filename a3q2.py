from random import randint

EvenWins = 0;
OddWins = 0;
Round = 1;


# Function that returns the outcome of rotation. # This functions generates a number between 1 and 10 and will return "Head"
# # if the number is even and will return "Tail" if the number is odd.
def place_penny():
    r = randint(1, 10);

    if r % 2 == 0:
        return "heads";
    else:
        return "tails";


# Function that displays Menu as seen in the assignment brief
def display_messageToConsole():
    print("This program allows you to play matching pennies agains a computer oppontent");
    print("the game will last 5 rounds");
    print("At the start of a round, each player picks either heads or tails");
    print("If the choices match, you win (+1 to you -1 to  computer");
    print("If the choices do not match,you lose (-1 to you -1 to  computer");



# module includes a main() function to check if the module has been launched in the main scope below:
if __name__ == "__main__":
    # Displaying messageToConsole
    display_messageToConsole();

for Round in range(1, 6): #5 rounds

    print("Beginning Round", Round);
    # Accepting the choice from the user.
    choice = input("\nEnter heads or tails: ");     #instruct user to enter heads or tails
    while (choice != "heads" and choice != "tails"):
        choice = input("\nYou did not enter heads or tails: ");   #incase use inputs choice other than heads or tails.

    pn1 = choice;
    pn2 = place_penny();     #creating variables pn1 and pn2 to go through the outcomes of the game.

    if pn1 == pn2 == "heads":   #if both coins lands on heads , even gets +1 point
        EvenWins += 1;
        OddWins -= 1;
        print("You chose", pn1);
        print("and the opponent chose", pn2);
        print("You Win!");
    if pn1 == pn2 == "tails":     #if both coins lands on tails, even gets +1 point.
        EvenWins += 1;
        OddWins -= 1;
        print("You chose", pn1);
        print("and the opponent chose", pn2);
        print("You Win!");

    if pn1 != pn2:               #if penny 1 does not equal to penny two then odds gets +1 point
        OddWins += 1
        EvenWins -= 1
        print("You chose", pn1);
        print("and the opponent chose", pn2);
        print("You lose!");

    print("Round", Round, "Over");

#to print at the end of the game, tells user that all rounds are complete and gives the final score of the game.
print("\n\nAll rounds complete!!!");
print("Your Score:", EvenWins);
print("Opponent Score:", OddWins);




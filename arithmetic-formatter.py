def arithmetic_arranger(problems, show_answers=False):

    # Return that there is too many problems to work with in the current implementation
    if len(problems) > 5:
        return "Error: Too many problems."

    # TODO: Refactor this 
    # Setup and build the problems to display in a vertical operation
    firstSet = []
    secondSet = []
    thirdSet = []
    fourthSet = []
    for problem in problems:
        brokenUp = problem.split(' ')
        
        # Return error if operator isn't minus and addition
        if brokenUp[1] != "-" and brokenUp[1] != "+":
            return "Error: Operator must be '+' or '-'."

        # Return error if numbers are more than a length of four
        if len(brokenUp[0]) > 4 or len(brokenUp[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Return error if user sent data are not digits
        if not brokenUp[0].isdigit() or not brokenUp[2].isdigit():
            return "Error: Numbers must only contain digits."

        # Retrieve the longest digits
        mostChars = sorted(brokenUp, key=len)[2]

        # Insert the top number for the top part of the equation
        firstSetFormatted = brokenUp[0].rjust(len(mostChars) + 2)
        
        # Insert the operator and second number for the bottom part of the equation
        secondSetFormatted = brokenUp[2].rjust(len(mostChars) + 1)
        secondSetFormatted = secondSetFormatted.replace("", brokenUp[1], 1)

        # Create the divider for the equation
        divider = ""
        while len(divider) < len(mostChars) + 2:
            divider += "-"

        # Do the calculation for either addition or subtraction
        if brokenUp[1] == "+":
            total = int(brokenUp[0]) + int(brokenUp[2])
        else:
            total = int(brokenUp[0]) - int(brokenUp[2])
        fourthSetFormatted = str(total).rjust(len(divider))

        # Add the solution to the equation lists
        firstSet.append(firstSetFormatted)
        secondSet.append(secondSetFormatted)
        thirdSet.append(divider)
        fourthSet.append(fourthSetFormatted)

    # Join the arrays to represent as strings
    firstSetFinished = "    ".join(firstSet)
    secondSetFinished = "    ".join(secondSet)
    thirdSetFinished = "    ".join(thirdSet)
    fourthSetFinished = "    ".join(fourthSet)

    # Put them together in one string
    problems = f"{firstSetFinished}\n{secondSetFinished}\n{thirdSetFinished}"

    # Show solution if the user send the flag
    if show_answers:
        problems += f"\n{fourthSetFinished}"

    return problems

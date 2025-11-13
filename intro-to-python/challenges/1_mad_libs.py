# Write a story with some words missing
story: str = """
Roses are {colour}
Violets are {colour2}
Sugar is {adjective}
And so are you
"""

# Ask the user to provide the missing words ̰
colour: str = input("Enter a colour: ")
colour2: str = input("Enter another colour: ")
adjective: str = input("Enter an adjective: ")

# Display the final story
print(story.format(colour=colour, colour2=colour2, adjective=adjective))

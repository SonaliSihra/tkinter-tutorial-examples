
# Start with an empty list. You can 'seed' the list with
#  some predefined values if you like.
names = []

# Set new_name to something other than 'quit'.
new_name = ''

# Start a loop that will run until the user enters 'quit'.
while new_name != '0':
    # Ask the user for a name.
    new_name = input("Please tell me someone I should know, or enter 'quit': ")

    # Add the new name to our list.
    names.append(new_name)

# Show that the name has been added to the list.
print(names)
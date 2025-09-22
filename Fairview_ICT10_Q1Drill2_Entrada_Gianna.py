from pyscript import display, document

# Get info and show message
def show_profile(e):
    name = document.getElementById("name").value
    age = document.getElementById("age").value
    school = document.getElementById("school").value

    # Multiline string with escape characters
    message = f"Student Profile:\n\tName: \"{name}\"\n\tAge: {age}\n\tSchool: \"{school}\""
    display(message, target="output")
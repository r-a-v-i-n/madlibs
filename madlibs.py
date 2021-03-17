"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")

@app.route('/game')
def show_madlib_form():
    """Get user's response re: if they'd like to play a game."""

    player_choice = request.args.get("game")

    if player_choice == "Yes":
        return render_template("game.html")
    elif player_choice == "No":
        return render_template("goodbye.html")
    else:
        return None

@app.route('/madlib')
def show_madlib():
    """Return madlib from player's choices in /game."""

    input_name = request.args.get("person")
    input_color = request.args.get("color")
    input_noun = request.args.get("noun")
    input_adj = request.args.get("adjective")

    if input_color[0] in "aeiou":
        input_color = 'an' + ' ' + input_color
    else:
        input_color = 'a' + ' ' + input_color
        
    return render_template("madlib.html",
                            person=input_name, color=input_color, 
                            noun=input_noun, adjective=input_adj)


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")

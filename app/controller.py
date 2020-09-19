from flask import render_template, request, session
from app.models.player_list import *
from app.models.game import *
from app.models.computer import *
from app import app

app.secret_key = 'dljsaklqk24e21cjn!Ew@@dsa5'



@app.route('/')
def index():
    return render_template('index.html', title='Home', players=players)

@app.route('/play')
def people():
    return render_template('play.html', title='2 player mode', players=players)

@app.route('/AI')
def computer():
    return render_template('ai.html', title="Computer", players=players)

@app.route('/player-2')
def second_player():
    return render_template('player_2.html', title="Second player", players=players)

@app.route('/choice', methods=['GET','POST'])
def user_choice():

    player1Name = request.form['player_1']
    player1Choice = request.form['player_1_choice']
    first_player= Player(player1Name, player1Choice)
    add_player(first_player)

    session["player1Choice"] = player1Choice
    return render_template('player_2.html', title='2 player mode', player=player1Choice)

@app.route('/choice2', methods=['POST'])
def user_choice_2():

    player2Name = request.form['player_2']
    player2Choice = request.form['player_2_choice']

    second_player= Player(player2Name, player2Choice)
    add_player(second_player)
    first_player = session.get("player1Choice", None)

    print(first_player)
    print(second_player.choice)

    winner = winner_of_game(first_player, second_player.choice)
    return render_template('result.html', title='2 player mode', players=players, winner=winner)



@app.route('/ai', methods=['POST'])
def against_computer():
    playerName = request.form['player']
    playerChoice = request.form['player_choice']

    newPlayer = Player(playerName, playerChoice)
    computer = computer_choice()
    print(playerChoice)
    print (computer)

    winner_1 = winner(newPlayer, computer)


    return render_template('result.html', title='AI mode', winner=winner_1)






    

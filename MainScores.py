from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def score_server():
    try:
        with open("Scores.txt", 'r') as user_score:
            content = user_score.read()
            return render_template('game_scores.html', score=content)

    except Exception as BAD_RETURN_CODE:
        with open("alt_score.txt", 'r') as user_score:
            content = user_score.read()
            return render_template('alt_scores.html', score=content, ERROR=BAD_RETURN_CODE)

if __name__ == "__main__":
    #port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=80)
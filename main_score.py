from flask import Flask, render_template
from score import calc_total_score, read_from_score_file

app = Flask(__name__)

@app.route('/')
def get_one():
    try:
        scores = read_from_score_file()
        scores_to_render = [i.split(" = ") for i in scores]
        total_score = calc_total_score(scores)
        return render_template('scores.html', scores=scores_to_render, total_score=total_score)
    except Exception as e:
        return render_template('error.html', error=e)


if __name__ == '__main__':
    app.run(debug=True)

from feedbackApp import app


if __name__ == '__main__':
	if app.env == 'dev':
		app.run(debug=True)
	else:
		app.run(debug=False)

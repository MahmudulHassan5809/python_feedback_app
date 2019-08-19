from flask import render_template,url_for,flash,redirect,request,Blueprint,abort
from feedbackApp.core.forms import FeedBackForm
from feedbackApp.models import Feedback
from feedbackApp import db,mail
from flask_mail import Message


core = Blueprint('core',__name__)


@core.route("/")
@core.route("/home")
def home():
	return render_template('index.html')

@core.route("/send-feedback",methods=['GET','POST'])
def send_feedback():
	form = FeedBackForm()
	if request.method == 'POST' and form.validate() and form.validate_on_submit():
		#customer = request.form['customer']
		if db.session.query(Feedback).filter(Feedback.customer == form.customer.data).count() == 0:

			msg = Message('New Feedback Submission',
                  sender='noreply@demo.com',
                  recipients=['mahmudul.hassan240@gmail.com'])

			msg.body = f'''New Feedback Submission:
					   Customer: {form.customer.data}
					   Rating: {form.rating.data}
					   Dealer: {form.dealer.data}
					   Comments: {form.comments.data}
					'''

			mail.send(msg)

			feed_back = Feedback(customer=form.customer.data,dealer=form.dealer.data,rating=form.rating.data,comments=form.comments.data)
			db.session.add(feed_back)
			db.session.commit()

			flash('FeedBack SuccessFully Send','success')
			return redirect(url_for('core.success'))
		else:
			flash('You Have Already Submitted FeedBack','warning')
			return redirect(url_for('core.home'))
	return render_template('send_feedback.html',title='Create Post',form=form)


@core.route("/success")
def success():
	return render_template('success.html')

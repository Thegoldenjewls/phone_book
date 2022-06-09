from flask import Blueprint, render_template

contactForm = Blueprint('contactForm', __name__, template_folder = 'contactForm-templates')

@contactForm.route('/contactForm', methods = ['POST'])
def enterInfo():
    return render_template('contactForm.html')
from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint('main', __name__, template_folder='../templates')

@main.route('/')
def index():
  return render_template('index.html')
from flask import Flask,render_template, url_for, redirect
import pandas as pd
import os
from os import listdir
import argparse


app = Flask(__name__)


@app.route('/<code>')
def hello_world_base(code):
	return(render_template('index.html', code=code))

if __name__ == '__main__':
	app.run()
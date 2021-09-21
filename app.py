#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def user():
  return render_template('index.html')
if __name__ == '__main__':
  app.run(debug = True, port= 5000)
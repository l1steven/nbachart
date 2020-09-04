from nbaapp import app
from flask import render_template
from nba_api.stats.endpoints import shotchartdetail
import os
import random

@app.route('/')
@app.route('/index.html')
def index():
    #player=shotchartdetail.ShotChartDetail(player_id='1628366')
    ran=random.choice([1,2])
    if(ran==1):
        return render_template('index.html',title='Steven Li')
    else:
        return render_template('index.html',title='Li Steven')
@app.route('/about.html')
def about():
    filename='\static/shot_chart.png'
    return render_template('about.html',chart=filename)
        
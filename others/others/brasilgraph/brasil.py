#import io
import json
from signal import siginterrupt

#Flask
from flask import send_file
from flask import Flask
from flask_restful import Resource, Api
from importlib.resources import Resource
from flask import request
import numpy as np
import os

# img
from PIL import Image
from numpy import asarray
# plot
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")


app = Flask(__name__)
api = Api(app)


@app.route('/plot/', methods=['POST'])

def plot():
    info = request.get_data()
    info = json.loads(info)
    plt.axis('off')
    plt.figure(figsize=(8, 6))
    a = sns.scatterplot(info['long'],info['lat'],hue = info['hue'],legend=False).figure
    os.remove('./temp2.png')
    a.savefig('temp2.png')
    img = Image.open('temp2.png')
    return({'img': asarray(img).tolist()})


@app.route('/imgplot/', methods=['GET'])
def get_image():
    return send_file('./temp2.png')#, mimetype='image/gif')

if __name__=='__main__':
    app.run(debug=True)

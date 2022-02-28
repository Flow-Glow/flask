import shutil

from flask import Flask

from flask import render_template

from flask_bootstrap import Bootstrap

import requests

import urllib.request

from PIL import Image

import urllib





app = Flask(__name__)

# make an app route
@app.route('/',methods=['GET','POST'])
def get_dog_images():
    # get the dog images
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    # get the response
    response_json = response.json()
    # get the image url
    image_url = response_json['message']
    print(image_url)
    # get the image
    image = Image.open(urllib.request.urlopen(image_url))
    # resize the image
    image = image.resize((300,300))
    # save the image
    image.save('static/dog.jpg')
    # return the image
    return render_template('index.html')




if __name__ == '__main__':



    #get_dog_images() if this is commented out



    app.run(host="0.0.0.0")
import os
from flask import Flask
from flask import render_template
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random

msg_list = [
    'Did you really read the debug message say?',
    # 'Maybe put some print statements in?',
    'You use tabs instead of spaces? That might be your problem',
    'Have you googled your error?',
    # 'Have you read the docs?',
    'I ate your rubber ducky. Sorry...',
    'Maybe try ipdb or Werkzeug for interactive debugging',
    'It might be a problem between your chair and your keyboard',
    'I recommend hard liquor',
    'The problem is that you pushed code after 5pm on Friday',
    'Maybe the problem is your thinking in java',


    ]


app = Flask(__name__, static_url_path='/static')

@app.route("/")
def hello():
    img = Image.open("sample_in.jpg")
    draw = ImageDraw.Draw(img)
    fonts_path = os.path.join(os.path.dirname(__file__), 'micross.ttf')
    font = ImageFont.truetype(fonts_path, 14)
    msg = random.choice(msg_list)
    # w, h = draw.textsize(msg)
    draw.text((250, 10), msg, fill="black", font=font)
    # draw.text((150, 0),"Did you check your spelling on your variables?",(0,0,255),font=font)
    image = 'static/sample-out.jpg'
    img.save(image)
    return render_template('snarky.html', image=image)

if __name__ == "__main__":
    app.run()

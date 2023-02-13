from flask import Flask

app = Flask(__name__)


@app.route('/')
def mars_1():
    return "Миссия Колонизация Марса"


@app.route('/index')
def mars_2():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def mars_3():
    spisok = ['Человечество вырастает из детства.',
              'Человечеству мала одна планета.',
              'Мы сделаем обитаемыми безжизненные пока планеты.',
              'И начнем с Марса!',
              'Присоединяйся!']
    return '<br>'.join(spisok)


@app.route('/image_mars')
def mars_image():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="static/mars.jpg" alt="здесь должна была быть картинка, но не нашлась">
                    <p>Вот она какая, красная планета</p>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
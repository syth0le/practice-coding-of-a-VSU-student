from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session

app = Flask(__name__)


@app.route('/')
def second_page():
    ext_page = {'address': '127.0.0.1:5000/index'}
    return '''
    <html>
        <head>
            <title>User's Page</title>
        </head>
        <body>
            <a href="home">home page</a>
        </body>
    </html>
    '''


@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # выдуманный пользователь
    return '''
<html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
    <h1>Hello, ''' + user['nickname'] + '''</h1>
  </body>
</html>
'''


@app.route("/home/")
def home():
    return '''
    <!DOCTYPE html>
<html class="yui3-js-enabled" lang="ru" lang="ru" dir="ltr" xml:lang="ru"><head>
		<meta charset="UTF-8">
		<title>TABLE</title>
		<style>
	.texrender {vertical-align:middle;}
	#page-admin-index h2 {
	padding:0px;
	padding-left: 24px;
	padding-top: 0;
	}
	.path-grade-report-grader .gradeparent {
	overflow: auto;
	}
	.topics span.hidden {
	    display: none;
	}
	.topics .hidden a{
	color:gray;
	}
	.plagiarism_apru_submissioncheck .singleselect{
	display: none;
	}
	</style>
	</head>
	
	<body>

		<header class="navbar navbar-fixed-top moodle-has-zindex" role="banner"> <!-- дописать классы нормально-->
			<div>
				<div id="headleft">
					<a href="">Посещаемость какой то группы</a> <!-- дописать ссылку-->
				</div>
			</div>
		</header>

		<div id="textcontainer-wrap">
			<div id="textcontainer">
				<div class="thetitle">
				<div class="innertitle"></div>
			</div>
				<div id="vsu_title">
					Электронный университет ВГУ
				</div>
			</div>
		</div>

		<div class="page-container" id="page">
			<div>
			<div>
				</div><table border="3">
				<caption><h2>Учет посещаемости</h2></caption>
			
				<tbody><tr>
					<th class="number">№</th>
					<th class="name">ФИО студента</th>
					<th class="rate">Рейтинг</th>
					<th class="percents">Посещаемость в %</th>
					<th class="status">Статус</th>
					<th class="all">Всего занятий</th>
					<th class="plus">Посещения</th>
					<th class="minus">Пропуски</th>
					<th class="smth">Заметки</th>
				</tr> 
				<tr>
					<td></td>
					<td><br></td>
					<td></td>
					<td></td>
					<td></td>
					<td></td>
					<td></td>
					<td></td>
					<td></td>
			    </tr>
                    <tr>
					<td></td>
					<td><br></td>
					<td></td>
					<td></td>
					<td></td>
					<td></td>
					<td></td>
					<td></td>
					<td></td>
			    </tr>
                    <tr>
					<td></td>
					<td><br></td>
					<td></td>
					<td></td>
					<td></td>
					<td></td>
					<td></td>
					<td></td>
					<td></td>
			    </tr>
                    <tr>
					<td></td>
					<td><br></td>
					<td></td>
					<td></td>
					<td></td>
					<td></td>
					<td></td>
					<td></td>
					<td></td>
			    </tr>
                    <tr>
					<td></td>
					<td><br></td>
					<td></td>
					<td></td>
					<td></td>
					<td></td>
					<td></td>
					<td></td>
					<td></td>
			    </tr>
                    <tr>
					<td></td>
					<td><br></td>
					<td></td>
					<td></td>
					<td></td>
					<td></td>
					<td></td>
					<td></td>
					<td></td>
			    </tr>
                    
                </tbody></table><br>
			<form>
	  			<button type="submit">Подтвердить</button>
			</form>
			</div> 
			<!-- закончилась часть мейн блока -->
			<footer>
				<div>
					<div class="logininfo">Личный кабинет пользователя: <a title="Просмотр профиля" href="ссылка на пользователя">ФИО студента</a> (<a href="ссылка на выход из профиля">Выход</a>)</div>
					<div class="homelink"><a href="https://edu.vsu.ru/course/view.php?id=3813">Посещаемость 1к ИВТ</a></div>
					<div><a href="https://download.moodle.org/mobile?version=2018051701.04&amp;lang=ru&amp;iosappid=633359593&amp;androidappid=com.moodle.moodlemobile">Скачать мобильное приложение</a></div>

					<div class="чо то еще вставить">
						<a href="">херня еще та</a>
					</div>	
					<!-- подумать над футером -->
				</div>
			</footer>
		</div>

	


</body></html>
    '''


@app.route('/visits-counter/')
def visits():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1  # чтение и обновление данных сессии
    else:
        session['visits'] = 1  # настройка данных сессии
    return "Total visits: {}".format(session.get('visits'))


@app.route('/delete-visits/')
def delete_visits():
    session.pop('visits', None)  # удаление данных о посещениях
    return 'Visits deleted'


@app.route("/session/")
def updating_session():
    res = str(session.items())

    cart_item = {'pineapples': '10', 'apples': '20', 'mangoes': '30'}
    if 'cart_item' in session:
        session['cart_item']['pineapples'] = '100'
        session.modified = True
    else:
        session['cart_item'] = cart_item
    return res


@app.route("/status")
def status():
    return {
        'status': True
    }


app.run()

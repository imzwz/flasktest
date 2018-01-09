from flask import Flask, render_template, request, redirect, url_for
from flask.ext.bootstrap import Bootstrap, WebCDN, ConditionalCDN, BOOTSTRAP_VERSION, JQUERY_VERSION, HTML5SHIV_VERSION, RESPONDJS_VERSION 
from flask.ext.sqlalchemy import SQLAlchemy 
from db import WeiboMysql

app = Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://winn:123456@127.0.0.1:3306/weibo?charset=utf8'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
def change_cdn_domestic(tar_app):
    static = tar_app.extensions['bootstrap']['cdns']['static']
    local = tar_app.extensions['bootstrap']['cdns']['local']

    def change_one(tar_lib, tar_ver, fallback):
        tar_js = ConditionalCDN('BOOTSTRAP_SERVE_LOCAL', fallback,
                WebCDN('//cdn.bootcss.com/' + tar_lib + '/' + tar_ver + '/'))
        tar_app.extensions['bootstrap']['cdns'][tar_lib] = tar_js

    libs = {'jquery': {'ver': JQUERY_VERSION, 'fallback': local},
            'bootstrap': {'ver': BOOTSTRAP_VERSION, 'fallback': local},
            'html5shiv': {'ver': HTML5SHIV_VERSION, 'fallback': static},
            'respond.js': {'ver': RESPONDJS_VERSION, 'fallback': static}}
    for lib, par in libs.items():
        change_one(lib, par['ver'], par['fallback'])

change_cdn_domestic(app)

@app.route('/user/<name>',methods=['GET','POST'])
def user(name):
    #if request.method =='POST':
    #    content = request.form['content']
    #    return render_template('user1.html', name=content)
    return render_template('user.html', name=name)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        content = request.form['content']
        print content
        return redirect(url_for('eventsearch', query=content)) 
    else:
        return render_template('event/index_new.html', title_name = 'homepage')
    

@app.route('/eventsearch?query=<query>', methods=['GET'])
def eventsearch(query):
    query_str = "%" + query + "%"
    page = request.args.get('page', 1, type=int)
    print WeiboMysql.query.filter(WeiboMysql.content.like(query_str)).count()
    pagination = WeiboMysql.query.filter(WeiboMysql.content.like(query_str)).order_by(WeiboMysql.time.desc()).paginate(page, per_page=10, error_out=False)
    weibos = pagination.items
    
    return render_template('event/eventsearch.html', query = query, weibos=weibos, pagination=pagination)

@app.route('/eventmap?query=<query>')
def eventmap(query):
    return render_template('event/eventmap.html', query=query)

@app.route('/device?query=<query>')
def device(query):
    return render_template('event/device_new.html', query=query)


@app.route('/getinfo')
def getinfo():
    return render_template('event/getinfo.html', title_name = 'getinfo')

@app.route('/help')
def help():
    return render_template('event/help.html', title_name = 'help')

@app.route('/kunming')
def kunming():
    return render_template('event/kunming.html', title_name = 'kunming')

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap, WebCDN, ConditionalCDN, BOOTSTRAP_VERSION, JQUERY_VERSION, HTML5SHIV_VERSION, RESPONDJS_VERSION 

app = Flask(__name__)
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

@app.route('/abstract/')
def abstract():
    return render_template('abstract.html', title_name = 'abstract demo')

@app.route('/')
def home():
    return render_template('home.html', title_name = 'welcome')

if __name__ == '__main__':
    app.run()

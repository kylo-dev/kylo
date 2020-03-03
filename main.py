import flask
import os

__Version__ = 'beta0.1'
__Author__ = ['littlefish12345']

def read_html(name):
    f = open(os.path.join(os.getcwd(),'html/' , name+'.html'),'r')
    html = f.read()
    f.close()
    return html

app = flask.Flask(__name__)

@app.route('/css/<css_name>') #css文件处理
def get_css_file(css_name):
    css_name = ''.join(css_name.split('..')) #稍微预防一下
    css_name = ''.join(css_name.split('/'))
    css_name = ''.join(css_name.split('\\'))
    print(os.path.join(os.getcwd(),'html','css',css_name))
    if os.path.isfile(os.path.join(os.getcwd(),'html','css',css_name)): #有文件就返回文件内容
        f = open(os.path.join(os.getcwd(),'html','css',css_name),'r')
        css_file = f.read()
        f.close()
        return flask.Response(css_file,mimetype='text/css')
    else:
        flask.abort(404) #没文件就返回404

@app.route('/js/<js_name>') #js文件处理
def get_js_file(js_name):
    js_name = ''.join(js_name.split('..')) #稍微预防一下
    js_name = ''.join(js_name.split('/'))
    js_name = ''.join(js_name.split('\\'))
    print(os.path.join(os.getcwd(),'html','js',js_name))
    if os.path.isfile(os.path.join(os.getcwd(),'html','js',js_name)): #有文件就返回文件内容
        f = open(os.path.join(os.getcwd(),'html','js',js_name),'r')
        js_file = f.read()
        f.close()
        return flask.Response(js_file,mimetype='text/js')
    else:
        flask.abort(404) #没文件就返回404

@app.route('/statics',defaults={'path':''}) #处理static
@app.route('/statics/<path:path>')
def get_static_file(path):
    static_name = ''.join(path.split('..')) #稍微预防一下
    static_list = static_name.split('/')
    static_path = os.path.join(os.getcwd(),'html','statics')
    for strs in static_list:
        static_path = os.path.join(static_path,strs)
    print(static_path)
    if os.path.isfile(static_path): #有文件就返回文件内容
        f = open(static_path,'rb')
        static_file = f.read()
        f.close()
        return static_file
    else:
        flask.abort(404) #没文件就返回404

@app.route('/')
def index():
    return read_html('index')

app.run(debug=True,host='',port=5000)

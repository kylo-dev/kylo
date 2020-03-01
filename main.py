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

@app.route('/assets',defaults={'path':''}) #处理assets
@app.route('/assets/<path:path>')
def get_assets_file(path):
    assets_name = ''.join(path.split('..')) #稍微预防一下
    assets_list = assets_name.split('/')
    assets_path = os.path.join(os.getcwd(),'html','assets')
    for strs in assets_list:
        assets_path = os.path.join(assets_path,strs)
    if os.path.isfile(assets_path): #有文件就返回文件内容
        f = open(assets_path,'rb')
        assets_file = f.read()
        f.close()
        return flask.Response(assets_file,mimetype='text/css')
    else:
        flask.abort(404) #没文件就返回404

@app.route('/images',defaults={'path':''}) #处理images
@app.route('/images/<path:path>')
def get_images_file(path):
    images_name = ''.join(path.split('..')) #稍微预防一下
    images_list = images_name.split('/')
    images_path = os.path.join(os.getcwd(),'html','images')
    for strs in images_list:
        images_path = os.path.join(images_path,strs)
    if os.path.isfile(images_path): #有文件就返回文件内容
        f = open(images_path,'rb')
        images_file = f.read()
        f.close()
        return images_file
    else:
        flask.abort(404) #没文件就返回404

@app.route('/')
def index():
    return read_html('index')

app.run(debug=True,host='',port=5000)

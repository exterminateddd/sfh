from flask import Flask, send_from_directory, jsonify, request, Response, make_response
from flask_cors import CORS
from json import loads, dumps
from random import randint
from os import path, remove
from time import time, sleep
from threading import Thread as T

app = Flask('sfh-flask')
app.config['UPLOAD_FOLDER'] = './file_storage'

CORS(app, expose_headers=['foo', 'content-disposition'])


def generate_filecode():
    filecode = ''.join(['ABCDEFGHIJKLMNOPQRSTUVWXYZ'[randint(0, 25)] for _ in range(6)])
    if filecode not in loads(open('./files.json', 'r+').read()).keys():
        return filecode
    else:
        return generate_filecode()


@app.route('/echo')
def echo_route():
    return 'ECHO WORKING'


@app.route('/check_if_file_exists/<string:code>', methods=["GET"])
def check_if_file_exists_route(code: str):
    files = loads(open('./files.json', 'r+').read())
    return jsonify({
        'result': code in files.keys()
    })


@app.route('/download_file/<string:code>', methods=["GET"])
def download_file_route(code: str):
    file_data = loads(open('./files.json', 'r+').read())[code]
    extension = file_data['extension']
    resp = make_response(send_from_directory(app.config['UPLOAD_FOLDER'], code+'.'+extension, as_attachment=True))
    resp.mimetype = file_data['mimetype']
    resp.headers.add('foo', 'bar')
    resp.headers.add('Access-Control-Expose-Headers', 'foo, Content-Disposition')
    return resp


@app.route('/upload_file', methods=["POST"])
def upload_file_route():
    if 'file' not in request.files:
        return Response('File not provided', status=415, mimetype='application/json')
    
    file_lifetime = request.form.get('lifetime', 600)
    uploaded_file = request.files['file']
    filecode = generate_filecode()
    extension = uploaded_file.filename.split('.')[-1]
    uploaded_file.save(path.join(app.config['UPLOAD_FOLDER'], filecode+'.'+extension))

    files_json = loads(open('./files.json', 'r+').read())
    files_json[filecode] = {
        'uploaded_at': time(),
        'expires_at': time()+int(file_lifetime),
        'extension': extension,
        'mimetype': uploaded_file.mimetype
    }
    open('./files.json', 'w+').write(dumps(files_json, indent=4))

    return Response(filecode, status=200, mimetype='application/json')


def check_file_expirations():
    while True:
        files_json = loads(open('./files.json', 'r+').read())
        filecodes_to_remove_from_json = []
        
        for code, file_data in files_json.items():
            if file_data.get('expires_at', 0)<=time():
                try:
                    remove(app.config['UPLOAD_FOLDER']+'/'+code+'.'+file_data['extension'])
                except FileNotFoundError:
                    print('file '+code+' not found')
                filecodes_to_remove_from_json.append(code)
                print('file '+code+' was deleted due to expiration.')
        for code in filecodes_to_remove_from_json:
            files_json.pop(code)
            open('./files.json', 'w+').write(dumps(files_json, indent=4))
        sleep(5)

background_thread = T(name='bg', target=check_file_expirations)
background_thread.start()

app.run(debug=True, host='0.0.0.0')

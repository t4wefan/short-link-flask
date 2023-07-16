from flask import Flask, request, jsonify, redirect
import random
import os

def save_url(url_id, url):
    path = "urls"
    if not os.path.exists(path):
        os.makedirs(path)

    filename = f"{url_id}.json"

    filepath = os.path.join(path, filename)

    with open(filepath, "w") as f:
        f.write(url)
        print(f"Token {url} saved to file {filename}")

def read_url(url_id):
    users_dir = "urls"
    filename = f"{url_id}.json"
    token_file_path = os.path.join(users_dir, filename)
    
    if os.path.exists(token_file_path):
        with open(token_file_path, "r") as f:
            token = f.read().strip()
        return token
    else:
        return ''

def check_url1(url_id):
    filename = f"urls/{url_id}.json"
    status = True if os.path.isfile(filename) else False
    return status


app = Flask(__name__)

def make_id():
    id = random.randint(100, 9999)
    while True:
        if check_url1(url_id=id) == True:
            id = random.randint(100, 10000)
        
        else:
            break
    return id



@app.route('/', methods=['POST'])
def add_url():
    url = request.form.get('url', '')
    id = request.form.get('id','')
    
    if id in [None, '']:
         id =  make_id()
    elif check_url1(url_id=id) == True :
        status = 'error'
        url = ''
        info = 'id already exists'

        return jsonify({
            'status': status,
            'url': url,
            'info': info

        })
    else:
        id = id
    
    save_url(url_id=id, url=url)
    status = 'success'
    print('url added  ' + url + ' id=' +str(id))
    return jsonify({
            'status': status,
            'url': str(request.url + 's/' + str(id)) 
            })  
    

@app.route('/s/<int:id>')
def redirect1(id):
    id = id
    url = read_url(url_id=id)
    if url == '':
        status = 'error'
        url = ''

        return jsonify({
            'status': status,
            'url': url

        })
    else :
        print('redirected to ' +  url)
        return redirect(str(url))
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)
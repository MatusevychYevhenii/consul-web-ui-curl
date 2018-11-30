#!/usr/bin/env python
from flask import Flask, request, render_template
import requests, json
import sys
import getopt

server = 'localhost'
port = 8500

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('init.html', IP = server, Port = port)

@app.route('/create', methods = ['POST'])
def create():
    if not request.form['id_create'] or not request.form['name'] or \
            not request.form['address'] or not request.form['port']:
        return render_template("error.html")

    try:
        int(request.form['port'])
    except ValueError:
        return render_template("error.html")

    result = json.dumps({"ID": request.form['id_create'],
                        "Name": request.form['name'],
                        "Address": request.form['address'],
                        "Port": int(request.form['port'])})

    server_url = "http://" + server + ':' + port + '/v1/agent/service/register'
    r = requests.put(server_url, data = result)
    result = request.form
    return render_template("create.html", result = result)

@app.route('/delete', methods = ['POST'])
def delete():
    if not request.form['id_delete']:
        return render_template("error.html")

    result = request.form['id_delete']
    server_url = "http://" + server + ':' + \
                port + '/v1/agent/service/deregister/' + result
    r = requests.put(server_url)
    return render_template("delete.html")

def usage():
    print('--server={consul ip/dns for requests}')
    print('--port={consul port for requests}')
    print('default: server=localhost, port=9100')

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], 's:p:h', ['server=', 'port='])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit(2)
        elif opt in ('-s', '--server'):
            server = arg
        elif opt in ('-p', '--port'):
            port = arg
        else:
            usage()
            sys.exit(2)
    app.run(host = '0.0.0.0', port=int("80"), debug=True)

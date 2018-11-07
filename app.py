from flask import Flask
app = Flask(__name__)

server_date=''
server_min=''

@app.route('/game/<date>/<min>')
def server_side(date,min):
   global server_date
   global server_min
   if min=='0':
     if server_date==date:
       min=server_min
       server_min='0'
       return "APP "+min
     else:
       return "NO TA"+server_date
   server_date=date
   server_min=min
   return 'DONE'


if __name__ == '__main__':
   app.run(debug = True)

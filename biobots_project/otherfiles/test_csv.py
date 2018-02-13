from flask import Flask, make_response  
app = Flask(__name__)

@app.route('/')  
def download_csv():  
    csv = 'foo,bar,baz\nhai,bai,crai\n'  
    response = make_response(csv)
    cd = 'attachment; filename=mycsv.csv'
    response.headers['Content-Disposition'] = cd 
    response.mimetype='text/csv'

    return response
	
	
if __name__ == '__main__':
	app.run(debug=True) #launch app 
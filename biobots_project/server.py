from os import path, getcwd
import json 
import pandas as pd
from flask import Flask, render_template, request, redirect, make_response, session 

###############################
### Intialize josn/pd data ### 
path = path.join(getcwd(), 'bioprint-data.json' )
with open(path) as json_data:
    data = json.load(json_data) #store json data as string 
data = pd.io.json.json_normalize(data) #convert to pandas df for speed and ease 

def col_rename(): #rename cols for easy handling ('_' better than '.')
    cols = [] 
    for col in data.columns:
        name = (str(col).split('.'))
        new_col = '_'.join(name)
        cols.append(new_col)
    data.columns = cols
col_rename() #dataframe fully initialzied 



###############################
### Setup Website for users ###
app = Flask(__name__)
app.secret_key = 'mnalavadi'

#user types in their serial# to access personal data (should be PW protected in future versions)
@app.route('/', methods=['GET', 'POST']) #homepage
def home(): 
	return render_template('homepage.html')
	
#get user serial num input, redirect
@app.route('/handle_data', methods=['POST']) 
def handle_data():
	serial_num = request.form['serial_num']
	session['serial_num'] = serial_num #store for session 
	url = '/profile/graph%s' % str(serial_num)
	return redirect(url, code=302)
	

#the meat and potatoes. Unique page for user with interactive charts, tables, and downloads feature 
@app.route('/profile/graph<int:serial_num>')
def graph(serial_num,
		  chartID = 'chart_ID',
		  chartID2 = 'chart_ID2',
		  chartID3 = 'chart_ID3',
		  chartID4 = 'chart_ID4',
		  
		  chartID_box = 'chart_ID_box',
		  chartID2_box = 'chart_ID2_box',
		  chartID3_box = 'chart_ID3_box',
		  chartID4_box = 'chart_ID4_box',
		  ):
		  
	serial_num = int(session.get('serial_num', None)) #grab serial #
	print 'SERIAL NUM SESSION VARIABLE OK:', type(serial_num), serial_num
	
	slice = data.ix[data['user_info_serial'] == serial_num] #only look at data for user of interst 
								
	#convert large dataframe into 3 smaller tables 		
	print_data_cols = []
	print_info_cols = []
	user_info_cols = []
	for col in slice.columns: #filter by main category
		if 'print_data' in col:
			print_data_cols.append(col)
		elif 'print_info' in col:
			print_info_cols.append(col)
		elif 'user_info' in col:
			user_info_cols.append(col)
		else:
			pass 	
	#build new full dataframes 
	print_data = pd.DataFrame(slice, columns=print_data_cols)
	print_info = pd.DataFrame(slice, columns=print_info_cols)
	user_info = pd.DataFrame(slice, columns=user_info_cols)
	#EXCEPTION convert from bool T/F to 1/0
	print_info['print_info_crosslinking_cl_enabled'] = print_info['print_info_crosslinking_cl_enabled'].astype(int) 
	
	#delineate print_info into 3 subcategories for tables
	cl_cols = ['print_info_crosslinking_cl_duration', 'print_info_crosslinking_cl_enabled', 'print_info_crosslinking_cl_intensity']
	cross_linking = print_info.loc[:,cl_cols]
	
	pres_cols = ['print_info_pressure_extruder1', 'print_info_pressure_extruder2']
	pressure = print_info.loc[:,pres_cols]
	
	lay_cols = ['print_info_resolution_layerNum', 'print_info_resolution_layerHeight']
	layer = print_info.loc[:,lay_cols]

	# build descriptive stats dataframes, convert to html table string
	print_data_vals = (print_data.describe()).to_html()
	cross_linking_vals = (cross_linking.describe()).to_html()
	pressure_vals = (pressure.describe()).to_html()
	layer_vals = (layer.describe()).to_html()
	#user_info_vals = (user_info.describe()).to_html() #don't include in tabular form 
	
	tables = [print_data_vals, cross_linking_vals, pressure_vals, layer_vals] #html tables to return 
	titles = ['na', 'Cell Viability & Elasticity',
			'Crosslinking', 
			'Extruder Pressure', 
			'Layer Resolution',
			]
	
	### Print Data charts -- % Alive/Dead/Elasticty ---
	print_data_series = [{"name": '% Cells Alive',	"data": (list(print_data['print_data_livePercent'].values))},
						 {"name": '% Cells Dead',  "data": (list(print_data['print_data_deadPercent'].values))}, 
						 {"name": 'Elasticity',  "data": (list(print_data['print_data_elasticity'].values))}
						 ]
	
	### Print Info charts -- % Crosslinking Duration, Intensity ---
	print_info_CL_series = [{"name": 'Crosslinking Duration (ms)',	"data": (list(print_info['print_info_crosslinking_cl_duration'].values))},
						    {"name": 'Crosslinking Intensity (mW/cm^2)',  "data": (list(print_info['print_info_crosslinking_cl_intensity'].values))}, 
						    {"name": 'Crosslinking Enabled (bool)',  "data": (list(print_info['print_info_crosslinking_cl_enabled'].values))}
						   ]
	
	### Print Info charts -- % Pressure Extruder 1, 2 ---
	print_info_pressure_series = [{"name": 'Pressure Extruder 1',	"data": (list(print_info['print_info_pressure_extruder1'].values))},
								  {"name": 'Pressure Extruder 2',  "data": (list(print_info['print_info_pressure_extruder2'].values))}, 
								 ]
	
	### Print Info charts -- % Resolution Layer Number, Height ---
	print_info_layer_series = [{"name": 'Layer Number',	"data": (list(print_info['print_info_resolution_layerNum'].values))},
						       {"name": 'Layer Height (cm)',  "data": (list(print_info['print_info_resolution_layerHeight'].values))}, 
							  ]							
							
							
	return render_template('usergraph.html',
							serial_num = serial_num,
							
							#data for charts 
							print_data_series = print_data_series,
							print_info_CL_series = print_info_CL_series,
							print_info_pressure_series = print_info_pressure_series,
							print_info_layer_series = print_info_layer_series,	
							
							#time series IDs
							print_data_chartID = chartID,
							print_info_CL_chartID = chartID2,
							print_info_pressure_chartID = chartID3,
							print_info_layer_chartID = chartID4,

							#boxplot IDs
							print_data_chartID_box= chartID_box,
							print_info_CL_chartID_box = chartID2_box,
							print_info_pressure_chartID_box = chartID3_box,
							print_info_layer_chartID_box = chartID4_box,
							
							#tables 
							tables = tables,
							titles = titles,
							)
				

@app.route('/profile/download_data', methods=['POST'])  
def download_csv():  
	serial_num = int(session.get('serial_num', None)) #grab user serial_num for filtering 
	print 'SERIAL NUM SESSION VARIABLE OK:', type(serial_num), serial_num
	
	if request.method == 'POST':
		if request.form['submit'] == "Download My Data":
			print 'POST REQUEST OK'
			slice = data.ix[data['user_info_serial'] == serial_num] #only look at user of interst  
			response = make_response(slice.to_csv()) #build csv 
			cd = 'attachment; filename=biobots_userdata.csv' #name
			response.headers['Content-Disposition'] = cd 
			response.mimetype='text/csv'
			
			return response
							
	
if __name__ == '__main__':
	app.run(debug=True) #launch app 
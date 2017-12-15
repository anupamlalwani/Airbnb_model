from flask import Flask, render_template, jsonify, redirect,url_for, request

from sklearn.externals import joblib

app = Flask(__name__, static_url_path='/static')

@app.route('/', methods = ['GET'])
def index():
	return render_template('model.html')

@app.route('/start-over')
def startover():
	return redirect("/", code=302)


@app.route('/get-user-data', methods=['POST'])
def predict_stuff():
    if request.method == 'POST':
        model = joblib.load('predict_price_bd_bh_nb.pkl')

        print('-----line 27--------')
        # print(request.form.get('accommodates'))

        accommodates = int(request.form.get('accommodates'))

        # print('accommodates')

        bedrooms = int(request.form.get('bedrooms'))
        bathrooms = float(request.form.get('bathrooms'))
        neighborhood = request.form.get('neighborhood')

        potential_listing = [
        accommodates, #accommodates                                  
		bedrooms, #bedrooms                                      
		bathrooms, #bathrooms                                      
		1 if (neighborhood == 'Bernal Heights') else 0, #Bernal Heights          
		1 if (neighborhood == 'Castro/Upper Market') else 0, #Castro/Upper Market     
		1 if (neighborhood == 'Chinatown') else 0, #Chinatown               
		1 if (neighborhood == 'Crocker Amazon') else 0, #Crocker Amazon          
		1 if (neighborhood == 'Diamond Heights') else 0, #Diamond Heights         
		1 if (neighborhood == 'Downtown/Civic Center') else 0, #Downtown/Civic Center   
		1 if (neighborhood == 'Excelsior') else 0, #Excelsior               
		1 if (neighborhood == 'Financial District') else 0, #Financial District      
		1 if (neighborhood == 'Glen Park') else 0, #Glen Park               
		1 if (neighborhood == 'Golden Gate Par') else 0, #Golden Gate Park        
		1 if (neighborhood == 'Haight Ashbury') else 0, #Haight Ashbury          
		1 if (neighborhood == 'Haight Ashbury') else 0, #c          
		1 if (neighborhood == 'Inner Sunset') else 0, #Inner Sunset            
		1 if (neighborhood == 'Lakeshore') else 0, #Lakeshore               
		1 if (neighborhood == 'Marina') else 0, #Marina                  
		1 if (neighborhood == 'Mission') else 0, #Mission                  
		1 if (neighborhood == 'Nob Hill') else 0, #Nob Hill                 
		1 if (neighborhood == 'Noe Valley') else 0, #Noe Valley               
		1 if (neighborhood == 'North Beach') else 0, #North Beach              
		1 if (neighborhood == 'Ocean View') else 0, #Ocean View               
		1 if (neighborhood == 'Outer Mission') else 0, #Outer Mission            
		1 if (neighborhood == 'Outer Richmond') else 0, #Outer Richmond           
		1 if (neighborhood == 'Outer Sunset') else 0, #Outer Sunset             
		1 if (neighborhood == 'Pacific Heights') else 0, #Pacific Heights          
		1 if (neighborhood == 'Parkside') else 0, #Parkside                 
		1 if (neighborhood == 'Potrero Hill') else 0, #Potrero Hill             
		1 if (neighborhood == 'Presidio') else 0, #Presidio                 
		1 if (neighborhood == 'Presidio Heights') else 0, #Presidio Heights         
		1 if (neighborhood == 'Russian Hill') else 0, #Russian Hill             
		1 if (neighborhood == 'Seacliff') else 0, #Seacliff                 
		1 if (neighborhood == 'South of Market') else 0, #South of Market          
		1 if (neighborhood == 'Treasure Island/YBI') else 0, #Treasure Island/YBI      
		1 if (neighborhood == 'Twin Peaks') else 0, #Twin Peaks               
		1 if (neighborhood == 'Visitacion Valley') else 0, #Visitacion Valley        
		1 if (neighborhood == 'West of Twin Peaks') else 0, #West of Twin Peaks       
		1 if (neighborhood == 'Western Addition') else 0 #Western Addition

        ]

        pred = model.predict([potential_listing])

        return render_template('model.html', pred = round(pred[0],2))


if __name__ == '__main__':
	app.run(debug=True, port = 2001)
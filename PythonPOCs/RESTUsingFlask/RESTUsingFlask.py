from flask import Flask,jsonify,request

app=Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR']=True
stores=[{'name':'Mystore1',
         'items':['Colgate','Pepsi','TajMahal Tea'],
         'type':'Kirana'},
        {'name':'Mystore2',
         'items':['Pipes','valves','Mseal'],
         'type':'Hardware'}
    ]

@app.route('/stores',methods=['GET'])
def get_stores():
    return jsonify({'stores':stores})

@app.route('/store/<string:name>',methods=['GET'])
def get_store(name):
    for store in stores:
        if store['name'].lower()==name.lower():
            return jsonify({'stores':store})

    return 'No store exists with that name'
        
@app.route('/store',methods=['POST'])
def create_store():
    store_data=request.get_json()
    new_store={
        'name':store_data['name'],
        'type':store_data['type'],
        'items':store_data['items']
    }
    stores.append(new_store)
    return 'Store created'

@app.route('/store/<string:name>/items',methods=['GET'])
def get_items(name):
    for store in stores:
        if store['name'].lower()==name.lower():
            return jsonify({'items':store['items']})
        
    return 'No store exists with that name'
        
@app.route('/store/<string:name>/items',methods=['POST'])
def create_items(name):
    item_data=request.get_json()
    for store in stores:
        if store['name'].lower()==name.lower():
            for item in item_data['items']:
                store['items'].append(item)
            return 'Items added'
        
    return 'No store exists with that name'
        
app.run(port=7888)
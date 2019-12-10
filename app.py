#importing libraries------
from flask import Flask
from flask_restful import Resource, Api, reqparse
import model

app = Flask(__name__)
api = Api(app)

class Prediction(Resource):                     #Prediction class inherits Resource class
    parser = reqparse.RequestParser()           #RequestParser class helps in defining input argument attributes.
    parser.add_argument('m_value',              #if the type attribute or required attribute is not satisfied
        type=float,                             #the post function returns string in help attribute.
        required=True,
        help="Invalid data. Please enter only numeric data"
    )
    parser.add_argument('c_value',
        type=float,
        required=True,
        help="Invalid data. Please enter only numeric data"
    )
    parser.add_argument('x_value',
        type=float,
        required=True,
        help="Invalid data. Please enter only numeric data"
    )
#----function which receives post request from client app and returns json after processing.
    def post(self):
        input_data =  Prediction.parser.parse_args()        #parser receives data from client app and converts into python dictionary
        m_value = input_data['m_value']                         
        c_value = input_data['c_value']                     
        x_value = input_data['x_value']                     

        model_instance = model.Regression(m_value, c_value)         #creates instance of Regression class and run constructor of class
        predicted_value = model_instance.predict(x_value)       #calls the predict function of Regression class and saves the return data to predicted_value variable
        return {"y": predicted_value}               #returns processed data to client app with default response code 200 OK

api.add_resource(Prediction, '/')           #To add a resource Prediction and define its Endpoint

if __name__ == '__main__':                  #To call app.run only on local system
    app.run(port=5000, debug=True)          # debug=True provides better error messages
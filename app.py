from flask import Flask
from flask_restful import Resource, Api, reqparse
import model

app = Flask(__name__)
api = Api(app)

class Prediction(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('width',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )
	parser.add_argument('length',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )
	parser.add_argument('height',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

	def post(self):
		request_data =  Prediction.parser.parse_args()
		w= request_data['width']						#extracts width from json data
		b= request_data['length']						#extracts length from json data
		x= request_data['height']						#extracts height from json data

		model_instance = model.Regression(w, b)						#creates instance of Regression class and run constructor of class
		predicted_value = float(model_instance.predict(x))		#calls the predict function of Regression class and saves the data to predicted value variable
		
		return {"volume": predicted_value}				#converts the dictionary to json data and return this data to client application

api.add_resource(Prediction, '/')

if __name__ == '__main__':						#To call app.run only on local system
    app.run(port=5000, debug=True)  # important to mention debug=True
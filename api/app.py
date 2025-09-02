from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

########################
# Calculate the likelhood a card is in your opening hand
#
#
########################
class OpeningHandProbability(Resource):
  def get(self):
    copies = request.args.get('copies', type=int)
    probability = .71

    if copies is None:
      return jsonify({"ERROR: Missing required parameters"}, 400)
    
    return jsonify({
      "copies" : copies,
      "probability" : probability
    })

########################
# Calculate the likehlihood a card is prized
#
#
########################
class PrizeProbability(Resource):
  def get(self):
    return {'message' : 'Test Dan'}
  
api.add_resource(PrizeProbability, '/prize')
api.add_resource(OpeningHandProbability, '/opening-hand')

if __name__ == '__main__':
  app.run(debug=True)

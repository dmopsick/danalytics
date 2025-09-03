from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from tcg_probability_calculator  import TcgProbabilityCalculator

app = Flask(__name__)
api = Api(app)

tcg_probability_calculator = TcgProbabilityCalculator()

class OpeningHandProbabilityAPI(Resource):
  """
  Calculate the likelhood a card is in your opening hand
  """
  def get(self):
    copies = request.args.get('copies', type=int)

    if copies is None:
      return jsonify({"ERROR: Missing required parameters"}, 400)

    probability = tcg_probability_calculator.opening_hand_probability(copies)
    
    return jsonify({
      "copies" : copies,
      "probability" : probability
    })

class PrizeProbability(Resource):
  """
  Calculate the likehlihood a card is prized
  """
  def get(self):
    copies = request.args.get('copies', type=int)

    if copies is None:
      return jsonify({"ERROR: Missing required parameters"}, 400)

    probability= tcg_probability_calculator.prizing_probability(copies)

    return jsonify({
      "copies" : copies,
      "probability" : probability
    })
  
# Add the APIs we built to our Flask app
api.add_resource(PrizeProbability, '/prize')
api.add_resource(OpeningHandProbabilityAPI, '/opening-hand')

if __name__ == '__main__':
  app.run(debug=True)

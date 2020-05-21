from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
from flask_restful import Resource, Api, reqparse
import pickle

app = Flask(__name__)
api = Api(app)


class fraudModel(Resource):
    def post(self):
        data = request.get_json()
        prediction = self.getPrediction(euro=data['euro'], 
                                   card_network=data['card_network'], 
                                   card_type=data['card_type'], 
                                   bank_country_id=data['bank_country_id'], 
                                   user_country_id=data['user_country_id'], 
                                   merchant=data['merchant'])
        return "The prediction is: {}<br> the input data is <br> {}".format(prediction, data) 
    
    def getPrediction(self, euro, card_network, card_type, bank_country_id, user_country_id, merchant):
        self.euro = float(euro)
        self.merchant = merchant
        self.card_network = card_network
        self.card_type = card_type
        self.bank_country_id = card_network
        self.user_country_id = user_country_id
        row_pd = self.featureEncode()
        if model.predict_proba(row_pd)[:,1] >= threshold:
            return 1
        else:
            return 0

    def featureEncode(self):
        self.log_euro = np.log(1+self.euro)
        self.same_country = self.bank_country_id==self.user_country_id
        if self.user_country_id in [6, 45]:
            self.country = str(self.user_country_id)
        else:
            self.country = 'other_country'
        row_pd = pd.DataFrame([{'log_euro':self.log_euro,
              'merchant':self.merchant,
              'card_network':self.card_network,
              'card_type':self.card_type,
              'same_country':self.same_country,
              'country':self.country
             }])
        encodedrow_pd = pd.get_dummies(row_pd.loc[:, categoricalFeatures], prefix_sep='_')
        encoded_features = encodedrow_pd.reindex(columns = encodedCategoricalFeatures, fill_value=0)
        encodedrow_pd = pd.concat([row_pd[list(features)].drop(categoricalFeatures, 1), encoded_features], axis=1)
        return encodedrow_pd

api.add_resource(fraudModel, '/predict/')
parser = reqparse.RequestParser()

if __name__ == "__main__":
    model = pickle.load(open('./log_reg_model_v1.pickle', 'rb'))
    features = pickle.load(open('./features.pickle', 'rb'))
    categoricalFeatures = ['merchant', 
                       'card_network',
                       'card_type',
                       'same_country',
                       'country']
    encodedCategoricalFeatures = pickle.load(open('./encodedVariables.pickle', 'rb'))
    threshold = pickle.load(open('./thresholds.pickle', 'rb'))
    app.run(debug=True)
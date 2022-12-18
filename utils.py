import pickle
import pandas as pd
import numpy as np
import config 
import json


class MedicalInsurance():
    def __init__(self,user_data):
        self.model_file_path = 'linear_reg_model.pkl'
        self.user_data = user_data

    def load_saved_data(self):    
        with open(self.model_file_path,"rb") as f:
            self.model = pickle.load(f)   

        with open(r"project_data.json",'r') as r:
            self.proj_data = json.load(r)   

    def get_predicted_price(self):   
        self.load_saved_data()

        gender = self.user_data['gender']
        smoker = self.user_data['smoker']
        #region = self.user_data['region']

        gender = self.proj_data['gender'][gender]
        smoker = self.proj_data['smoker'][smoker]

        #region = "region_"+ region
        #region_index = np.where(np.array(self.proj_data['Columns']) == region)[0][0]
        #print('region_index :',region_index)

        col_count = len(self.proj_data['Columns'])
        test_array = np.zeros(col_count)
        
        test_array[0] = eval(self.user_data['age'])
        test_array[1] = gender
        test_array[2] = eval(self.user_data['bmi'])
        test_array[3] = eval(self.user_data['children'])
        test_array[4] = smoker
        #test_array[region_index] = 1
        print(test_array)

        predicted_charges = np.around(self.model.predict([test_array])[0],3)
        print('predicted_charges :',predicted_charges)
        return predicted_charges

if __name__ == '__main__':
    ins = MedicalInsurance()
    ins



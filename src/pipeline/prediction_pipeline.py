import sys
import os
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object
import pandas as pd


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model_path=os.path.join('artifacts','model.pkl')

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            data_scaled=preprocessor.transform(features)

            pred=model.predict(data_scaled)
            return pred
            

        except Exception as e:
            logging.info("Exception occured in prediction")
            raise CustomException(e,sys)
        
class CustomData:
    def __init__(self,
                 Delivery_person_Ratings:float,
                 Type_of_order:int,
                 Festival:int,
        
                 Weather_conditions:str,
                 Road_traffic_density:str,
                 City:str):
        
        self.Weather_conditions=Weather_conditions
        self.Road_traffic_density=Road_traffic_density
        self.City=City
        self.x=x
        self.y=y
        self.z=z
        self.Weather_conditions = Weather_conditions
        self.Road_traffic_density = Road_traffic_density
        self.City = City

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'Weather_conditions':[self.Weather_conditions],
                'Road_traffic_density':[self.Road_traffic_density],
                'City':[self.City],
                'x':[self.x],
                'y':[self.y],
                'z':[self.z],
                'Weather_conditions':[self.Weather_conditions],
                'Road_traffic_density':[self.Road_traffic_density],
                'City':[self.City]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomException(e,sys)
import os
import sys
import dill

import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
from src.exception import CustomException
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)


    except Exception as ex:
        raise CustomException(ex, sys)
    

def evaluate_model(X_train, y_train, X_test, y_test, models):
    '''
        Function that will perform the training and evaulation of the models
    '''
    try:
        report = {}
        for i in range(len(list(models))):
            
            model = list(models.values())[i]
            model.fit(X_train, y_train)
            
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            # R2- Score: statistical measure that represents the proportion of the variance in the 
            # dependent variable that is predictable from the independent variables

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)


            report[list(models.keys())[i]] = test_model_score # Adding Model Scores in the dict
        
        return report

    except Exception as e:
        raise CustomException(e, sys)
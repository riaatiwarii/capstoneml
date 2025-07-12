import os
import sys
import numpy as np
import pandas as pd
import pickle 

from src.exception import CustomException
from sklearn.model_selection import GridSearchCV
import dill
from sklearn.metrics import r2_score

def save_object(file_path, obj):
  try:
    dir_path = os.path.dirname(file_path)
    os.makedirs(dir_path, exist_ok=True)

    with open(file_path, 'wb') as file_obj:
      dill.dump(obj, file_obj)

  except Exception as e:
    raise CustomException(e,sys)
  
def evaluate_model(x, y, x_test, y_test, models,param):
    report = {}
    try:
        for i in range(len(list(models))):
          model = list(models.values())[i]
          para=param[list(models.keys())[i]]

          gs = GridSearchCV(model,para,cv=3)
          gs.fit(x,y)

          model.set_params(**gs.best_params_)
          model.fit(x,y)

          y_train_pred=model.predict(x)
          y_test_pred=model.predict(x_test)

          train_model_score = r2_score(y, y_train_pred)
          test_model_score = r2_score(y_test, y_test_pred)

          report[list(models.keys())[i]] = test_model_score

        return report
           
    except Exception as e:
        raise CustomException(e, sys)
    
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)
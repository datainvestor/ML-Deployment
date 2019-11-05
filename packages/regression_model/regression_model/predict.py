import numpy as np
import pandas as pd

from regression_model.processing.data_management import load_pipeline
from regression_model.config import config

#load pickle file- this is the pipeline
pipeline_file_name = 'regression_model.pkl'
_price_pipe = load_pipeline(file_name=pipeline_file_name)

#function that gets input data,
def make_prediction(*, input_data) -> dict:
    """Make a prediction using the saved model pipeline."""

    data = pd.read_json(input_data)
    prediction = _price_pipe.predict(data[config.FEATURES]) #  use pipeline that we loaded above to make predictions so all the preprocessing functions will lun on this data before
    output = np.exp(prediction) #this will give prediciton at the end
    response = {'predictions': output}

    return response

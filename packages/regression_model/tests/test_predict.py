import math

from regression_model.predict import make_prediction
from regression_model.processing.data_management import load_dataset


def test_make_single_prediction():
    # Given
    test_data = load_dataset(file_name='test.csv') #load data
    single_test_json = test_data[0:1].to_json(orient='records') #select single row from the csv

    # When
    subject = make_prediction(input_data=single_test_json)

    # Then
    assert subject is not None
    assert isinstance(subject.get('predictions')[0], float) #prediction come as dictionary so we extract preditions and that should be float
    assert math.ceil(subject.get('predictions')[0]) == 112476

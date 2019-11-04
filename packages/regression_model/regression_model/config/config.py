import pathlib
#this is new way of defining paths 


import regression_model


PACKAGE_ROOT = pathlib.Path(regression_model.__file__).resolve().parent #root folder
TRAINED_MODEL_DIR = PACKAGE_ROOT / 'trained_models' #directory where w place our trained models
DATASET_DIR = PACKAGE_ROOT / 'datasets' #specify where we find dataet direcotry

TESTING_DATA_FILE = DATASET_DIR / 'test.csv'
TRAINING_DATA_FILE = DATASET_DIR / 'train.csv'
TARGET = 'SalePrice'


#specifdy features that we are pulling from train.csv
FEATURES = ['MSSubClass', 'MSZoning', 'Neighborhood',
            'OverallQual', 'OverallCond', 'YearRemodAdd',
            'RoofStyle', 'MasVnrType', 'BsmtQual', 'BsmtExposure',
            'HeatingQC', 'CentralAir', '1stFlrSF', 'GrLivArea',
            'BsmtFullBath', 'KitchenQual', 'Fireplaces', 'FireplaceQu',
            'GarageType', 'GarageFinish', 'GarageCars', 'PavedDrive',
            'LotFrontage',
            # this one is only to calculate temporal variable:
            'YrSold']

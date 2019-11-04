import pathlib
#this is new way of defining paths 
#pipeline file is the heart of the package

#directories that will be used be various functions
PACKAGE_ROOT = pathlib.Path(__file__).resolve().parent #root folder
TRAINED_MODEL_DIR = PACKAGE_ROOT / 'trained_models' #directory where w place our trained models
DATASET_DIR = PACKAGE_ROOT / 'datasets' #specify where we find dataet direcotry

TESTING_DATA_FILE = DATASET_DIR / 'test.csv'
TRAINING_DATA_FILE = DATASET_DIR / 'train.csv'
TARGET = 'SalePrice'

#specifdy features that we are pulling from train.csv
FEATURES = ['MSSubClass', 'MSZoning', 'Neighborhood', 'OverallQual',
            'OverallCond', 'YearRemodAdd', 'RoofStyle', 'MasVnrType',
            'BsmtQual', 'BsmtExposure', 'HeatingQC', 'CentralAir',
            '1stFlrSF', 'GrLivArea', 'BsmtFullBath', 'KitchenQual',
            'Fireplaces', 'FireplaceQu', 'GarageType', 'GarageFinish',
            'GarageCars', 'PavedDrive', 'LotFrontage',
            # this variable is only to calculate temporal variable:
            'YrSold']

#this will persist the pipeline
def save_pipeline() -> None:
    """Persist the pipeline."""

    pass

#finction that will run train model
def run_training() -> None:
    """Train the model."""

    print('Training...')


if __name__ == '__main__':
    run_training()

from sklearn.pipeline import Pipeline
#Pipeline from sklearn allows tyo define series of transfomrations and pre processing on the data

import preprocessors as pp

#these categorical variable will be passed into categorical inputer
CATEGORICAL_VARS = ['MSZoning',
                    'Neighborhood',
                    'RoofStyle',
                    'MasVnrType',
                    'BsmtQual',
                    'BsmtExposure',
                    'HeatingQC',
                    'CentralAir',
                    'KitchenQual',
                    'FireplaceQu',
                    'GarageType',
                    'GarageFinish',
                    'PavedDrive']

PIPELINE_NAME = 'lasso_regression'

#this is where we set in pipeline for the categorical imputer to run
price_pipe = Pipeline(
    [
        ('categorical_imputer',
         pp.CategoricalImputer(variables=CATEGORICAL_VARS)),
    ])

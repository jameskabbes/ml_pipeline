import os
import sys
import dir_ops as do #module found in Analytics-Packages
from dir_ops import Path #custom classes found in Analytics-Packages
from dir_ops import Dir #custom classes found in Analytics-Packages

'''
This is a file for all repository-specific parameters.
If you have something changes user by user, put it in your user profile
'''

### Set up the file structure info - these are objects from the Path/Dir classes
params_Path = Path( os.path.abspath(__file__) )
repo_Dir = Dir( params_Path.ascend() )
data_Dir = Dir( repo_Dir.join('Data') )
wiki_Dir = Dir( repo_Dir.join( repo_Dir.dirs[-1] + '.wiki' ) ) #Repository/Repository.wiki
templates_Dir = Dir( repo_Dir.join('Templates') )
main_class_templates_Dir = Dir( templates_Dir.join('Main Class Templates') )
code_templates_Dir = Dir( templates_Dir.join('Code Templates') )

template_Paths = {
'Models':                   Path( main_class_templates_Dir.join('Models.py') ),
'Model':                    Path( main_class_templates_Dir.join('Model.py') ),
'Input_Files':              Path( main_class_templates_Dir.join('Input_Files.py') ),
'Input_File':               Path( main_class_templates_Dir.join('Input_File.py') ),
'Features':                 Path( main_class_templates_Dir.join('Features.py') ),
'Feature':                  Path( main_class_templates_Dir.join('Feature.py') ),
'Input_File_child':         Path( templates_Dir.join('Input_File Child Class.py') ),
'model_inputs':             Path( templates_Dir.join('model_inputs.xlsx') ),
'algorithm':                Path( code_templates_Dir.join( 'algorithm.py' ) ),
'preprocessing':            Path( code_templates_Dir.join( 'preprocessing.py' ) ),
'postprocessing':           Path( code_templates_Dir.join( 'postprocessing.py' ) ),
'generic_cleaning':         Path( code_templates_Dir.join( 'generic_cleaning.py' ) ),
'joining':                  Path( code_templates_Dir.join( 'joining.py') )
}

relative_dirs = {
'Input_File_child': 'Input Files',
'algorithm': 'Algorithms',
'preprocessing': 'Preprocessing',
'postprocessing': 'Postprocessing',
'generic_cleaning': 'Generic Cleaning',
'joining': 'Joining',
'data': 'Data'
}

CLASSES_KEYS = [
'Models',
'Model',
'Input_Files',
'Input_File',
'Features',
'Feature'
]

CODE_KEYS = [
'algorithm',
'joining',
'generic_cleaning',
'preprocessing',
'postprocessing'
]

relative_data_dirs = {
'business_users' : 'Business Users',
'cached': 'Cached',
'cleaned': 'Cleaned',
'cleaned_samples': 'Cleaned Samples',
'model_pickles': 'Model Pickles',
'query_results_staging': 'Query Results Staging',
'raw': 'Raw',
'raw_samples': 'Raw Samples',
'results': 'Results',
'results_sample' : 'Results Sample',
'results_simple' : 'Results Simple',
'shap': 'SHAP',
}

FEATURES_SHEET_NAME = 'Features'
PARAMETERS_SHEET_NAME = 'Parameters'

FEATURE_COL = 'Feature'
PARAMETER_COL = 'Parameter'

MODEL_INPUTS_SUFFIX = '_MODEL_INPUTS'
PROPENSITY_COL_PREFIX = 'PROPENSITY_'

NICKNAME_SEP = '-'

### DEFAULT PARAMS, CAN BE CHANGED IN THE MODELS CLASS
PARQUET_ENGINE = 'fastparquet'
DEFAULT_FEATURE_FLAG = 0
FEATURE_FLAG_CODES = {
0: 'ignore',
1: 'drop_at_preprocess',
2: 'use_in_model'
}

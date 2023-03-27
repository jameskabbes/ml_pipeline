import dir_ops as do
import os
import py_starter as ps

###
_Dir = do.Dir( os.path.abspath( __file__ ) ).ascend()   #Dir that contains the package 
_src_Dir = _Dir.ascend()                                  #src Dir that is one above
_repo_Dir = _src_Dir.ascend()                    

templates_Dir = _Dir.join_Dir( path = 'templates')
code_templates_Dir = templates_Dir.join_Dir( path = 'code' )
main_class_templates_Dir = templates_Dir.join_Dir( path = 'main_class' )


### Load Settings
sys_args, sys_kwargs = ps.get_system_input_arguments()

if 'cwd_dir' in sys_kwargs:
    _cwd_Dir = do.Dir( do.get_cwd() )
else:
    _cwd_Dir = do.Dir( sys_kwargs['cwd_dir'] )

ml_pipeline_Dir = _cwd_Dir.join_Dir( 'ml_pipeline' )
if not ml_pipeline_Dir.exists():
    ml_pipeline_Dir.create( override = True )

# 1
default_settings_Path = _Dir.join_Path( 'default_settings.json' )
settings = ps.Settings( **ps.json_to_dict( default_settings_Path.read() ) )

# 2
user_settings_Path = ml_pipeline_Dir.join_Path( 'settings.json' )
if not user_settings_Path.exists():
    user_settings_Path.create( override = True )

settings.merge( ps.Settings( **ps.json_to_dict( user_settings_Path.read() ) ) )

# 3
settings.merge( ps.Settings( **sys_kwargs ) ) 

### Set Dirs
if settings.data_dir != '':
    data_Dir = do.Dir( settings.data_dir )
else:
    data_Dir = _cwd_Dir.join_Dir( path = settings.data_rel_dir )





### Set up the file structure info - these are objects from the Path/Dir classes
repo_Dir = params_Path.ascend()
data_Dir = do.Dir( repo_Dir.join('Data') )
main_class_templates_Dir = do.Dir( templates_Dir.join('main_class_templates') )
code_templates_Dir = do.Dir( templates_Dir.join('code_templates') )

template_Paths = {
'Models':                   do.Path( main_class_templates_Dir.join('Models.py') ),
'Model':                    do.Path( main_class_templates_Dir.join('Model.py') ),
'Input_Files':              do.Path( main_class_templates_Dir.join('Input_Files.py') ),
'Input_File':               do.Path( main_class_templates_Dir.join('Input_File.py') ),
'Features':                 do.Path( main_class_templates_Dir.join('Features.py') ),
'Feature':                  do.Path( main_class_templates_Dir.join('Feature.py') ),
'Input_File_child':         do.Path( templates_Dir.join('Input_File Child Class.py') ),
'model_inputs':             do.Path( templates_Dir.join('model_inputs.xlsx') ),
'main_py':                  do.Path( templates_Dir.join( 'main.py') ),
'main_ipy':                 do.Path( templates_Dir.join( 'main.ipynb') ),
'algorithm':                do.Path( code_templates_Dir.join( 'algorithm.py' ) ),
'preprocessing':            do.Path( code_templates_Dir.join( 'preprocessing.py' ) ),
'postprocessing':           do.Path( code_templates_Dir.join( 'postprocessing.py' ) ),
'generic_cleaning':         do.Path( code_templates_Dir.join( 'generic_cleaning.py' ) ),
'joining':                  do.Path( code_templates_Dir.join( 'joining.py') )

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




###
from .Base import Base
from .Feature import Feature
from .Features import Features
from .InputFile import InputFile
from .InputFiles import InputFiles
from .Model import Model
from .Models import Models
from . import utils
from . import Templates

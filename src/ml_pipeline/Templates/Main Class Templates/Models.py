if __name__ == '__main__':
    import user_profile_import
    user_profile = user_profile_import.init()

### import from ML-Pipeline
import ML_Models
import ML_Model
import ML_Input_Files
import ML_Input_File
import ML_Features
import ML_Feature
import ML_support as mlsf
import ML_params as mlp

### import from Analytics-Packages
import dir_ops as do
from dir_ops import Dir
from dir_ops import Path
import py_starter as ps

# import from python packages
import os
import pandas as pd

file_Path = Path( os.path.abspath(__file__) )
name = file_Path.root.split( ML_Models.Models.SUFFIX )[0]
repo_Dir = Dir( file_Path.ascend() )

custom_Model_module =       ps.import_module_from_path( repo_Dir.join( name + ML_Model.Model.SUFFIX + '.py' ) )
custom_Input_Files_module = ps.import_module_from_path( repo_Dir.join( name + ML_Input_Files.Input_Files.SUFFIX + '.py' ) )
custom_Input_File_module =  ps.import_module_from_path( repo_Dir.join( name + ML_Input_File.Input_File.SUFFIX + '.py' ) )
custom_Features_module =    ps.import_module_from_path( repo_Dir.join( name + ML_Features.Features.SUFFIX + '.py' ) )
custom_Feature_module =     ps.import_module_from_path( repo_Dir.join( name + ML_Feature.Feature.SUFFIX + '.py' ) )

###
#  EDIT HERE FOR DEFAULT INPUT FILE DATABASE CONNECTION
###
database_conn_params = {}
###
#
###

class Models( ML_Models.Models ):

    OVERRIDE_KWARGS = {
    'Model_class_pointer':       custom_Model_module.Model,
    'Input_Files_class_pointer': custom_Input_Files_module.Input_Files,
    'Input_File_class_pointer':  custom_Input_File_module.Input_File,
    'Features_class_pointer':    custom_Features_module.Features,
    'Feature_class_pointer':     custom_Feature_module.Feature,
    'database_conn_params':      database_conn_params
    }

    def __init__( self, **supplemental_kwargs ):

        joined_kwargs = ps.replace_default_kwargs( Models.OVERRIDE_KWARGS, **supplemental_kwargs )
        ML_Models.Models.__init__( self, name, repo_Dir, **joined_kwargs )

if __name__ == '__main__':

    Models_inst = Models()
    Models_inst.run()

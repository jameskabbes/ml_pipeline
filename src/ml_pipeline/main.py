import user_profile_import
user_profile = user_profile_import.init()

import ML_Model
import ML_Input_File
import ML_support as mlsf

from dir_ops import Dir
from dir_ops import Path
import dir_ops as do

import ML_params as params

###

Models = ML_Model.Models( 'MO-EE', params.repo_Dir )

Models.print_imp_atts()
Models.print_all_atts()

Models.get_random_Model().print_atts()

### import from ML-Pipeline
import ML_Input_Files
import ML_support as mlsf
import ML_params as mlp

### import from Analytics-Packages
import dir_ops as do
from dir_ops import Dir
from dir_ops import Path
import py_starter as ps

import os
import pandas as pd

class Input_Files( ML_Input_Files.Input_Files ):

    OVERRIDE_KWARGS = {
    }

    def __init__( self, Model_inst, **supplemental_kwargs ):

        joined_kwargs = ps.replace_default_kwargs( Input_Files.OVERRIDE_KWARGS, **supplemental_kwargs )
        ML_Input_Files.Input_Files.__init__( self, Model_inst, **joined_kwargs  )

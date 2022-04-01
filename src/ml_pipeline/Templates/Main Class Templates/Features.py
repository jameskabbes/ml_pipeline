### import from ML-Pipeline
import ML_Features
import ML_support as mlsf
import ML_params as mlp

### import from Analytics-Packages
import dir_ops as do
from dir_ops import Dir
from dir_ops import Path
import py_starter as ps

import os
import pandas as pd

class Features( ML_Features.Features ):

    OVERRIDE_KWARGS = {
    }

    def __init__( self, Input_File_inst, **supplemental_kwargs ):

        joined_kwargs = ps.replace_default_kwargs( Features.OVERRIDE_KWARGS, **supplemental_kwargs )
        ML_Features.Features.__init__( self, Input_File_inst, **joined_kwargs  )

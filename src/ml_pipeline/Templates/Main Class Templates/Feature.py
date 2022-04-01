### import from ML-Pipeline
import ML_Feature
import ML_support as mlsf
import ML_params as mlp

### import from Analytics-Packages
import dir_ops as do
from dir_ops import Dir
from dir_ops import Path
import py_starter as ps

import os
import pandas as pd

class Feature( ML_Feature.Feature ):

    OVERRIDE_KWARGS = {
    }

    def __init__( self, Features_inst, ncol, flag, **supplemental_kwargs ):

        joined_kwargs = ps.replace_default_kwargs( Feature.OVERRIDE_KWARGS, **supplemental_kwargs )
        ML_Feature.Feature.__init__( self, Features_inst, ncol, flag, **joined_kwargs  )

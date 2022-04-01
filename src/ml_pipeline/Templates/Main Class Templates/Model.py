### import from ML-Pipeline
import ML_Model
import ML_support as mlsf
import ML_params as mlp

### import from Analytics-Packages
import dir_ops as do
from dir_ops import Dir
from dir_ops import Path
import py_starter as ps

import os
import pandas as pd

class Model( ML_Model.Model ):

    OVERRIDE_KWARGS = {
     }

    def __init__( self, Models_inst, name, **supplemental_kwargs ):

        joined_kwargs = ps.replace_default_kwargs( Model.OVERRIDE_KWARGS, **supplemental_kwargs )
        ML_Model.Model.__init__( self, Models_inst, name, **joined_kwargs  )

import pandas as pd
import ML_support as mlsf

import "__Parent_Input_File_Pointer__" as Parent_Input_File
import py_starter as ps

import dir_ops as do
from dir_ops import Path
from dir_ops import Dir

import os
file_Path = Path( os.path.abspath(__file__) )

###
#  FILL OUT AS NEEDED
###
QUERY = None
DATABASE_CONN_PARAMS = {}
__NICKNAME__ = None #This should be automatically replaced by Input_Files.gen_Input_File_child()
###
#
###

class Input_File( Parent_Input_File.Input_File ):

    DEFAULT_KWARGS = {
    'query': QUERY,
    'database_conn_params': DATABASE_CONN_PARAMS,
    'root': file_Path.root,
    'nickname': NICKNAME
    }

    def __init__( self, Input_Files_inst, **override_kwargs ):

        ### set the default/overridden kwargs
        joined_kwargs = ps.replace_default_kwargs( Input_File.DEFAULT_KWARGS, **override_kwargs )
        self.set_atts( joined_kwargs )

        Parent_Input_File.Input_File.__init__( self, Input_Files_inst, **joined_kwargs )

    def clean( self ):

        df = self.df_raw.copy()
        ### Insert Preprocessing instructions



        ###
        self.df_cleaned = df

    def preprocess( self ):

        df = self.Model.df_pre.copy()
        ### Insert Preprocessing instructions



        ###
        self.Model.df_pre = df

### ML-Pipeline
import ML_ParentClass
import ML_support as mlsf
import ML_params as mlp

###
import py_starter as ps

class Feature( ML_ParentClass.ML_ParentClass ):

    SUFFIX = '_FEATURE'

    DEFAULT_KWARGS = {
    }

    UPDATED_OPTIONS = {
    1: [ '', 'do_nothing' ]
    }


    def __init__( self, Features_inst, ncol, flag, **override_kwargs ):

        ##
        ML_ParentClass.ML_ParentClass.__init__( self, Feature.DEFAULT_KWARGS, **override_kwargs )

        ### Set up parents
        self.Features = Features_inst
        self.Input_File = self.Features.Input_File
        self.Input_Files = self.Input_File.Input_Files
        self.Model = self.Input_Files.Model
        self.Models = self.Model.Models

        #
        self.ncol = ncol
        self.flag = flag
        self.flag_code = self.Models.feature_flag_codes[ self.flag ]
        nickname, self.col = mlsf.split_ncol( self.ncol )

    def __len__( self ):

        return 1

    def __iter__( self ):

        self.i = -1
        return self

    def __next__( self ):

        self.i += 1
        if self.i >= len(self):
            raise StopIteration
        else:
            return None

    def print_imp_atts( self, print_off = True ):

        return self._print_imp_atts_helper( atts = ['col','ncol','flag','Input_File'], print_off = print_off )

    def print_one_line_atts( self, print_off = True, leading_string = '\t' ):

        return self._print_one_line_atts_helper( atts = ['type','col','ncol','flag','Input_File'], print_off = print_off, leading_string = leading_string )

    def update_ncol( self ):

        self.ncol = mlsf.join_nickname_and_col(self.Input_File.nickname, self.col)

    def update_col( self ):

        nickname, self.col = mlsf.split_ncol( self.ncol )

    def rename( new_col ):

        self.col = new_col
        self.ncol = join_nickname_and_col( self.Input_File.nickname, self.ncol )

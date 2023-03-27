import ml_pipeline

class InputFile( ml_pipeline.InputFile ):

    DEFAULT_KWARGS = {}

    def __init__( self, *args, **kwargs ):
        ml_pipeline.InputFile.__init__( self, *args, **kwargs )
        

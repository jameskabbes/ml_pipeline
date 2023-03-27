import ml_pipeline

class InputFiles( ml_pipeline.InputFiles ):

    DEFAULT_KWARGS = {}

    def __init__( self, *args, **kwargs ):
        ml_pipeline.InputFiles.__init__( self, *args, **kwargs )
        

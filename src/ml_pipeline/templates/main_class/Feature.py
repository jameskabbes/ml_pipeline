import ml_pipeline

class Feature( ml_pipeline.Feature ):

    DEFAULT_KWARGS = {}

    def __init__( self, *args, **kwargs ):
        ml_pipeline.Feature.__init__( self, *args, **kwargs )
        

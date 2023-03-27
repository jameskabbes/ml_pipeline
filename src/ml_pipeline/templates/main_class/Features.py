import ml_pipeline

class Features( ml_pipeline.Features ):

    DEFAULT_KWARGS = {}

    def __init__( self, *args, **kwargs ):
        ml_pipeline.Features.__init__( self, *args, **kwargs )
        

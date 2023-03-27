import ml_pipeline

class Model( ml_pipeline.Model ):

    DEFAULT_KWARGS = {}

    def __init__( self, *args, **kwargs ):
        ml_pipeline.Model.__init__( self, *args, **kwargs )
        

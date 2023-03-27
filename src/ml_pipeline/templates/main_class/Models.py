import ml_pipeline

class Models( ml_pipeline.Model ):

    DEFAULT_KWARGS = {}

    def __init__( self, *args, **kwargs ):
        ml_pipeline.Models.__init__( self, *args, **kwargs )
        

from kabbes_menu import Menu
import py_seedlings as ps
import random


class Base( Menu ):

    DEFAULT_KWARGS = {}

    def __init__( self, **override_kwargs ):

        Menu.__init__( self )

        kwargs = ps.merge_dicts( self.DEFAULT_KWARGS, override_kwargs )
        self.set_atts( kwargs )


    def custom_func( self ):

        func_input = input( 'Enter the ' + self.type + ' Class method you would like to run: ' )

        if self.has_attr( func_input ):
            self.run_method( func_input )

        else:
            print ('class ' + str(self.type) + ' does not have that method')

    def get_random_Child( self ):

        ind = random.randrange( len(self) )
        return list(self)[ ind ]

    def lambda_on_Children( self, lambda_func ):

        return [ lambda_func(Child_inst) for Child_inst in self ]

    def select_Children_where( self, att, value ):

        '''return a list of Children instances where Child_att == Child_value '''

        instances = []
        for Child_inst in self:

            if Child_inst.has_attr( att ):
                if Child_inst.get_attr( att ) == value:
                    instances.append( Child_inst )

        return instances

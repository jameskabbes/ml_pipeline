import sys
sys_args = sys.argv[1:]

from ml_pipeline.ml_pipeline import run
run( *sys_args )


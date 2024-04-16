
from os import getcwd
from time import time
from collections import deque 
from zigzag.classes.stages.Stage import Stage

output_dir = getcwd() + '/outputs/runtime'

#Todo: use logger instead of print
class RuntimeMeter:

    def __init__(self):
        self.measures = {}

    def start(self,stage):

        stage_name = get_name(stage)
        
        if stage_name in self.measures:
            raise ValueError(f"Measure for stage {stage} already started.")
        self.measures[stage_name] = time()
    
    def stop(self,stage):
        end_time = time()
        stage_name = get_name(stage)
        if stage_name not in self.measures:
            raise ValueError(f"Measure for stage {stage} not started.")
        elapsed = end_time - self.measures[stage_name]
        self.measures[stage_name] = elapsed
    
    def show_results(self):
        print(f"Execution times: ({len(self.measures)} stages, in seconds)")
        for name,measure in self.measures.items():
            print(f"\t - {name}: {measure}")

def get_name(stage):
    if isinstance(stage,Stage):
        return stage.__class__.__name__
    return stage
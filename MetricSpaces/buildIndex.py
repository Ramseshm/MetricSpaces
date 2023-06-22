import json
import importlib as lb

def load_algorithm(algo,*argsv):
	algorithm_path="."+algo
	algorithm=lb.import_module(algorithm_path,"MetricSpaces.Algorithm")
	if(len(argsv)==0):
		algos=algorithm.algo()
	else:
		algos=algorithm.algo(argsv)
	return algos

def build(algo,bd,*argsv):
	if(isinstance(algo,str) == True):
		algorithm=load_algorithm(algo,bd,argsv)
		data=algorithm.build()
		algorithm.space.cleandix()
		indexname="index"+algo
	else:
		algo.set_bd(bd)
		data=algo.build()
		algo.space.cleandix()
		indexname=algo.get_index_name()
	path="./"+indexname+".json"
	with open(path, 'w') as f:
		json.dump(data, f,indent=4)
	return indexname

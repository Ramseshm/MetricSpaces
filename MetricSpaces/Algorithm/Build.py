import importlib.util as lib

def load_algorithm(algo,*argsv):
	algorithm_path="libp/Algorithm/"+algo+".py"
	#algorithm_path=lib.find_spec(algo,)
	#print(algorithm_path)
	algorithm= lib.spec_from_file_location(algo,algorithm_path).loader.load_module()
	return algorithm

def build(algo,*argsv):
	algorithm=load_algorithm(algo)
	algorithm.build()
	return algorithm.build()

def config(**kwargs):
	for arg in kwargs:
		pass
import json
import importlib as lb

def load_index(index_name):
	index_path="./"+index_name+".json"
	with open(index_path,"r") as f:
		data=json.load(f)
	return data
	
def load_algorithm(algo):
	algorithm_path="."+algo
	algorithm=lb.import_module(algorithm_path,"MetricSpaces.Algorithm")
	return algorithm.algo()

def search(index_name,*argsv):
	index_dic=load_index(index_name)
	algorithm=load_algorithm(index_dic["algorithm"])
	algorithm.set_space(index_dic["space"])
	algorithm.set_bd(index_dic["db"])
	results=algorithm.query(index_dic,argsv[0],argsv[1])
	del index_dic
	return results
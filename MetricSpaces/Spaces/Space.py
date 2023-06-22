import importlib.util as lib
import importlib as lb
def load_space(space):
	space_path="."+space
	#spaceload=lib.spec_from_file_location(space,space_path).loader.load_module()
	spaceload=lb.import_module(space_path,"MetricSpaces.Spaces")
	return spaceload




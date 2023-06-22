from ..Spaces import Space
import random
class algo:
	"""
	Build-fase, add code to make your algorithm index, include function and varibles.
	check manual for more information.
	"""
	def __init__(self,args):
		if(len(args)==0):
			"""
			Query-fase constructor
			"""
			pass
		else:
			pass

	def build(self):

		#index={space:"",algorithm:""}
		pass
	def set_db(self,db):
		#self.db=db
		pass
	def set_index_name(self,name):
		#self.index_name=name
		pass
	def set_space(self,space):
		#self.space=Space.load_space(space)
		pass
	def get_index_name(self):
		#return self.index_name
		pass
			
	def config(self,**kwargsv):
		pass
	"""
	Query/Search-fase, add code to make query, include function and variables.
	Check manual for more information. 
	"""
	def search_radius(self,can,r):
		result=list()
		for x in can:
			distqu=self.space.Distance(0,x)
			if(distqu<=r):
				result.append(x)
		return result
	def search_knn(self,can,k):
		r=999999999
		nn=list()
		nnaux=list()
		for x in can:
			if(len(nn)==k):
				r=max(nnaux)
				if(self.space.Distance(0,x)<r):
					nn[-1]=x
					nnaux[-1]=self.space.Distance(0,x)
					aux1=list()
					nnaux1=nnaux.copy()
					nnaux1.sort()
					for i in nnaux1:
						aux1.append(nn[nnaux.index(i)])
					nn=aux1
					nnaux=nnaux1
			else:
				aux1=list()
				nn.append(x)
				nnaux.append(self.space.Distance(0,x))
				nnaux1=nnaux.copy()
				nnaux1.sort()
				for i in nnaux1:
					aux1.append(nn[nnaux.index(i)])
				nn=aux1
				nnaux=nnaux1
		return nn

	def query(self,index,q,r):

		results=list()
		if(r>0):
			results=search_radius(q,r)
		else:
			results=search_knn(q,int(abs(r)))
		return results


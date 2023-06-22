from ..Spaces import Space
import random
class algo:
	"""
	Build-fase, add code to make your algorithm index, include function and varibles.
	check manual for more information.
	"""
	def __init__(self,args=list()):
		"""
			Query-fase constructor
		"""
		if(len(args)==0):
			self.db=None
			self.space=None
			self.n_pivots=0
		else:
			self.db =args[0]
			self.n_pivots=args[1][0]
			self.space=Space.load_space("vectors")

	def build(self):
	#-------Carga de base de datos---------------
		x=self.space.loadDB(self.db)
	#-------Seleccionar pivotes------------------
		piv=list()
		for i in range(self.n_pivots):
			piv.append(random.randint(1,self.space.tam()-1))
	#-------Crear tabla de pivotes---------------
		piv_tab=[[]]
		for i in range(1,self.space.tam()):
			aux=list()
			for p_i in piv:
				aux.append(self.space.Distance(i,p_i))
			piv_tab.append(aux)
	#-------Crear índice-----------------------
		index={"db":self.db,
			   "space":self.space.name(),
			   "algorithm":"pivots",
			   "tablapiv": piv_tab,
			   "pivotes":  piv
			   }

		return index

	def set_db(self,db):
		self.db=db
	def set_index_name(self,name):
		self.index_name=name
	def set_space(self,space):
		self.space=Space.load_space(space)
	def get_index_name(self):
		return self.index_name
			
	def config(self,**kwargsv):
		self.n_pivots=kwargsv["npivots"]


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
	#-------Cargar base de datos-----------------
		x=self.space.loadDB(self.db)
		self.space.add(q)
		



		results=list()
		if(r>0):
			results=search_radius(q,r)
		else:
			results=search_knn(q,int(abs(r)))
		return results


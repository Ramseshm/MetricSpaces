from ..Spaces import Space
import random
class algo:
	def __init__(self,args=list()):
		if(len(args)==0):
			#Caso-modificable/Query
			self.npermutantes=0
			self.db =None
			self.space=None
		else:
			#Caso-general/Build
			self.db =args[0]
			self.npermutantes=args[1][0]
			self.space=Space.load_space("vectors")

	def set_bd(self,bd):
		self.db=bd
	def set_index_name(self,name):
		self.index_name=name
	def set_space(self,space):
		self.space=Space.load_space(space)
	def get_index_name(self):
		return self.index_name
	def get_algorithm(self):
		return "permutantes"
	def config(self,**kwargsv):
		self.npermutantes=kwargsv["np"]

	def perm(self,l1):
	  """
	  l1.append(l1[0].copy())
	  l2=l1[0].copy()
	  l1[1].sort()
	  """
	  l1.sort(key=lambda elem: elem[1])
	  aux=list()
	  
	  for i in l1:
	    j=i[0]
	    aux.append(j)

	  return aux

	def build(self):
		x=self.space.loadDB(self.db)
				##Seleccionar permutantes
		per=list()
		"""
		for i in range(self.npermutantes):
			per.append(random.randint(1,(self.space.tam()-1)))
		"""
		while(len(per)<self.npermutantes):
			P=random.randint(1,self.space.tam())
			if(P not in per):
				per.append(P)

		##matriz de permutaciones
		self.space.tam()
		Pi=[[]]
		for i in range(1,(self.space.tam())):
			aux=[]
			for j in per:
				aux.append((per.index(j)+1,self.space.Distance(i,j)))  
			Pi.append(self.perm(aux))
		#creacion de indice
		indice={"db":self.db,
				"perm":per,
				"tablaPerm":Pi,
				"space":self.space.name(),
				"algorithm":"permutantes"
				}
		return indice


##PARTE DE CREACION DE LA CONSULTA---------------------------------------------
	def Sradio(self,can,r):
		result=list()
		for x in can:
			distqu=self.space.Distance(0,x)
			if(distqu<=r):
				result.append(x)
		return result
	def Skvecinos(self,can,k):
		r=999999999
		nn=list()
		nnaux=list()
		last=0
		for x in can:
			if(len(nn)==k):
				r=max(nnaux)
				if(self.space.Distance(0,x)<r):
					last=can.index(x)
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
		#print("permutantes: ","encontré el ultimo en la posición: ",last)
		#print("el primero en la posición: ",can.index(nn[0]))
		return nn,last

	def query_perm(self,q):
		"""
		q.append(q[0].copy())
		q[1].sort()
		"""
		q.sort(key=lambda elem: elem[1])
		aux=list()
		for i in q:
			j=i[0]+1
			aux.append(j)
		return aux

	def perminv(self,l1):
		aux=list()
		for i in range(len(l1)):
			res=l1.index(i+1)
			aux.append(res+1)
		return aux

	def ordenar(self,l1):
		l1.sort(key=lambda elem: elem[1])
		aux=list()
		for i in l1:
			aux.append(i[0])
		return aux

	
	"""
	def ordenar(self,l1):
		l1.append(l1[0].copy())
		l1[1].sort()
		aux=list()
		for i in l1[1]:
			j=l1[0].index(i)
			aux.append(j+1)
			l1[0][j]=-1
		return aux
	"""
	def Distancia(self,i,qinv,Indice):
		Sum=0
		for j in range(len(Indice["tablaPerm"][i])):
			r1=abs((j+1)-qinv[Indice["tablaPerm"][i][j]-1])
			Sum=Sum+r1
		return Sum

	def query(self,index,q,r):
		l=self.space.loadDB(self.db)
		self.space.add(q)
		qperm=[]
		for x in index["perm"]:
			qperm.append((index["perm"].index(x),self.space.Distance(0,x)))
		index["tablaPerm"][0]=self.query_perm(qperm)
		qinv=self.perminv(index["tablaPerm"][0])
		#--------------------
		aux=[]
		for i in range(1,len(index["tablaPerm"])):
			aux.append((i,self.Distancia(i,qinv,index)))
		candidatos=self.ordenar(aux)
		"""
		print(index["tablaPerm"][0])
		for k in range(10):
			print("candidato: ",candidatos[k])
			print(index["tablaPerm"][candidatos[k]])
		"""

		results=list()
		if (r>0):
			results=self.Sradio(candidatos,r)
		else:
			results=self.Skvecinos(candidatos,int(abs(r)))
		return results

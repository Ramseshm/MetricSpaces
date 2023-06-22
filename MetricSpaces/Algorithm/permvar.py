from ..Spaces import Space
import random
class algo:
		def __init__(self,args=list()):
				if(len(args)==0):
						#Caso-modificable/Query
						self.npermutantes=0
						self.db =None
						self.space=None
						self.PermlenMin=0
						self.PermlenMax=0
				else:
						#Caso-general/Build
						self.db =args[0]
						self.npermutantes=args[1][0]
						self.space=Space.load_space("vectors")
						self.PermlenMin=args[1][1]
						self.PermlenMax=args[1][2]

		def set_index_name(self,name):
				self.index_name=name
		def set_bd(self,bd):
				self.db=bd
		def set_space(self,space):
				self.space=Space.load_space(space)
		def get_index_name(self):
			return self.index_name
		def get_algorithm(self):
			return "permvar"

			
		def config(self,**kwargsv):
				self.PermlenMin=kwargsv["Min"]
				self.PermlenMax=kwargsv["Max"]
				self.npermutantes=kwargsv["np"]

		def perm(self,l1):
			"""
			l1.append(l1[0].copy())
			l2=l1[0].copy()
			l1[1].sort()
			"""
			l1.sort(key=lambda elem: elem[1])
			aux=list()
			"""
			corregir permutación 
			"""
			contador=0
			region=2*l1[0][1]
			d=l1[0][1]
			for i in l1:
				j=i[0]
				aux.append(j)

			for i in range(len(l1)):
				if(l1[i][1]<=region):
					contador=contador+1
			if (contador<=self.PermlenMin):
				return aux[:self.PermlenMin],d
			elif(contador>=self.PermlenMax):
				return aux[:self.PermlenMax],d
			else:
				return aux[:contador],d

		def build(self):
				x=self.space.loadDB(self.db)
				
								##Seleccionar permutantes
				per=list()
				while(len(per)<self.npermutantes):
					P=random.randint(1,self.space.tam())
					if(P not in per):
						per.append(P)
				#for i in range(self.npermutantes):
						#per.append(random.randint(1,self.space.tam()-1))
						
				##matriz de permutaciones
				Pi=[[]]
				r_pi=[[]]
				for i in range(1,self.space.tam()):
						aux=[]
						for j in per:
							aux.append((per.index(j)+1,self.space.Distance(i,j)))
						p,r=self.perm(aux)  
						Pi.append(p)
						r_pi.append(r)


				#promedio de "cortes"
				"""
				prom=0
				for i in range(1,len(Pi)):
						prom=prom+len(Pi[i])
				prom=int((prom/(len(Pi)-1)))
				"""
				#creacion de indice
				indice={"db":self.db,
								"perm":per,
								"tablaPerm":Pi,
								"piv":r_pi,
								"space":self.space.name(),
								"algorithm":"permvar",
								"bounds":(self.PermlenMin,self.PermlenMax)
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
				contador=0
				last=0
				for x in can:
						if(len(nn)==k):
								r=max(nnaux)
								if(self.space.Distance(0,x)<r):
										last=can.index(x)
										contador=contador+1
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
								contador=contador+1
								aux1=list()
								nn.append(x)
								nnaux.append(self.space.Distance(0,x))
								nnaux1=nnaux.copy()
								nnaux1.sort()
								for i in nnaux1:
										aux1.append(nn[nnaux.index(i)])
								nn=aux1
								nnaux=nnaux1
				#print("PS","encontré el ultimo en la posición: ",last)
				#print("el primero en la posición: ",can.index(nn[0]))
				return nn
		def query_perm(self,q,r):
				"""
				q.append(q[0].copy())
				q[1].sort()
				aux=list()
				"""
				q.sort(key=lambda elem: elem[1])
				aux=list()
				region=2*q[0][1]	
				contador=0

				for i in q:
						j=i[0]+1
						aux.append(j)

				for i in range(len(q)):
					if(q[i][1]<=region):
						contador=contador+1

				if (contador<=self.PermlenMin):
					return aux,self.PermlenMin
				elif(contador>=self.PermlenMax):
					return aux,self.PermlenMax
				else:
					return aux,contador
		
		def maximo(self,a,b):
			if(a<=b):
				return b
			else:
				return a
		
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

		def Distancia(self,i,qinv,m_q,Indice):
				Sum=0
				pen=list()
				contcom=m_q
				maxi=0
				for j in range(len(Indice["tablaPerm"][i])):

						r1=abs((j+1)-qinv[Indice["tablaPerm"][i][j]-1])

						Sum=Sum+r1

						maxi=self.maximo(r1,maxi)
						#penalizacion
						#compartidos
						if(qinv[Indice["tablaPerm"][i][j]-1]<=m_q):
							contcom=contcom-1
								#-----------

				Sum=Sum+ (Sum*contcom) + ((maxi)*(len(Indice["tablaPerm"][0])-len(Indice["tablaPerm"][i])))

				return Sum

		def query(self,index,q,r):
				x=self.space.loadDB(self.db)
				self.PermlenMax=index["bounds"][0]
				self.PermlenMax=index["bounds"][1]
				self.space.add(q)
				qperm=[]
				qdis=list()
				for x in index["perm"]:
						dist_qp=self.space.Distance(0,x)
						qperm.append((index["perm"].index(x),dist_qp))
						qdis.append(dist_qp)
				index["tablaPerm"][0],mq=self.query_perm(qperm,r)
				qinv=self.perminv(index["tablaPerm"][0])
				qdis.sort()


				#print("permutacion consulta: ",index["tablaPerm"][0])
				#print(index["perm"])
				#print(qdis)
				#--------------------
				aux=[]


				for n in range(1,len(index["tablaPerm"])):
					if(abs(index["piv"][n]-qdis[index["tablaPerm"][0].index(index["tablaPerm"][n][0])])<abs(r)):
						aux.append((n,self.Distancia(n,qinv,mq,index)))
						#aux[0].append(self.Distancia(i,qinv,mq,index))
				
				candidatos=self.ordenar(aux)

				results=list()
				#print(index["tablaPerm"][0])
				#print(aux[10][0][0])
				"""
				for k in range(10):
					print(aux[0][k],"--",k)
					print(index["tablaPerm"][aux[0][k][0]])
				"""
				if (r>0):
						results=self.Sradio(candidatos,r)
				else:
						results=self.Skvecinos(candidatos,int(abs(r)))
				return results

"""
		def print(self):
				print("indice permutaciones variables:")
				print(f'Base de datos:----------------------{self.db}')
				print(f'Espacio:----------------------------{self.space.name()}')
				print(f'Num.permutaciones:------------------{self.npermutantes}')
				print(f'Configuracion adicional:')
				print(f'Tamaño minimo de permutacion:-------{self.PermlenMin}')
				print(f'Tamaño maximo de permutacion:-------{self.PermlenMax}')
"""

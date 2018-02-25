class Node:
	def __init__(self,dist,key):
		self.dist=dist
		self.key=key
class MinHeap:
	def __init__(self,n):
		self.array=[None for i in range(n)]
		self.alist=[[]for i in range(n)]
		self.wlist=[[-2 for i in range(n)]for i in range(n)]
		self.n=n
		self.n1=n
		self.stack=[]
	def insert(self,s):
		e=int(input("enter the number of edges:"))
		print("enter  the edges:")
		for i in range(e):
			str=input()
			str=str.split()
			left=int(str[0])
			right=int(str[1])
			weight=int(str[2])
			self.alist[left].append(right)
			self.alist[right].append(left)
			self.wlist[left][right]=weight
			self.wlist[right][left]=weight
		for i in range(self.n):
			self.array[i]=Node(999,i)
		self.array[s].dist=0
		while(self.n>0):
			w=self.extractMin()
			for v in self.alist[w.key]:

				for i in range(self.n):
					if v==self.array[i].key:
						if(w.dist+self.wlist[w.key][v]<self.array[i].dist):
							self.array[i].dist=w.dist+self.wlist[w.key][v]
						break;
			self.heapsort()
			
		
	def heapify(self,i):
		parent=i
		left=2*i+1
		right=2*i+2
		if(left<self.n and self.array[left].dist<self.array[parent].dist):
			parent=left
		if(right<self.n and self.array[right].dist<self.array[parent].dist):
			parent=right
		if(parent!=i):
			temp=Node(self.array[i].dist,self.array[i].key)
			self.array[i].key=self.array[parent].key
			self.array[i].dist=self.array[parent].dist
			self.array[parent].key=temp.key
			self.array[parent].dist=temp.dist
			self.heapify(parent)
	def heapsort(self):
		for i in range(int(self.n/2)-1,-1,-1):
			self.heapify(i)
	def extractMin(self):
		temp=self.array[self.n-1]
		self.array[self.n-1]=self.array[0]
		self.array[0]=temp
		
		min=self.array[self.n-1]
		self.n=self.n-1
		self.heapsort()
		self.stack.append(min.key)
		return(min)
		


def main():
	n=int(input("enter the number of vertices:"))
	t=MinHeap(n)
	s=int(input("enter the source vertex:"))
	t.insert(s)
	print(t.stack)	


main()
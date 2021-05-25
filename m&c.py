'''
Missionaries and Cannibals problem solve using Breadth First Search (BFS)
--------------------------------------------------------------------

Program state:

Array L of size 2, 
L[0] - Number of missionaries on the left side of the river
L[1] - Number of cannibals on the left side of the river

Array R of size 2, 
R[0] - Number of missionaries on the right side of the river 
R[1] - Number of cannibals on the right side of the river 

B,
B=0  - Boat is on the left side of the river 
B=1  - Boat is on the right side of the river 

'''

from copy import deepcopy

POSSIBILITIES = [[1,1],[0,2],[2,0],[0,1],[1,0]]

class State():
	
	def __init__(self, left, boat, right): #Base Class`
		self.left=left;
		self.boat = boat;
		self.right=right;
		self.prev = None
		
	def __str__(self):
		return("({},{}) - ({},{}) - {}".format(self.left[0],self.left[1],self.right[0],self.right[1],self.boat))
	
	#Check constraints
	def isValidStateCheck(self):	
		#For both banks, the missionaries present on the bank cannot be outnumbered by cannibals
		if(0 < self.left[0] < self.left[1] or 0 < self.right[0] < self.right[1]):
			return False	
		
		#More missionaries/Cannibals are not transported than exist on a side
		if(self.left[0]<0 or self.left[1]<0 or self.right[0]<0 or self.right[1]<0):
			return False
		
		return True

	def __eq__(self, other):
		return (self.left[0]==other.left[0] and self.left[1] == other.left[1] and self.right[0]==other.right[0] and self.right[1]==other.right[1] and self.boat==other.boat)
		
	def __hash__(self):
		return hash((self.left[0],self.left[1],self.boat,self.right[0],self.right[1]))
	
	def __str__(self):
		return("({},{}) - ({},{}) - {}".format(self.left[0],self.left[1],self.right[0],self.right[1],self.boat))
	
	#Successfully move all missionaries and cannibals from the left side to the right
	def GoalState(self):
		return(self.left[0]==0 and self.left[1]==0)

def nextStates(current):
	nodes=[]

	for action in POSSIBILITIES:
		
		nextState = deepcopy(current)
		nextState.prev=current
		
		#Boat will be on the opposite side
		nextState.boat = 1-current.boat
		
		#Left to right
		if(current.boat==0):

			#Increase the number in the right side
			nextState.right[0]+=action[0]
			nextState.right[1]+=action[1]
			
			#Decreases the number in the left side
			nextState.left[0]-=action[0]
			nextState.left[1]-=action[1]
		
		#Right to left
		elif(current.boat==1):
			
			#Decreases the number in the right side
			nextState.right[0]-=action[0]
			nextState.right[1]-=action[1]
			
			#Increase the number in the left side
			nextState.left[0]+=action[0]
			nextState.left[1]+=action[1]
		
		if nextState.isValidStateCheck():
			nodes.append(nextState)

	return nodes
	
def bfs(roots):
	
	if roots.GoalState():
		return roots
	
	visited = set()
	queue = [roots]

	while queue:
		state = queue.pop()
		if state.GoalState():
			return state
		
		visited.add(state)
		
		for child in nextStates(state):
			if child in visited:
				continue

			if child not in queue:
				queue.append(child)

def main():
	initial_state = State([3,3],0,[0,0])
	state = bfs(initial_state)
	
	path=[]
	while state:
		path.append(state)
		state = state.prev
		
	path=path[::-1]
	
	print("")
	print("Missionaries and Cannibals problem solve using Breadth First Search")
	print("M - Missionaries		C - Cannibals		b - Boat")
	print("")

	#print state result
	for state in path:
		
		if state.boat:
			print("""{:3} |         b| {:3}\n{:3} |          | {:3}""".format("C"*state.left[1], "C"*state.right[1], "M"*state.left[0], "M"*state.right[0]))
		else:
			print("""{:3} |b         | {:3}\n{:3} |          | {:3}""".format("C"*state.left[1], "C"*state.right[1], "M"*state.left[0], "M"*state.right[0]))
		print("-------------------------")
		print("")
		print("-------------------------")

if __name__ == "__main__":
	main()
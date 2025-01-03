from typing import Optional

class Node:
	def __init__(self, start: int, end: int):
		self.start: int = start
		self.end: int = end
		self.left_child: Optional[Node] = None
		self.right_child: Optional[Node] = None

	def insert(self, node: 'Node') -> bool:
		# Check for overlap
		print("self.start",self.start)
		print("self.end",self.end)
		print("node.end",node.end)
		print("self.right_child",self.right_child)
		print("self.left_child",self.left_child)
		if node.end <= self.start:
			if not self.left_child:
				self.left_child = node
				print("self.left_child",self.left_child)
				return True
			return self.left_child.insert(node)
		
		elif node.start >= self.end:  
			if not self.right_child:
				self.right_child = node
				
				return True
			return self.right_child.insert(node)
		else:
			
			return False

class Calendar:
	def __init__(self):
		self.root: Optional[Node] = None

	def book(self, start: int, end: int) -> bool:
		if start >= end:
			# Invalid interval
			return False
		if self.root is None:
			self.root = Node(start=start, end=end)
			return True
		return self.root.insert(Node(start=start, end=end))

calendar = Calendar()
print(calendar.book(10, 20))  # True
print(calendar.book(15, 25))  # False (overlap)
print(calendar.book(20, 30)) 
print(calendar.book(40, 50)) 
print(calendar.book(1, 9)) 
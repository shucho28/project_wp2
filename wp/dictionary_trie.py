# marker is the address of nodes on the table
# a node having a tag implies path from root to that node is a valid word
import sys

table = {}
marker = 0

class Node:
	data = ''
	child = None
	sibling = None
	tag = None
	
	def add(self, new_data, tag):
		#print(new_data, tag, self.data)
		global table, marker
		index = -1
		if new_data[0] != self.data[0]:
			if self.sibling != None:
				sibling_object = table[self.sibling]
				return sibling_object.add(new_data,tag)
			else:
				self.sibling = marker
				if marker == None:
					print(self.data)
				sibling_object = Node()
				sibling_object.data = new_data
				table[marker] = sibling_object
				marker += 1
				sibling_object.tag = tag
				if tag == None:
					return None
				return tag+1
		for i in range(min(len(self.data), len(new_data))):
			if self.data[i] != new_data[i]:
				index = i
				break
		if index != -1:
			data1 = self.data[index:]
			data2 = new_data[index:]
			self.data = self.data[:index]
			self_tag = self.tag
			self.tag = None
			old_child = Node()
			old_child.data = data1
			old_child.tag = self_tag
			old_child.child = self.child
			self.child = marker
			table[marker] = old_child
			marker += 1
			new_child = Node()
			new_child.data = data2
			new_child.tag = tag
			old_child.sibling = marker
			table[marker] = new_child
			marker += 1
			return tag+1
		else:
			if len(self.data) < len(new_data):
				new_data = new_data[len(self.data):]
				if self.child != None:
					child_object = table[self.child]
					return child_object.add(new_data,tag)
				else:
					self.child = marker
					if marker == None:
						print(self.data)
					child_object = Node()
					child_object.data = new_data
					child_object.tag = tag
					table[marker] = child_object
					marker += 1
					if tag == None:
						return None
					return tag+1
			else:
				self.tag = tag
				if tag == None:
					return None
				return tag+1

class Dictionary:
	root = None
	tag = 0

	def update_table(self):
		global table, marker
		table = pickle.load(open('english.chow','rb'))
		marker = pickle.load(open('marker.chow','rb'))

	def addWord(self,word):
		global marker, table
		if self.root == None:
			self.root = Node()
			self.root.data = word
			table[marker] = self.root
			marker += 1
			self.root.tag = self.tag
			self.tag += 1
		else:
			self.tag = self.root.add(word,self.tag)
	
	def addWord2(self, word):
		self.update_table()
		self.addWord(word)
	
	def searchWord(self, word, input_table):
		global table
		table = input_table
		current = self.root
		while(1):
			sylabs = current.data
			i = len(sylabs)
			if word[:i] == sylabs:
				word = word[i:]
				if word != '':
					current = table[current.child]
				else:					
					if current.tag == None:
						return -1
					return current.tag
			else:
				if current.sibling != None:
					current = table[current.sibling]
				else:
					return -1
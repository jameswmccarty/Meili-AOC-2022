"""

https://aoc.meilisearch.com/

--- SOS GPS ---

Hey fellow,

🎅 Santa needs your help once again to save this festive moment 🎄

With the world population officially hitting 8 billion people, Santa's job isn't getting easier. Enter the ✨Gift-o-tron-3000✨.

Santa could already see it! Using all the saved time to enjoy more cookies and a few extra glasses of milk left by the kids! The perfect Christmas all around... Or so it should have been.

Unfortunately, the shady elf merchant of this machine "forgot" to mention that the Gift Positioning System (GPS) of the machine significantly slows down with the number of kids increasing.

Luckily, we can provide our own GPS algorithm to the Gift-o-tron-3000! Lucky indeed, you know your way around code. They don't call you the sharpest coder of the North Pole for nothing! All the kids of the world and Santa themself are counting on you! Let operation SOS GPS begin ✨

The kids' address list looks as follows:

tamo - RLRLR
loic - RLLL
kero - LRLR
luna - LRRR
caro - LRL
lena - RLLR
thomas - LRLL
tommy - LLL
chayaline - LRLL


On the left is the kid's name that needs to get their gift. On the right is the path from Santa's home to the kid's house. An L means Santa needs to turn left, and an R means they need to turn right. For example, for Santa to go to luna's house, they need to turn left, right, right, and right.

Unfortunately (again), Rudolph has a bad left foot. We need to prioritize turning left before they run out of steam. With the input above, our new GPS map must look like this:


          LL - - - - - - tommy
          /   L - - - -  chayaline, thomas
         /   /
        /   L - - - - -  caro
       /   / \
      /   /   R - - - -  kero
     L - R - RR - - - -  luna
    /
   /      L - - - - - -  loic
  o      /
   \    L - R - - - - -  lena
    \  /
     RL - RLR - - - - -  tamo
  


Notice how some nodes are collapsed together? That's the important part; it will define how many stops Santa's reindeer needs to make. Basically, one per node.

Your goal is to find which kid Santa can get to with as few stops as possible and gives his name.

In the above case, tommy and tamo are the only kids accessible in two instructions. But since tommy appears first in the structure, he gets his gift first.

To determine who is first in the structure, you must use the lexicographical comparison between their path. In this case, LLL appears before RLRLR. In case a path is a subset of another, the shorter wins.


To begin, get your puzzle input. 

BRAVO!

--- Part2 ---

You are able to find the closest kids! But what about the others? The old GPS became so slow that we would not have been able to deliver all the gifts on time!

Now, you need to count how many stops it'll take Santa to go from the closest to the next closest kid until there are no kids remaining. Even kids in Antarctica must receive their well deserved gifts!

You need to find how many stops Santa will make. The number of stops will help Santa know how many carrots they needs to bring for their beloved reindeers.


Step 0: We're at Santa house.

           LL - - - - -  tommy
          /   L - - - -  chayaline, thomas
         /   /
        /   L - - - - -  caro
       /   / \
      /   /   R - - - -  kero
     L - R - RR - - - -  luna
    /
   /      L - - - - - -  loic
  o      /
   \    L - R - - - - -  lena
    \  /
     RL - RLR - - - - -  tamo

Step 1: tommy is the closest, 2 stops away.

           LL - - - - -  2 stops in total
          /   L - - - -  chayaline, thomas
         /   /
        /   L - - - - -  caro
       /   / \
      /   /   R - - - -  kero
     L - R - RR - - - -  luna
    /
   /      L - - - - - -  loic
  o      /
   \    L - R - - - - -  lena
    \  /
     RL - RLR - - - - -  tamo

Step 2: caro is the closest, 3 stops away.

              L - - - -  chayaline, thomas
             /
            L - - - - -  5 stops in total
           / \
          /   R - - - -  kero
     L - R - RR - - - -  luna
    /
   /      L - - - - - -  loic
  o      /
   \    L - R - - - - -  lena
    \  /
     RL - RLR - - - - -  tamo

Step 3: chayaline and thomas are the closest, 1 stops away.

              L  - - - - 6 stops in total
             /
            L
           / \
          /   R - - - -  kero
     L - R - RR - - - -  luna
    /
   /      L - - - - - -  loic
  o      /
   \    L - R - - - - -  lena
    \  /
     RL - RLR - - - - -  tamo

Step 4: kero is the closest, 2 stops away.

            L
           / \
          /   R - - - -  8 stops in total
     L - R - RR - - - -  luna
    /
   /      L - - - - - -  loic
  o      /
   \    L - R - - - - -  lena
    \  /
     RL - RLR - - - - -  tamo


Step 5: luna is the closest, 3 stops away.

     L - R - RR - - - -  11 stops in total
    /
   /      L - - - - - -  loic
  o      /
   \    L - R - - - - -  lena
    \  /
     RL - RLR - - - - -  tamo

Step 6: tamo is the closest, 5 stops away.

          L - - - - - -  loic
  o      /
   \    L - R - - - - -  lena
    \  /
     RL - RLR - - - - -  16 stops in total

Step 7: loic is the closest, 3 stops away.

          L - - - - - -  19 stops in total
  o      /
   \    L - R - - - - -  lena
    \  /
     RL


Step 8: lena is the closest, 2 stops away.

  o
   \    L - R - - - - -  21 stops in total
    \  /
     RL


In the example above, we have 21 stops in total.

Don't forget: If two kids are at the same distance, you still need to deliver your gift to the kid that's first, in the lexicographical order from the point of view of Santa's house.

Although it hasn't changed, you can still get your puzzle input. 

TURBO BRAVO²!

"""

class inode:

	def __init__(self):
		self.left = None
		self.right = None
		self.parent = None
		self.is_left = False
		self.visited = False
		self.contents = []

	def traverse(self,hops=0):
		global total_to_deliver, lex_order
		if len(self.contents) > 0:
			print(self.contents,hops)
			for i in sorted(self.contents):
				lex_order.append(i)
			total_to_deliver += 1
		if self.left != None:
			if self.right == None:
				self.left.traverse(hops)
			else:
				self.left.traverse(hops+1)
		if self.right != None:
			if self.left == None:
				self.right.traverse(hops)
			else:
				self.right.traverse(hops+1)

	def print_traverse(self,hops=0,lead=''):
		global lex_order
		if len(self.contents) > 0:
			print(lead,self.contents,hops)
			for i in sorted(self.contents):
				lex_order.append(i)
		if self.left != None:
			if self.right == None:
				self.left.print_traverse(hops,lead+'-')
			else:
				self.left.print_traverse(hops+1,lead+'-')
		if self.right != None:
			if self.left == None:
				self.right.print_traverse(hops,lead+'-')
			else:
				self.right.print_traverse(hops+1,lead+'-')

	def do_consolidation(self):
		# Am a leaf node
		if len(self.contents) > 0 and self.left == None and self.right == None:
			while self.parent != None and len(self.parent.contents) == 0 and (self.parent.left == None or self.parent.right == None):
				#print("Arrived at leaf node with contents: ",self.contents)
				# copy out contents
				flag = self.is_left
				t_contents = self.contents[:]
				self.contents = []
				self = self.parent
				self.contents = t_contents[:]
				if flag:
					self.left = None
				else:
					self.right = None
		elif len(self.contents) == 0 and (self.left == None or self.right == None):
			if self.parent != None and len(self.contents) == 0:
				if self.is_left:
					if self.left == None:
						self.parent.left = self.right
						self.parent.left.is_left = True
						self.right.parent = self.parent
					else:
						self.parent.left = self.left
						self.parent.left.is_left = True
						self.left.parent = self.parent
				else:
					if self.left == None:
						self.parent.right = self.right
						self.parent.right.is_left = False
						self.right.parent = self.parent
					else:
						self.parent.right = self.left
						self.parent.right.is_left = False
						self.left.parent = self.parent
				self = self.parent
		if self.left != None:
			self.left.do_consolidation()
		if self.right != None:
			self.right.do_consolidation()

	def print_node(self):
		print("My contents ",self.contents)

lex_order = []
head = None
orig_head = None
acc  = 0
current_min = float('inf')
dest = None
total_to_deliver = 0
dest_steps = 0
to_visit = set()

def do_bfs(node):
	global head, total_to_deliver
	seen = set()
	steps = 0
	q = []
	q.append((steps,node))
	seen.add(node)
	while len(q) > 0:
		q = sorted(q,key=lambda x:x[0])
		steps, current = q.pop(0)
		if len(current.contents) > 0:
			candidates = []
			for entry in q:
				if entry[0] <= steps and len(entry[1].contents) > 0:
					candidates.append(entry[1])
			if len(candidates) > 0:
				min_lex_order = float('inf')
				for i in current.contents:
					min_lex_order = min(min_lex_order,lex_order.index(i))
				for entry in candidates:
					for i in entry.contents:
						if lex_order.index(i) < min_lex_order:
							min_lex_order = lex_order.index(i)
							current = entry
			#	print("!!! Conflict candidates number: ", len(candidates), " setting to ",current.contents)
			#print("BFS found ",current.contents," in ",steps," steps.")
			current.contents = []
			current.visited = True
			head = current
			total_to_deliver -= 1
			return steps
		else:
			if current.left != None and current.left not in seen:
				q.append((steps+1,current.left))
				seen.add(current.left)
			if current.right != None and current.right not in seen:
				q.append((steps+1,current.right))
				seen.add(current.right)
			if current.parent != None and current.parent not in seen:
				q.append((steps+1,current.parent))
				seen.add(current.parent)

	return float('inf')

if __name__ == "__main__":

	def parse_line(line):
		global head
		current = head
		name,path = line.strip().split(' - ')
		for char in path:
			if char == 'L':
				if current.left == None:
					current.left = inode()
					current.left.parent = current
					current = current.left
					current.is_left = True
				else:
					current = current.left
			elif char == 'R':
				if current.right == None:
					current.right = inode()
					current.right.parent = current
					current = current.right
				else:
					current = current.right
		current.contents.append(name)

	# Part 1 Solution
	head = inode()
	orig_head = head
	with open("input","r") as infile:
		for line in infile.readlines():
			parse_line(line.strip())
	head.traverse() # ['bearach'] 10 -- Grep for smallest number of steps...first listing

	# Part 2 Solution

	head.do_consolidation()
	while total_to_deliver > 0:
		acc += do_bfs(head)
	print(acc) 	# 37371

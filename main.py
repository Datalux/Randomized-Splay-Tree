import splaytree, randomizedst
import time

print("[+] Loading IV...")

iv = []

file = open("iv.txt", "r") 
for line in file:
    iv.append(int(line))

print("[ ] IV loaded!\n")

st = splaytree.SplayTree()
rst = randomizedst.RandomizedSplayTree(1)

print("[+] Insert IV values in Splay Tree... ")
start_time = time.time()
for i in iv:
    st.insert(i)
print("--- %s seconds ---" % (time.time() - start_time))    
print("[ ] Done\n")

print("[+] Insert IV values in Randomized Splay Tree... ")
start_time = time.time()
for i in iv:
    rst.insert(randomizedst.Node(i))
print("--- %s seconds ---" % (time.time() - start_time))    
print(f"[ ] Done (with {rst.getSplayn()} splays)\n")


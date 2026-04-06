from pyDatalog import pyDatalog

pyDatalog.clear()

# Declare all terms
pyDatalog.create_terms('has_leg, likes, brother_of, employee, parent, ancestor, grandparent')
pyDatalog.create_terms('age, citizen, can_vote, has, low_stock')
pyDatalog.create_terms('enrolled, prerequisite, can_take')
pyDatalog.create_terms('king, greedy, evil')
pyDatalog.create_terms('X, Y, Z, A, Q')

# -------------------------------
# 1. Basic Facts
# -------------------------------
+has_leg('John')
+likes('Raju', 'fish')
+brother_of('Raju', 'Rani')

print("Basic Facts:")
print(has_leg(X))
print(likes('Raju', Y))
print(brother_of('Raju', Z))

# -------------------------------
# 2. Employee
# -------------------------------
+employee('Alice', 50000)
+employee('Bob', 60000)

print("\nEmployee Data:")
print(employee(X, Y))

# -------------------------------
# 3. Ancestor
# -------------------------------
+parent('alex', 'sharon')
+parent('sharon', 'Charlie')

ancestor(X, Y) <= parent(X, Y)
ancestor(X, Y) <= (parent(X, Z) & ancestor(Z, Y))

print("\nAncestors of Charlie:")
print(ancestor(X, 'Charlie'))

# -------------------------------
# 4. Grandparent
# -------------------------------
+parent('Alan', 'Bobby')
+parent('Bobby', 'ange')
+parent('ange', 'Danny')

grandparent(X, Y) <= (parent(X, Z) & parent(Z, Y))

print("\nGrandparents:")
print(grandparent(X, Y))

# -------------------------------
# 5. Voting Eligibility
# -------------------------------
+age('Alice', 20)
+citizen('Alice', 'USA')
+age('JOHN', 10)
+citizen('JOHN', 'USA')

can_vote(X) <= (age(X, A) & citizen(X, 'USA') & (A > 18))

print("\nCan Vote:")
print(can_vote(X))

# -------------------------------
# 6. Low Stock
# -------------------------------
+has('ProductA', 2)
+has('ProductB', 5)
+has('ProductC', 15)

low_stock(X) <= (has(X, Q) & (Q < 10))

print("\nLow Stock Products:")
print(low_stock(X))

# -------------------------------
# 7. Course Prerequisite
# -------------------------------
+enrolled('Alice', 'Math101')
+enrolled('Alice', 'CS101')
+prerequisite('CS101', 'Math101')
+prerequisite('Math101', 'Math102')

can_take('Alice', X) <= (enrolled('Alice', Y) & prerequisite(Y, X))

print("\nCourses Alice Can Take:")
print(can_take('Alice', X))

# -------------------------------
# 8. Evil Kings
# -------------------------------
+king('john')
+greedy('john')
+king('jack')
+greedy('jack')
+king('tom')

evil(X) <= (king(X) & greedy(X))

print("\nEvil Kings:")
print(evil(X))

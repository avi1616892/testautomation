class Family:
    last_name="Gavriel"


class Child1 (Family):
    first_name="Avi"


class Child2 (Family):
    sibling_name="Aviel"


child1=Child1()
print(Child1.first_name + " " +Child1.last_name)

child2=Child2()
print(Child2.sibling_name + " " +Child2.last_name)
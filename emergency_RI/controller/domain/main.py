from node import Node

class Domain:
    def __init__(self):
        pass

    def accept_visitor(self, node: Node, visitor):
        return node.accept_visitor(visitor)
    
    def add_child(self, node: Node, child):
        return node.add_child(child)

    def create_node():
        pass

    def delete_child(self, node: Node, child_id):
        return node.delete_child(child_id)

    def get_children_ex(id, node: Node, children_type, values, properties, use_regex=True):
        return node.get_children_ex(id, node, children_type, values, properties, use_regex)
        
    def get_first_child(self, node: Node, child_type, values, properties, use_regex=True):
        return node.get_first_child(child_type, values, properties, use_regex)
    
    def get_next_sibling(self, node):
        return node.get_next_sibling()

    def get_num_children(self, node: Node, children_type = None):
        return node.get_num_children(children_type)
    
    def get_num_parents(self, node: Node, parent_types = None):
        return node.get_num_parents(parent_types)
    
    def get_previous_sibling(self, node: Node):
        return node.get_previous_sibling()
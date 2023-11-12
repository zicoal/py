class Tree(dict):
    """Simple Tree data structure

    Stores data in the form:

    {
        "a": {
            "b": {},
            "c": {},
        },
        "d": {
            "e": {},
        },
    }

    And can be nested to any depth.
    """

    def __missing__(self, key):
        value = self[key] = type(self)()
        return value

    def insert(self, node, ancestors):
        """Insert the supplied node, creating all ancestors as required.

        This expects a list (possibly empty) containing the ancestors,
        and a value for the node.
        """
        if not ancestors:
            self[node]
        else:
            self[ancestors[0]].insert(node, ancestors[1:])

    def label(self, labels, sort_key=lambda x: x[0]):
        """Return a nested 2-tuple with just the supplied labels.

        Realistically, the labels could be any type of object.
        """
        return sorted([
            (
                labels.get(key),
                value.label(labels, sort_key)
            ) for key, value in self.items()
        ], key=sort_key)
'''
data=[
  {
    "node": 1,
    "ancestors": [],
    "label": "Australia"
  },
  {
        "node": 7,
        "ancestors": [1, 2],
        "label": "Barossa Valley"
    },
  {
    "node": 2,
    "ancestors": [1],
    "label": "South Australia"
  },
  {
    "node": 3,
    "ancestors": [1],
    "label": "Victoria"
  },
  {
    "node": 4,
    "ancestors": [1, 2],
    "label": "South-East"
  },
  {
    "node": 5,
    "ancestors": [1, 3],
    "label": "Western Districts"
  },
  {
    "node": 6,
    "ancestors": [],
    "label": "New Zealand"
  },
  {
    "node": 8,
    "ancestors": [1, 2],
    "label": "Riverland"
  }
]
tree = Tree()
labels = {}
data.append({
    "node": "11",
    "ancestors": [8],
    "label": "Sydney"
  })
data.append({
    "node": "12",
    "ancestors": ['11'],
    "label": "wuhan"
  })
labels = {}
for node in data:
    tree.insert(node['node'], node['ancestors'])
    labels[node['node']] = node['label']
print(tree.label(labels))
'''
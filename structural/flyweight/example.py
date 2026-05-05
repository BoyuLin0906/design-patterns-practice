def print_section(title):
    print(f'\n=== {title} ===')


class TreeType:
    def __init__(self, name, texture):
        self.name = name
        self.texture = texture

    def draw(self, x, y):
        print(f'Draw {self.name} tree with {self.texture} texture at ({x}, {y})')


class TreeFactory:
    def __init__(self):
        self._tree_types = {}

    def get_tree_type(self, name, texture):
        key = (name, texture)

        if key not in self._tree_types:
            self._tree_types[key] = TreeType(name, texture)
            print(f'Create flyweight for {name} / {texture}')

        return self._tree_types[key]

    def show_pool(self):
        print(f'Tree types in pool: {len(self._tree_types)}')
        for tree_type in self._tree_types.values():
            print(f'- {tree_type.name} / {tree_type.texture}')


class Tree:
    def __init__(self, x, y, tree_type: TreeType):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def draw(self):
        self.tree_type.draw(self.x, self.y)


class Forest:
    def __init__(self, tree_factory: TreeFactory):
        self.tree_factory = tree_factory
        self.trees = []

    def plant_tree(self, x, y, name, texture):
        tree_type = self.tree_factory.get_tree_type(name, texture)
        tree = Tree(x, y, tree_type)
        self.trees.append(tree)

    def draw(self):
        for tree in self.trees:
            tree.draw()


if __name__ == '__main__':
    tree_factory = TreeFactory()
    forest = Forest(tree_factory)

    print_section('Plant Trees')
    forest.plant_tree(2, 5, 'oak', 'rough bark')
    forest.plant_tree(4, 8, 'oak', 'rough bark')
    forest.plant_tree(7, 3, 'pine', 'needle bark')
    forest.plant_tree(9, 6, 'oak', 'rough bark')
    forest.plant_tree(12, 4, 'pine', 'needle bark')

    print_section('Draw Forest')
    forest.draw()

    print_section('Flyweight Pool')
    tree_factory.show_pool()

    print_section('Reuse Check')
    first_tree = forest.trees[0]
    second_tree = forest.trees[1]
    third_tree = forest.trees[2]
    print(first_tree.tree_type is second_tree.tree_type)
    print(first_tree.tree_type is third_tree.tree_type)

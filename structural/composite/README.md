# Composite Pattern Practice

Composite is a structural design pattern that lets you treat individual objects and nested groups of objects through the same interface.

Files:

- `structural/composite/example.py`: a filesystem example with files and folders that share one interface and calculate total size recursively
- `structural/composite/README.md`: short notes for this pattern

Example:

- `FileSystemNode` is the shared component interface for both files and folders
- `FileItem` is the leaf object and returns its own size from `get_size()`
- `Folder` is the composite object and can `add()` or `remove()` child nodes
- `Folder.get_size()` walks through all child nodes and sums their sizes, including nested folders
- the main block builds a small `home` folder tree, removes one file, adds an archive folder, and shows how the total size changes

Advantages:

- lets client code work with files and folders in the same way
- makes recursive tree operations like size calculation simple to express
- supports nested structures without changing the client code

Disadvantages:

- can overgeneralize the shared interface if leaf and composite objects differ too much
- debugging large trees can be harder because behavior is spread across many objects

When to use:

- when your model naturally forms a tree such as files, folders, menus, or organization charts
- when client code should treat single objects and grouped objects uniformly
- when recursive operations should work the same way at every level of the structure

Reference:

- https://refactoring.guru/design-patterns/composite

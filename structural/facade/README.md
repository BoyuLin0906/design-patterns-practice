# Facade Pattern Practice

This folder shows a simple Facade pattern example.

Facade is a structural design pattern that provides a simplified interface to a complex subsystem.

Files:

- `structural/facade/example.py`: a data import example that reads CSV or JSON, validates records, transforms them, and saves them through one facade
- `structural/facade/README.md`: short notes for this pattern

Example:

- `RecordReader` is the shared reader interface for file-loading components
- `CsvFileReader` and `JsonFileReader` are the subsystem classes that know how to load different file formats
- `RecordValidator` checks that each imported record has the required fields
- `RecordTransformer` normalizes the imported data into the shape used by the application
- `CustomerDatabase` simulates the database layer that stores the final records
- `DataImportFacade` is the facade that coordinates validation, transformation, and saving through one `import_file()` call after the reader, validator, and transformer are injected from outside

Advantages:

- hides the multi-step import workflow behind one simple entry point
- keeps the facade independent from specific file-reading implementations
- makes it easier to replace one subsystem part without changing the client

Disadvantages:

- can grow too large if every import-related feature is added to one facade
- may hide useful subsystem flexibility when clients need more control

When to use:

- when a workflow depends on several classes that should feel like one operation to the client
- when you want to isolate business code from parsing, validation, transformation, and persistence details
- when the subsystem may change and you want one stable entry point

Reference:

- https://refactoring.guru/design-patterns/facade

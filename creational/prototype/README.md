# Prototype Pattern Practice

Prototype is a creational design pattern that creates new objects by cloning existing configured objects instead of building them from scratch every time.

Files:

- `creational/prototype/example.py`: a report configuration example that is cloned with `deepcopy` and then slightly adjusted
- `creational/prototype/README.md`: short notes for this pattern

Example:

- `ReportConfig` is the concrete prototype that stores the report name, file type, selected columns, filters, and `format_settings`
- `ReportConfig.clone()` uses Python `deepcopy` so copied report settings can be changed without affecting the original prototype
- `ReportConfig.show()` prints the current settings so the example stays focused on cloning instead of export behavior
- the main block starts with one CSV report config, clones it, changes the cloned copy to XLSX, and replaces the CSV `format_settings` with XLSX-specific settings such as `sheet_name` and `freeze_header`
- the last section shows the original CSV config again to prove that the cloned copy did not change the source object

Advantages:

- avoids repeating the same report setup when most settings are shared
- makes it easy to reuse a prepared report config and adjust only the needed settings
- keeps cloning focused on the configured report instead of rebuilding it from scratch

Disadvantages:

- still adds cloning logic for a simple example
- can become harder to manage if many report presets are very similar
- deep copying can be tricky when a report contains more complex nested settings

When to use:

- when report setup is repetitive and you want reusable presets
- when you want to clone a configured object and then slightly adjust its settings
- when the same base report may need small variations, such as CSV and XLSX versions

Reference:

- https://refactoring.guru/design-patterns/prototype

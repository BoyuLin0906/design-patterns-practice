# Abstract Factory Pattern Practice

Abstract Factory is a creational design pattern that creates families of related objects without exposing their concrete classes to client code.

Files:

- `creational/abstract_factory/example.py`: a cloud provider example with Local, AWS, and GCP factories that create storage and message queue services
- `creational/abstract_factory/README.md`: short notes for this pattern

Example:

- `StorageService` and `MessageQueue` are the two abstract product interfaces
- `CloudProviderFactory` is the abstract factory that creates both products in one related family
- `LocalCloudProviderFactory`, `AwsCloudProviderFactory`, and `GcpCloudProviderFactory` are the concrete factories
- `MinioStorageService` with `KafkaMessageQueue`, `AwsS3StorageService` with `AwsSqsService`, and `GcpCloudStorageService` with `GcpPubSubService` are the matching product variants
- `show_environment()` is a small helper that keeps the main block readable while using only `CloudProviderFactory`, `StorageService`, and `MessageQueue`

Advantages:

- keeps storage and messaging services from the same provider family together
- lets client code switch environments without changing workflow logic
- makes it easy to add another provider by adding one factory and matching products

Disadvantages:

- introduces many classes for a small example
- adding a new product type requires updating every factory
- can feel heavier than direct object creation when only one environment is needed

When to use:

- when the code must work with families of related products, but should not depend on their concrete classes
- when the created objects must stay compatible with one another, such as storage and queue services from the same environment
- when a class starts collecting multiple factory methods for different product types and that creation logic should be extracted into one factory interface

Reference:

- https://refactoring.guru/design-patterns/abstract-factory

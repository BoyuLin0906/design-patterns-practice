from abc import ABC, abstractmethod


def print_section(title):
    print(f'\n=== {title} ===')


class StorageService(ABC):
    @abstractmethod
    def upload(self, file_name, content):
        raise NotImplementedError('Subclasses must implement upload().')


class MessageQueue(ABC):
    @abstractmethod
    def send_message(self, queue_name, message):
        raise NotImplementedError('Subclasses must implement send_message().')


class CloudProviderFactory(ABC):
    @abstractmethod
    def create_storage_service(self):
        raise NotImplementedError(
            'Subclasses must implement create_storage_service().'
        )

    @abstractmethod
    def create_message_queue(self):
        raise NotImplementedError(
            'Subclasses must implement create_message_queue().'
        )


class MinioStorageService(StorageService):
    def upload(self, file_name, content):
        print(f'MinIO uploads {file_name} with content: {content}')


class AwsS3StorageService(StorageService):
    def upload(self, file_name, content):
        print(f'AWS S3 uploads {file_name} with content: {content}')


class GcpCloudStorageService(StorageService):
    def upload(self, file_name, content):
        print(f'GCP Cloud Storage uploads {file_name} with content: {content}')


class KafkaMessageQueue(MessageQueue):
    def send_message(self, queue_name, message):
        print(f'Kafka publishes to {queue_name}: {message}')


class AwsSqsService(MessageQueue):
    def send_message(self, queue_name, message):
        print(f'AWS SQS sends to {queue_name}: {message}')


class GcpPubSubService(MessageQueue):
    def send_message(self, queue_name, message):
        print(f'GCP Pub/Sub sends to {queue_name}: {message}')


class LocalCloudProviderFactory(CloudProviderFactory):
    def create_storage_service(self):
        return MinioStorageService()

    def create_message_queue(self):
        return KafkaMessageQueue()


class AwsCloudProviderFactory(CloudProviderFactory):
    def create_storage_service(self):
        return AwsS3StorageService()

    def create_message_queue(self):
        return AwsSqsService()


class GcpCloudProviderFactory(CloudProviderFactory):
    def create_storage_service(self):
        return GcpCloudStorageService()

    def create_message_queue(self):
        return GcpPubSubService()


def show_environment(factory: CloudProviderFactory, file_name, content):
    storage_service = factory.create_storage_service()
    message_queue = factory.create_message_queue()

    storage_service.upload(file_name, content)
    message_queue.send_message(
        'file-events',
        f'{file_name} is uploaded and ready for processing',
    )


if __name__ == '__main__':
    print_section('Local Environment')
    show_environment(LocalCloudProviderFactory(), 'report.csv', 'id,name')

    print_section('AWS Environment')
    show_environment(AwsCloudProviderFactory(), 'report.csv', 'id,name')

    print_section('GCP Environment')
    show_environment(GcpCloudProviderFactory(), 'report.csv', 'id,name')

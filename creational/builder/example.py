from abc import ABC, abstractmethod


def print_section(title):
    print(f'\n=== {title} ===')


class AppConfig:
    def __init__(self):
        self.app_name = None
        self.host = None
        self.port = None
        self.debug_mode = False
        self.database_url = None
        self.cache_enabled = False
        self.log_level = 'WARNING'

    def show(self):
        print(f'app_name: {self.app_name}')
        print(f'host: {self.host}')
        print(f'port: {self.port}')
        print(f'debug_mode: {self.debug_mode}')
        print(f'database_url: {self.database_url}')
        print(f'cache_enabled: {self.cache_enabled}')
        print(f'log_level: {self.log_level}')


class AppConfigBuilder(ABC):
    @abstractmethod
    def reset(self):
        raise NotImplementedError('Subclasses must implement reset().')

    @abstractmethod
    def set_app_name(self, name):
        raise NotImplementedError('Subclasses must implement set_app_name().')

    @abstractmethod
    def set_host(self, host):
        raise NotImplementedError('Subclasses must implement set_host().')

    @abstractmethod
    def set_port(self, port):
        raise NotImplementedError('Subclasses must implement set_port().')

    @abstractmethod
    def enable_debug_mode(self):
        raise NotImplementedError(
            'Subclasses must implement enable_debug_mode().'
        )

    @abstractmethod
    def set_database_url(self, database_url):
        raise NotImplementedError(
            'Subclasses must implement set_database_url().'
        )

    @abstractmethod
    def enable_cache(self):
        raise NotImplementedError('Subclasses must implement enable_cache().')

    @abstractmethod
    def set_log_level(self, level):
        raise NotImplementedError('Subclasses must implement set_log_level().')


class EnvironmentConfigBuilder(AppConfigBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.config = AppConfig()

    def set_app_name(self, name):
        self.config.app_name = name

    def set_host(self, host):
        self.config.host = host

    def set_port(self, port):
        self.config.port = port

    def enable_debug_mode(self):
        self.config.debug_mode = True

    def set_database_url(self, database_url):
        self.config.database_url = database_url

    def enable_cache(self):
        self.config.cache_enabled = True

    def set_log_level(self, level):
        self.config.log_level = level

    def get_product(self):
        return self.config


class AppConfigDirector:
    def build_local_config(self, builder: AppConfigBuilder):
        builder.reset()
        builder.set_app_name('TaskFlow')
        builder.set_host('127.0.0.1')
        builder.set_port(8000)
        builder.enable_debug_mode()
        builder.set_database_url('sqlite:///taskflow.db')
        builder.set_log_level('DEBUG')

    def build_production_config(self, builder: AppConfigBuilder):
        builder.reset()
        builder.set_app_name('TaskFlow')
        builder.set_host('0.0.0.0')
        builder.set_port(443)
        builder.set_database_url('postgresql://app:secret@db.internal/taskflow')
        builder.enable_cache()
        builder.set_log_level('ERROR')


if __name__ == '__main__':
    director = AppConfigDirector()
    builder = EnvironmentConfigBuilder()

    director.build_local_config(builder)
    local_config = builder.get_product()

    director.build_production_config(builder)
    production_config = builder.get_product()

    print_section('Local Config')
    local_config.show()

    print_section('Production Config')
    production_config.show()

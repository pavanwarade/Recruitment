import configparser
import json
import os
import yaml


class ConfigParser:

    def __init__(self, yaml_file_path, json_file_path, env_file_path):
        self.yaml_file_path = yaml_file_path
        self.json_file_path = json_file_path
        self.env_file_path = env_file_path
        self.config = self.read_config_file(self.yaml_file_path)

    def get_extension(self, file_path):
        _, ext = os.path.splitext(file_path)

        return ext

    def read_config_file(self, file_path):
        ext = self.get_extension(file_path=file_path)
        config = dict()

        if ext == '.yaml':
            with open(file_path, 'r') as yaml_file:
                config = yaml.safe_load(yaml_file)


        elif ext == '.cfg' or ext == '.conf':
            config_parser = configparser.ConfigParser()
            config_parser.read(file_path)
            for section in config_parser.sections():
                config.update(dict(config_parser.items(section)))

        self.write_config_to_json(config)
        self.write_config_to_env_file(config)
        self.write_config_to_env(config)

        return config

    def write_config_to_env(self, config):
        for key, value in config.items():
            os.environ[key] = str(value)

    def write_config_to_json(self, config):
        with open(self.json_file_path, 'w') as json_file:
            json.dump(config, json_file, indent=4)

    def write_config_to_env_file(self, config):
        with open(self.env_file_path, 'w') as env_file:
            for key, value in config.items():
                env_file.write(f'{key}={value}\n')


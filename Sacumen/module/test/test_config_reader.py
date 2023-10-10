import os
import tempfile
import pytest
from module.config_reader import ConfigParser

@pytest.fixture
def sample_yaml_config():
    config_data = """
    key1: value1
    key2: value2
    """
    with tempfile.NamedTemporaryFile(suffix=".yaml", delete=False) as temp_file:
        temp_file.write(config_data.encode("utf-8"))
        temp_file.flush()
        yield temp_file.name
    os.remove(temp_file.name)

@pytest.fixture
def sample_cfg_config():
    config_data = """
    [section1]
    key3: value3
    key4: value4
    """
    with tempfile.NamedTemporaryFile(suffix=".cfg", delete=False) as temp_file:
        temp_file.write(config_data.encode("utf-8"))
        temp_file.flush()
        yield temp_file.name
    os.remove(temp_file.name)

@pytest.fixture
def temp_env_vars():
    os.environ["TEST_VAR1"] = "test_value1"
    os.environ["TEST_VAR2"] = "test_value2"
    yield
    # Clean up environment variables after testing
    del os.environ["TEST_VAR1"]
    del os.environ["TEST_VAR2"]

def test_read_yaml_config(sample_yaml_config):
    parser = ConfigParser(sample_yaml_config, "test.json", "test.env")
    config = parser.config
    assert config == {"key1": "value1", "key2": "value2"}

def test_read_cfg_config(sample_cfg_config):
    parser = ConfigParser(sample_cfg_config, "test.json", "test.env")
    config = parser.config
    assert config == {"key3": "value3", "key4": "value4"}

def test_write_config_to_env(temp_env_vars, sample_yaml_config):  #
    config = {"key1": "new_value1", "key5": "value5"}
    parser = ConfigParser(sample_yaml_config, "test.json", "test.env")
    print(f"config:{config}")
    parser.write_config_to_env(config)
    assert os.environ["key1"] == "new_value1"
    assert os.environ["key5"] == "value5"

def test_write_config_to_json(sample_yaml_config):
    config = {"key1": "value1", "key2": "value2"}
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as temp_file:
        json_file_path = temp_file.name
        parser = ConfigParser(sample_yaml_config, json_file_path, "test.env")
        parser.write_config_to_json(config)

    with open(json_file_path, "r") as f:
        json_data = f.read()
        assert json_data == '{\n    "key1": "value1",\n    "key2": "value2"\n}'


def test_write_config_to_env_file(sample_yaml_config):
    config = {"key1": "value1", "key2": "value2"}
    with tempfile.NamedTemporaryFile(suffix=".env", delete=False) as temp_file:
        env_file_path = temp_file.name
        parser = ConfigParser(sample_yaml_config, "test.json", env_file_path)
        parser.write_config_to_env_file(config)

    with open(env_file_path, "r") as f:
        env_data = f.read()
        assert env_data == 'key1=value1\nkey2=value2\n'

def test_extract_file_extension(sample_yaml_config):
    # Test cases for different file extensions
    test_cases = [
        ("config.yaml", ".yaml"),
        ("config.cfg", ".cfg"),
        ("config.conf", ".conf"),
        ("config.json", ".json"),
        ("config.env", ".env"),
        ("config.txt", ".txt"),
    ]
    parser = ConfigParser(sample_yaml_config, "test.json", "test.env")
    for file_name, expected_extension in test_cases:
        extension = parser.get_extension(file_name)
        assert extension == expected_extension


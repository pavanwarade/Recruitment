import os
from module.config_reader import ConfigParser


if __name__ == "__main__":
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    yaml_file_path = os.path.join(ROOT_DIR, "module/files/YAMLsample.yaml").replace("/", "\\")

    # TODO: uncomment the below two lines for .cfg and .conf
    # cfg_file_path = os.path.join(ROOT_DIR, "/module/files/CFGsample.cfg").replace("/", "\\")
    # conf_file_path = os.path.join(ROOT_DIR, "/module/files/CONFsample.conf").replace("/", "\\")
    json_file_path = os.path.join(ROOT_DIR, "module/files/JSONsample.json").replace("/", "\\")
    env_file_path = os.path.join(ROOT_DIR, "module/files/ENVsample.env").replace("/", "\\")
    configparser = ConfigParser(yaml_file_path, json_file_path, env_file_path)

    print(f"Config Parser Successfully executed ....!")


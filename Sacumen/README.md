# Configuration Parser Module

A Python module for reading and write configuration files.

## Project Structure

 * [Sacumen]()
   * [module](module)
      
     * [files](module/files)
       * [init.py](module/files/__init__.py)
       * [CFGsample.cfg](module/files/CFGsample.cfg)
       * [CONFsample.conf](module/files/CONFsample.conf)
       * [ENVsample.env](module/files/ENVsample.env)
       * [JSONsample.json](module/files/JSONsample.json)
       * [YAMLsample.yaml](module/files/YAMLsample.yaml)
     
     * [test](module/test)
       
       * [init.py](module/test/__init__.py)
       * [test.env](module/test/test.env)
       * [test.json](module/test/test.json)
       * [test_config_reader.py](module/test/test_config_reader.py)
     * [init.py](module/__init__.py)
     * [config_reader.py](module/config_reader.py)

   * [main.py](main.py)
   * [README.md](README.md)


## Code Details
from config_parser_module import ConfigParser
###
#### Create an instance of ConfigParser with the path to your configuration file
configparser = ConfigParser(yaml_file_path, json_file_path, env_file_path)
###
#### To get extentions of the file
configparser.get_extension(file_path)
###
#### Read the configuration file
configparser.read_config_file(config)

###
#### Set configurations in the OS environment
configparser.write_config_to_env(config)
###
#### Save configurations to a JSON file
configparser.write_config_to_json(config)
###
#### Save configurations to a env file
configparser.write_config_to_env_file(config)
###
## Supported Formats
YAML (.yaml),
ConfigParser (.cfg, .conf)

###
#### To Run all tests:

coverage run -m pytest test_config_reader.py
###
#### To see report:
coverage report
###
#### To create report HTML:

coverage html 
###
#### Current code coverage status:
 Using added test cases covered **100 % code coverage**
 check the below snapshot:
####
![Coverage_Report](https://github.com/pavanwarade/Recruitment/assets/22584875/69b04df9-7e59-48fa-b012-a1b6c3d72a6d)

## License

@copyright (c) 2023 All right reserved.


## Feedback

If you have any feedback, please reach out to me at **pavanswarade@gmail.com**
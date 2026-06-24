import os
import yaml
from src.meridian_automation import logger
import json 

# loading the model
import joblib # mostly this won't be necessary as the meridian model is saved in pickle and binpb format 
import pickle

from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError, BoxKeyError

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a yaml file and returns a ConfigBox object.
    
    Args:
        path_to_yaml (Path): Path to the yaml file.
    
    Raises:
        ValueError: If the yaml file is empty.
        BoxValueError: If there is an error while reading the yaml file.
        BoxKeyError: If there is an error while reading the yaml file.
        
    Returns:
        ConfigBox: ConfigBox object containing the contents of the yaml file.
    """
    # try:
    #     with open(path_to_yaml) as yaml_file:
    #         content = yaml.safe_load(yaml_file)
    #         if content is None:
    #             raise ValueError(f"The yaml file at {path_to_yaml} is empty.")
    #         else:
    #             logger.info(f"Yaml file : {path_to_yaml} loaded successfully")
    #             return ConfigBox(content)
    # except BoxValueError as e:
    #     logger.error(f"Error occurred while reading yaml file {path_to_yaml}: {e}")
    #     raise ValueError(f"Error occurred while reading yaml file {path_to_yaml}: {e}")
    # except BoxKeyError as e:
    #     logger.error(f"Error occurred while reading yaml file {path_to_yaml}: {e}")
    #     raise ValueError(f"Error occurred while reading yaml file {path_to_yaml}: {e}")
    # except Exception as e:
    #     logger.error(f"Error occurred while reading yaml file {path_to_yaml}: {e}")
    #     raise ValueError(f"Error occurred while reading yaml file {path_to_yaml}: {e}")

    try :
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            if content is None:
                raise ValueError(f'The yaml file at {path_to_yaml} is empty.')
            logger.info(f"Yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
        
    except BoxValueError as e:
        logger.error(f"Error occurred while reading yaml file {path_to_yaml}: {e}")
        raise ValueError(f"Error occurred while reading yaml file {path_to_yaml}: {e}")
    except Exception as e:
        logger.error(f"Error occurred while reading yaml file {path_to_yaml}: {e}")
        raise ValueError(f"Error occurred while reading yaml file {path_to_yaml}: {e}")
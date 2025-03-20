import json
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_config(config_file='config/config.json'):
    """
    Load configuration settings from a JSON file.
    
    :param config_file: Path to the configuration file.
    :return: Dictionary containing configuration settings.
    """
    if not os.path.exists(config_file):
        logger.error(f"Configuration file {config_file} does not exist.")
        raise FileNotFoundError(f"Configuration file {config_file} does not exist.")
    
    try:
        with open(config_file, 'r') as file:
            config = json.load(file)
            logger.info(f"Configuration loaded successfully from {config_file}.")
            return config
    except json.JSONDecodeError as e:
        logger.error(f"Error decoding JSON from {config_file}: {e}")
        raise

# Example usage
if __name__ == "__main__":
    config = load_config()
    print(config)

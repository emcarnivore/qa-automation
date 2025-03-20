import json
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_test_data(data_file='data/test_data.json'):
    """
    Load test data from a JSON file.

    :param data_file: Path to the test data file.
    :return: Dictionary containing test data.
    """
    if not os.path.exists(data_file):
        logger.error(f"Test data file {data_file} does not exist.")
        raise FileNotFoundError(f"Test data file {data_file} does not exist.")
    
    try:
        with open(data_file, 'r') as file:
            test_data = json.load(file)
            logger.info(f"Test data loaded successfully from {data_file}.")
            return test_data
    except json.JSONDecodeError as e:
        logger.error(f"Error decoding JSON from {data_file}: {e}")
        raise

# Example usage
if __name__ == "__main__":
    test_data = load_test_data()
    print(test_data)

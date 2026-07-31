# ==========================================================
# Data Ingestion Component
# Purpose:
# 1. Read dataset
# 2. Save raw data
# 3. Split into train and test
# 4. Start Data Transformation
# ==========================================================

import os
import sys
from dataclasses import dataclass

import pandas as pd
from sklearn.model_selection import train_test_split

from src.logger import logging
from src.exception import CustomException
from src.components.transformation import DataTransformation

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))

# ==========================================================
# Configuration Class
# ==========================================================

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join(ROOT_DIR, "artifacts", "train.csv")
    test_data_path: str = os.path.join(ROOT_DIR, "artifacts", "test.csv")
    raw_data_path: str = os.path.join(ROOT_DIR, "artifacts", "data.csv")


# ==========================================================
# Data Ingestion Class
# ==========================================================

class DataIngestion:

    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):

        logging.info("Entered Data Ingestion Component")

        try:
            raw_data_path = os.path.join(ROOT_DIR, "notebook", "data", "stud.csv")
            df = pd.read_csv(raw_data_path)
            logging.info("Dataset loaded successfully.")

            os.makedirs(
                os.path.dirname(self.ingestion_config.train_data_path),
                exist_ok=True
            )

            df.to_csv(
                self.ingestion_config.raw_data_path,
                index=False,
                header=True
            )

            logging.info("Raw dataset saved.")

            train_set, test_set = train_test_split(
                df,
                test_size=0.2,
                random_state=42
            )

            train_set.to_csv(
                self.ingestion_config.train_data_path,
                index=False,
                header=True
            )

            test_set.to_csv(
                self.ingestion_config.test_data_path,
                index=False,
                header=True
            )

            logging.info("Train-Test Split completed.")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)


# ==========================================================
# Main Function
# ==========================================================

if __name__ == "__main__":

    obj = DataIngestion()

    train_data, test_data = obj.initiate_data_ingestion()

    logging.info("Starting Data Transformation...")

    data_transformation = DataTransformation()

    train_arr, test_arr, preprocessor_obj_file_path = (
        data_transformation.initiate_data_transformation(
            train_data,
            test_data
        )
    )

    logging.info("Data Transformation Completed Successfully.")

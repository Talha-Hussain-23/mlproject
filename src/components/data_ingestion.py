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


# ==========================================================
# Configuration Class
# ==========================================================

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "data.csv")


# ==========================================================
# Data Ingestion Class
# ==========================================================

class DataIngestion:

    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):

        logging.info("Entered Data Ingestion Component")

        try:
            # Read Dataset
            df = pd.read_csv("notebook/data/stud.csv")
            logging.info("Dataset loaded successfully.")

            # Create artifacts folder
            os.makedirs(
                os.path.dirname(self.ingestion_config.train_data_path),
                exist_ok=True
            )

            # Save raw dataset
            df.to_csv(
                self.ingestion_config.raw_data_path,
                index=False,
                header=True
            )

            logging.info("Raw dataset saved.")

            # Train-Test Split
            train_set, test_set = train_test_split(
                df,
                test_size=0.2,
                random_state=42
            )

            # Save train dataset
            train_set.to_csv(
                self.ingestion_config.train_data_path,
                index=False,
                header=True
            )

            # Save test dataset
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
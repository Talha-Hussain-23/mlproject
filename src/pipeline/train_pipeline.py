import sys

from src.components.data_ingestion import DataIngestion
from src.components.transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.exception import CustomException
from src.logger import logging


class TrainPipeline:

    def __init__(self):
        self.data_ingestion = DataIngestion()
        self.data_transformation = DataTransformation()
        self.model_trainer = ModelTrainer()

    def initiate_training_pipeline(self):
        try:
            logging.info("Starting training pipeline.")

            train_path, test_path = self.data_ingestion.initiate_data_ingestion()
            logging.info("Data ingestion completed.")

            train_arr, test_arr, _ = self.data_transformation.initiate_data_transformation(
                train_path,
                test_path
            )
            logging.info("Data transformation completed.")

            score = self.model_trainer.initiate_model_trainer(
                train_arr,
                test_arr
            )
            logging.info(f"Training pipeline completed with model R2 score: {score:.4f}")
            return score

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    score = TrainPipeline().initiate_training_pipeline()
    print(f"Training completed. Best test R2 score: {score:.4f}")

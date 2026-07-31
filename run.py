from src.pipeline.train_pipeline import TrainPipeline
from src.pipeline.predict_pipeline import CustomData, PredictPipeline


def main():
    print("Running training pipeline...")
    score = TrainPipeline().initiate_training_pipeline()
    print(f"Training completed with best test R2 score: {score:.4f}")

    sample = CustomData(
        gender="female",
        race_ethnicity="group B",
        parental_level_of_education="bachelor's degree",
        lunch="standard",
        test_preparation_course="completed",
        reading_score=72,
        writing_score=74,
    )

    print("Running sample prediction...")
    prediction = PredictPipeline().predict(sample.get_data_as_data_frame())
    print(f"Sample prediction: {prediction}")


if __name__ == "__main__":
    main()

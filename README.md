# End to End ML Project

This repository contains a simple end-to-end machine learning project for predicting student math scores based on demographic and academic features.

## What is included

- `src/components/data_ingestion.py` - ingests raw student data and creates train/test splits.
- `src/components/transformation.py` - builds a preprocessing pipeline and saves a preprocessor.
- `src/components/model_trainer.py` - evaluates candidate regression models and saves the best model.
- `src/pipeline/train_pipeline.py` - coordinates ingestion, transformation, and model training.
- `src/pipeline/predict_pipeline.py` - loads saved artifacts and makes predictions from new data.
- `run.py` - a runnable entrypoint that trains the model and makes a sample prediction.

## Run the project

1. Activate your Python environment.
2. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

3. Run the project:

```bash
python run.py
```

4. Alternative training command:

```bash
python -m src.pipeline.train_pipeline
```

## Outputs

Training produces these artifacts under `artifacts/`:

- `train.csv`
- `test.csv`
- `data.csv`
- `preprocessor.pkl`
- `model.pkl`

## Notes

- The model predicts `math_score` from features including reading/writing scores and categorical student demographics.
- Logs are written under `logs/`.

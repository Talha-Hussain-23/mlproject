import os
import sys
import pickle
from typing import Any, Dict

import numpy as np
import pandas as pd

from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException
from src.logger import logging


def save_object(file_path: str, obj: Any) -> None:
    """
    Save any Python object using pickle.

    Parameters
    ----------
    file_path : str
        Path where object will be saved.

    obj : Any
        Python object to save.
    """
    try:
        dir_path = os.path.dirname(file_path)

        if dir_path:
            os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

        logging.info(f"Object saved successfully at: {file_path}")

    except Exception as e:
        logging.error("Error while saving object.")
        raise CustomException(e, sys)


def load_object(file_path: str) -> Any:
    """
    Load a pickled object.

    Parameters
    ----------
    file_path : str

    Returns
    -------
    Any
        Loaded Python object.
    """
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"{file_path} does not exist.")

        with open(file_path, "rb") as file_obj:
            obj = pickle.load(file_obj)

        logging.info(f"Object loaded successfully from: {file_path}")

        return obj

    except Exception as e:
        logging.error("Error while loading object.")
        raise CustomException(e, sys)


def evaluate_models(
    X_train,
    y_train,
    X_test,
    y_test,
    models: Dict,
    param: Dict
) -> Dict:
    """
    Train multiple models using GridSearchCV and evaluate them.

    Parameters
    ----------
    X_train : Training features

    y_train : Training labels

    X_test : Testing features

    y_test : Testing labels

    models : Dictionary
        {
            "Linear Regression": LinearRegression(),
            "Random Forest": RandomForestRegressor()
        }

    param : Dictionary
        {
            "Linear Regression": {},
            "Random Forest": {
                "n_estimators":[100,200]
            }
        }

    Returns
    -------
    Dict
        Dictionary containing train score,
        test score and best parameters.
    """

    try:

        report = {}

        logging.info("Model evaluation started.")

        for model_name, model in models.items():

            logging.info(f"Training {model_name}")

            parameters = param.get(model_name, {})

            gs = GridSearchCV(
                estimator=model,
                param_grid=parameters,
                cv=3,
                scoring="r2",
                n_jobs=-1,
                verbose=0
            )

            gs.fit(X_train, y_train)

            best_model = gs.best_estimator_

            y_train_pred = best_model.predict(X_train)
            y_test_pred = best_model.predict(X_test)

            train_score = r2_score(y_train, y_train_pred)
            test_score = r2_score(y_test, y_test_pred)

            report[model_name] = {
                "train_r2": train_score,
                "test_r2": test_score,
                "best_params": gs.best_params_
            }

            logging.info(
                f"{model_name} | "
                f"Train R2: {train_score:.4f} | "
                f"Test R2: {test_score:.4f}"
            )

        logging.info("Model evaluation completed.")

        return report

    except Exception as e:
        logging.error("Error occurred during model evaluation.")
        raise CustomException(e, sys)
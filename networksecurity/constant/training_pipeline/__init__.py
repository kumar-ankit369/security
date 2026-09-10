import os
import sys
import numpy as np
import pandas as pd

TARGET_COLUMN = "Result"
PIPELINE_NAME : str = "NetworkSecurity"
ARTIFACT_DIR : str = "Artifacts"
FILE_NAME : str = "phisingData.csv"


TRAIN_FILE_NAME : str = "train.csv"
TEST_FILE_NAME : str = "test.csv"

SCHEMA_FILE_PATH : str = os.path.join("config","schema.yaml")


DATA_INGESTION_COLLECTION_NAME : str = "NetworkData"
DATA_INGESTION_DATABASE_NAME : str = "NetworkSecurity"
DATA_INGESTION_DIR_NAME : str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR_NAME : str = "feature_store"
DATA_INGESTION_INGESTED_DIR_NAME : str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION : float = 0.2



DATA_VALIDATION_DIR_NAME : str = "data_validation"
DATA_VALIDATION_VALID_DIR_NAME : str = "valid"
DATA_VALIDATION_INVALID_DIR_NAME : str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR_NAME : str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME : str = "report.yaml"
PREPROCESSING_OBJECT_FILE_NAME : str = "preprocessor.pkl"


DATA_TRANSFORMATION_IMPUTER_PARAMS : dict = {
    "missing_values": np.nan,
    "n_neighbours": 3,
    "weights": "uniform",
}
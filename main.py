from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig


import sys


if __name__ == "__main__":
    try:
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        logging.info("Initiate the data ingestion process")
        dataingestionartiact = data_ingestion.initiate_data_ingestion()
        df = data_ingestion.export_collection_as_dataframe()
        print(df.head())
    except Exception as e:
        raise NetworkSecurityException(e,sys)
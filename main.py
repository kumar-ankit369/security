from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig


import sys


if __name__ == "__main__":
    try:
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        logging.info("Initiate the data ingestion process")
        dataingestionartiact = data_ingestion.initiate_data_ingestion()
        logging.info("Data ingestion process completed")
        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartiact,data_validation_config)
        logging.info("Initiate the data validation process")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data validation process completed")
        print(data_validation_artifact)
        data_tranformation_config=DataTransformationConfig(trainingpipelineconfig)
        data_transformation= DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("Data transformation process completed")





    except Exception as e:
        raise NetworkSecurityException(e,sys)
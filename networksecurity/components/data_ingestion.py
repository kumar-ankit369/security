from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging




from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact



import os
import sys
import numpy as np
import pandas as pd
import pymongo  



from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

MONGO_DB_URL = os.getenv("MONGO_DB_URL")  # Get the MongoDB URL from environment variables



class DataIngestion:

    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            logging.info(f"{'='*20}Data Ingestion log started.{'='*20}")

            self.data_ingestion_config = data_ingestion_config

        except Exception as e:
            raise NetworkSecurityException(e,sys)


    def export_collection_as_dataframe(self):
        try:
            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            collection = self.mongo_client[database_name][collection_name]



            df=pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df=df.drop(columns=["_id"],axis=1)



            df.replace({"na": np.nan}, inplace=True)
            return df
        except Exception as e:
            raise NetworkSecurityException(e,sys)


           
    def __initiate_data_ingestion(self):

        try:
            dataframe = self.export_collection_as_dataframe()
            datafraame= self.export_data_into_feature_store(dataframe)
            self.split_data_as_train_test(dataframe=datafraame)
            dataingestionartifact = DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path,test_file_path=self.data_ingestion_config.testing_file_path)

            return dataingestionartifact


        except Exception as e:
            raise NetworkSecurityException(e,sys)
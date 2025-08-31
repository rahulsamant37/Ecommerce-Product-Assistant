# from langchain_core.documents import Document
# from langchain_astradb import AstraDBVectorStore
# from Product_Assistant.utils.model_loader import ModelLoader
# from Product_Assistant.utils.config_loader import load_config

# import os
# import pandas as pd
# from typing import List
from dotenv import load_dotenv
load_dotenv()

class DataIngestion:
    """
    Class to handle data transformation and ingestion into AstraDB vector store.
    """
    def __init__(self):
        """_summary_
        """
        pass
    
    def _load_env_variables(self):
        """Load environment variables from .env file.
        """
        pass
        
    def _get_csv_path(self):
        """Get the path to the CSV file.
        """
        pass
    
    def _load_csv(self):
        """Load the CSV file into a DataFrame.
        """
        pass
    
    def transform_data(self):
        """Transform the data for ingestion.
        """
        pass
    
    def store_in_vector_db(self):
        """Store the transformed data in the vector database.
        """
        pass
    
    def run_pipeline(self):
        """Run the entire data ingestion pipeline.
        """
        pass
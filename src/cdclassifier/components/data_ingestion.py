import os
import zipfile
from cdclassifier import logger
from cdclassifier.utils.common import get_size
from cdclassifier.utils.common import get_dataset
from cdclassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            # filename, header = request.urlretrieve(
            #     url=self.config.source_URL,
            #     filename = self.config.local_data_file
            # )
            get_dataset(
                secret_dir = Path(self.config.api_file),
                dataset= self.config.dataset,
                dataset_path= Path(self.config.local_data_file)
            )
            filename = self.config.local_data_file.split('/')[-1]
            
            logger.info(f"{filename} download complete!")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
    
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
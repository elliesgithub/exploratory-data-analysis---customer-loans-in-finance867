import yaml
from sqlalchemy import create_engine
import pandas as pd

def load_credentials(file_path='credentials.yaml'):
    with open(file_path, 'r') as file:
        credentials = yaml.safe_load(file)
    return credentials

class RDSDatabaseConnector:
    def __init__(self, credentials):
        self.credentials = credentials
        self.engine = self.create_engine()

    def create_engine(self):
        engine = create_engine(
            f"postgresql+psycopg2://{self.credentials['RDS_USER']}:{self.credentials['RDS_PASSWORD']}@{self.credentials['RDS_HOST']}:{self.credentials['RDS_PORT']}/{self.credentials['RDS_DATABASE']}"
        )
        return engine

    def extract_data_to_dataframe(self, query):
        df = pd.read_sql(query, self.engine)
        return df

    def save_data_to_csv(self, dataframe, filename='loan_payments.csv'):
        dataframe.to_csv(filename, index=False)
        print(f'Data saved to {filename}') 

def load_local_data(file_path):
    df = pd.read_csv(file_path)
    print(f"Data Shape: {df.shape}")
    print("\nSample of the Data:")
    print(df.head())
    return df

if __name__ == "__main__":
    credentials = load_credentials()
    rds_connector = RDSDatabaseConnector(credentials)
    
    sql_query = "SELECT * FROM loan_payments"
    
    data_frame = rds_connector.extract_data_to_dataframe(sql_query)
    rds_connector.save_data_to_csv(data_frame)

    local_file_path = 'loan_payments.csv'
    load_local_data(local_file_path)





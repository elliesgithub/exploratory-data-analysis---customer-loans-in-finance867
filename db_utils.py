import yaml
from sqlalchemy import create_engine
import pandas as pd

def load_credentials(file_path='credentials.yaml'):
    """ 
    This function is used to load database credentials from a YAML file.

    """
    with open(file_path, 'r') as file:
        credentials = yaml.safe_load(file)
    return credentials

class RDSDatabaseConnector:
    """ 
    This class connects to the Relational Database Service which contains the loan payments data
    """
    def __init__(self, credentials):
        """
        This method initialises the RDSDatabaseConnector.
        """
        self.credentials = credentials
        self.engine = self.create_engine()

    def create_engine(self):
        """
        This method creates a SQAlchemy engine which allows data to be extracted from the database
        """
        engine = create_engine(
            f"postgresql+psycopg2://{self.credentials['RDS_USER']}:{self.credentials['RDS_PASSWORD']}@{self.credentials['RDS_HOST']}:{self.credentials['RDS_PORT']}/{self.credentials['RDS_DATABASE']}"
        )
        return engine

    def extract_data_to_dataframe(self, query):
        """ 
        This method extracts data from the RDS using a SQL Query and returns it as a dataframe.
        """
        df = pd.read_sql(query, self.engine)
        return df

def save_data_to_csv(self, dataframe, filename='loan_payments.csv'):
    """ 
    This method saves the dataframe to a .csv file.
    """
    dataframe.to_csv(filename, index=False)
    print(f'Data saved to {filename}') 


if __name__ == "__main__":
    credentials = load_credentials()
    rds_connector = RDSDatabaseConnector(credentials)
    
    sql_query = "SELECT * FROM loan_payments"
    
    data_frame = rds_connector.extract_data_to_dataframe(sql_query)
    rds_connector.save_data_to_csv(data_frame)

    local_file_path = 'loan_payments.csv'
    





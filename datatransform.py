import pandas as pd

class DataTransform:
    def __init__(self, dataframe) -> None:
        self.dataframe = dataframe
    """
    This is used in order to transform pre-existing data in the dataframes columns. 
    """
    

    def convert_dates_to_datetime(self, columns):
        """
        This method transforms all data which involves dates into a datetime formatting. 
        """
        for column in columns:
            self.dataframe[column] = self.dataframe[column].apply(lambda x: pd.to_datetime(x, errors='coerce', format='%b-%Y'))
        return self.dataframe
    
    
    def convert_to_categorical(self, columns):
        """
        This method transforms data into categorical data types. 
        """
        for column in columns:
            self.dataframe[column] = pd.Categorical(self.dataframe[column])
        return self.dataframe
    
    
    def convert_string_to_integer(self, columns):
        """
        This method transforms data by removing non-numerical characters in a string
        """
        for column in columns:
            if column in ['term']:
                self.dataframe[column] = self.dataframe[column].str.extract('(\d+)').astype('Int64')
            else:
                self.dataframe[column] = pd.to_numeric(self.dataframe[column], errors='coerce').astype('Int64')
        return self.dataframe
    

    def drop_columns(self, column):
        """
        Drop columns with a percentage of NULL values exceeding the threshold of 10%.
        """
        self.dataframe.drop(column, axis=1, inplace=True)
        return self.dataframe
    

    def drop_rows(self,column):
        self.dataframe.dropna(subset=column, inplace=True)
        return self.dataframe





    

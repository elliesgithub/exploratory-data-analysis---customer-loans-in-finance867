import pandas as pd

class DataFrameInfo:
    def __init__(self, dataframe):
        self.df = dataframe

    def describe_data_types(self):
        """
        Returns a summary of data types in the DataFrame.
        """
        return self.df.dtypes


    def median(self, column):
        """
        Returns the median of columns.
        """
        if self.df[column].dtype.name in ['int64', 'float64']:
            return self.df[column].median()
        else:
            return None


    def standard_deviation(self, column):
        """
        Returns the standard deviation of columns.
        """
        if self.df[column].dtype.name in ['int64', 'float64']:
            return self.df[column].std()
        else:
            return None


    def mean(self, column):
        """
        Returns the mean of columns.
        """
        if self.df[column].dtype.name in ['int64', 'float64']:
            return self.df[column].mean()
        else:
            return None


    def count_distinct_values(self, column):
        """
        Returns the number of distinct values in a specified column.
        """
        return self.df[column].nunique()


    def shape(self):
        """
        Returns the shape (number of rows and columns) of the DataFrame.
        """
        return self.df.shape


    def null_count(self):
        """
        Returns the count of null values in each column.
        """
        return self.df.isnull().sum()


    def null_percentage(self):
        """
        Returns the percentage of null values in each column.
        """
        return (self.df.isnull().mean() * 100).round(2)
    
    
    def get_columns_with_null_values(self):
        """
        Returns only the columns with null values 
        """
        columns_with_null = self.df.columns[self.df.isnull().any()].tolist()
        return columns_with_null
    

    def identify_skewed_columns(self,threshold =  0.5):
        """
        Returns skeweness of a column 
        """
        skewed_columns_list = []

        for column in self.df.columns:
            if column != 'term' and pd.api.types.is_numeric_dtype(self.df[column]):
                skewness = self.df[column].skew(numeric_only=True)
                if abs(skewness) > threshold:
                    print(f"Skewness of {column}: {skewness}")
                    skewed_columns_list.append(column)

        return skewed_columns_list 
    
    

   







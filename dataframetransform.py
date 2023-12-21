import numpy as np
import pandas as pd
from scipy import stats
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 


class DataFrameTransform:
    def __init__(self, dataframe):
        self.df = dataframe
        
        
    def impute_with_mean(self, column):
        """
        Method used to fill null values in a column with the mean value.

        Parameters:


        Returns:
        Dataframe with null values imputed.

        """
        self.df[column].fillna(self.df[column].mean(), inplace=True)
        
    

    def impute_with_median(self, column):
        """
        Method used to fill null values in a column with the mean value

        Parameters:

        Returns:
        Dataframe with null values imputed.
        """
        self.df[column].fillna(self.df[column].median(), inplace=True)


    def save_null_data_to_csv(self, filename='loan_payments_null_imputations.csv'):
        """ 
        This method saves the dataframe to a .csv file.
        """
        self.df.to_csv(filename, index=False)
        print(f'Data saved to {filename}')


    def boxcox(self, column):
        boxcox_column = stats.boxcox(self.df[column]+1)
        boxcox_column = pd.Series(boxcox_column[0])
        return boxcox_column


    def yeojohnson(self, column):
        yeojohnson_column = stats.yeojohnson(self.df[column])
        yeojohnson_column = pd.Series(yeojohnson_column[0])
        return yeojohnson_column


    def log(self, column):
        log_column = self.df[column].map(lambda i: np.log1p(i) if i > 0 else 0)
        return log_column


    def apply_best_transformation(self, skewed_columns_list):
        """
        This applies the transformation which reduces the skew of columns the most
        """
        best_transformations = {}
        for column in skewed_columns_list:
            boxcox_column = self.boxcox(column)
            boxcox_skewness = boxcox_column.skew()
            
            yeojohnson_column = self.yeojohnson(column)
            yeojohnson_skewness = yeojohnson_column.skew()
            
            log_column = self.log(column)
            log_skewness = log_column.skew()
            
            best_transformation, best_skewness = min([('Box-Cox', boxcox_skewness), ('Yeo-Johnson', yeojohnson_skewness), ('Log', log_skewness)],
            key=lambda x: abs(x[1]))
            
            best_transformations[column] = {'Transformation': best_transformation, 'Skewness': best_skewness}
            
            if best_transformation == 'Box-Cox':
                self.df[column] = boxcox_column
            elif best_transformation == 'Yeo-Johnson':
                self.df[column] = yeojohnson_column
            elif best_transformation == 'Log':
                self.df[column] = log_column
                
                
            print(f"Best transformation for {column}: {best_transformation} (Skewness: {best_skewness})")
        return best_transformations



    def save_changed_skewed_data_to_csv(self, filename='loan_payments_changed_skewed_data.csv'):
        """ 
        This method saves the dataframe to a .csv file.
        """
        self.df.to_csv(filename, index=False)
        print(f'Data saved to {filename}')


    def remove_outliers(self, columns):
        for column in columns:
            Q1 = self.df[column].quantile(0.25)
            Q3 = self.df[column].quantile(0.75)
            IQR = Q3 - Q1
            print(f"Q1 (25th percentile): {Q1}")
            print(f"Q3 (75th percentile): {Q3}")
            print(f"IQR: {IQR}")
            
            outliers = self.df[(self.df[column] < (Q1 - 1.5 * IQR)) | (self.df[column] > (Q3 + 1.5 * IQR))]
            print("Outliers:")
            print(outliers[column])

            self.df = self.df.drop(outliers.index)

    def save_removed_outliers_and_over_correlation_to_csv(self, filename='loan_payments_outliers_and_correlation.csv'):
        """ 
        This method saves the dataframe to a .csv file.
        """
        self.df.to_csv(filename, index=False)
        print(f'Data saved to {filename}')

    def identify_highly_correlated_columns(self, threshold=0.8):
        numeric_columns = self.df.select_dtypes(include='number')
        correlation_matrix = numeric_columns.corr()
        highly_correlated_columns = set()
        for i, col_i in enumerate(correlation_matrix.columns):
            for col_j in correlation_matrix.columns[:i]:
                correlation_value = correlation_matrix.loc[col_i, col_j]
                if abs(correlation_value) > threshold:
                    print(f"Columns '{col_i}' and '{col_j}': {correlation_value}")
                    highly_correlated_columns.add(col_i)
                    highly_correlated_columns.add(col_j)

        # Print or return the highly correlated columns
        return highly_correlated_columns


    def remove_highly_correlated_columns(self, threshold=0.8):
        # Identify highly correlated columns
        highly_correlated_columns = self.identify_highly_correlated_columns(threshold=threshold)
        self.df = self.df.drop(columns=highly_correlated_columns)

        print("Columns removed:", highly_correlated_columns)



    







    



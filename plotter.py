import pandas as pd
from matplotlib import pyplot
import missingno as msno
import pandas as pd
from scipy import stats
import seaborn as sns
import plotly.express as px
from statsmodels.graphics.gofplots import qqplot
import numpy as np


class Plotter:
    """
    This method visualises missing data patterns in the dataframe using different visualisations
    
    """
    def __init__(self, dataframe):
        self.df = dataframe


    def missing_matrix(self):
        """
        Generates and displays a missingness matrix
        """
        return msno.matrix(self.df)
    
    def missing_heatmap(self):
        """
        Generates and displays a missingness heatmap
        """
        return msno.heatmap(self.df)
    

    def histogram(self):
        """
        Generates histogram 
        """
        for column in self.df.columns:
            skewness = self.df[column].skew()
            fig = px.histogram(self.df, x=column, nbins=30, title=f'Histogram of {column}(Skewness: {skewness:.2f})')
            fig.show()
    
    def histogram_skews(self,skewed_columns_list):
        for column in skewed_columns_list:
            skewness = self.df[column].skew()
            fig = px.histogram(self.df, x=column, nbins=30, title=f'Histogram of {column}(Skewness: {skewness:.2f})')
            fig.show()


    def qqplot_skews(self,skewed_columns_list):
        for column in skewed_columns_list:
            skewness = self.df[column].skew()
            qq_plot = qqplot(self.df[column], scale=1, line='q')
            pyplot.title(f'QQ Plot for {column}(Skewness: {skewness:.2f})')
            pyplot.show()


    def boxcox(self, column):
        """
        Performs boxcox transformation and visualisation
        """
        constant = 1 - self.df[column].min()
        adjusted_column = self.df[column] + constant
        boxcox_column, _ = stats.boxcox(adjusted_column)
        boxcox_column = pd.Series(boxcox_column)
        pyplot.figure()
        t = sns.histplot(boxcox_column, label="Skewness: %.2f" % (boxcox_column.skew()))
        t.legend()
        pyplot.title(f"Box-Cox Transformation: {column}")
        pyplot.show()
        pyplot.close()
        return boxcox_column
    

    def yeojohnson(self, column):
        """
        Performs yeojohnson transformation and visualisation 
        """
        yeojohnson_column = self.df[column]
        yeojohnson_column = stats.yeojohnson(yeojohnson_column)
        yeojohnson_column= pd.Series(yeojohnson_column[0])
        pyplot.figure()
        t=sns.histplot(yeojohnson_column,label="Skewness: %.2f"%(yeojohnson_column.skew()) )
        t.legend()
        pyplot.title(f"Yeo-Johnson Transformation: {column}")
        pyplot.show()
        pyplot.close()
        return yeojohnson_column
    

    def log(self,column):
         """
         Performs log transformation and visualisation 
         """
         log_column = self.df[column].map(lambda i: np.log1p(i) if i > 0 else 0)
         pyplot.figure()
         t= sns.histplot(log_column,label="Skewness: %.2f"%(log_column.skew()) )
         t.legend()
         pyplot.title(f"Log Transformation: {column}")
         pyplot.show()
         pyplot.close()
         return log_column
    

    def visualise_boxplot_for_outliers(self,skewed_columns_list):
        """
        Visualises boxplot 
        """
        for column in skewed_columns_list:
            pyplot.figure(figsize=(10, 5))
            sns.boxplot(x=self.df[column])
            pyplot.title(f'Box plot  of {column}')
            pyplot.show()

    
    def visualise_correlation_matrix(self):
        """
        Visualises correlation matrix
        """
        numeric_columns = self.df.select_dtypes(include='number')
        correlation_matrix = numeric_columns.corr()
        fig = px.imshow(correlation_matrix, title="Correlation matrix for the dataset")
        fig.show()
        return correlation_matrix
    

    def plot_pie_chart(self, labels_column, values_column, title):
        """
        Visualises pie chart 
        """
        fig = px.pie(self.df, names=labels_column, values=values_column, title=title)
        fig.show()


    def plot_bar_chart(self, x_column, y_column, title, xlabel, ylabel):
        """
        Visualises bar chart 
        """
        fig = px.bar(self.df, x=x_column, y=y_column, title=title, labels={x_column: xlabel, y_column: ylabel})
        fig.show()

    
    
    

    
       
        
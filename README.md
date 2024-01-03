# Exploratory Data Analysis - Customer Loans in Finance

## Table of Contents
[Project Description](#ProjectDescription)
[Installation](#Installation)
[Usage](#Usage)
[File structure of the project](#Filestructureoftheproject)
[License](#License)



## Project Description
This project focuses on extracting loan payment data from a database in the cloud (an AWS Relational Database). It is then converted into a local csv file and datas pandaframe to later be transformed and analysed. 

The data is first converted to formatting which allows for easier data analysis. Information such as datatypes, statistical values and **null counts/percentages** can then be worked out. Data is then **removed/imputed** depending on the extent of missing values. **Skewed columns are transformed**, **outliers removed** and **overly correlated columns removed**. This is done within the EDANotebook.ipynb.

Within the Analysis_visualisation.ipynb notebook their is **calculations of loss, projected loss, possible loss and indicators of loss**. 

The aim of the project is to gain an understanding of the data and identify patterns which exist. Furthermore, once the data has been transformed in the EDA notebook a further analysis is performed on the dataset in the Analysis visualisation notebook to try to identify any patterns or trends which were not identified in the first notebook. Using this further analysis a team could be more informed about which loans are a higher and lower risk to a company.

I have learnt a lot in this project about being able to conncect to reational databases and how to transfrom data columns/rows in order to be analyse and visualise to gain insights. For null values different imputation techniques were used including mean and median; For skeweness transformatons of yeojohnson, boxcox and log were all used to see which reduced skew by the most; For outliers interquartlie range was used and for collinearity correlation matrices. This includes the plotting of these data visualisations on different graphs such as histograms, qq plots, boxplots etc.



## Installation
1. Clone the github repository into a terminal using the command below.
```
git clone https://github.com/elliesgithub/exploratory-data-analysis---customer-loans-in-finance867.git
```
2. Make sure the prerequisite packages are installed in a conda environment. You can see the pacakages needed in the *'conda_environment.yaml'* script. 
3. Run the scripts described in the usage instructions.


## Usage
1. Run the *'db_utils.py'* file in order to connect to the AWS Relational Database. This creates the original *'loan_payments.csv'*. The *credentials.yaml* of the database has been omitted from the repository to protect data.
2. Secondly, run the *'EDANotebook.ipynb'* notebook. This notebook performs transformations on the dataframe to **change null values, skewness, outliers and collinearity** and saves different .csv's according to the transformations performed. 
(at this point you can optionally run the *'skewness.ipynb'* file which uses the *'loan_payments_null_imputations.ipynb'* file to see the full visualisations of each method of transforming the skewed columns before applying the method which results in the most reduced skewness in the main EDA notebook.)
3. The *'Analysis_visualisation.ipynb'* is then run to visualise the different current and projected losses which can be gathered from the data post null imputations (*'loan_payments_null_imputations.ipynb'*).



## File structure of the project
Exploratory Data Analysis
├─ Loan_datasets/
│  ├─ loan_payments.csv
│  ├─ loan_payments_changed_skewed_data.csv 
│  ├─ loan_payments_null_imputations.csv          
│  └─ loan_payments_outliers_and_correlation.csv 
├─ Analysis_visualisation.ipynb 
├─ EDANotebook.ipynb        
├─ skewness.ipynb  
├─ conda_environment.yaml                  
├─ dataframeinfo.py
├─ dataframetransform.py
├─ db_utils.py
├─ plotter.py
├─ LICENSE.txt
├─ README.md




(Readme documentation)
- README.md

(CSV files)
- loan_payments.csv
- loan_payments_changed_skewed_data.csv
- loan_payments_null_imputations.csv
- loan_payments_outliers_and_correlation.csv

(Python scripts)
- db_utils.py
- datatransform.py
- dataframeinfo.py
- dataframetransform.py
- plotter.py

(Notebooks)
- skewness.ipynb
- EDANotebook.ipynb
- Analysis_visualisation.ipynb

(YAML file)
- conda_environment.yaml

(License document)
- LICENSE.txt

Omitted files = 
- .gitignore 
- credentials.yaml


## License
MIT License
A short and simple permissive license with conditions only requiring preservation of copyright and license notices. Licensed works, modifications, and larger works may be distributed under different terms and without source code.
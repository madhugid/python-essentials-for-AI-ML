# Azure CLI (Azure Command-Line Interface): A command-line tool that allows management and interaction with Azure services and resources.
import azure.cli.core

cli = azure.cli.core.AzureCli()
cli.invoke(["storage", "account", "list"])

# Azure ML (Azure Machine Learning) Studio: A cloud-based environment for machine learning development and deployment.
from azureml.core import Workspace

ws = Workspace.create(name='myworkspace', 
                     subscription_id='...', 
                     resource_group='myresourcegroup', 
                     location='eastus')

# Transformers: A Hugging Face library for natural language processing tasks
from transformers import pipeline

classifier = pipeline("sentiment-analysis")
result = classifier("I love this course!")
print(result)

# Datasets: A Hugging Face library for loading datasets.
from datasets import load_dataset

dataset = load_dataset("glue", "mrpc")
train_dataset = dataset["train"]
print(len(train_dataset))

# Open Datasets: An Azure resource for loading curated public datasets.
from azureml.opendatasets import PublicHolidays

holidays = PublicHolidays()
holidays_df = holidays.to_pandas_dataframe()
print(holidays_df.head())

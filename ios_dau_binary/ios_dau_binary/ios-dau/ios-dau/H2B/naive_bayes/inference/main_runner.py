# Databricks notebook source
# MAGIC %run Repos/apps/ios-dau/utils/parallel_notebook_runner

# COMMAND ----------

Notebook.runner(notebook_name = './main',
                arguments={"envs": "master_NB,master_preprocessing"},
                start_date=date(2022,8,7), 
                end_date=date(2022,10,31),
                timeout=3600*5,
                parallel_runs=5)
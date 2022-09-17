import os

from google.cloud import bigquery
from google.oauth2 import service_account
from loguru import logger
from common import env


class BigqueryDac:
    def __init__(self) -> None:
        self._credentials = service_account.Credentials.from_service_account_file(env.GCS_KEY_FILE)
        self.bigquery_client = bigquery.Client(credentials=self._credentials, project=self._credentials.project_id)


    def select_query(self, query):
        try:
            results = self.bigquery_client.query(query)
            return results.to_dataframe()

        except Exception as e:
            logger.error(e)

            return None

    
    def select_query_param(self, query, query_parameters):
        try:
            job_config = bigquery.QueryJobConfig(query_parameters=query_parameters)
            results = self.bigquery_client.query(query,  job_config=job_config)

            return results.to_dataframe()

        except Exception as e:
            logger.error(e)

            return None


    def execute_query(self, query):
        try:
            query_job = self.bigquery_client.query(query)
            results = query_job.result()
            
            return results.to_dataframe()

        except Exception as e:
            logger.error(e)

            return None


    def execute_query_v2(self, origin_table, table_id, query):
        try:
            if self.CheckTableExists(table_id) is False:
                job = self.bigquery_client.copy_table(origin_table, table_id)  
                job.result()

            query_job = self.bigquery_client.query(query)
            results = query_job.result()

            return results

        except Exception as e:
            logger.error(e)

            return None


    def check_table_exists(self, table_id):
        try:
            self.bigquery_client.get_table(table_id)
            return True

        except Exception as e:
            logger.error(e)

            return False

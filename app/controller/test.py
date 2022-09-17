from loguru import logger
from common.connector import BigqueryDac


async def read_bigquery_data():
    try:
        dac = BigqueryDac()
        data = dac.select_query('SELECT * FROM `mpp-biz-dev.plcc_test.plcc_all_20210816` LIMIT 10')

        return data

    except Exception as e:
        logger.error(e)

        return None


import argparse
import json
import os
import os.path
from datetime import datetime

import pendulum


def pretty(*ag):
    d = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'{d} - {ag[0]}')


def main():
    parser = argparse.ArgumentParser(description='tiktok pipeline')
    parser.add_argument("-s", "--start_date", help="start date",
                        default=pendulum.now().subtract(days=5).to_date_string())
    parser.add_argument("-e", "--end_date", help="end date", default=pendulum.now().subtract(days=1).to_date_string())

    args = parser.parse_args()
    started = datetime.now()
    sf_account = os.environ['SNOWFLAKE_ACCOUNT']
    sf_username = os.environ['SNOWFLAKE_USERNAME']
    sf_role = os.environ['SNOWFLAKE_ROLE']
    sf_password = os.environ['SNOWFLAKE_PASSWORD']
    sf_database = os.environ['SNOWFLAKE_DATABASE']
    sf_schema = os.environ['SNOWFLAKE_SCHEMA']
    sf_warehouse = os.environ['SNOWFLAKE_WAREHOUSE']

    conf = {'start_date': args.start_date,
            'end_date': args.end_date,
            'auth_token': os.environ['TIKTOK_API_KEY'],
            'advertiser_id': os.environ['TIKTOK_ADVERTISER_ID']}

    tap = 'tap-tiktok'
    target = 'atidiv-target-snowflake'
    tap_config = 'tiktok_config.json'
    target_config = 'snowflake_config.json'

    with open(tap_config, 'w') as out:
        json.dump(conf, out)

    snowflake_conf = {
        "snowflake_account": sf_account,
        "snowflake_username": sf_username,
        "snowflake_role": sf_role,
        "snowflake_password": sf_password,
        "snowflake_database": sf_database,
        "snowflake_schema": sf_schema,
        "snowflake_warehouse": sf_warehouse,
        "add_metadata_columns": False
    }

    with open(target_config, 'w') as out:
        json.dump(snowflake_conf, out)

    r = os.system(
        f" ~/.virtualenvs/{tap}/bin/{tap}  --config {tap_config}  | ~/.virtualenvs/{target}/bin/{target} -c {target_config}")

    if r != 0:
        raise Exception('error occurred!')

    ended = datetime.now()
    pretty(f'execution time : {ended - started}')


if __name__ == '__main__':
    main()

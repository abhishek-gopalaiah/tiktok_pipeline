"# tiktok_pipeline" 
```
cd tiktok_ads # tiktok_pipeline directory

python3 -m venv ~/.virtualenvs/atidiv-target-snowflake
source ~/.virtualenvs/atidiv-target-snowflake/bin/activate

pip install git+https://github.com/atidivhq/atidiv-target-snowflake.git

python3 -m venv ~/.virtualenvs/tap-tiktok
source ~/.virtualenvs/tap-tiktok/bin/activate

cd tiktok_ads # tiktok_pipeline directory
poetry install tap-tiktok

```


```
#!/bin/bash

export SNOWFLAKE_ACCOUNT=hma660xx
export SNOWFLAKE_USERNAME=atidiv
export SNOWFLAKE_PASSWORD=Spasskeexxx
export SNOWFLAKE_DATABASE=ATI
export SNOWFLAKE_SCHEMA=RAW_TIKTOK
export SNOWFLAKE_WAREHOUSE=PC_FIVETRAN_WH
export SNOWFLAKE_ROLE=SYSADMIN
export TIKTOK_API_KEY=xxxxxxxxxxx


cd /home/atidiv/github/pipelines
git pull
source /home/atidiv/github/pipelines/.venv/bin/activate
cd tiktok_pipeline

# export START_DATE=2020-01-01
export TIKTOK_ADVERTISER_ID=696408xxxxx0553089
python pipeline.py #--start_date 2020-01-01


# export START_DATE=2020-01-01
export SNOWFLAKE_SCHEMA=RAW_TIKTOK
export TIKTOK_ADVERTISER_ID=68865xxxxx4323842


python pipeline.py #--start_date 2020-01-01
```

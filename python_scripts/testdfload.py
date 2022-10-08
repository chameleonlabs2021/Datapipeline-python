
import pandas as pd
from deepchecks.tabular import Dataset
from deepchecks.tabular.suites import data_integrity

def load_config():
    """Load configurations from the file `main.yaml` under the `config` directory"""
    with initialize(version_base=None, config_path="../config"):
        config = compose(config_name="main")
    return config

def read_new_data(config):
    """Read data from PostgreSQL database"""
    with open ("config.json" , "r") as f:
            config_data= json.loads(f.read() )

        db = config_data["StgDatabase"]  #change to staging for your database
        user=config_data["USER"]
        password=config_data["PASSWORD"]
        host=config_data["HOST"]
        port=config_data["PORT"]
        reconCsvPath=config_data["reconCsvPath"]

    connection = config.connection
    engine = create_engine('postgresql://'+user+':'+password+'@'+host+':'+port+'/'+db)
    query = f'SELECT * FROM "{config.data.raw}"'
    df = pd.read_sql(query, con=engine)
    return df

def init_dataset(data: pd.DataFrame, config):
    return Dataset(
        data, cat_features=list(config.cat_cols), label=config.label
    )

def create_data_integrity_suite(dataset: Dataset, config):
    integ_suite = data_integrity(columns=list(config.check_integrity_cols))
    result = integ_suite.run(dataset)
    result.save_as_html(config.report.data_integrity)
    return result

def is_suite_passed(result):
    assert result.passed()

def check_data_integrity():
    config = load_config()
    df = read_new_data(config)
    dataset = init_dataset(df, config)
    result = create_data_integrity_suite(dataset, config)
    is_suite_passed(result)

if __name__=="__main__":
    check_data_integrity()
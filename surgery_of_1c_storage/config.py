import configparser
import os

PARAMS = configparser.ConfigParser()


def init_config(config_file_name):
    if not os.path.exists(config_file_name):
        full_path = os.path.abspath(config_file_name)
        raise Exception(f'Файл с конфигурацией не найден по указанному пути: {full_path}')
    PARAMS.read(config_file_name)
    return PARAMS


def create_config_file(filename, db_type):

    with open(filename, 'w') as f:
        if db_type == 'psql':
            f.write(get_template_config_psql().strip())
        elif db_type == 'mssql':
            f.write(get_template_config_mssql.strip())
        else:
            raise Exception('Неизвестный тип СУБД')
    print(f'Шаблон конфигурационного файла для {db_type} сохранен в {filename}')

def get_template_config_psql():

    db_type = os.getenv('SOOC_DB_TYPE') if os.getenv('SOOC_DB_TYPE') != None else "Postgres"
    server = os.getenv('SOOC_DB_SERVER') if os.getenv('SOOC_DB_SERVER') != None else "host"
    user = os.getenv('SOOC_DB_USER') if os.getenv('SOOC_DB_USER') != None else "postgres"
    password = os.getenv('SOOC_DB_PASSWORD') if os.getenv('SOOC_DB_PASSWORD') != None else "postgres"
    basename = os.getenv('SOOC_DB_BASENAME') if os.getenv('SOOC_DB_BASENAME') != None else "infobase"
    port = os.getenv('SOOC_DB_PORT') if os.getenv('SOOC_DB_PORT') != None else "5432"
    tables_with_config_file = os.getenv('SOOC_TABLES_WITH_CONFIG_FILE') if os.getenv('SOOC_TABLES_WITH_CONFIG_FILE') != None else "params,files,config,configsave,configcas,configcassave"
    file_encode_mode = os.getenv('SOOC_FILE_ENCODE_MODE') if os.getenv('SOOC_FILE_ENCODE_MODE') != None else ".encode_modes"
    template_config_file_psql = f"""
    [Database]
    TYPE = {db_type}
    SERVER = {server}
    USER = {user}
    PASSWORD = {password}
    BASENAME = {basename}
    PORT = {port}

    [InnerStructureKeys]
    TABLES_WITH_CONFIG_FILE = {tables_with_config_file}

    [Coder]
    FILE_ENCODE_MODE = {file_encode_mode}
    """
    return template_config_file_psql

def get_template_config_mssql():
    
    db_type = os.getenv('SOOC_DB_TYPE') if os.getenv('SOOC_DB_TYPE') != None else "Postgres"
    server = os.getenv('SOOC_DB_SERVER') if os.getenv('SOOC_DB_SERVER') != None else "host"
    user = os.getenv('SOOC_DB_USER') if os.getenv('SOOC_DB_USER') != None else "postgres"
    password = os.getenv('SOOC_DB_PASSWORD') if os.getenv('SOOC_DB_PASSWORD') != None else "postgres"
    basename = os.getenv('SOOC_DB_BASENAME') if os.getenv('SOOC_DB_BASENAME') != None else "infobase"
    port = os.getenv('SOOC_DB_PORT') if os.getenv('SOOC_DB_PORT') != None else "5432"
    tables_with_config_file = os.getenv('SOOC_TABLES_WITH_CONFIG_FILE') if os.getenv('SOOC_TABLES_WITH_CONFIG_FILE') != None else "params,files,config,configsave,configcas,configcassave"
    file_encode_mode = os.getenv('SOOC_FILE_ENCODE_MODE') if os.getenv('SOOC_FILE_ENCODE_MODE') != None else ".encode_modes"
    odbc_driver = "{SQL Server Native Client 11.0}"
    template_config_file_mssql = f"""
    [Database]
    TYPE = {db_type}
    SERVER = {server}
    USER = {user}
    PASSWORD = {password}
    BASENAME = {basename}
    PORT = {port}
    ODBC_DRIVER={odbc_driver}

    [InnerStructureKeys]
    TABLES_WITH_CONFIG_FILE = {tables_with_config_file}

    [Coder]
    FILE_ENCODE_MODE = {file_encode_mode}
    """
    return template_config_file_mssql
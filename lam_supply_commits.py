# %%
import pyodbc
import pandas as pd

CONNECTION_STRING = f'\
            DRIVER={{ODBC Driver 17 for SQL Server}};\
            ENCRYPT=no;\
            SERVER=172.20.103.105;\
            DATABASE=MDC_AX2009SP1_PROD;\
            UID=USSQLUser;\
            PWD=Insp1r0n2022'

def get_ax_lead_times():
    ITEMID = 0
    LEADTIME = 1

    cursor = pyodbc.connect(CONNECTION_STRING).cursor()

    cursor.execute(LEAD_TIMES_QUERY)

    rows = [tuple(r) for r in cursor.fetchall()]

    data = dict()

    for row in rows:
        data[row[ITEMID]] = row[LEADTIME]

    return 


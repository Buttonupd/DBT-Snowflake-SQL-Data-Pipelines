import json
from airflow.models.connection import Connection
import pandas as pd


c = Connection(
     conn_id="conn_id",
     description="connection description",
     host="DKARIUKI-PC\BASES]SQL_SERVER",
     login="",
     password="",
     extra=json.dumps(dict(this_param="some val", that_param="other val*")),
 )
conn = c.test_connection()

print(conn)

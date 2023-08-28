import json
from airflow.models.connection import Connection
import pandas as pd


c = Connection(
     conn_id="conn_id",
     description="connection description",
     host="DKARIUKI-PC\BASES]SQL_SERVER",
     login="sa",
     password="Saf3rthanc0v1d19",
     extra=json.dumps(dict(this_param="some val", that_param="other val*")),
 )
conn = c.test_connection()

print(conn)

import pandas as pd
import json

def get_map_graph_values(engine):
    query_copilot = f'''SELECT 
      s.station, 
      t.data, 
      t.hora, 
      t."radiacao global (kj/m2)", 
      t."vento rajada maxima (m/s)", 
      t."vento direcao horaria (gr) (° (gr))", 
      t."vento velocidade horaria (m/s)", 
      t."temperatura maxima na hora ant. (aut) (°c)", 
      t."temperatura minima na hora ant. (aut) (°c)",
      st.*
    FROM 
      (SELECT station FROM collected GROUP BY station) AS s
    LEFT JOIN 
      collected AS t
    ON 
      s.station = t.station AND t.data = (SELECT MAX(data) FROM collected WHERE station = s.station) AND t.hora = (SELECT MAX(hora) FROM collected WHERE station = s.station AND data = (SELECT MAX(data) FROM collected WHERE station = s.station))
    JOIN
      stations AS st
    ON
      s.station = st.station_code;
    '''
    df = pd.read_sql_query(query_copilot,engine)
    df.drop(['collect','first'],axis=1,inplace=True)
    df = df.astype(str)
    df = df.reset_index()
    df = df.iloc[:,2:]
    return json.dumps(df.to_dict(orient='records'))
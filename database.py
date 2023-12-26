from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://5n2w6bb8ygk5jgj4aszm:pscale_pw_XXt4RTMoDxMiwmljrWX4hz36nvtb64jGfLMVmekxpbk@aws.connect.psdb.cloud/lublogs?charset=utf8mb4"
engine = create_engine(db_connection_string,
                       connect_args={
                           "ssl":{
                               "ssl_ca": "/etc/ssl/cert.pem"
                           }
                       })
def load_jobs_from_db():
    with engine.connect() as conn: ##don't forget add() behind connect
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(row)
        return jobs
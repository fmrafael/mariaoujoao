from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import pandas as pd
from flask_bootstrap import Bootstrap

engine = create_engine('sqlite:///babynames.db', echo = True)
engine.connect()

app = Flask(__name__)
Bootstrap(app)
 


df = pd.read_sql_table(
    'babynames',
    con=engine,
    columns=['Nome','Gênero','Origem','Significado','Curiosidade']
)


#r_set=cur.execute('''SELECT Nome,Gênero,Origem,Significado,Curiosidade from babynames ''');
#for row in r_set:
 #   data = row

@app.route("/", methods=("POST", "GET"))
def home():
  return render_template("index.html",tables=[df.to_html( classes='data', header="true",index="false")], titles=df.columns.values)


if __name__ == '__main__':
  app.run(host='0.0.0.0',port=8080, debug=True)


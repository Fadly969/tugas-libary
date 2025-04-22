from flask import Flask, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    df = pd.read_csv('data fadly.txt', sep='\t')
    df.columns = df.columns.str.strip()

    numeric_cols = ['Units Sold', 'Price', 'Revenue', 'Discount', 'Units Returned']
    stats = {}

    for col in numeric_cols:
        data = df[col].dropna().values
        stats[col] = {
            'mean': round(np.mean(data), 2),
            'median': round(np.median(data), 2),
            'std_dev': round(np.std(data), 2)
        }

    # Ambil 20 baris pertama
    table_data = df.head(20)
    return render_template('index.html', stats=stats, table=table_data.to_dict(orient='records'), columns=table_data.columns)

if __name__ == '__main__':
    app.run(debug=True)

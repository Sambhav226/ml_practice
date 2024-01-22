from flask import Flask, render_template, request
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    import matplotlib
    matplotlib.use('Agg')
    distribution_type = request.form['distribution_type']
    sample_size = int(request.form['sample_size'])

    # Generate sample data based on distribution_type and sample_size
    if distribution_type == 'binomial':
        # Replace this with your binomial data generation logic
        data = np.random.binomial(10, 0.5, sample_size)
    elif distribution_type == 'normal':
        data = np.random.normal(0, 1, sample_size)
    elif distribution_type == 'bernoulli':
        data = np.random.choice([0, 1], size=sample_size)

    # Create a histogram
    plt.hist(data, bins=10)
    plt.title('Sample Data Histogram')
    plt.xlabel('Value')
    plt.ylabel('Frequency')

    # Save the plot as an image and convert it to base64
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    img_base64 = base64.b64encode(img_buffer.read()).decode('utf-8')

    plt.close()

    return render_template('result.html', img_base64=img_base64)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask
from flask import render_template
from flask import request
from flask import send_from_directory
from flask import after_this_request
from scraper import *

app = Flask(__name__)

filename = ''
df = pd.DataFrame()

@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'GET':
        return render_template('home.html')

@app.route('/results')
def results():
    scraper = ClogauScraper()
    scraper.run()
    
    set_filename(scraper.filename)
    set_df(scraper.df)
    return render_template('results.html', products=scraper.results)

def set_filename(f):
    global filename 
    filename = f

def set_df(dframe):
    global df 
    df = dframe

@app.route('/download')
def download():
    global filename
    f = filename

    global df
    dframe = df

    # Temporarily create a csv file to be dowloaded
    file_path = f + '.csv'
    df.to_csv(f + '.csv')

    # Remove local csv file after download
    file_handle = open(file_path, 'r')
    @after_this_request
    def remove_file(response):
        try:
            os.remove(file_path)
            file_handle.close()
        except Exception as error:
            app.logger.error("Error removing or closing downloaded file handle", error)
        return response

    return send_from_directory('', f + '.csv', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, threaded=True)


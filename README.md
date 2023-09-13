
# Web scraper app
This project web scrapes the website and gets quotes. The script scrapes following data for each quote: 
* a quote 
* author of the quote
* tags of the quote


## Installing requirements 
Before running create the virtual environment and activate it. 
Then, make sure to install the required libraries with the following command:

Installing with pip
```bash
pip install -r requirements.txt
```

## Running the code
Before running the script make sure the following variables are available .env : 
* Proxy referred as Proxy
* Website URL referred as INPUT_URL
* Output JSONL line reffered as OUTPUT_FILE


To run the code 
```bash
python run.py
```

The following code was tested on MacOS and Chrome. 
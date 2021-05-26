# Job-offers-data-mining
## Description

Mining job offers data in the US

## How to use it

### Step 1: Installing packages using the following command:
pip install -r requirements.txt

### Step 2: Fixing careerjet api issue:
inside careerjet_api_client folder, you will find a file "__init_.py", wherever you find the following line "except Exception,e:" replace it with "except Exception as e:".
the carrerjet_api_client should be found inside your virtual environnement lib folder, for example "/venv/lib/careerjet_api_client"

### Step 3: running the program using command line:
inside the project folder, open command line and run the following command: "python main.py"

-- Note that i used argparse to parse command line arguments, for each argument there's a help text that explains its role and how it works, there's a default value for each
argument, for example keywords are set to "python automation" and location is set to "New York city", but it can be modified using the parsed args --

## example:
python python main.py -l "new jersey" -k "machine learning" -c "jobs_list_2.csv"
-l: is an optional argument for specifying location, if not set, default value will be taken.
-k: is an optional argument for specifying keywords, if not set, default value will be taken.
-c: is used for specifying where to store the result of the api call, in this example the data will be stored in jobs_list_2.csv in the same folder

## Other arguments:
-p: specifying number of pages to extract data from, if you don't wont to get all the jobs, you can give it an integer that represents number of pages to extract data from.
-ps: specifying page size, ie. number of jobs that a single page will contain, default is 99
-ai: API id that is given once you create an account in careerjet, but you can use the default one.
-u: website base url, leave the default value.



**Important note:** the base url is modified by add_url_params function, it takes location and keywords passed as argument, and adds it to the url.

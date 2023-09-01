# Installation
This file explains how to install and test the source code used in the article. There are two major parts that are need to correctly setup the environment: The Database, and the Library. The following segments guide the environment setup:

## Database

MongoDB is needed to use the dump available at `requirements` directory. To install it, you need to apply the following commands:

1. Unzip *similar-bug-reports-recommender-dataset-dump.zip*:
```
unzip similar-bug-reports-recommender-dataset-dump.zip -d similar-bug-reports-recommender-dataset-dump
```
2. Restore database dump using the output directory of the step before:
```
mongorestore -d <desired_database_name> similar-bug-reports-recommender-dataset-dump
```

## Library

To test the *bug-report-recommender* library, you can use a Python virtual environment to install and use the library available at requirements:

1. Install venv;
```
python -m venv venv
```
2. Access venv;
```
./venv/bin/activate
```
3. Install `requirements.txt` present on the `requirements` directory on the virtual environment;
```
pip install -r requirements.txt
```
4. Install *bug-report-recommender* lib present on `requirements` on the virtual environment;
```
pip install bugreportrecommender-0.0.6-py3-none-any.whl
```
5. Copy the _example.py_ file (which can be found on [Requirements](https://github.com/guimcarneiro/similar-bug-reports-recommender/tree/main/requirements)) to your venv directory and execute the _example.py_ file to check for recommendations.
```
python example.py
```

**Obs.:** Do not forget to change the variables *TEST_DATABASE* e *TEST_DATABASE_HOST* on _example.py_ to the values defined to the respective dataset created using the dump from **Database Section**.

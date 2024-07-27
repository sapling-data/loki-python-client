# Loki API Python Client
Python client for the Loki Cloud OS API. This library makes it easy to call the web service APIs of a running Loki application. Using the Loki API Python Client you will be able to call APIs for such actions as: retrieving data; saving data; executing query/list operations; and running jobs. 

# Background
The intent of this project is to allow contribuitions to the Loki API Python Client from any existing users of the Loki technology. We have open sourced this effort to remove restrictions and resolve ownership issues in a way that best benefits the Loki user community. For non-Loki users we welcome the use of this project as a reference on creating a Python API client and we welcome any feedback on that topic. That being said, we recognize that we, as the founders of this project, are not experts in the subject of Python APIs (or on open source project management for that matter) and hope to learn something from the effort.

# About Loki
Loki is a closed source application server technology developed by Sapling Data, LLC. The Loki techology is a data oriented cloud operating system that allows you to build and deploy applications in the cloud. Loki automatically generates web services APIs from the models that you define in the application. For more information about the Loki technology please see https://saplingdata.com.

# Quick Start
Make sure you are running a Python 3 environment.

First, install the library. In the terminal run this command to pull the latest library development code:

    $ python3 -m pip install git+https://github.com/sapling-data/loki-python-client.git

Optionally, you can set up credentials in a file of your choosing. In our examples and tests we install them in a .env file on our local Mac OS or linux system. To the file add your credentials and url for the Loki API:

    [default]
    username = myuser
    password = mypassword
    hosturl = https://host/appName

To try out the library you can use the following example code.  You will need to supply your own Loki query urn and credential file path.

    from loki import Loki
    loki = Loki(username='testuser', password='testpassword', hosturl="https://testurl")
    result = loki.data.query("urn:com:loki:examples:model:queries:listDocuments")
    if not result.is_success():
        raise Exception(result.get_error())
    print(result.get_response().status_code)
    print(result.get_response().content)
    print(result.get_response().json())
    for r in result.to_array():
        for v in r:
            print(v)

# Using In Jupyter Notebook

Make sure you are running a Python 3 environment.

Open the terminal in Jupyter Notebook and install the library. To pull the latest library development code use:

    $ source activate python3
    $ python3 -m pip install git+https://github.com/sapling-data/loki-python-client.git

You can provide your credentials directly in the notebook code, or optionally, you can set up credentials in a file of your choosing. In our example we install them in a file "~/loki-python-client/config.txt". To the file add your credentials and url for the Loki API:

    [default]
    username = myuser
    password = mypassword
    hosturl = https://host/appName

Restart the notebook kernel

Test with this code in your notebook. You will need to supply your own loki query urn and credential file path.

    import pandas as pd
    import numpy as np
    from loki import Loki
    loki = Loki("/home/user/loki/config.txt")
    # or to hardcode: loki = Loki(username='testuser', password='testpassword', hosturl="https://testurl")
    print( loki._username )
    print( loki._hosturl )
    result = loki.data.query("urn:com:loki:examples:model:queries:listDocuments",None)
    if not result.is_success():
        raise Exception(result.get_error())
    data = pd.DataFrame( result.to_array() )
    data.columns = ['plan_type', 'year', 'patient_count']
    data.head()

# Development

## Getting Started

Clone the git repo:

    $ git clone https://github.com/sapling-data/loki-python-client.git

### Set up a Python Environment

Conda is used in this project with its configuration in the environment.yml file

1. Install Anaconda from: https://www.anaconda.com/download/
2. In the project folder run:

    conda env create -f environment.yml -p .conda

3. Activate the conda environment using:

    conda activate .conda

### Testing

In this project unittest is used for testing. All tests are under the "tests" directory.
The "unit" subdirectory contains tests that can be run localy without a connection to a Loki server.
The "integration" subdirectory contains tests that require a connection to specific application on a loki server.
Because they connect to a loki server, the integration tests can more fully test loki-python-client functionality.

To run tests you can use:

    python -m unittest discover -p "*_test.py"
# email_tools

Tools for extracting and manipulating emails in the MSG and TXT format.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.


### Prerequisites

Install the Email_Tools package on your computer

```
pip install https://github.com/cevans-sdge/Email_Tools.git
```

## Daily Peak Emails

### Converting Daily Peak Emails Into Formatted .txt Files

Currently supports converting .msg and .txt files into standardized .txt format

```
from email_tools import DemandEmailManager

src_path = '** Directory where emails are stored **'
dest_path = '** Directory where you want to save formatted .txt files **'

# Instantiate Demand Email Manager
dem = DemandEmailManager(src_path, dest_path)

# Add additional load paths (if required)
dem.add_load_path('** Add an additional source directory, if required **')

# Load all compatible email message formats into Email Queue
dem.email_queue()
print(f'Queue contains {len(dem.queue)} emails')

# Load formatted email strings into "emails" attribute
dem.load_all_emails()
print(f'Loaded {len(dem.emails)} unique emails')

# Convert emails into TXT format and save them in specified save destinations
dem.reformat_emails()
```

### Generate Demand Peak DataFrame

```
from email_tools.classes import DemandEmailManager

src_path = '** Directory where emails are stored **'
dest_path = '** Directory where you want to save formatted .txt files **'

# Instantiate Demand Email Manager
dem = DemandEmailManager(src_path, dest_path)

# Pull formatted email files from Save Paths in DataFrame
dem.results_to_df()
```

## Authors

* **Colin Evans** - Senior Economic Advisor ~ San Diego Gas & Electric

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details

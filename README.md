# email_tools

Tools for extracting and manipulating emails in the MSG and TXT format.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

<!-- 
### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```
-->

End with an example of getting some data out of the system or using it for a little demo

## Daily Peak Emails

Explain how to run the automated tests for this system

### Converting Daily Peak Emails Into Formatted .txt Files

Currently supports converting .msg and .txt files into standardized .txt format

```
from email_manipulation import DemandEmailManager

test_load_path = r'\\NAS-CP1B\data\MKTG\BUS_ANAL\EVAL\Forecasting\8-Peak\Stata\EMS Peak Emails - Copy'
test_save_path = r'\\NAS-CP1B\data\MKTG\BUS_ANAL\EVAL\Forecasting\8-Peak\Stata\EMS Peak Emails'

# Instantiate Demand Email Manager
dem = DemandEmailManager(test_load_path, test_save_path)

# Add additional load paths
dem.add_load_path(r'\\NAS-CP1B\data\MKTG\BUS_ANAL\EVAL\Forecasting\8-Peak\Stata\Tims Daily Peak emails')
dem.add_load_path(r'\\NAS-CP1B\data\MKTG\BUS_ANAL\EVAL\Forecasting\8-Peak\Stata\Archive\EMS Peak Emails')

# Load all compatible email message formats into Email Queue
dem.email_queue()
print(f'Queue contains {len(dem.queue)} emails')

# Load formatted email strings into "emails" attribute
dem.load_all_emails()
print(f'Loaded {len(dem.emails)} unique emails')

# Convert emails into TXT format and save them in specified save destinations
dem.reformat_emails()
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 
-->
## Authors

* **Colin Evans** 
<!--   *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
--->

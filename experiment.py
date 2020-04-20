from email_tools.classes import DemandEmailManager

src_path = r'\\NAS-CP1B\data\MKTG\BUS_ANAL\EVAL\Forecasting\8-Peak\Stata\EMS Peak Emails - Source Files'
dest_path = r'\\NAS-CP1B\data\MKTG\BUS_ANAL\EVAL\Forecasting\8-Peak\Stata\EMS Peak Emails'

# Instantiate Demand Email Manager
dem = DemandEmailManager(src_path, dest_path)

# Pull formatted email files from Save Paths
dem.results_to_df()

print(dem.results.info())
print(dem.results.head())
print(dem.results.tail())
print(dem.results.describe())

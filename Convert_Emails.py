from email_tools.classes import DemandEmailManager

src_path = r'\\NAS-CP1B\data\MKTG\BUS_ANAL\EVAL\Forecasting\8-Peak\Stata\EMS Peak Emails - Source Files'
dest_path = r'\\NAS-CP1B\data\MKTG\BUS_ANAL\EVAL\Forecasting\8-Peak\Stata\EMS Peak Emails'

# Instantiate Demand Email Manager
dem = DemandEmailManager(src_path, dest_path)

# Load all compatible email message formats into Email Queue
dem.email_queue()
print(f'Queue contains {len(dem.queue)} emails')

# Load formatted email strings into "emails" attribute
dem.load_all_emails()
print(f'Loaded {len(dem.emails)} unique emails')

# Convert emails into TXT format and save them in specified save destinations
dem.reformat_emails()
print('Converted all emails into destination folder')

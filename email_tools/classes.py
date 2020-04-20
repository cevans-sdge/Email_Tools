import extract_msg
import email
import re
import os
import pandas as pd
from glob import glob


class EmailManager:
    def __init__(self, load_path, save_path):
        self.load_paths = [load_path]
        self.save_paths = [save_path]
        self.verify_paths()
        self.queue = []
        self.emails = []

    def verify_paths(self):
        for lp in self.load_paths:
            if os.path.exists(lp):
                pass
            else:
                print(f'Path does not exist: {lp}')
                break
        for sp in self.save_paths:
            if os.path.exists(sp):
                pass
            else:
                os.mkdir(sp)

    def add_load_path(self, new_path):
        if os.path.exists(new_path):
            self.load_paths.append(new_path)
        else:
            print(f'Path does not exist: {new_path}')

    def add_save_path(self, new_path):
        if os.path.exists(new_path):
            self.save_paths.append(new_path)
        else:
            os.mkdir(new_path)
            self.save_paths.append(new_path)

    def email_queue(self):
        files = []
        for load in self.load_paths:
            files += glob(os.path.join(load, '*.msg'))
            files += glob(os.path.join(load, '*.txt'))
        self.queue = files

    def load_email(self, filename):
        if filename.find('.msg') > 0:
            content = extract_msg.Message(filename)
            if content.to:
                to_string = content.to.strip()
            else:
                to_string = content.cc.strip()
            headers = {
                'From': content.sender.strip(),
                'Sent': pd.to_datetime(content.date, infer_datetime_format=True).strftime("%A, %B %d, %Y %I:%M:%S %p"),
                'To': to_string,
                'Subject': content.subject.strip().replace("/", '-').replace(":", "")
            }
            max_header_len = max([len(k) + 1 for k in headers.keys()])
            header_str = '\n'.join(f"{k}:{' ' * (max_header_len - len(k))}\t{v}" for k, v in headers.items())
            email_str = '\n\n'.join([
                header_str,
                '/n'.join([x.strip() for x in content.body.replace('\r', '').split('\n') if x.strip() not in ['']])
            ])
            return email_str
        elif filename.find('.txt') > 0:
            with open(filename, 'r') as fn:
                content = email.message_from_file(fn)
            if content.get('To'):
                to_string = content.get('To').strip()
            else:
                to_string = content.get('Cc').strip()
            headers = {
                'From': content.get('From').strip(),
                'Sent': pd.to_datetime(content.get('Sent'), infer_datetime_format=True).strftime("%A, %B %d, %Y %I:%M:%S %p"),
                'To': to_string,
                'Subject': content.get('Subject').strip().replace("/", '-').replace(":", "")
            }
            max_header_len = max([len(k) + 1 for k in headers.keys()])
            header_str = '\n'.join(f"{k}:{' ' * (max_header_len - len(k))}\t{v}" for k, v in headers.items())
            email_str = '\n\n'.join([
                header_str,
                '\n'.join([x.strip() for x in content.get_payload().replace('\r', '').split('\n') if x.strip() not in ['']])
            ])
            return email_str
        else:
            return None

    def parse_email_string(self, message):
        content = email.message_from_string(message)
        if content.get('To'):
            to_string = content.get('To').strip()
        else:
            to_string = content.get('Cc').strip()
        parse = {
            'From': content.get('From').strip(),
            'Sent': pd.to_datetime(content.get('Sent'), infer_datetime_format=True).strftime("%A, %B %d, %Y %I:%M:%S %p"),
            'To': to_string,
            'Subject': content.get('Subject').strip().replace("/", '-').replace(":", ""),
            'Body': content.get_payload(),
            'Filename': content.get('Subject').strip().replace("/", '-').replace(":", "") + '.txt'
        }
        return parse

    def parse_email_file(self, path, message):
        with open(os.path.join(path, message)) as fn:
            content = email.message_from_file(fn)
        if content.get('To'):
            to_string = content.get('To').strip()
        else:
            to_string = content.get('Cc').strip()
        parse = {
            'From': content.get('From').strip(),
            'Sent': pd.to_datetime(content.get('Sent'), infer_datetime_format=True).strftime("%A, %B %d, %Y %I:%M:%S %p"),
            'To': to_string,
            'Subject': content.get('Subject').strip().replace("/", '-').replace(":", ""),
            'Body': content.get_payload(),
            'Filename': content.get('Subject').strip().replace("/", '-').replace(":", "") + '.txt'
        }
        return parse

    def reset_queue(self):
        files = []
        for load in self.save_paths:
            files += glob(os.path.join(load, '*.msg'))
            files += glob(os.path.join(load, '*.txt'))
        self.queue = files


class DemandEmailManager(EmailManager):
    def __init__(self, load_path, save_path):
        super().__init__(load_path, save_path)
        self.load_paths = [load_path]
        self.save_paths = [save_path]
        self.verify_paths()
        self.queue = []
        self.emails = []
        self.results = None

    def load_all_emails(self, limit=None):
        if self.queue:
            if not limit:
                queue = self.queue.copy()
            else:
                if len(self.queue) < limit:
                    queue = self.queue.copy()
                else:
                    queue = self.queue[:limit].copy()
            for i, message in enumerate(queue):
                print(f'Load Email {i + 1} of {len(queue)}')
                if message.find('.msg') > 0:
                    content = extract_msg.Message(message)
                    if content.to:
                        to_string = content.to.strip()
                    else:
                        to_string = content.cc.strip()
                    headers = {
                        'From': content.sender.strip(),
                        'Sent': pd.to_datetime(content.date, infer_datetime_format=True).strftime("%A, %B %d, %Y %I:%M:%S %p"),
                        'To': to_string,
                        'Subject': content.subject.strip().replace("/", '-').replace(":", "")
                    }
                    # Check that email contains the standard phrase "The actual recorded", otherwise ignore
                    if content.body.find('The actual recorded') >= 0:
                        max_header_len = max([len(k) + 1 for k in headers.keys()])
                        header_str = '\n'.join(f"{k}:{' ' * (max_header_len - len(k))}\t{v}" for k, v in headers.items())
                        email_str = '\n\n'.join([
                            header_str,
                            '\n'.join([x.strip() for x in content.body.replace('\r', '').split('\n') if x.strip() not in ['']])
                        ])
                        self.emails.append(email_str)
                elif message.find('.txt') > 0:
                    with open(message, 'r') as fn:
                        content = email.message_from_file(fn)
                    if content.get('To'):
                        to_string = content.get('To').strip()
                    else:
                        to_string = content.get('Cc').strip()
                    headers = {
                        'From': content.get('From').strip(),
                        'Sent': pd.to_datetime(content.get('Sent'), infer_datetime_format=True).strftime("%A, %B %d, %Y %I:%M:%S %p"),
                        'To': to_string,
                        'Subject': content.get('Subject').strip().replace("/", '-').replace(":", "")
                    }
                    # Check that email contains the standard phrase "The actual recorded", otherwise ignore
                    if content.get_payload().find('The actual recorded') >= 0:
                        max_header_len = max([len(k) + 1 for k in headers.keys()])
                        header_str = '\n'.join(f"{k}:{' ' * (max_header_len - len(k))}\t{v}" for k, v in headers.items())
                        email_str = '\n\n'.join([
                            header_str,
                            '\n'.join([x.strip() for x in content.get_payload().replace('\r', '').split('\n') if x.strip() not in ['']])
                        ])
                        self.emails.append(email_str)
                # Only keep unique versions of the email strings
                self.emails = list(set(self.emails))

    def reformat_emails(self):
        if self.emails:
            for i, message in enumerate(self.emails):
                print(f'Converting Email {i + 1} of {len(self.emails)}')
                if message:
                    parse = self.parse_email_string(message)
                    for save_path in self.save_paths:
                        if os.path.exists(os.path.join(save_path, parse['Filename'])):
                            parse_compare = self.parse_email_file(save_path, parse['Filename'])
                            if parse['Body'] == parse_compare['Body']:
                                if parse['Sent'] > parse_compare['Sent']:
                                    with open(os.path.join(save_path, parse['Filename']), 'w') as save_fn:
                                        save_fn.write(message)
                            else:
                                valid = False
                                index = 1
                                while not valid:
                                    save_fn = os.path.join(save_path, parse['Filename'].replace('.', f' {index}.'))
                                    if not os.path.exists(os.path.join(save_path, save_fn)):
                                        with open(os.path.join(save_path, save_fn), 'w') as new_file:
                                            new_file.write(message)
                                        valid = True
                                    else:
                                        index += 1
                        else:
                            with open(os.path.join(save_path, parse['Filename']), 'w') as save_fn:
                                save_fn.write(message)

    def results_to_df(self):
        # Reset queue to pull all formatted files from Save Paths
        self.reset_queue()
        # Reset emails attribute
        self.load_all_emails()
        if self.emails:
            all_data = []
            for message in self.emails:
                parse = email.message_from_string(message)
                sent_date = parse.get('Sent')
                body = [x for x in parse.get_payload().split('\n') if 'The actual recorded' in x]
                # Ensure parsed strings are formatted correctly
                keys = ['The', 'actual', 'recorded', 'demand', 'for', 'was', 'MW', 'at']
                data = []
                for line in body:
                    for key in keys:
                        if (f' {key} ' not in line) & (key in line):
                            line = line.replace(key, f' {key} ')
                    line = [x.strip().replace('.', '') for x in line.split(' ') if (x != '') & (x not in keys)]
                    validated = line.copy()
                    # Check if calculation failed in email
                    fail = any(elem.find('Failed') >= 0 for elem in line)
                    if not fail:
                        # Perform validations
                        # Check to see if the Demand Type spans multiple elements in list
                        if not (re.findall(r'\d*/\d*/\d{4}', line[1])):
                            validated[0] = ' '.join(line[:2])
                            del line[1]
                            del validated[1]
                        # Date Formatting
                        if line[1] != re.findall(r'\d*/\d*/\d{4}', line[1])[0]:
                            validated[1] = re.findall(r'\d*/\d*/\d{4}', line[1])[0]
                        # Integer Formatting
                        validated[2] = int(validated[2])
                        # Date Formatting
                        if line[3] != re.findall(r'\d*/\d*/\d{4}', line[3])[0]:
                            validated[3] = re.findall(r'\d*/\d*/\d{4}', line[3])[0]
                        # Time Formatting
                        if not (re.findall(r'\d{2}:\d{2}:\d{2}', line[4])):
                            sub = line[4].replace(':', '')
                            if len(sub) < 6:
                                validated[4] = ':'.join(['0' + sub[0], sub[1:3], sub[-2:]])
                            else:
                                validated[4] = ':'.join([sub[:2], sub[2:4], sub[-2:]])
                        else:
                            validated[4] = re.findall(r'\d*:\d{2}:\d{2}', line[4])[0]
                        # Uppercase AM/PM
                        if line[-1].upper() in ['AM', 'PM']:
                            validated[-1] = line[-1].upper()
                        else:
                            validated[-1] = 'PM'
                        try:
                            data.append(
                                [validated[0], pd.to_datetime(' '.join(validated[-3:]), infer_datetime_format=True),
                                 validated[2], pd.to_datetime(sent_date, infer_datetime_format=True)]
                            )
                        except:
                            pass
                if data:
                    df = pd.DataFrame(data, columns=['DemandType', 'Time', 'MW', 'AsOfDate'])
                else:
                    df = pd.DataFrame(columns=['DemandType', 'Time', 'MW', 'AsOfDate'])
                all_data.append(df)
        df = pd.concat(all_data, ignore_index=True)
        df.drop_duplicates(inplace=True)
        df.sort_values(by=['Time', 'DemandType'], ignore_index=True, inplace=True)
        self.results = df

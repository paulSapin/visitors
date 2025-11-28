from enum import Enum
from dateutil.relativedelta import relativedelta
import yaml

def hello():
    return "Hello"


class Category(Enum):  # along with values to implement "1+1" rule and required approval
    Undergraduate = [0, 0]
    Master = [0, 0]
    PhD = [1, 0]
    Academic = [0, 1]
    Honorary = [0, 0]


class Candidate:

    def __init__(self, candidate: dict):

        # Assess profile
        if candidate['profile'] == 'Undergraduate':
            profile = Category.Undergraduate
        elif candidate['profile'] == 'Master' or candidate['profile'] == 'MSc':
            profile = Category.Master
        elif candidate['profile'] == 'PhD':
            profile = Category.PhD
        elif candidate['profile'] == 'Academic':
            profile = Category.Academic
        elif candidate['profile'] == 'Honorary':
            profile = Category.Honorary
        else:
            profile = None

        # Compute end date
        duration_months = candidate['duration_months']
        endDate = candidate['startingDate'] + relativedelta(months=candidate['duration_months'])

        # Register info
        self.info = \
            {'Name': candidate['name'],
             'Country': candidate['country'],
             'Email': candidate['email'],
             'Profile': profile,
             'Funding Source': candidate['fundingSource'],
             'Start Date': candidate['startingDate'],
             'End Date': endDate,
             'Duration': f'{candidate['duration_months']} months',
            }

        # Recap progress
        fees = f"{round(duration_months * 6000 / 12)} £ to be paid 1 month before end of stay (email Viji)"
        self.progress = {
            'Funding': candidate['progress']['Funding'] if self.info['Funding Source'] is not None else 'N/A',
            'Application': candidate['progress']['Application'],
            'Approval': candidate['progress']['Approval'],
            'ATAS': candidate['progress']['ATAS'] if self.needATAS() else 'N/A',
            'VISA': candidate['progress']['VISA'],
            'Fees': fees if self.benchFees() else None}

    """ METHODS """

    def benchFees(self):

        if self.info['Profile'] in [Category.Undergraduate, Category.Master]:
            if self.info['Duration'] <= 6:
                return False
            else:
                return True
        elif self.info['Profile'] in [ Category.PhD, Category.Honorary, Category.Academic]:
            return True
        else:
            return None

    def needATAS(self):

        atas_exempt_countries = [
            # includes UK nationals
            "United Kingdom", "UK",
            # EU + EEA + Switzerland
            "Austria",
            "Belgium",
            "Bulgaria",
            "Croatia",
            "Cyprus",
            "Czechia", "Czech Republic",
            "Denmark",
            "Estonia",
            "Finland",
            "France",
            "Germany",
            "Greece",
            "Hungary",
            "Ireland",
            "Italy",
            "Latvia",
            "Lithuania",
            "Luxembourg",
            "Malta",
            "Netherlands",
            "Poland",
            "Portugal",
            "Romania",
            "Slovakia",
            "Slovenia",
            "Spain",
            "Sweden",
            "Iceland",
            "Liechtenstein",
            "Norway",
            "Switzerland",
            # Other explicitly listed exempt nationalities
            "Australia",
            "Canada",
            "Japan",
            "New Zealand",
            "Singapore",
            "South Korea",
            "United States of America", "United States", "USA"
        ]
        return False if self.info['Country'] in atas_exempt_countries else True

    def getApprovalFrom(self):

        if self.info['Profile'] is Category.Undergraduate or self.info['Profile'] is Category.Master:
            return "Andreas Kogelbauer (Director of Course Operations)"
        elif self.info['Profile'] is Category.PhD:
            return "Cleo Kontoravdi (Director of Postgraduate Studies)"
        elif self.info['Profile'] is Category.Honorary:
            return "Omar Matar (Head of Department)"
        elif self.info['Profile'] is Category.Academic:
            return "Ronny Pini (Director of Resources)"
        else:
            return None

    def applyVia(self):

        if self.info['Profile'] in [Category.Undergraduate, Category.Master, Category.PhD]:
            return "MyImperial (online)"
        elif self.info['Profile'] in [Category.Honorary, Category.Academic]:
            return "Leah Grey (A&SM)"
        else:
            return None


class Calendar:

    def __init__(self):

        with open("../candidates/list.yaml", "r", encoding="utf-8") as f:
            list_of_candidates = yaml.safe_load(f)

        self.candidates = {}
        for candidate in list_of_candidates:
            self.candidates[candidate] = Candidate(list_of_candidates[candidate])

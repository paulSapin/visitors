from enum import Enum

def hello():
    return "Hello"


class Category(Enum):  # along with values to implement "1+1" rule and required approval
    Undergraduate = [0, 0]
    Master = [0, 0]
    PhD = [1, 0]
    Academic = [0, 1]
    Honorary = [0, 0]

class Candidate:

    def __init__(self,
                 name: str | None ,
                 email: str | None ,
                 country: str | None ,
                 profile: Category | None,
                 dates, *,
                 funding: str | None = None,
                 status: str | None = None,):

        self.name = name
        self.email = email
        self.country = country
        self.profile = profile
        self.funding = funding
        self.status = {'Funding': '',
                       'Approved': '',
                       'Application': '',
                       'ATAS': '',
                       'VISA': '',
                       'Fees': ''}

    """ METHODS """

    @property
    def benchFees(self):

        if self.profile in [Category.Undergraduate, Category.Master]:
            return 'Free'
        elif self.profile in [ Category.PhD, Category.Honorary, Category.Academic]:
            return "6,000 £/year"
        else:
            return None

    @property
    def application_needATAS(self):

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
        return False if self.country in atas_exempt_countries else True

    @property
    def application_getApprovalFrom(self):

        if self.profile is Category.Undergraduate or self.profile is Category.Master:
            return "Andreas Kogelbauer (Director of Course Operations)"
        elif self.profile is Category.PhD:
            return "Cleo Kontoravdi (Director of Postgraduate Studies)"
        elif self.profile is Category.Honorary:
            return "Omar Matar (Head of Department)"
        elif self.profile is Category.Academic:
            return "Ronny Pini (Director of Resources)"
        else:
            return None

    @property
    def application_applyVia(self):

        if self.profile in [Category.Undergraduate, Category.Master, Category.PhD]:
            return "MyImperial (online)"
        elif self.profile in [Category.Honorary, Category.Academic]:
            return "Leah Grey (A&SM)"
        else:
            return None

    """ PROPERTIES """

    @property
    def name(self) -> str | None:
        return self._name

    @name.setter
    def name(self, value: str | None):
        if value is None or  isinstance(value, str):
            self._name = value
        else:
            raise ValueError('The name must be a str or None.')

    @property
    def email(self) -> str | None:
        return self._email

    @email.setter
    def email(self, value: str | None):
        if value is None or  isinstance(value, str):
            self._email = value
        else:
            raise ValueError('The email must be a str or None.')

    @property
    def country(self) -> str | None:
        return self._country

    @country.setter
    def country(self, value: str | None):
        if value is None or  isinstance(value, str):
            self._country = value
        else:
            raise ValueError('The country must be a str or None.')

    @property
    def profile(self) -> Category | None:
        return self._profile

    @profile.setter
    def profile(self, value: Category | None):
        if value is None or  isinstance(value, Category):
            self._profile = value
        else:
            raise ValueError('The profile must be a Category or None.')

    @property
    def funding(self) -> bool | None:
        return self._funding

    @funding.setter
    def funding(self, value: str | None):
        if value is None or  isinstance(value, str):
            self._funding = value
        else:
            raise ValueError('The fundingRequired must be a str or None.')
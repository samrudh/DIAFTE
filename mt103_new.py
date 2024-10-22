from __future__ import unicode_literals

import re
from datetime import date
from schwifty import BIC


class MT103(object):
    """
    Parses an MT103 standard banking format string into a string-like Python
    object so you can do things like `mt103.basic_header` or `print(mt103)`.
    Usage:
    mt103 = MT103("some-mt-103-string")
    print("basic header: {}, bank op code: {}, complete message: {}".format(
        mt103.basic_header,
        mt103.text.bank_operation_code
        mt103
    ))
    With considerable help from:
    http://www.sepaforcorporates.com/swift-for-corporates/read-swift-message-structure/
    """

    MESSAGE_REGEX = re.compile(
        "^"
        "({1:(?P<basic_header>[^}]+)})?"
        "({2:(?P<application_header>[IO][^}]+)})?"
        "({3:(?P<user_header>({113:[A-Z]{4}})?({108:[A-Z0-9]{0,16}}))})?"
        "({4:\s*(?P<text>.+?)\s*-})?"
        "({5:(?P<trailer>[^}]+)})?"
        "$",
        re.DOTALL
    )

    def __init__(self, message):

        if message is None:
            message = ""

        self.raw = message.strip()
        self.basic_header = None
        self.application_header = None
        self.user_header = None
        self.text = None
        self.trailer = None

        self._boolean = False

        self._populate_by_parsing()

    def __str__(self):
        return self.raw

    def __repr__(self):
        return str(self)

    def __bool__(self):
        return self._boolean
    __nonzero__ = __bool__  # Python 2

    def _populate_by_parsing(self):
        self.return_dict = {}

        if not self.raw:
            return

        m = self.MESSAGE_REGEX.match(self.raw)

        self._boolean = bool(m)

        if not m:
            print ('*'*20)
            print ('Message Not Matching : ',self.raw)
            return None

        self.basic_header = m.group("basic_header")
        self.application_header = m.group("application_header")
        self.user_header = m.group("user_header")
        self.trailer = m.group("trailer")

        self.text = Text(m.group("text") or "")
        
        
        try:
            basic_header = self.basic_header[3:14]
            self.basic_bic = BIC(basic_header)
        except:
            pass
        try:
            self.basic_bank_code = self.basic_bic.bank_code
        except:
            self.basic_bank_code=None
        try:
            self.basic_branch_code = self.basic_bic.branch_code
        except:
            self.basic_branch_code=None
        try:
            self.basic_country_code = self.basic_bic.country_code
        except:
            self.basic_country_code=None
        try:
            self.basic_location_code = self.basic_bic.location_code
        except:
            self.basic_location_code = None
        try:
            self.basic_country_bank_code = self.basic_bic.country_bank_code
        except:
            self.basic_country_bank_code = None
        try:
            application_header = self.application_header[4:15]
            self.application_bic = BIC(application_header)
        except:
            pass
        try:
            self.application_bank_code = self.application_bic.bank_code
        except:
            self.application_bank_code=None
        try:
            self.application_branch_code = self.application_bic.branch_code
        except:
            self.application_branch_code=None
        try:
            self.application_country_code = self.application_bic.country_code
        except:
            self.application_country_code=None
        try:
            self.application_location_code = self.application_bic.location_code
        except:
            self.application_location_code = None
        try:
            self.application_country_bank_code = self.application_bic.country_bank_code
        except:
            self.application_country_bank_code = None
        
        try:
            self.return_dict['basic_bank_code']=self.basic_bank_code
        except:
            pass
        try:
            self.return_dict['basic_branch_code']=self.basic_branch_code
        except:
            pass
        try:
            self.return_dict['basic_country_code']=self.basic_country_code
        
        except:
            pass
        try:
            self.return_dict['basic_location_code']=self.basic_location_code
        
        except:
            pass
        try:
            self.return_dict['basic_country_bank_code']=self.basic_country_bank_code
        
        except:
            pass
        try:
            self.return_dict['application_bank_code']=self.application_bank_code
        except:
            pass
        try:
            self.return_dict['application_branch_code']=self.application_branch_code        
        except:
            pass
        try:
            self.return_dict['application_country_code']=self.application_country_code        
        except:
            pass
        try:
            self.return_dict['application_location_code']=self.application_location_code        
        except:
            pass
        try:
            self.return_dict['application_country_bank_code']=self.application_country_bank_code        
        except:
            pass
        try:
            self.return_dict['transaction_reference']=self.text.transaction_reference        
        except:
            pass
        try:
            self.return_dict['bank_operation_code']=self.text.bank_operation_code        
        except:
            pass
        try:
            self.return_dict['interbank_settled_currency']=self.text.interbank_settled_currency        
        except:
            pass
        try:
            self.return_dict['interbank_settled_amount']=self.text.interbank_settled_amount        
        except:
            pass
        try:
            self.return_dict['original_ordered_currency']=self.text.original_ordered_currency        
        except:
            pass
        try:
            self.return_dict['original_ordered_amount']=self.text.original_ordered_amount        
        except:
            pass
        try:
            self.return_dict['ordering_customer']=self.text.ordering_customer        
        except:
            pass
        try:
            self.return_dict['ordering_institution']=self.text.ordering_institution        
        except:
            pass
        try:
            self.return_dict['sender_correspondent']=self.text.sender_correspondent        
        except:
            pass
        try:
            self.return_dict['receiver_correspondent']=self.text.receiver_correspondent        
        except:
            pass
        try:
            self.return_dict['intermediary']=self.text.intermediary        
        except:
            pass
        try:
            self.return_dict['account_with_institution']=self.text.account_with_institution        
        except:
            pass
        try:
            self.return_dict['beneficiary']=self.text.beneficiary        
        except:
            pass
        try:
            self.return_dict['remittance_information']=self.text.remittance_information        
        except:
            pass
        try:
            self.return_dict['details_of_charges']=self.text.details_of_charges        
        except:
            pass
        try:
            self.return_dict['sender_to_receiver_information']=self.text.sender_to_receiver_information        
        except:
            pass
        try:
            self.return_dict['regulatory_reporting']=self.text.regulatory_reporting        
        except:
            pass
        try:
            self.return_dict['date']=self.text.date
        except:
            pass
        try:
            self.return_dict['application_branch_code']=self.application_branch_code        
        except:
            pass
        try:
            self.return_dict['application_country_code']=self.application_country_code        
        except:
            pass
        try:
            self.return_dict['application_location_code']=self.application_location_code        
        except:
            pass
        try:
            self.return_dict['application_country_bank_code']=self.application_country_bank_code        
        except:
            pass
        try:
            self.return_dict['transaction_reference']=self.text.transaction_reference        
        except:
            pass
        try:
            self.return_dict['bank_operation_code']=self.text.bank_operation_code        
        except:
            pass
        try:
            self.return_dict['interbank_settled_currency']=self.text.interbank_settled_currency        
        except:
            pass
        try:
            self.return_dict['interbank_settled_amount']=self.text.interbank_settled_amount        
        except:
            pass
        try:
            self.return_dict['original_ordered_currency']=self.text.original_ordered_currency        
        except:
            pass
        try:
            self.return_dict['original_ordered_amount']=self.text.original_ordered_amount        
        except:
            pass
        try:
            self.return_dict['ordering_customer']=self.text.ordering_customer        
        except:
            pass
        try:
            self.return_dict['ordering_institution']=self.text.ordering_institution        
        except:
            pass
        try:
            self.return_dict['sender_correspondent']=self.text.sender_correspondent        
        except:
            pass
        try:
            self.return_dict['receiver_correspondent']=self.text.receiver_correspondent        
        except:
            pass
        try:
            self.return_dict['intermediary']=self.text.intermediary        
        except:
            pass
        try:
            self.return_dict['account_with_institution']=self.text.account_with_institution        
        except:
            pass
        try:
            self.return_dict['beneficiary']=self.text.beneficiary        
        except:
            pass
        try:
            self.return_dict['remittance_information']=self.text.remittance_information        
        except:
            pass
        try:
            self.return_dict['details_of_charges']=self.text.details_of_charges        
        except:
            pass
        try:
            self.return_dict['sender_to_receiver_information']=self.text.sender_to_receiver_information        
        except:
            pass
        try:
            self.return_dict['regulatory_reporting']=self.text.regulatory_reporting        
        except:
            pass
        try:
            self.return_dict['date']=self.text.date
        except:
            pass
        
            
    def get_all_fields(self):
        
        return self.return_dict


class Text(object):
    """
    With considerable help from:
    https://en.wikipedia.org/wiki/MT103 and
    https://gist.github.com/dmcruz/9940a6b217ff701b8f3e
    """

    REGEX = re.compile(
        "^"
        "(:20:(?P<transaction_reference>[^\s:]+)\s*)?"
        "(:23B:(?P<bank_operation_code>[^\s:]+)\s*)?"
        "(:32A:"
            "(?P<value_date_year>\d\d)"  # NOQA
            "(?P<value_date_month>\d\d)"
            "(?P<value_date_day>\d\d)"
            "(?P<interbank_settled_currency>[A-Z]{3})"
            "(?P<interbank_settled_amount>[\d,]+)"
        "\s*)?"
        "(:33B:"
            "(?P<original_ordered_currency>[A-Z]{3})"
            "(?P<original_ordered_amount>[\d,]+)"
        "\s*)?"
        "(:50[AFK]:(?P<ordering_customer>.*?)\s*(?=(:\d\d)?))?"
        "(:52[AD]:(?P<ordering_institution>.*?)\s*(?=(:\d\d)?))?"
        "(:53[ABD]:(?P<sender_correspondent>[^\s:]*)\s*)?"
        "(:54[ABD]:(?P<receiver_correspondent>.*?)\s*(?=(:\d\d)?))?"
        "(:56[ACD]:(?P<intermediary>.*?)\s*(?=(:\d\d)?))?"
        "(:57[ABCD]:(?P<account_with_institution>.*?)\s*(?=(:\d\d)?))?"
        "(:59A?:(?P<beneficiary>.*?)\s*(?=(:\d\d)?))?"
        "(:70:(?P<remittance_information>.*?)\s*(?=(:\d\d)?))?"
        "(:71A:(?P<details_of_charges>.*?)\s*(?=(:\d\d)?))?"
        "(:72:(?P<sender_to_receiver_information>.*?)\s*(?=(:\d\d)?))?"
        "(:77A:(?P<regulatory_reporting>.*?)\s*(?=(:\d\d)?))?"
        "$",
        re.DOTALL
    )

    def __init__(self, raw):

        self.raw = raw

        self.transaction_reference = None
        self.bank_operation_code = None
        self.interbank_settled_currency = None
        self.interbank_settled_amount = None
        self.original_ordered_currency = None
        self.original_ordered_amount = None
        self.ordering_customer = None
        self.ordering_institution = None
        self.sender_correspondent = None
        self.receiver_correspondent = None
        self.intermediary = None
        self.account_with_institution = None
        self.beneficiary = None
        self.remittance_information = None
        self.details_of_charges = None
        self.sender_to_receiver_information = None
        self.regulatory_reporting = None
        self.date = None

        self._boolean = False

        self._populate_by_parsing()

    def __str__(self):
        return self.raw

    def __repr__(self):
        return str(self)

    def __bool__(self):
        return self._boolean
    __nonzero__ = __bool__  # Python 2

    def _populate_by_parsing(self):

        if not self.raw:
            return

        m = self.REGEX.match(self.raw)

        self._boolean = bool(m)

        if not m:
            return

        for k, v in m.groupdict().items():
            if v is None:
                continue
            if k.startswith("value_date_"):
                continue
            setattr(self, k, v)

        try:
            self.date = date(
                2000 + int(m.group("value_date_year")),
                int(m.group("value_date_month")),
                int(m.group("value_date_day"))
            )
        except (ValueError, TypeError):
            pass  # Defaults to None

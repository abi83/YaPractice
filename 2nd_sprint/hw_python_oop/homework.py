import datetime as dt
import hw_settings as hws


class Calculator:
    def __init__(self, day_limit: int):
        self.limit = day_limit
        self.records = []

    def add_record(self, new_record):
        """
        Adding Record with making some checks.
        Duplicated Records is not allowed
        Managing actions of over limit records is available with
        :param new_record: a Record object
        :return: None
        """

        if (not hws.allow_over_limit
                and new_record.amount > self._get_today_remained()):
            if hws.over_limit_action == 'err':
                raise RuntimeError(f'Allow over {self.limit} day limit option'
                                   f'is {hws.allow_over_limit}.'
                                   f'Over_limit_action is set to'
                                   f'{hws.over_limit_action}. So your record '
                                   f'was not added')

            if hws.over_limit_action == 'wrn':
                print('Take attention! Your day limit is over!'
                      'New record will be added')
            else:
                print('Your over_limit_action option is incorrect.'
                      'Make sure it is in [\'err\', \'wrn\']\n'
                      'New record will be added')

        if not self._duplicated(new_record):
            self.records.append(new_record)
        else:
            raise RuntimeError('Duplicating Record is not available')

    def get_today_stats(self):
        today = dt.date.today()
        return sum([
            record.amount
            for record in self.records
            if record.date == today
        ])

    def get_week_stats(self):
        today = dt.date.today()
        start_week_date = today - dt.timedelta(7)
        return sum([
            record.amount
            for record in self.records
            if start_week_date < record.date <= today
        ])

    def _get_today_remained(self):
        return self.limit - self.get_today_stats()

    def _duplicated(self, new_record):
        for record in self.records:
            if (new_record.date == record.date and
                    new_record.amount == record.amount and
                    new_record.comment == record.comment):
                return True
        return False


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        today_left = self._get_today_remained()

        if self._get_today_remained() > 0:
            return f'Сегодня можно съесть что-нибудь ещё,' \
                   f' но с общей калорийностью не более {today_left} кКал'

        return f'Хватит есть!'


class CashCalculator(Calculator):
    USD_RATE = 63.21
    EURO_RATE = 73.12
    RUB_RATE = 1.0

    def show_currency(self):
        print(f'Курс доллара: {self.USD_RATE}. Курс евро: {self.EURO_RATE}')

    def get_today_cash_remained(self, currency):

        currency_dict = {
            'usd': [self.USD_RATE, 'USD'],
            'eur': [self.EURO_RATE, 'Euro'],
            'rub': [self.RUB_RATE, 'руб']
        }

        if currency not in currency_dict.keys():
            raise ValueError(f'Currency {currency} is not accepted')

        try:
            today_left = (round(self._get_today_remained() /
                                currency_dict[currency][0], 2))
            # remains value in 'currency'
        except ZeroDivisionError:
            print(f'{currency} RATE == 0 is not possible')
            return

        if today_left > 0:
            return f'На сегодня осталось {today_left}' \
                   f' {currency_dict[currency][1]}'
        if today_left == 0:
            return 'Денег нет, держись'
        return f'Денег нет, держись: твой долг - {abs(today_left)}' \
               f' {currency_dict[currency][1]}'


class Record:
    """
    A class for simple records in our Calculators
    self.amount: value of something. INT is better
    self.comment: string comment
    self.date: String with date in '%d.%m.%Y' format.
    Checks if format is right, date is in allowed period etc.
    See @date.setter doc for more information
    """

    def __init__(self, amount: int, comment: str, date: str = None):
        self.amount = amount
        self.comment = comment
        self.date = date

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, input_date: str):
        """
        Making some checks before setting a date:
        1. Setting date as today, when no date_input is given
        2. raises TypeError, when not 'str' type of date_input is given
        3. processing ValueErrors, when date_input not in required format
        given. for example: '32.12.1999'
        Sets today date in this case.
        4. special feature: checking possible mistakes, if mistake
        in date_input is for sure. Processing input_date like '08.05.1883'.
        You can manage this feature inside _incredible_input_data_check method.

        :param input_date: some string with a date in '%d.%m.%Y' format.
        Like '17.09.2020'
        :return: None
        """

        today = dt.date.today()

        if not input_date:
            # Setting date as today, when no date is given
            self._date = today
            return

        try:
            datetime_processing = dt.datetime.strptime(input_date, '%d.%m.%Y')
            date_processing = dt.datetime.date(datetime_processing)

        # checking the right format of date string
        except ValueError:
            self._date = today
            return
            # setting date as today by default if date value is incorrect

        # checking 'str' type of date_input
        except TypeError:
            raise TypeError('Make sure giving string type of data')

        self._incredible_input_data_check(date_processing)
        self._date = date_processing

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, input_comment):
        """
        Making a check for max_length
        :param input_comment: A string with some description of a Record.
        :return: None
        """

        input_comment_possibility = len(input_comment) < hws.max_length

        if (not input_comment_possibility
                and hws.too_long_comment_action == 'err'):
            raise ValueError(f'Comment is too long.'
                             f' Make it in {hws.max_length} symbols limit')

        out_comment = input_comment  # start from 'ign'

        if (not input_comment_possibility
                and hws.too_long_comment_action != 'ign'):
            out_comment = input_comment[:hws.max_length]

        if hws.too_long_comment_action == 'wrn':
            print(f'Value ALERT! Your comment is too long.'
                  f' It was cut to {hws.max_length} symbols limit')

        if hws.too_long_comment_action not in ['wrn', 'cut', 'ign', 'err']:
            print(f'Argument ALERT!:'
                  f'too_long_comment_action {hws.too_long_comment_action}'
                  f'not found. Action was made by default.'
                  f'See more information in @comment.setter doc')

        self._comment = out_comment

    def show_record(self):
        return f'Дата: {self._date}' \
               f'Текст:{self.comment}' \
               f'Значение: {self.amount}'

    @staticmethod
    def _incredible_input_data_check(date_processing):
        """
        Checks incredible input_data like 05.09.1883 and making one of action
        set in incredible_date_action option (see hw_settings.py):
            'sln' option sets incredible_date as today silently (default)
            'wrn' option sets incredible_date as today with a warning message
            'err' option raises ValueError, if input_date not in allowed period
        Period accepted for input data set by input_date_possibility option
        :return: None
        """
        today = dt.date.today()

        input_date_allowed = (today - dt.timedelta(hws.input_date_possibility)
                              < date_processing <
                              today + dt.timedelta(hws.input_date_possibility)
                              )

        if not input_date_allowed and hws.incredible_date_action == 'err':
            raise ValueError(f'{date_processing} is not in allowed period')

        if not input_date_allowed and hws.incredible_date_action == 'msg':
            print(f'Value ALERT!:'
                  f'Given date {date_processing} seems to be wrong')

        if (not input_date_allowed
                and hws.incredible_date_action not in ['sln', 'msg', 'err']):
            print(f'Argument ALERT!:'
                  f'incredible_date_action {hws.incredible_date_action} not'
                  f'found. Action was made by default see more information'
                  f'in @date.setter documentation.')


if __name__ == '__main__':
    pass

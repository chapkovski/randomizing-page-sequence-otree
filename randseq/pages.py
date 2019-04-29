from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import json


class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


initial_page_sequence = [
    MyPage,
    Results
]


page_sequence = [

]


class MyPage(Page):
    def inner_dispatch(self):
        page_seq = int(self.__class__.__name__.split('_')[1])
        page_to_show = json.loads(self.player.page_sequence)[page_seq]
        self._is_frozen = False
        self.__class__ = globals()[page_to_show]
        return super(globals()[page_to_show], self).inner_dispatch()


for i, _ in enumerate(initial_page_sequence):
    NewClassName = "Page_{}".format(i)
    A = type(NewClassName, (MyPage,), {})
    locals()[NewClassName] = A
    page_sequence.append(locals()[NewClassName])


from src import __version__
from src.crawl_leetcode import LeetCodeUser

user1 = LeetCodeUser("user1", "password")

def test_version():
    assert __version__ == '0.1.0'

def test_get_ac_ids():
    expected = user1.get_ac_frontend_ids()
    achieved = []
    assert expected == achieved

def test_get_non_ac_ids():
    non_ac_ids = user1.get_non_ac_frontend_ids()
    q_lambda = lambda x: x['stat']['frontend_question_id']
    ordered_questions = sorted(user1.get_question_list(), key=q_lambda)
    for expected, question in zip(non_ac_ids, ordered_questions):
        achieved = question['stat']['frontend_question_id']
        assert expected == achieved


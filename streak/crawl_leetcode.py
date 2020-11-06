import requests
import json

USER_AGENT = (
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2)'
        'AppleWebKit/537.36 (KHTML, like Gecko)'
        'Chrome/79.0.3945.130 Safari/537.36')
LEETCODE_API_URL = 'https://leetcode.com/api/problems/all/'

class LeetCodeUser():
    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password

    def get_question_list(self):
        session = requests.session()
        headers = {'User-Agent': USER_AGENT, 'Connection': 'keep-alive'}
        response = requests.get(LEETCODE_API_URL, headers = headers, timeout = 10)
        parsed_res = json.loads(response.content.decode('utf-8'))
        return parsed_res['stat_status_pairs']

    def get_ac_frontend_ids(self):
        question_list = self.get_question_list()
        ac_frontend_ids = []
        q_lambda = lambda x: x['stat']['frontend_question_id']
        for question in sorted(question_list, key=q_lambda):
            q_id = question['stat']['frontend_question_id']
            if question['status'] == 'ac':
                ac_frontend_ids.append(q_id)
        return ac_frontend_ids

    def get_non_ac_frontend_ids(self):
        question_list = self.get_question_list()
        non_ac_frontend_ids = []
        q_lambda = lambda x: x['stat']['frontend_question_id']
        for question in sorted(question_list, key=q_lambda):
            q_id = question['stat']['frontend_question_id']
            if question['status'] != 'ac':
                non_ac_frontend_ids.append(q_id)
        return non_ac_frontend_ids


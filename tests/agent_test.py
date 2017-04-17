#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        Unit Tests for Agent Methods
            - remove_control_characters
            - test_echo
            - create_datafeed
            - read_datafeed
            - send_message
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@joyce.nyc'
__copyright__ = 'Copyright 2017, Symphony Communication Services LLC'

import httpretty
import unittest
import symphony


class Agent_tests(unittest.TestCase):

    @httpretty.activate
    def test_test_echo(self):
        ''' test get_user_id_by_email '''
        # register response
        httpretty.register_uri(httpretty.GET, "http://fake.pod/pod/v1/user",
                               body='{"id": 123456, "emailAddress": "test@fake.pod" }',
                               status=200,
                               content_type='text/json')
        # dummy authenticate
        symphony_pod_uri = 'http://fake.pod/'
        session_token = 'sessions'
        keymngr_token = 'keys'
        pod = symphony.Pod(symphony_pod_uri, session_token, keymngr_token)
        # run test query
        response = pod.get_userid_by_email('test@fake.pod')
        # verify return
        assert response['id'] == 123456
        assert response['emailAddress'] == "test@fake.pod"

    @httpretty.activate
    def test_create_datafeed(self):
        ''' test user_feature_update '''
        # register response
        httpretty.register_uri(httpretty.POST, "http://fake.pod/pod/v1/admin/123456/features/update",
                               body='{ "format": "TEXT", "message": "OK" }',
                               status=200,
                               content_type='text/json')
        # dummy authenticate
        symphony_pod_uri = 'http://fake.pod/'
        session_token = 'sessions'
        keymngr_token = 'keys'
        pod = symphony.Pod(symphony_pod_uri, session_token, keymngr_token)
        # run test query
        test_feature_query = '[{"entitlment": "isExternalRoomEnabled", "enabled": true },'\
                             '{"entitlment": "isExternalIMEnabled", "enabled": true }]'
        status_code, response = pod.user_feature_update('123456', test_feature_query)
        # verify return
        assert status_code == 200


if __name__ == '__main__':
    unittest.main()

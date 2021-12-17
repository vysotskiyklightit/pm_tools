from common.constants import BoardPreference

list_owner_public = {
    'username': 'test_user',
    'pm_username': 'pm_board',
    'contrib_usernames': ['pm_board', 'some_person'],
    'auth_username': 'pm_board',
    'board_preference': BoardPreference.public.value,
    'len_response': 1
}
list_owner_private = {
    'username': 'test_user',
    'pm_username': 'pm_board',
    'contrib_usernames': ['pm_board', 'some_person'],
    'auth_username': 'pm_board',
    'board_preference': BoardPreference.private.value,
    'len_response': 1
}
list_contrib_private = {
    'username': 'test_user',
    'pm_username': 'pm_board',
    'contrib_usernames': ['pm_board', 'some_person'],
    'auth_username': 'some_person',
    'board_preference': BoardPreference.private.value,
    'len_response': 1
}
list_user_private = {
    'username': 'test_user',
    'pm_username': 'pm_board',
    'contrib_usernames': ['pm_board', 'some_person'],
    'auth_username': 'test_user',
    'board_preference': BoardPreference.private.value,
    'len_response': 0
}
get_owner_public = {
    'username': 'test_user',
    'pm_username': 'pm_board',
    'contrib_usernames': ['pm_board', 'some_person'],
    'auth_username': 'pm_board',
    'board_preference': BoardPreference.public.value,
    'status_code': 200
}
get_owner_private = {
    'username': 'test_user',
    'pm_username': 'pm_board',
    'contrib_usernames': ['pm_board', 'some_person'],
    'auth_username': 'pm_board',
    'board_preference': BoardPreference.private.value,
    'status_code': 200
}
get_contrib_private = {
    'username': 'test_user',
    'pm_username': 'pm_board',
    'contrib_usernames': ['pm_board', 'some_person'],
    'auth_username': 'some_person',
    'board_preference': BoardPreference.private.value,
    'status_code': 200
}
get_user_private = {
    'username': 'test_user',
    'pm_username': 'pm_board',
    'contrib_usernames': ['pm_board', 'some_person'],
    'auth_username': 'test_user',
    'board_preference': BoardPreference.private.value,
    'status_code': 403
}
put_owner_public = {
    'username': 'test_user',
    'pm_username': 'pm_board',
    'contrib_usernames': ['pm_board', 'some_person'],
    'auth_username': 'pm_board',
    'board_preference': BoardPreference.public.value,
    'status_code': 200
}
put_owner_private = {
    'username': 'test_user',
    'pm_username': 'pm_board',
    'contrib_usernames': ['pm_board', 'some_person'],
    'auth_username': 'pm_board',
    'board_preference': BoardPreference.private.value,
    'status_code': 200
}
put_user_private = {
    'username': 'test_user',
    'pm_username': 'pm_board',
    'contrib_usernames': ['pm_board', 'some_person'],
    'auth_username': 'test_user',
    'board_preference': BoardPreference.private.value,
    'status_code': 403
}
delete_owner_public = {
    'username': 'test_user',
    'pm_username': 'pm_board',
    'contrib_usernames': ['pm_board', 'some_person'],
    'auth_username': 'pm_board',
    'board_preference': BoardPreference.public.value,
    'status_code': 204
}
delete_owner_private = {
    'username': 'test_user',
    'pm_username': 'pm_board',
    'contrib_usernames': ['pm_board', 'some_person'],
    'auth_username': 'pm_board',
    'board_preference': BoardPreference.private.value,
    'status_code': 204
}
delete_user_private = {
    'username': 'test_user',
    'pm_username': 'pm_board',
    'contrib_usernames': ['pm_board', 'some_person'],
    'auth_username': 'test_user',
    'board_preference': BoardPreference.private.value,
    'status_code': 403
}

post_pm = {
    'username': 'test_user5',
    'pm_username': 'pm_board1',
    'contrib_usernames': ['pm_board1', 'some_person'],
    'auth_username': 'pm_board1',
    'board_preference': BoardPreference.private.value,
    'status_code': 201
}
post_user = {
    'username': 'test_user5',
    'pm_username': 'pm_board1',
    'contrib_usernames': ['pm_board1', 'some_person'],
    'auth_username': 'test_user5',
    'board_preference': BoardPreference.private.value,
    'status_code': 403
}

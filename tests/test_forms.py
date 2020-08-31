# -*- coding: utf-8 -*-

from my_url_shortner.user.forms import LoginForm, RegisterForm


# class TestRegisterForm():
#     """Testing valid and invalid cases for the register user form"""

#     def test_error_shown_for_already_registered_username(self, testapp):
#         """Should receive an error when registering an already used username"""

#         register_form = RegisterForm(
#             username = "prajjwolm",
#             email = "vjn98verv089h@test.com",
#             password = "test1234%",
#             confirm = "test1234%"
#         )

#         assert register_form.validate() is False
#         assert "prajjwolm has already been registered" in register_form.username.errors

#     def test_error_shown_for_already_registered_email(self, testapp):
#         """Should receive an error when registering an already used email"""

#         register_form = RegisterForm(
#             username = "fn248f23f",
#             email = "prajjwolm@gmail.com",
#             password = "test1234%",
#             confirm = "test1234%"
#         )

#         assert register_form.validate() is False
#         assert "prajjwolm@gmail.com has already been registered" in register_form.email.errors

#     def test_error_shown_for_invalid_password(self, testapp):
#         """Should receive an error when registering with an invalid password"""

#         register_form = RegisterForm(
#             username = "fn248f23f",
#             email = "vjn98verv089h@test.com",
#             password = "testtest",
#             confirm = "testtest"
#         )

#         assert register_form.validate() is False
#         assert "Passwords need to be at least 8 chars long, and have a letter, number and one of: @$!%*#?&" in register_form.password.errors

#     def test_valid_user_can_register(self, testapp):
#         """User with all valid inputs can register"""

#         register_form = RegisterForm(
#             username = "testUser",
#             email = "unitTest@test.com",
#             password = "test1234%",
#             confirm = "test1234%"
#         )

#         assert register_form.validate() is True


class TestLoginForm():
    """Testing valid and invalid cases for the login user form"""

    def test_valid_user_can_login(self, testapp, user):
        """"""

        print(f"user.username - {user.username}")
        login_form = LoginForm(
            username = user.username,
            password = "test1234%"
        )

        assert login_form.validate() is True
        assert login_form.user == user

    # def test_invalid_user_cannot_login(self, testapp):
    #     """"""

    #     assert False
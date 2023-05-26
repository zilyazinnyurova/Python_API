from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions



class TestUserDelete(BaseCase):

    def test_cannot_delete_user_2(self):

        #LOGIN_ID_2
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "X-csrf-token")
        user_id_2 = self.get_json_value(response1, "user_id")


        # DELETE
        response2 = MyRequests.delete(
            f"/user/{user_id_2}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response2, 400)
        assert response2.content.decode("utf-8") == f"Please, do not delete test users with ID 1, 2, 3, 4 or 5.", \
            f"Unexpected response content {response2.content}"
    def test_delete_user_random(self):

        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # LOGIN_AFTER_REGISTER

        login_data = {
            'email': email,
            'password': password
        }

        response2 = MyRequests.post(f"/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "X-csrf-token")
        user_id = self.get_json_value(response2, "user_id")

        # DELETE_AFTER_LOGIN

        response3 = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response3, 200)


        # GET_DATA_AFTER_DELETE
        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response4, 404)
        assert response4.content.decode("utf-8") == f"User not found", f"Unexpected response content {response4.content}"

    def test_delete_another_user_with_another_s_session(self):

        # REGISTER_1
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        user_id_1 = self.get_json_value(response1, "id")

        # REGISTER_2
        register_data = self.prepare_registration_data()
        response2 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, "id")

        email = register_data['email']
        password = register_data['password']


        # LOGIN_AFTER_REGISTER
        data = {
            'email': email,
            'password': password
        }

        response3 = MyRequests.post(f"/user/login", data=data)
        auth_sid = self.get_cookie(response3, "auth_sid")
        token = self.get_header(response3, "X-csrf-token")
        user_id_2 = self.get_json_value(response3, "user_id")

        # DELETE

        response4 = MyRequests.delete(
            f"/user/{user_id_1}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_code_status(response4, 200)


        # GET_DATA_AFTER_DELETE
        response5 = MyRequests.get(
            f"/user/{user_id_1}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response5, 200)

        username = self.get_json_value(response5, "username")
        assert username == f"learnqa", f"Unexpected response content {response5.content}"

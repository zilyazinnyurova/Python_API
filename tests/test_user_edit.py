from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")


        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "X-csrf-token")

        # EDIT
        new_name = "Changed Name"
        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response3, 200)



        # GET
        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            new_name,
            "Wrong name of the user after edit"
        )




        # Ex17_EDIT WITHOUT AUTH
        response5 = MyRequests.put(f"/user/{user_id}", data={"firstName": new_name})

        Assertions.assert_code_status(response5, 400)
        assert response5.content.decode("utf-8") == f"Auth token not supplied", f"Unexpected response content {response5.content}"




        # Ex17_GET_DATA_OTHER_USER_BEFORE
        user_id_other = "1"
        response6 = MyRequests.get(
            f"/user/{user_id_other}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        username = self.get_json_value(response6, "username")


        # EDIT_OTHER_USER
        username_new = "Changed Name"
        response7 = MyRequests.put(f"/user/{user_id_other}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"username": username_new}
        )

        Assertions.assert_code_status(response7, 200)


        # GET_DATA_OTHER_USER
        response8 = MyRequests.get(
            f"/user/{user_id_other}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response8,
            "username",
            username,
            "Successful update without authorization"
        )


        # Ex17_EDIT_EMAIL
        email_new = "testexample.com"
        response9 = MyRequests.put(f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"email": email_new}
        )

        Assertions.assert_code_status(response9, 400)
        assert response9.content.decode("utf-8") == f"Invalid email format", f"Unexpected response content {response9.content}"


        # Ex17_EDIT_EMAIL_WITHOUT_@
        firstName_name = "t"
        response10 = MyRequests.put(f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": firstName_name}
        )

        Assertions.assert_code_status(response10, 400)

        error = self.get_json_value(response10, "error")
        assert error == f"Too short value for field firstName", f"Unexpected response content {response10.content}"

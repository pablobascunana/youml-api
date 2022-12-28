from core.services.jwt import JwtToken


class TestJwtToken:

    payload = {"a": "abc"}

    def test_encode(self):
        token = JwtToken().encode(self.payload, 1)
        assert "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9" in token

    def test_decode(self):
        token = JwtToken().encode({"a": "abc"}, 1)
        payload = JwtToken().decode(token)
        assert payload["a"] == self.payload["a"]
        assert "exp" in payload

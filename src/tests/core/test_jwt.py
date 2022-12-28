from core.services.jwt import JwtToken


class TestJwtToken:

    payload = {"a": "abc"}

    def test_encode(self):
        token = JwtToken().encode(self.payload)
        assert "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9" in token

    def test_decode(self):
        token = JwtToken().encode({"a": "abc"})
        payload = JwtToken().decode(token)
        assert payload["a"] == self.payload["a"]
        assert "exp" in payload

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(
    TokenObtainPairSerializer
):

    @classmethod
    def get_token(cls, user):

        token = super().get_token(user)

        # 🔥 CUSTOM TOKEN DATA
        token['role'] = user.role
        token['username'] = user.username

        return token

    def validate(self, attrs):

        data = super().validate(attrs)

        # 🔥 RESPONSE DATA
        data['role'] = self.user.role
        data['username'] = self.user.username

        return data
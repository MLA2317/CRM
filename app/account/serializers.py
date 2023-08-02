from rest_framework import serializers
from .models import Account
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from rest_framework.exceptions import AuthenticationFailed


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=40, write_only=True)
    password2 = serializers.CharField(min_length=6, max_length=40, write_only=True)

    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'phone', 'password', 'password2', 'role', 'gender')

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError({
                'success': False, 'message': 'Password did not match, Please tyr again!'
            })
        return attrs

    def create(self, validated_data):
        del validated_data['password2']
        return Account.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=16, required=True)
    password = serializers.CharField(max_length=40, write_only=True)
    tokens = serializers.SerializerMethodField(read_only=True)

    def get_tokens(self, obj):
        phone = obj.get('phone')
        tokens = Account.objects.get(phone=phone).tokens
        return tokens

    class Meta:
        model = Account
        fields = ('phone', 'tokens', 'password')

    def validate(self, attrs):
        phone = attrs.get('phone')
        password = attrs.get('password')
        user = authenticate(phone=phone, password=password)
        if not user:
            raise AuthenticationFailed({
                'success': False, 'message': 'Phone or password is not correct'
            })
        if not user.is_active:
            raise AuthenticationFailed({
                'message': 'Account disabled'
            })

        data = {
            'phone': user.phone,
        }
        return data


class AccountAdminUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = (
            'id', 'first_name', 'last_name', 'phone', 'birth_year', 'image_url', 'role', 'gender', 'is_staff',
            'is_teacher', 'is_student', 'is_active')


class AccountsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'first_name', 'last_name', 'phone', 'birth_year', 'image_url', 'role', 'gender')


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=64, write_only=True)
    password2 = serializers.CharField(min_length=6, max_length=64, write_only=True)

    class Meta:
        model = Account
        fields = ('password', 'password2')

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        request = self.context['request']
        user = request.user
        current_password = user.password
        if password != password2:
            raise serializers.ValidationError({
                'success': False, 'message': 'Password did not match, Please tyr again!'
            })

        if check_password(password, current_password):
            raise serializers.ValidationError(
                {'success': False, 'message': 'New password should not similar to current password'})
        user.set_password(password)
        user.save()
        return attrs


class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("id", "first_name", "last_name", "phone")
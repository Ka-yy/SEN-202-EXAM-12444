from rest_framework import serializers
from models import Manager, Intern

class ManagerSerializer(serializers.ModelSerializer):
    """
    Manager serializer with encapsulation
    Protects sensitive fields like has_company_card from modification
    """
    role = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Manager
        fields = [
            'id', 'first_name', 'last_name', 'full_name', 'email', 
            'phone_number', 'hire_date', 'salary', 'is_active',
            'department', 'has_company_card', 'team_size', 'budget_limit',
            'role', 'created_at', 'updated_at'
        ]
        # Encapsulation: Protect sensitive fields from modification
        read_only_fields = ['has_company_card', 'created_at', 'updated_at', 'id']

    def get_role(self, obj):
        """Use polymorphic method"""
        return obj.get_role()

    def get_full_name(self, obj):
        return obj.get_full_name()


class ManagerReadOnlySerializer(serializers.ModelSerializer):
    """
    Read-only serializer for Manager (used in relationships)
    """
    full_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Manager
        fields = ['id', 'full_name', 'department', 'email']
        read_only_fields = '__all__'

    def get_full_name(self, obj):
        return obj.get_full_name()


class InternSerializer(serializers.ModelSerializer):
    """
    Intern serializer
    """
    role = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField()
    mentor_details = ManagerReadOnlySerializer(source='mentor', read_only=True)
    
    class Meta:
        model = Intern
        fields = [
            'id', 'first_name', 'last_name', 'full_name', 'email',
            'phone_number', 'hire_date', 'salary', 'is_active',
            'mentor', 'mentor_details', 'internship_end', 'university', 
            'field_of_study', 'role', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at', 'id']

    def get_role(self, obj):
        """Use polymorphic method"""
        return obj.get_role()

    def get_full_name(self, obj):
        return obj.get_full_name()

    def validate_mentor(self, value):
        """Ensure mentor is an active manager"""
        if value and not value.is_active:
            raise serializers.ValidationError("Mentor must be an active manager.")
        return value


class StaffRoleSerializer(serializers.Serializer):
    """
    Serializer for staff role information
    Demonstrates polymorphism usage
    """
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    email = serializers.EmailField()
    role = serializers.CharField()
    department = serializers.CharField(required=False)
    mentor_name = serializers.CharField(required=False)

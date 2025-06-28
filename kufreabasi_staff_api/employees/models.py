from django.db import models
from django.core.validators import EmailValidator

# create a reusable address model and associate it with the Manger & intern  module using ForeignKey and create a serializer for the address model 

class StaffBase(models.Model):
    """
    Abstract base model for all staff members
    Demonstrates inheritance - common fields for all employees
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    phone_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def get_role(self):
        """
        Polymorphic method - to be overridden by subclasses
        Returns role-specific label
        """
        return "Staff Member"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.get_full_name()} - {self.get_role()}"


class Manager(StaffBase):
    """
    Manager model inheriting from StaffBase
    Contains manager-specific fields
    """
    department = models.CharField(max_length=100)
    has_company_card = models.BooleanField(default=True)  # Sensitive field

    def get_role(self):
        """
        Polymorphic implementation for Manager
        """
        return "Manager"

    class Meta:
        db_table = 'staff_manager'
        verbose_name = 'Manager'
        verbose_name_plural = 'Managers'


class Intern(StaffBase):
    """
    Intern model inheriting from StaffBase
    Contains intern-specific fields
    """
    mentor = models.ForeignKey(
        Manager, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='interns'
    )
    internship_end = models.DateField()

    def get_role(self):
        """
        Polymorphic implementation for Intern
        """
        return "Intern"

    class Meta:
        db_table = 'staff_intern'
        verbose_name = 'Intern'
        verbose_name_plural = 'Interns'

class Address(models.Model):
    """
    Reusable Address model that can be associated with any staff member
    """
    street_address = models.CharField(max_length=255)
    apartment_unit = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100, default='United States')
    address_type = models.CharField(
        max_length=20,
        choices=[
            ('home', 'Home'),
            ('work', 'Work'),
            ('mailing', 'Mailing'),
            ('emergency', 'Emergency Contact')
        ],
        default='home'
    )
    is_primary = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'staff_address'
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
        ordering = ['-is_primary', 'address_type']

    def __str__(self):
        address_parts = [self.street_address]
        if self.apartment_unit:
            address_parts.append(f"Apt {self.apartment_unit}")
        address_parts.extend([self.city, self.state_province, self.postal_code])
        return ", ".join(address_parts)

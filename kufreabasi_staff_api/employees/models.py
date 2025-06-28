from django.db import models
from django.core.validators import EmailValidator

class StaffBase(models.Model):
    """
    Abstract base model for all staff members
    Demonstrates inheritance - common fields for all employees
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    phone_number = models.CharField(max_length=15)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
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

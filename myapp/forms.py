from django import forms
from django.core.mail import send_mail
from django.conf import settings

# Complete list of countries
COUNTRIES = [
    ('', 'Select Country/Region'),
    ('US', 'United States'),
    ('CA', 'Canada'),
    ('GB', 'United Kingdom'),
    ('AU', 'Australia'),
    ('DE', 'Germany'),
    ('FR', 'France'),
    ('IT', 'Italy'),
    ('ES', 'Spain'),
    ('JP', 'Japan'),
    ('CN', 'China'),
    ('IN', 'India'),
    ('BR', 'Brazil'),
    ('MX', 'Mexico'),
    ('PH', 'Philippines'),
    ('SG', 'Singapore'),
    ('AE', 'United Arab Emirates'),
    ('ZA', 'South Africa'),
    ('NG', 'Nigeria'),
    ('KE', 'Kenya'),
    ('EG', 'Egypt'),
    ('SA', 'Saudi Arabia'),
    ('KR', 'South Korea'),
    ('ID', 'Indonesia'),
    ('MY', 'Malaysia'),
    ('TH', 'Thailand'),
    ('VN', 'Vietnam'),
    ('PK', 'Pakistan'),
    ('BD', 'Bangladesh'),
    ('RU', 'Russia'),
    ('TR', 'Turkey'),
    ('NL', 'Netherlands'),
    ('SE', 'Sweden'),
    ('CH', 'Switzerland'),
    ('NO', 'Norway'),
    ('FI', 'Finland'),
    ('DK', 'Denmark'),
    ('BE', 'Belgium'),
    ('AT', 'Austria'),
    ('IE', 'Ireland'),
    ('PL', 'Poland'),
    ('PT', 'Portugal'),
    ('GR', 'Greece'),
    ('CZ', 'Czech Republic'),
    ('HU', 'Hungary'),
    ('RO', 'Romania'),
    ('IL', 'Israel'),
    ('AR', 'Argentina'),
    ('CL', 'Chile'),
    ('CO', 'Colombia'),
    ('PE', 'Peru'),
    ('NZ', 'New Zealand'),
    ('other', 'Other')
]

# Industry choices
INDUSTRIES = [
    ('', 'Select Industry'),
    ('technology', 'Technology'),
    ('healthcare', 'Healthcare'),
    ('finance', 'Finance'),
    ('retail', 'Retail'),
    ('manufacturing', 'Manufacturing'),
    ('education', 'Education'),
    ('telecom', 'Telecommunications'),
    ('hospitality', 'Hospitality'),
    ('transportation', 'Transportation'),
    ('energy', 'Energy'),
    ('agriculture', 'Agriculture'),
    ('construction', 'Construction'),
    ('media', 'Media & Entertainment'),
    ('government', 'Government'),
    ('nonprofit', 'Non-Profit'),
    ('other', 'Other')
]

# Service choices
SERVICES = [
    ('', 'Select Service'),
    ('customer-support', 'Customer Support'),
    ('data-entry', 'Data Entry'),
    ('virtual-assistant', 'Virtual Assistant'),
    ('software-development', 'Software Development'),
    ('accounting', 'Accounting & Finance'),
    ('marketing', 'Digital Marketing'),
    ('hr', 'Human Resources'),
    ('it-support', 'IT Support'),
    ('content-moderation', 'Content Moderation'),
    ('ecommerce-support', 'E-commerce Support'),
    ('transcription', 'Transcription Services'),
    ('other', 'Other')
]

# Company size choices
COMPANY_SIZES = [
    ('', 'Select Size'),
    ('1-10', '1-10 employees'),
    ('11-50', '11-50 employees'),
    ('51-200', '51-200 employees'),
    ('201-500', '201-500 employees'),
    ('501-1000', '501-1000 employees'),
    ('1001-5000', '1001-5000 employees'),
    ('5000+', '5000+ employees')
]

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20, required=False)
    company = forms.CharField(max_length=100)
    country = forms.ChoiceField(choices=COUNTRIES)
    industry = forms.ChoiceField(choices=INDUSTRIES)
    company_size = forms.ChoiceField(choices=COMPANY_SIZES)
    service = forms.ChoiceField(choices=SERVICES)
    message = forms.CharField(required=False, widget=forms.Textarea)

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '')
        if phone and not phone.replace('+', '').replace('-', '').replace(' ', '').isdigit():
            raise forms.ValidationError("Phone number should contain only digits, spaces, hyphens, and plus signs.")
        return phone

    def send_email(self):
        """Send email with form data"""
        if not self.is_valid():
            return False
        
        try:
            # Get cleaned data
            data = self.cleaned_data
            
            # Helper function to get display values for choice fields
            def get_display_value(field_name, value):
                choice_dict = {
                    'country': dict(COUNTRIES),
                    'industry': dict(INDUSTRIES),
                    'service': dict(SERVICES),
                    'company_size': dict(COMPANY_SIZES)
                }
                return choice_dict.get(field_name, {}).get(value, value)
            
            # Create email subject
            subject = f"New Contact Form Submission from {data['first_name']} {data['last_name']}"
            
            # Create email body
            email_body = f"""
New Contact Form Submission

Contact Information:
- Name: {data['first_name']} {data['last_name']}
- Email: {data['email']}
- Phone: {data['phone'] if data['phone'] else 'Not provided'}
- Company: {data['company']}

Company Details:
- Country: {get_display_value('country', data['country'])}
- Industry: {get_display_value('industry', data['industry'])}
- Company Size: {get_display_value('company_size', data['company_size'])}
- Service Interested In: {get_display_value('service', data['service'])}

Message:
{data['message'] if data['message'] else 'No message provided'}

---
This email was sent from your website contact form.
            """
            
            # Format the from_email to include customer name
            from_email_with_name = f"{data['first_name']} {data['last_name']} <{settings.DEFAULT_FROM_EMAIL}>"
            
            send_mail(
                subject=subject,
                message=email_body,
                from_email=from_email_with_name,
                recipient_list=['sohailshaikhavp75@gmail.com'],
                fail_silently=False,
            )
            return True
            
        except Exception as e:
            print(f"Email sending failed: {e}")
            return False
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = 'weekly'

    def items(self):
        return [
            'index',
            'our_services',
            'about_us',
            'our_team',
            'values_mission_and_vision',
            'locations',
            'faqs',
            'industry-experience',
            'industry-experience/in_we_serve_retail_ecommerce',
            'industry-experience/in_we_serve_education',
            'industry-experience/in_we_serve_marketing_services',
            'industry-experience/in_we_serve_financial_services',
            'industry-experience/in_we_serve_telecommunications',
            'industry-experience/in_we_serve_real_estate',
            'industry-experience/in_we_serve_media_communications',
            'industry-experience/in_we_serve_website_design_development',
            'industry-experience/in_we_serve_insurance',
            'Why-Value-Connect-Solution',
            'Why-Value-Connect-Solution/Value-Pillars',
            'Why-Value-Connect-Solution/Reasons-to-Outsource',
            'Why-Value-Connect-Solution/Processes',
            'Why-Value-Connect-Solution/Security-Standards-And-Disaster-Recovery-Planning',
            'Why-Value-Connect-Solution/Processes/Training',
            'Why-Value-Connect-Solution/Processes/Quality-Assurance',
            'Why-Value-Connect-Solution/Processes/Recruiting-and-Staffing',
            'Why-Value-Connect-Solution/Processes/Implementation',
            'Why-Value-Connect-Solution/Processes/Client-Services',
            # Add all 'our-services' subpages here
            'inbound_call_center_services',
            'technical_support',
            'order_processing',
            'customer_service_outsourcing',
            'customer_retention_support',
            'overflow_call_handling',
            'billing_inquiries',
            'after_hours_support',
            'troubleshoooting_services',
            'outbound_call_center_solutions',
            'software_training_services',
            'software_installation_support',
            'software_and_app_support',
            'lead_generation',
            'appointment_setting',
            'telemarketing',
            'clinical_trial_recruiting',
            'back_office_support',
            'data_entry',
            'data_mining',
            'claim_filing',
            'form_processing',
        ]

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        if item == 'index':
            return 1.0
        elif item in ['our_services', 'about_us', 'industry-experience']:
            return 0.8
        else:
            return 0.5

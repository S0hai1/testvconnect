# main/urls.py
from django.urls import path
from . import views


from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap
from myapp.sitemaps import StaticViewSitemap

sitemaps_dict = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', views.index, name='index'),
    path('our-services/', views.our_services, name='our_services'),
    path('our-services/inbound-call-center-services/', views.inbound_call_center_services, name='inbound_call_center_services'),
    path('our-services/technical-support/', views.technical_support_page, name='technical_support'),
    path('our-services/order-processing-services/', views.order_processing_services, name='order_processing'),
    path('our-services/customer-service-outsourcing/', views.customer_service_outsourcing, name='customer_service_outsourcing'),
    path('our-services/customer-retention-support/', views.customer_retention_support, name='customer_retention_support'),
    path('our-services/overflow-call-handling/', views.overflow_call_handling, name='overflow_call_handling'),
    path('our-services/billing-inquiries/', views.billing_inquiries, name='billing_inquiries'),
    path('our-services/after-hours-support/', views.after_hours_support, name='after_hours_support'),
    path('our-services/troubleshoooting-services/', views.troubleshoooting_services, name='troubleshoooting_services'),
    path('our-services/outbound-call-center-solutions/', views.outbound_call_center_solutions, name='outbound_call_center_solutions'),
    path('our-services/software-training-services/', views.software_training_services, name='software_training_services'),
    path('our-services/software-installation-support/', views.software_installation_support, name='software_installation_support'),
    path('our-services/software-and-app-support/', views.software_and_app_support, name='software_and_app_support'),
    path('our-services/lead-generation/', views.lead_generation, name='lead_generation'),
    path('our-services/appointment-setting/', views.appointment_setting, name='appointment_setting'),
    path('our-services/telemarketing/', views.telemarketing, name='telemarketing'),
    path('our-services/clinical-trial-recruiting/', views.clinical_trial_recruiting, name='clinical_trial_recruiting'),

    path('our-services/back-office-support/', views.back_office_support, name='back_office_support'),
    path('our-services/data-entry/', views.data_entry, name='data_entry'),
    path('our-services/data-mining/', views.data_mining, name='data_mining'),
    path('our-services/claim-filing/', views.claim_filing, name='claim_filing'),
    path('our-services/form-processing/', views.form_processing, name='form_processing'),


    path('about-us/', views.about_us, name='about_us'),
    path('about-us/our-team/', views.our_team, name='our_team'),
    path('about-us/values-mission-and-vision/', views.values_mission_and_vision, name='values_mission_and_vision'),
    path('about-us/locations/', views.locations, name='locations'),
    path('about-us/faqs/', views.faqs, name='faqs'),

    path('contact-form-submit/', views.contact_form_submit, name='contact_form_submit'),
    path('contact-us/', views.contact_us, name='contact-us'),



    #industry_experience
    path('industry-experience/',views.industry_experience,name='industry-experience'),
    path('industry-experience/retail-ecommerce/', views.in_we_serve_retail_ecommerce, name='industry-experience/in_we_serve_retail_ecommerce'),
    path('industry-experience/education/', views.in_we_serve_education, name='industry-experience/in_we_serve_education'),
    path('industry-experience/marketing-services/', views.in_we_serve_marketing_services, name='industry-experience/in_we_serve_marketing_services'),
    path('industry-experience/financial-services/', views.in_we_serve_financial_services, name='industry-experience/in_we_serve_financial_services'),
    path('industry-experience/telecommunications/', views.in_we_serve_telecommunications, name='industry-experience/in_we_serve_telecommunications'),
    path('industry-experience/real-estate/', views.in_we_serve_real_estate, name='industry-experience/in_we_serve_real_estate'),
    path('industry-experience/media-communications/', views.in_we_serve_media_communications, name='industry-experience/in_we_serve_media_communications'),
    path('industry-experience/website-design-development/', views.in_we_serve_website_design_development, name='industry-experience/in_we_serve_website_design_development'),
    path('industry-experience/insurance/', views.in_we_serve_insurance, name='industry-experience/in_we_serve_insurance'),

       
        



    # Why VCS
    path('Why-Value-Connect-Solution', views.why_vcs, name='Why-Value-Connect-Solution'),
    path('Why-Value-Connect-Solution/Value-Pillars', views.Value_Pillars, name='Why-Value-Connect-Solution/Value-Pillars'),
    path('Why-Value-Connect-Solution/Reasons-to-Outsource', views.Reasons_to_Outsource, name='Why-Value-Connect-Solution/Reasons-to-Outsource'),
    path('Why-Value-Connect-Solution/Processes', views.Processes, name='Why-Value-Connect-Solution/Processes'),
    path('Why-Value-Connect-Solution/Security-Standards-And-Disaster-Recovery-Planning', views.Security_Standards, name='Why-Value-Connect-Solution/Security-Standards-And-Disaster-Recovery-Planning'),
         
         #processes 
        path('Why-Value-Connect-Solution/Processes/Training', views.training_view, name='Why-Value-Connect-Solution/Processes/Training'),
        path('Why-Value-Connect-Solution/Processes/Quality-Assurance', views.quality_assurance_view, name='Why-Value-Connect-Solution/Processes/Quality-Assurance'),
        path('Why-Value-Connect-Solution/Processes/Recruiting-and-Staffing', views.recruiting_staffing_view, name='Why-Value-Connect-Solution/Processes/Recruiting-and-Staffing'),
        path('Why-Value-Connect-Solution/Processes/Implementation', views.implementation_view, name='Why-Value-Connect-Solution/Processes/Implementation'),
        path('Why-Value-Connect-Solution/Processes/Client-Services', views.client_services_view, name='Why-Value-Connect-Solution/Processes/Client-Services'),
        

    # for SEO
    path('robots.txt', views.robots_txt, name='robots_txt'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps_dict}, name='django.contrib.sitemaps.views.sitemap'),

]

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .forms import ContactForm
import json

# Create your views here.


def index(request):
    context = {
        'title': "Value ConnectSolutions - Digital Growth & Business Solutions",
        'meta_description': "Welcome to ValueConnectSolution – your partner for digital growth and business empowerment. We offer expert solutions and services for businesses in USA, Canada, UK, Australia, and India.",
        'meta_keywords': "home, homepage, valueconnectsolution, digital solutions, business services, global, USA, Canada, UK, Australia, India",
        'og_title': "Home - ValueConnectSolution",
        'og_description': "Welcome to our home page - we help you thrive digitally.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'website',
        'og_image': 'myapp/images/home-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "Home - ValueConnectSolution",
        'twitter_description': "Explore our services to empower your business.",
        'twitter_image': 'myapp/images/home-twitter.jpg',
        'favicon': 'myapp/images/favicon-home.png',
    }
    return render(request, 'myapp/index.html', context)

def our_services(request):
    context = {
        'title': "Our Services - Global Business Solutions",
        'meta_description': "Explore ValueConnectSolution's comprehensive services: call center solutions, back-office support, and specialized industry expertise for businesses in USA, Canada, UK, Australia, and India.",
        'meta_keywords': "our services, business solutions, call center, back office, industry expertise, outsourcing, global services, USA, Canada, UK, Australia, India",
        'og_title': "Our Services - ValueConnectSolution",
        'og_description': "Explore our comprehensive range of services tailored for global businesses.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'website',
        'og_image': 'myapp/images/default-og.jpg', # Default image
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "Our Services - ValueConnectSolution",
        'twitter_description': "Discover the full suite of ValueConnectSolution services for your global business needs.",
        'twitter_image': 'myapp/images/default-twitter.jpg', # Default image
        'favicon': 'myapp/images/favicon.png', # Default favicon
    }
    return render(request, 'myapp/our_services.html', context)

def inbound_call_center_services(request):
    context = {
        'title': "Inbound Call Center Services - Global Support",
        'meta_description': "ValueConnectSolution offers professional inbound call center services. We provide superior customer support, technical assistance, and order processing for businesses worldwide, including USA, Canada, UK, Australia, India.",
        'meta_keywords': "inbound call center, customer support, technical assistance, order processing, call handling, customer service, global contact center, USA, Canada, UK, Australia, India",
        'og_title': "Inbound Call Center - ValueConnectSolution",
        'og_description': "Reliable inbound call center services for exceptional customer experiences.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'service',
        'og_image': 'myapp/images/inbound-call-center-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "Inbound Call Center - ValueConnectSolution",
        'twitter_description': "Elevate your customer interactions with our expert inbound call center solutions.",
        'twitter_image': 'myapp/images/inbound-call-center-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
    }
    return render(request, 'myapp/inbound_call_center_services.html', context)

def technical_support_page(request):
    context = {
        'title': "Technical Support - IT Help Desk Solutions",
        'meta_description': "Get reliable technical support services from ValueConnectSolution. We offer troubleshooting, software assistance, and IT help desk solutions to ensure seamless global operations for your business.",
        'meta_keywords': "technical support, IT help desk, software support, troubleshooting, tech assistance, remote support, global IT support, USA, Canada, UK, Australia, India",
        'og_title': "Technical Support - ValueConnectSolution",
        'og_description': "Expert IT help desk and technical support for businesses worldwide.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'service',
        'og_image': 'myapp/images/tech-support-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "Technical Support - ValueConnectSolution",
        'twitter_description': "Seamless tech support and troubleshooting to keep your operations running smoothly.",
        'twitter_image': 'myapp/images/tech-support-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
    }
    return render(request, 'myapp/technical_support_page.html', context)

def order_processing_services(request):
    context = {
        'title': "Order Processing Services - Efficient Fulfillment",
        'meta_description': "ValueConnectSolution provides efficient and accurate order processing services. Streamline your sales fulfillment and enhance customer satisfaction with our expert team supporting global businesses.",
        'meta_keywords': "order processing, sales fulfillment, order management, e-commerce support, transaction processing, global order processing, USA, Canada, UK, Australia, India",
        'og_title': "Order Processing - ValueConnectSolution",
        'og_description': "Streamline your order fulfillment with our precise and efficient processing services.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'service',
        'og_image': 'myapp/images/order-processing-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "Order Processing - ValueConnectSolution",
        'twitter_description': "Accurate and swift order processing to boost your e-commerce and sales operations.",
        'twitter_image': 'myapp/images/order-processing-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
    }
    return render(request, 'myapp/order_processing_services.html', context)

def customer_service_outsourcing(request):
    context = {
        'title': "Customer Service Outsourcing - Global Excellence",
        'meta_description': "Outsource your customer service to ValueConnectSolution for exceptional client interactions. We provide multi-channel support tailored for businesses in USA, Canada, UK, Australia, and India.",
        'meta_keywords': "customer service outsourcing, outsourced support, client care, multi-channel, customer satisfaction, global customer service, BPO, USA, Canada, UK, Australia, India",
        'og_title': "Customer Service Outsourcing - ValueConnectSolution",
        'og_description': "Achieve exceptional customer satisfaction through our outsourced customer service solutions.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'service',
        'og_image': 'myapp/images/customer-service-outsourcing-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "Customer Service Outsourcing - ValueConnectSolution",
        'twitter_description': "Enhance customer experiences and loyalty with our comprehensive outsourced services.",
        'twitter_image': 'myapp/images/customer-service-outsourcing-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
    }
    return render(request, 'myapp/customer_service_outsourcing.html', context)

def customer_retention_support(request):
    context = {
        'title': "Customer Retention Support - Build Loyalty",
        'meta_description': "Boost customer loyalty and reduce churn with ValueConnectSolution's retention support. Our strategies help you build lasting relationships and maximize customer lifetime value globally.",
        'meta_keywords': "customer retention, customer loyalty, churn reduction, customer lifetime value, client retention strategies, global customer retention, USA, Canada, UK, Australia, India",
        'og_title': "Customer Retention - ValueConnectSolution",
        'og_description': "Strategies and support to build lasting customer loyalty and reduce churn.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'service',
        'og_image': 'myapp/images/customer-retention-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "Customer Retention - ValueConnectSolution",
        'twitter_description': "Maximize customer lifetime value with our dedicated retention programs.",
        'twitter_image': 'myapp/images/customer-retention-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
    }
    return render(request, 'myapp/customer_retention_support.html', context)

def overflow_call_handling(request):
    context = {
        'title': "Overflow Call Handling Services - Never Miss a Call",
        'meta_description': "Ensure no customer call goes unanswered with ValueConnectSolution's overflow call handling services. We provide seamless support during peak times for businesses worldwide.",
        'meta_keywords': "overflow call handling, call center overflow, peak hour support, inbound call management, never miss a call, global call handling, USA, Canada, UK, Australia, India",
        'og_title': "Overflow Call Handling - ValueConnectSolution",
        'og_description': "Efficiently manage high call volumes and ensure all customer calls are answered.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'service',
        'og_image': 'myapp/images/overflow-call-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "Overflow Call Handling - ValueConnectSolution",
        'twitter_description': "Maintain exceptional service even during peak periods with our reliable overflow support.",
        'twitter_image': 'myapp/images/overflow-call-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
    }
    return render(request, 'myapp/overflow_call_handling.html', context)

def billing_inquiries(request):
    context = {
        'title': "Billing Inquiries Support - Streamlined Solutions",
        'meta_description': "ValueConnectSolution offers expert billing inquiries support. Resolve customer billing questions efficiently, improve satisfaction, and reduce administrative burden for your global operations.",
        'meta_keywords': "billing inquiries, billing support, payment processing, invoice support, customer billing, financial inquiries, global billing, USA, Canada, UK, Australia, India",
        'og_title': "Billing Inquiries - ValueConnectSolution",
        'og_description': "Expert support for all customer billing questions and inquiries.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'service',
        'og_image': 'myapp/images/billing-inquiries-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "Billing Inquiries - ValueConnectSolution",
        'twitter_description': "Efficiently manage billing queries to enhance customer satisfaction and operational flow.",
        'twitter_image': 'myapp/images/billing-inquiries-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
    }
    return render(request, 'myapp/billing_inquiries.html', context)

def after_hours_support(request):
    context = {
        'title': "After-Hours Support - 24/7 Customer Care",
        'meta_description': "Provide continuous customer support with ValueConnectSolution's after-hours services. We ensure your clients receive assistance beyond standard business hours, globally.",
        'meta_keywords': "after-hours support, 24/7 support, overnight support, extended hours, non-business hour support, global customer care, USA, Canada, UK, Australia, India",
        'og_title': "After-Hours Support - ValueConnectSolution",
        'og_description': "Round-the-clock customer support to ensure your clients are always covered.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'service',
        'og_image': 'myapp/images/after-hours-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "After-Hours Support - ValueConnectSolution",
        'twitter_description': "Expand your customer service reach with our reliable 24/7 support solutions.",
        'twitter_image': 'myapp/images/after-hours-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
    }
    return render(request, 'myapp/after_hours_support.html', context)

def troubleshoooting_services(request):
    context = {
        'title': "Troubleshooting Services - Expert Problem Solving",
        'meta_description': "ValueConnectSolution provides comprehensive troubleshooting services. Our experts diagnose and resolve technical issues quickly and efficiently, minimizing downtime for global businesses.",
        'meta_keywords': "troubleshooting services, problem resolution, technical issue fix, IT problem solving, software troubleshooting, global tech support, USA, Canada, UK, Australia, India",
        'og_title': "Troubleshooting Services - ValueConnectSolution",
        'og_description': "Swift and effective troubleshooting to resolve technical issues and minimize disruption.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'service',
        'og_image': 'myapp/images/troubleshooting-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "Troubleshooting Services - ValueConnectSolution",
        'twitter_description': "Get expert assistance for all your technical challenges and ensure smooth operations.",
        'twitter_image': 'myapp/images/troubleshooting-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
    }
    return render(request, 'myapp/troubleshoooting_services.html', context)

def outbound_call_center_solutions(request):
    context = {
        'title': "Outbound Call Center Solutions - Sales & Outreach",
        'meta_description': "Drive sales and effective outreach with ValueConnectSolution's outbound call center solutions. We specialize in lead generation, telemarketing, and appointment setting for global markets.",
        'meta_keywords': "outbound call center, telemarketing, lead generation, appointment setting, sales outreach, telesales, global outbound, USA, Canada, UK, Australia, India",
        'og_title': "Outbound Call Center - ValueConnectSolution",
        'og_description': "Strategic outbound call center services to drive sales and business growth.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'service',
        'og_image': 'myapp/images/outbound-call-center-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "Outbound Call Center - ValueConnectSolution",
        'twitter_description': "Fuel your sales pipeline with our effective lead generation and telemarketing expertise.",
        'twitter_image': 'myapp/images/outbound-call-center-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
    }
    return render(request, 'myapp/outbound_call_center_solutions.html', context)

def software_training_services(request):
    context = {
        'title': "Software Training Services - User Adoption",
        'meta_description': "Enhance user proficiency with ValueConnectSolution's software training services. We provide comprehensive training programs to ensure smooth software adoption for businesses worldwide.",
        'meta_keywords': "software training, user adoption, software tutorials, tech education, IT training, global software training, USA, Canada, UK, Australia, India",
        'og_title': "Software Training - ValueConnectSolution",
        'og_description': "Comprehensive software training to maximize user proficiency and system adoption.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'service',
        'og_image': 'myapp/images/software-training-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "Software Training - ValueConnectSolution",
        'twitter_description': "Empower your team with the skills to effectively use new software and applications.",
        'twitter_image': 'myapp/images/software-training-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
    }
    return render(request, 'myapp/software_training_services.html', context)

def software_installation_support(request):
    context = {
        'title': "Software Installation Support - Seamless Setup",
        'meta_description': "ValueConnectSolution offers reliable software installation support. Ensure a smooth and hassle-free setup for all your applications with our expert assistance, globally.",
        'meta_keywords': "software installation, setup support, application installation, tech setup, software deployment, global installation, USA, Canada, UK, Australia, India",
        'og_title': "Software Installation - ValueConnectSolution",
        'og_description': "Hassle-free software installation support for smooth and efficient setups.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'service',
        'og_image': 'myapp/images/software-installation-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "Software Installation - ValueConnectSolution",
        'twitter_description': "Ensure proper software deployment and configuration with our expert assistance.",
        'twitter_image': 'myapp/images/software-installation-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
    }
    return render(request, 'myapp/software_installation_support.html', context)

def software_and_app_support(request):
    context = {
        'title': "Software & App Support - Comprehensive Help",
        'meta_description': "Get comprehensive software and app support from ValueConnectSolution. We provide assistance for various applications, ensuring optimal performance and user satisfaction for global users.",
        'meta_keywords': "software support, app support, application assistance, tech help, software troubleshooting, mobile app support, global app support, USA, Canada, UK, Australia, India",
        'og_title': "Software & App Support - ValueConnectSolution",
        'og_description': "Comprehensive support for all your software and mobile application needs.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'service',
        'og_image': 'myapp/images/software-app-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "Software & App Support - ValueConnectSolution",
        'twitter_description': "Ensure optimal performance and user satisfaction with our dedicated app and software support.",
        'twitter_image': 'myapp/images/software-app-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
    }
    return render(request, 'myapp/software_and_app_support.html', context)

def lead_generation(request):
    context = {
        'title': "Lead Generation Services - Boost Your Sales",
        'meta_description': "Accelerate your sales pipeline with ValueConnectSolution's lead generation services. We identify and qualify high-quality leads for businesses across USA, Canada, UK, Australia, and India.",
        'meta_keywords': "lead generation, sales leads, qualified leads, B2B leads, lead nurturing, prospecting, global lead generation, USA, Canada, UK, Australia, India",
        'og_title': "Lead Generation - ValueConnectSolution",
        'og_description': "Generate high-quality leads to boost your sales and market reach.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'service',
        'og_image': 'myapp/images/lead-generation-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "Lead Generation - ValueConnectSolution",
        'twitter_description': "Accelerate your sales pipeline with our expert lead generation strategies.",
        'twitter_image': 'myapp/images/lead-generation-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
    }
    return render(request, 'myapp/lead_generation.html', context)

def appointment_setting(request):
    context = {
        'title': "Appointment Setting Services - Drive Meetings",
        'meta_description': "Fill your calendar with qualified meetings using ValueConnectSolution's appointment setting services. We connect you with key decision-makers in USA, Canada, UK, Australia, and India.",
        'meta_keywords': "appointment setting, sales appointments, meeting scheduling, B2B appointments, sales development, global appointment setting, USA, Canada, UK, Australia, India",
        'og_title': "Appointment Setting - ValueConnectSolution",
        'og_description': "Efficient appointment setting to connect you with qualified prospects.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'service',
        'og_image': 'myapp/images/appointment-setting-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "Appointment Setting - ValueConnectSolution",
        'twitter_description': "Streamline your sales process by letting us schedule your key business meetings.",
        'twitter_image': 'myapp/images/appointment-setting-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
    }
    return render(request, 'myapp/appointment_setting.html', context)

def telemarketing(request):
    context = {
        'title': "Telemarketing Services - Effective Campaigns",
        'meta_description': "Launch impactful telemarketing campaigns with ValueConnectSolution. Our expert team conducts targeted outreach, sales calls, and surveys for businesses globally.",
        'meta_keywords': "telemarketing, phone sales, telesales, direct marketing, outbound campaigns, customer surveys, global telemarketing, USA, Canada, UK, Australia, India",
        'og_title': "Telemarketing Services - ValueConnectSolution",
        'og_description': "Impactful telemarketing campaigns for sales, lead generation, and customer engagement.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'service',
        'og_image': 'myapp/images/telemarketing-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "Telemarketing Services - ValueConnectSolution",
        'twitter_description': "Reach your target audience effectively with our professional telemarketing solutions.",
        'twitter_image': 'myapp/images/telemarketing-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
    }
    return render(request, 'myapp/telemarketing.html', context)

def clinical_trial_recruiting(request):
    context = {
        'title': "Clinical Trial Recruiting - Patient Enrollment",
        'meta_description': "ValueConnectSolution specializes in efficient clinical trial recruiting. We help research organizations in USA, Canada, UK, Australia, and India find and enroll eligible patients rapidly.",
        'meta_keywords': "clinical trial recruiting, patient enrollment, medical research, clinical studies, participant recruitment, global clinical trials, USA, Canada, UK, Australia, India",
        'og_title': "Clinical Trial Recruiting - ValueConnectSolution",
        'og_description': "Accelerate your clinical trials with our efficient patient recruitment services.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'service',
        'og_image': 'myapp/images/clinical-trial-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "Clinical Trial Recruiting - ValueConnectSolution",
        'twitter_description': "Connect with eligible participants faster through our specialized recruiting solutions.",
        'twitter_image': 'myapp/images/clinical-trial-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
    }
    return render(request, 'myapp/clinical_trial_recruiting.html', context)

def back_office_support(request):
    context = {
        'title': "Back Office Support - Operational Efficiency",
        'meta_description': "Optimize your business operations with ValueConnectSolution's back office support services. We handle administrative tasks, data management, and more for global enterprises.",
        'meta_keywords': "back office support, administrative services, data management, operational support, BPO, back office outsourcing, global operations, USA, Canada, UK, Australia, India",
        'og_title': "Back Office Support - ValueConnectSolution",
        'og_description': "Streamline your administrative tasks and enhance operational efficiency with our back office support.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'service',
        'og_image': 'myapp/images/back-office-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "Back Office Support - ValueConnectSolution",
        'twitter_description': "Focus on core business activities while we manage your essential back-office functions.",
        'twitter_image': 'myapp/images/back-office-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
    }
    return render(request, 'myapp/back_office_support.html', context)

def data_entry(request):
    context = {
        'title': "Data Entry Services - Accurate & Efficient",
        'meta_description': "Ensure accuracy and efficiency with ValueConnectSolution's data entry services. We handle high volumes of data, converting raw information into structured formats for global businesses.",
        'meta_keywords': "data entry, data processing, accurate data, data capture, data management, digital data entry, global data entry, USA, Canada, UK, Australia, India",
        'og_title': "Data Entry Services - ValueConnectSolution",
        'og_description': "Reliable and accurate data entry services for all your information management needs.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'service',
        'og_image': 'myapp/images/data-entry-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "Data Entry Services - ValueConnectSolution",
        'twitter_description': "Ensure precision and efficiency in data handling with our expert data entry solutions.",
        'twitter_image': 'myapp/images/data-entry-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
    }
    return render(request, 'myapp/data_entry.html', context)

def data_mining(request):
    context = {
        'title': "Data Mining Services - Insights & Analysis",
        'meta_description': "Uncover valuable insights with ValueConnectSolution's data mining services. We extract meaningful patterns from your data to support strategic decision-making for businesses worldwide.",
        'meta_keywords': "data mining, data analysis, business intelligence, data insights, pattern recognition, strategic data, global data mining, USA, Canada, UK, Australia, India",
        'og_title': "Data Mining Services - ValueConnectSolution",
        'og_description': "Unlock valuable insights and patterns from your data with our advanced data mining services.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'service',
        'og_image': 'myapp/images/data-mining-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "Data Mining Services - ValueConnectSolution",
        'twitter_description': "Leverage data-driven intelligence for strategic decision-making and business growth.",
        'twitter_image': 'myapp/images/data-mining-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
    }
    return render(request, 'myapp/data_mining.html', context)

def claim_filing(request):
    context = {
        'title': "Claim Filing Services - Expert Processing",
        'meta_description': "Streamline your claim filing process with ValueConnectSolution. We provide expert assistance in processing and managing various types of claims efficiently for global clients.",
        'meta_keywords': "claim filing, claims processing, insurance claims, medical claims, document filing, claim management, global claims, USA, Canada, UK, Australia, India",
        'og_title': "Claim Filing Services - ValueConnectSolution",
        'og_description': "Efficient and accurate claim filing services to simplify your processing needs.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'service',
        'og_image': 'myapp/images/claim-filing-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "Claim Filing Services - ValueConnectSolution",
        'twitter_description': "Expert assistance in managing and submitting various types of claims seamlessly.",
        'twitter_image': 'myapp/images/claim-filing-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
    }
    return render(request, 'myapp/claim_filing.html', context)


def about_us(request):
    context = {
        'title': "About Us - ValueConnectSolution",
        'meta_description': "Learn about ValueConnectSolution, a leading provider of global business process outsourcing (BPO) and customer experience solutions. Discover our commitment to excellence and client success.",
        'meta_keywords': "about us, ValueConnectSolution, BPO, outsourcing company, mission, vision, values, global business, USA, Canada, UK, Australia, India",
        'og_title': "About Us - ValueConnectSolution",
        'og_description': "Discover the ValueConnectSolution story, our mission, and our commitment to global excellence.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'website',
        'og_image': 'myapp/images/about-us-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "About Us - ValueConnectSolution",
        'twitter_description': "Learn more about our journey and what drives us to deliver exceptional BPO services.",
        'twitter_image': 'myapp/images/about-us-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
    }
    return render(request, 'myapp/about_us.html', context)

def our_team(request):
    team_members = [
        # Leadership
        {
            'name': 'John Doe',
            'title': 'CEO',
            'image': '/static/images/john_doe.jpg', # Adjust path as needed
            'category': 'leadership',
            'description': 'John is the visionary leader guiding our company\'s growth and strategy.'
        },
        {
            'name': 'Jane Smith',
            'title': 'Chief Operating Officer',
            'image': '/static/images/jane_smith.jpg', # Adjust path as needed
            'category': 'leadership',
            'description': 'Jane oversees daily operations, ensuring efficiency and productivity.'
        },
        # Client Support
        {
            'name': 'Emily White',
            'title': 'Senior Client Support Specialist',
            'image': '/static/images/emily_white.jpg', # Adjust path as needed
            'category': 'client_support',
            'description': 'Emily is dedicated to providing exceptional support and building strong client relationships.'
        },
        {
            'name': 'Michael Brown',
            'title': 'Client Support Representative',
            'image': '/static/images/michael_brown.jpg', # Adjust path as needed
            'category': 'client_support',
            'description': 'Michael assists clients with their inquiries and ensures their satisfaction.'
        },
        # Trainees
        {
            'name': 'Sarah Lee',
            'title': 'Marketing Trainee',
            'image': '/static/images/sarah_lee.jpg', # Adjust path as needed
            'category': 'trainee',
            'description': 'Sarah is a bright new talent learning the ropes in our marketing department.'
        },
        # General Team
        {
            'name': 'David Green',
            'title': 'Software Developer',
            'image': '/static/images/david_green.jpg', # Adjust path as needed
            'category': 'team',
            'description': 'David is a key member of our development team, building robust software solutions.'
        },
        {
            'name': 'Alice Johnson', # Added unique name
            'title': 'Project Manager',
            'image': '/static/images/alice_johnson.jpg', # Adjust path as needed
            'category': 'team',
            'description': 'Alice leads various projects, ensuring timely delivery and client satisfaction.'
        },
        {
            'name': 'Robert Williams', # Added unique name
            'title': 'Quality Assurance Analyst',
            'image': '/static/images/robert_williams.jpg', # Adjust path as needed
            'category': 'team',
            'description': 'Robert ensures the highest quality standards across all our services.'
        },
        {
            'name': 'Laura Davis', # Added unique name
            'title': 'Data Analyst',
            'image': '/static/images/laura_davis.jpg', # Adjust path as needed
            'category': 'team',
            'description': 'Laura transforms raw data into actionable insights for our clients.'
        },
        {
            'name': 'Chris Miller', # Added unique name
            'title': 'Operations Coordinator',
            'image': '/static/images/chris_miller.jpg', # Adjust path as needed
            'category': 'team',
            'description': 'Chris ensures the smooth day-to-day operations of our service delivery.'
        },
        {
            'name': 'Olivia Kim',
            'title': 'HR Coordinator',
            'image': '/static/images/olivia_kim.jpg', # Adjust path as needed
            'category': 'team',
            'description': 'Olivia manages human resources, fostering a supportive and productive work environment.'
        },
        {
            'name': 'Daniel Wilson', # Added unique name
            'title': 'Marketing Specialist',
            'image': '/static/images/daniel_wilson.jpg', # Adjust path as needed
            'category': 'team',
            'description': 'Daniel supports our marketing efforts, enhancing our brand\'s visibility.'
        },
        {
            'name': 'Sophia Martinez', # Added unique name
            'title': 'Recruitment Specialist',
            'image': '/static/images/sophia_martinez.jpg', # Adjust path as needed
            'category': 'team',
            'description': 'Sophia is instrumental in attracting and onboarding top talent to our team.'
        },
        {
            'name': 'James Taylor', # Added unique name
            'title': 'Training Manager',
            'image': '/static/images/james_taylor.jpg', # Adjust path as needed
            'category': 'team',
            'description': 'James develops and delivers training programs for our staff.'
        },
        {
            'name': 'Mia Anderson', # Added unique name
            'title': 'Compliance Officer',
            'image': '/static/images/mia_anderson.jpg', # Adjust path as needed
            'category': 'team',
            'description': 'Mia ensures that all our operations adhere to industry regulations and standards.'
        },
    ]

    # Filter team members by category
    leadership_team = [member for member in team_members if member['category'] == 'leadership']
    client_support_team = [member for member in team_members if member['category'] == 'client_support']
    trainee_team = [member for member in team_members if member['category'] == 'trainee']
    general_team = [member for member in team_members if member['category'] == 'team']

    context = {
        'title': "Our Team - Meet the Experts",
        'meta_description': "Meet the dedicated professionals at ValueConnectSolution who drive our success and deliver exceptional services to clients across USA, Canada, UK, Australia, and India.",
        'meta_keywords': "our team, leadership, staff, employees, ValueConnectSolution team, experts, global team, USA, Canada, UK, Australia, India",
        'og_title': "Our Team - ValueConnectSolution",
        'og_description': "Get to know the passionate individuals behind ValueConnectSolution's global success.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'profile', # Changed to profile as it's about people
        'og_image': 'myapp/images/our-team-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "Our Team - ValueConnectSolution",
        'twitter_description': "Discover the talent and expertise that makes ValueConnectSolution a leader in BPO.",
        'twitter_image': 'myapp/images/our-team-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
        'leadership_team': leadership_team,
        'client_support_team': client_support_team,
        'trainee_team': trainee_team,
        'general_team': general_team,
    }
    return render(request, 'myapp/our_team.html',context)


def values_mission_and_vision(request):
    context = {
        'title': "Values, Mission, Vision - ValueConnectSolution",
        'meta_description': "Discover the core values, mission, and vision that guide ValueConnectSolution in delivering outstanding BPO and customer experience services globally.",
        'meta_keywords': "company values, mission statement, vision statement, ValueConnectSolution culture, ethics, global business principles, USA, Canada, UK, Australia, India",
        'og_title': "Our Values, Mission & Vision - ValueConnectSolution",
        'og_description': "Learn about the foundational principles that drive ValueConnectSolution's commitment to excellence.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'website',
        'og_image': 'myapp/images/values-mission-vision-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "Our Values, Mission & Vision - ValueConnectSolution",
        'twitter_description': "Explore the pillars of our organization's success and guiding philosophy.",
        'twitter_image': 'myapp/images/values-mission-vision-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
    }
    return render(request, 'myapp/values_mission_and_vision.html', context)

def locations(request):
    context = {
        'title': "Our Global Locations - ValueConnectSolution",
        'meta_description': "Find ValueConnectSolution's global office locations and contact information. We serve clients in USA, Canada, UK, Australia, and India with strategic presence.",
        'meta_keywords': "global locations, office addresses, contact us, USA, Canada, UK, Australia, India, ValueConnectSolution locations, international presence",
        'og_title': "Our Locations - ValueConnectSolution",
        'og_description': "Discover ValueConnectSolution's strategic global presence to serve clients worldwide.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'website',
        'og_image': 'myapp/images/locations-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "Our Locations - ValueConnectSolution",
        'twitter_description': "Connect with us across our international offices for seamless service delivery.",
        'twitter_image': 'myapp/images/locations-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
    }
    return render(request, 'myapp/locations.html', context)

def faqs(request):
    context = {
        'title': "FAQs - ValueConnectSolution Services",
        'meta_description': "Find answers to frequently asked questions about ValueConnectSolution's BPO and customer experience services, pricing, and operational models for global clients.",
        'meta_keywords': "FAQs, frequently asked questions, ValueConnectSolution FAQs, outsourcing questions, BPO services, client queries, support, USA, Canada, UK, Australia, India",
        'og_title': "FAQs - ValueConnectSolution",
        'og_description': "Get quick answers to common questions about ValueConnectSolution and our services.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'website',
        'og_image': 'myapp/images/faqs-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "FAQs - ValueConnectSolution",
        'twitter_description': "Your go-to resource for information on our BPO solutions and client support.",
        'twitter_image': 'myapp/images/faqs-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
    }
    return render(request, 'myapp/faqs.html', context)


def form_processing(request):
    context = {
        'title': "Form Processing Services - Data Management",
        'meta_description': "ValueConnectSolution offers efficient form processing services, converting paper and digital forms into actionable data for businesses worldwide.",
        'meta_keywords': "form processing, data processing, digital forms, paper forms, data conversion, document management, global form processing, USA, Canada, UK, Australia, India",
        'og_title': "Form Processing - ValueConnectSolution",
        'og_description': "Streamline your data capture and management with our expert form processing services.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'service',
        'og_image': 'myapp/images/form-processing-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "Form Processing - ValueConnectSolution",
        'twitter_description': "Efficiently convert various forms into structured data for informed decision-making.",
        'twitter_image': 'myapp/images/form-processing-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
    }
    return render(request, 'myapp/form_processing.html', context)


@csrf_exempt
@require_POST
def contact_form_submit(request):
    try:
        data = json.loads(request.body)
        
        form = ContactForm(data)
        
        if form.is_valid():
            # Send email instead of saving to database
            email_sent = form.send_email()
            
            if email_sent:
                return JsonResponse({
                    'success': True,
                    'message': 'Thank you! Your message has been sent successfully. We\'ll get back to you soon.'
                })
            else:
                return JsonResponse({
                    'success': False,
                    'message': 'Your form was valid but we couldn\'t send the email. Please try again later.'
                }, status=500)
        else:
            errors = {field: error[0] for field, error in form.errors.items()}
            return JsonResponse({
                'success': False,
                'errors': errors
            }, status=400)
            
    except json.JSONDecodeError as e:
        return JsonResponse({
            'success': False,
            'message': 'Invalid JSON data received.'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'An error occurred: {str(e)}'
        }, status=500)

# --- Industry Experience Overview ---
def industry_experience(request):
    """
    View for the main Industry Experience landing page.
    This page should ideally provide an overview of all industries served
    by The Value Connect Solutions.
    """
    context = {
        'title': 'Industry Expertise & Services | ValueConnectSolution',
        'meta_description': 'Explore how ValueConnectSolution delivers specialized services across diverse industries, from retail to financial services, education, and beyond. Discover our industry-specific support for USA, Canada, UK, Australia, and India.',
        'meta_keywords': 'industry expertise, industry solutions, specialized services, vertical markets, BPO by industry, global industries, USA, Canada, UK, Australia, India',
        'og_title': 'Industry Expertise - ValueConnectSolution',
        'og_description': 'Discover our specialized services tailored for various industries, driving growth and efficiency.',
        'og_url': request.build_absolute_uri(),
        'og_type': 'website',
        'og_image': 'myapp/images/industry-experience-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': 'Industry Expertise - ValueConnectSolution',
        'twitter_description': 'See how our tailored solutions empower businesses across diverse sectors globally.',
        'twitter_image': 'myapp/images/industry-experience-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
        'hero_title': 'Specialized Industry Services by ValueConnectSolution',
        'hero_description': 'At ValueConnectSolution, we empower businesses across a wide range of sectors with expert services, driving efficiency, enhancing customer satisfaction, and fostering growth through tailored support.'
        # You might want to add a list of industries here for display on the main page.
    }
    return render(request, 'myapp/industry_experience.html', context)

# --- Individual Industry Pages ---

def in_we_serve_retail_ecommerce(request):
    """View for Retail and E-Commerce industry page"""
    context = {
        'title': 'Retail & E-Commerce Services | ValueConnectSolution',
        'meta_description': 'Optimize your retail and e-commerce operations with comprehensive services from ValueConnectSolution, including omnichannel customer support, order management, and inventory solutions for global markets.',
        'meta_keywords': 'retail outsourcing, e-commerce support, omnichannel customer service, order management, inventory solutions, retail BPO, global retail, USA, Canada, UK, Australia, India',
        'og_title': 'Retail & E-Commerce - ValueConnectSolution',
        'og_description': 'Tailored support for retail and e-commerce businesses to optimize operations and customer experience.',
        'og_url': request.build_absolute_uri(),
        'og_type': 'service',
        'og_image': 'myapp/images/retail-ecommerce-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': 'Retail & E-Commerce - ValueConnectSolution',
        'twitter_description': 'Enhance your online and offline retail presence with our comprehensive support services.',
        'twitter_image': 'myapp/images/retail-ecommerce-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
        'industry_name': 'Retail & E-Commerce',
        'hero_description': 'ValueConnectSolution delivers tailored omnichannel customer support, efficient order management, precise inventory services, and effective retention strategies for both digital and traditional retailers.',
        'services': [
            'Omnichannel Customer Support & Live Chat',
            'E-commerce Order Processing & Management',
            'Retail Inventory Management Support',
            'E-commerce Returns & Refunds Processing',
            'Product Catalog Management Services',
            'Customer Retention Programs for Retailers',
            'Multi-channel Customer Support (Email, Phone, Social)',
            'Sales Analytics & Performance Reporting'
        ],
        'benefits': [
            'Increased customer satisfaction and loyalty in retail',
            'Reduced operational costs for e-commerce businesses',
            '24/7 retail customer support availability',
            'Improved order accuracy and fulfillment rates',
            'Enhanced customer experience across all retail channels'
        ]
    }
    return render(request, 'myapp/in_we_serve_retail_ecommerce.html', context)

def in_we_serve_education(request):
    """View for Education industry page"""
    context = {
        'title': 'Education Sector Services | ValueConnectSolution',
        'meta_description': 'Streamline educational processes with ValueConnectSolution\'s services for student support, enrollment, course management, and alumni relations in academia, serving global institutions.',
        'meta_keywords': 'education outsourcing, student support, enrollment services, academic support, edtech support, alumni relations, global education, USA, Canada, UK, Australia, India',
        'og_title': 'Education Sector Services - ValueConnectSolution',
        'og_description': 'Comprehensive support services for educational institutions and edtech companies.',
        'og_url': request.build_absolute_uri(),
        'og_type': 'service',
        'og_image': 'myapp/images/education-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': 'Education Sector Services - ValueConnectSolution',
        'twitter_description': 'Streamline operations and enhance student experiences with our tailored solutions for education.',
        'twitter_image': 'myapp/images/education-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
        'industry_name': 'Education',
        'hero_description': 'ValueConnectSolution provides comprehensive support for educational institutions and edtech companies, covering student support, enrollment services, course management, and alumni relations.',
        'services': [
            'Student Enrollment & Admissions Support',
            'Academic Support Services & Helpdesks',
            'Course Registration Assistance',
            'Alumni Relations & Engagement Management',
            'Student Information System (SIS) Support',
            'Online Learning Platform Technical Support',
            'Financial Aid Application Processing',
            'Parent-Teacher Communication Facilitation'
        ],
        'benefits': [
            'Improved student retention rates for educational institutions',
            'Streamlined and efficient enrollment processes',
            'Enhanced overall student experience',
            'Reduced administrative burden for educators',
            'Better engagement with parents and students'
        ]
    }
    return render(request, 'myapp/in_we_serve_education.html', context)

def in_we_serve_marketing_services(request):
    """View for Marketing Services industry page"""
    context = {
        'title': 'Marketing Services Support | ValueConnectSolution',
        'meta_description': 'Boost your marketing efforts with ValueConnectSolution\'s expert support, including lead generation, campaign management, and digital marketing assistance for agencies and brands worldwide.',
        'meta_keywords': 'marketing outsourcing, lead generation, campaign management, digital marketing support, market research, social media management, global marketing, USA, Canada, UK, Australia, India',
        'og_title': 'Marketing Services Support - ValueConnectSolution',
        'og_description': 'Expert support to enhance your marketing campaigns, lead generation, and brand visibility.',
        'og_url': request.build_absolute_uri(),
        'og_type': 'service',
        'og_image': 'myapp/images/marketing-services-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': 'Marketing Services Support - ValueConnectSolution',
        'twitter_description': 'Drive better ROI and efficiency for your marketing efforts with our specialized assistance.',
        'twitter_image': 'myapp/images/marketing-services-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
        'industry_name': 'Marketing Services',
        'hero_description': 'ValueConnectSolution offers essential support for marketing agencies and brands, specializing in lead generation, comprehensive campaign management, in-depth customer research, and robust digital marketing assistance.',
        'services': [
            'Lead Generation & Qualification Services',
            'Marketing Campaign Management & Execution',
            'Market Research & Data Analysis',
            'Social Media Management & Engagement',
            'Email Marketing Campaign Support',
            'Content Creation & Curation Assistance',
            'SEO & Digital Marketing Support',
            'Customer Database Management & CRM'
        ],
        'benefits': [
            'Higher quality leads and increased conversion rates',
            'Reduced marketing operational costs',
            'Improved marketing campaign Return on Investment (ROI)',
            'Enhanced brand visibility and online presence',
            'Better customer targeting and segmentation strategies'
        ]
    }
    return render(request, 'myapp/in_we_serve_marketing_services.html', context)

def in_we_serve_financial_services(request):
    """View for Financial Services industry page"""
    context = {
        'title': 'Financial Services Support | ValueConnectSolution',
        'meta_description': 'Get secure and compliant support for banking, investment, and fintech from ValueConnectSolution, covering claims processing, KYC, and customer onboarding for global financial institutions.',
        'meta_keywords': 'financial services BPO, banking support, fintech solutions, investment support, claims processing, KYC, customer onboarding, regulatory compliance, global finance, USA, Canada, UK, Australia, India',
        'og_title': 'Financial Services Support - ValueConnectSolution',
        'og_description': 'Secure and compliant support for banking, investment, and fintech operations.',
        'og_url': request.build_absolute_uri(),
        'og_type': 'service',
        'og_image': 'myapp/images/financial-services-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': 'Financial Services Support - ValueConnectSolution',
        'twitter_description': 'Enhance efficiency and compliance in your financial operations with our expert assistance.',
        'twitter_image': 'myapp/images/financial-services-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
        'industry_name': 'Financial Services',
        'hero_description': 'ValueConnectSolution provides secure, compliant support for banking, investment, and fintech companies, encompassing efficient claims processing, customer onboarding, and robust financial operations.',
        'services': [
            'Customer Onboarding & KYC (Know Your Customer)',
            'Financial Claims Processing',
            'Account Management & Support',
            'Fraud Detection & Prevention Support',
            'Loan Processing & Servicing Assistance',
            'Investment Support Services',
            'Regulatory Compliance Support for Finance',
            'Financial Document Processing & Management'
        ],
        'benefits': [
            'Enhanced security and regulatory compliance in finance',
            'Faster processing times for financial transactions',
            'Reduced operational risks in financial services',
            'Improved customer trust and satisfaction',
            'Cost-effective scaling of financial operations'
        ]
    }
    return render(request, 'myapp/in_we_serve_financial_services.html', context)

def in_we_serve_telecommunications(request):
    """View for Telecommunications industry page"""
    context = {
        'title': 'Telecommunications Industry Services | ValueConnectSolution',
        'meta_description': 'Leading telecommunications service and support from ValueConnectSolution. We offer customer care, technical troubleshooting, billing support, and sales assistance for telecom providers globally.',
        'meta_keywords': 'telecom outsourcing, telecommunications support, customer care telecom, technical troubleshooting, billing support, telecom sales, global telecom, USA, Canada, UK, Australia, India',
        'og_title': 'Telecommunications Services - ValueConnectSolution',
        'og_description': 'Comprehensive customer care and technical support for the telecommunications industry.',
        'og_url': request.build_absolute_uri(),
        'og_type': 'service',
        'og_image': 'myapp/images/telecommunications-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': 'Telecommunications Services - ValueConnectSolution',
        'twitter_description': 'Ensure seamless operations and enhanced customer satisfaction for your telecom business.',
        'twitter_image': 'myapp/images/telecommunications-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
        'industry_name': 'Telecommunications',
        'hero_description': 'ValueConnectSolution delivers comprehensive customer care, technical troubleshooting, billing support, and sales assistance specifically for telecom providers and equipment manufacturers.',
        'services': [
            'Telecommunications Customer Care & Support',
            'Technical Troubleshooting for Telecom Networks',
            'Billing & Payment Support',
            'Telecom Sales & Upselling Services',
            'Network Issue Resolution Assistance',
            'Equipment Installation Support',
            'Service Activation & Deactivation',
            'Customer Retention Programs for Telecom'
        ],
        'benefits': [
            'Reduced customer churn in telecommunications',
            'Improved service quality and network reliability',
            'Faster issue resolution for telecom customers',
            'Increased customer satisfaction for telecom providers',
            '24/7 technical support availability for telecommunications'
        ]
    }
    return render(request, 'myapp/in_we_serve_telecommunications.html', context)

def in_we_serve_real_estate(request):
    """View for Real Estate industry page"""
    context = {
        'title': 'Real Estate Industry Support | ValueConnectSolution',
        'meta_description': 'Empower your real estate business with ValueConnectSolution\'s support for lead qualification, property management, client communication, and transaction coordination globally.',
        'meta_keywords': 'real estate outsourcing, lead qualification, property management support, client communication, transaction coordination, real estate BPO, global real estate, USA, Canada, UK, Australia, India',
        'og_title': 'Real Estate Industry Support - ValueConnectSolution',
        'og_description': 'Specialized support services to enhance efficiency and growth in the real estate sector.',
        'og_url': request.build_absolute_uri(),
        'og_type': 'service',
        'og_image': 'myapp/images/real-estate-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': 'Real Estate Industry Support - ValueConnectSolution',
        'twitter_description': 'Streamline operations from lead nurturing to transaction closing for real estate businesses.',
        'twitter_image': 'myapp/images/real-estate-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
        'industry_name': 'Real Estate',
        'hero_description': 'ValueConnectSolution provides specialized support for real estate professionals, including efficient lead qualification, comprehensive property management assistance, seamless client communication, and precise transaction coordination.',
        'services': [
            'Real Estate Lead Qualification & Nurturing',
            'Property Management Support Services',
            'Client Communication Management',
            'Transaction Coordination Assistance',
            'Appointment Scheduling for Real Estate Agents',
            'Real Estate Market Research & Analysis',
            'Document Management for Property Listings',
            'CRM Management for Real Estate'
        ],
        'benefits': [
            'Higher conversion rates for real estate leads',
            'Improved client relationships and trust',
            'Streamlined real estate transaction processes',
            'Better lead management and follow-up',
            'Increased agent productivity and focus'
        ]
    }
    return render(request, 'myapp/in_we_serve_real_estate.html', context)

def in_we_serve_media_communications(request):
    """View for Media and Communications industry page"""
    context = {
        'title': 'Media & Communications Support | ValueConnectSolution',
        'meta_description': 'Enhance your media and communications operations with ValueConnectSolution, offering content moderation, audience engagement, social media management, and customer service globally.',
        'meta_keywords': 'media outsourcing, communications support, content moderation, audience engagement, social media management, media customer service, global media, USA, Canada, UK, Australia, India',
        'og_title': 'Media & Communications - ValueConnectSolution',
        'og_description': 'Comprehensive support for media and communications companies, fostering engagement and content quality.',
        'og_url': request.build_absolute_uri(),
        'og_type': 'service',
        'og_image': 'myapp/images/media-communications-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': 'Media & Communications - ValueConnectSolution',
        'twitter_description': 'Safeguard your brand and engage your audience effectively with our specialized media services.',
        'twitter_image': 'myapp/images/media-communications-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
        'industry_name': 'Media & Communications',
        'hero_description': 'ValueConnectSolution provides essential support for media and entertainment companies, focusing on content moderation, audience engagement, strategic social media management, and dedicated customer service.',
        'services': [
            'Content Moderation Services',
            'Social Media Management for Media',
            'Audience Engagement Strategies',
            'Customer Service for Media Companies',
            'Content Creation Support & Curation',
            'Community Management & Moderation',
            'Brand Monitoring & Reputation Management',
            'Digital Asset Management Services'
        ],
        'benefits': [
            'Enhanced brand reputation in media',
            'Improved audience engagement and loyalty',
            'Consistent content quality and brand voice',
            'Better crisis management and public relations',
            'Increased social media presence and impact'
        ]
    }
    return render(request, 'myapp/in_we_serve_media_communications.html', context)

def in_we_serve_website_design_development(request):
    """View for Website Design and Development Services industry page"""
    context = {
        'title': 'Website Design & Dev Support | ValueConnectSolution',
        'meta_description': 'Expert support for website design and development agencies from ValueConnectSolution, including technical assistance, client communication, project management, and quality assurance globally.',
        'meta_keywords': 'website design support, web development support, technical assistance web, client communication web, project management web, quality assurance web, global web development, USA, Canada, UK, Australia, India',
        'og_title': 'Website Design & Development - ValueConnectSolution',
        'og_description': 'Comprehensive support for web design and development agencies, ensuring project success and client satisfaction.',
        'og_url': request.build_absolute_uri(),
        'og_type': 'service',
        'og_image': 'myapp/images/website-design-dev-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': 'Website Design & Development - ValueConnectSolution',
        'twitter_description': 'Streamline your web projects with our expert assistance in every phase, from development to QA.',
        'twitter_image': 'myapp/images/website-design-dev-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
        'industry_name': 'Website Design and Development Services',
        'hero_description': 'ValueConnectSolution offers comprehensive support for web development agencies and freelancers, including technical assistance, streamlined client communication, efficient project management, and rigorous quality assurance.',
        'services': [
            'Technical Support for Web Projects',
            'Client Communication & Relationship Management',
            'Project Management for Web Development',
            'Quality Assurance & Website Testing',
            'Website Maintenance & Updates',
            'Content Management for Websites',
            'SEO Optimization Support for Web Developers',
            'Website Performance Monitoring'
        ],
        'benefits': [
            'Improved project delivery times for web agencies',
            'Better client satisfaction and retention',
            'Reduced technical issues and bugs',
            'Enhanced website performance and user experience',
            'Streamlined development processes and workflows'
        ]
    }
    return render(request, 'myapp/in_we_serve_website_design_development.html', context)

def in_we_serve_insurance(request):
    """View for Insurance industry page"""
    context = {
        'title': 'Insurance Industry Support | ValueConnectSolution',
        'meta_description': 'Comprehensive insurance industry support from ValueConnectSolution, covering claims processing, policy management, customer service, and underwriting assistance for global insurance companies and brokers.',
        'meta_keywords': 'insurance outsourcing, claims processing, policy management, insurance customer service, underwriting support, risk assessment, premium collection, global insurance, USA, Canada, UK, Australia, India',
        'og_title': 'Insurance Industry Support - ValueConnectSolution',
        'og_description': 'Expert support for the insurance sector, enhancing efficiency in claims, policy, and customer service.',
        'og_url': request.build_absolute_uri(),
        'og_type': 'service',
        'og_image': 'myapp/images/insurance-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': 'Insurance Industry Support - ValueConnectSolution',
        'twitter_description': 'Streamline your insurance operations with our compliant and secure back-office and customer support.',
        'twitter_image': 'myapp/images/insurance-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
        'industry_name': 'Insurance',
        'hero_description': 'ValueConnectSolution provides expert support for insurance companies and brokers, including efficient claims processing, robust policy management, dedicated customer service, and precise underwriting assistance.',
        'services': [
            'Insurance Claims Processing',
            'Policy Management & Administration',
            'Insurance Customer Service',
            'Underwriting Support Services',
            'Risk Assessment & Analysis',
            'Premium Collection Services',
            'Fraud Investigation Support for Insurance',
            'Compliance Management for Insurance Sector'
        ],
        'benefits': [
            'Faster claims processing and resolution',
            'Improved customer satisfaction in insurance',
            'Reduced operational costs for insurers',
            'Enhanced compliance with insurance regulations',
            'Better risk management strategies'
        ]
    }
    return render(request, 'myapp/in_we_serve_insurance.html', context)


#why_vcs
def why_vcs(request):
    context = {
        'title': "Why Choose ValueConnectSolution? | Advantages",
        'meta_description': "Discover why ValueConnectSolution is your ideal partner for BPO and customer experience. Learn about our unique advantages, commitment to quality, and global service delivery for clients in USA, Canada, UK, Australia, and India.",
        'meta_keywords': "why choose us, ValueConnectSolution advantages, outsourcing benefits, quality BPO, customer experience partner, global solutions, USA, Canada, UK, Australia, India",
        'og_title': "Why ValueConnectSolution - Your Global BPO Partner",
        'og_description': "Explore the compelling reasons to choose ValueConnectSolution for your business's growth and efficiency.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'website',
        'og_image': 'myapp/images/why-vcs-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "Why ValueConnectSolution - Global BPO",
        'twitter_description': "Understand our commitment to delivering unparalleled value and results for your business.",
        'twitter_image': 'myapp/images/why-vcs-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
    }
    return render(request, 'myapp/why_vcs.html', context)

def Value_Pillars(request):
    context = {
        'title': "Our Value Pillars - Guiding Principles",
        'meta_description': "Learn about the core value pillars that define ValueConnectSolution's operations and commitment to client success, including innovation, integrity, and excellence in global service delivery.",
        'meta_keywords': "value pillars, core values, company principles, innovation, integrity, excellence, client focus, global service, USA, Canada, UK, Australia, India",
        'og_title': "Our Value Pillars - ValueConnectSolution",
        'og_description': "Discover the foundational principles that drive ValueConnectSolution's operations and success.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'website',
        'og_image': 'myapp/images/value-pillars-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "Our Value Pillars - ValueConnectSolution",
        'twitter_description': "Understand the commitment to quality, innovation, and integrity that defines our services.",
        'twitter_image': 'myapp/images/value-pillars-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
    }
    return render(request, 'myapp/Value_Pillars.html', context)

def Reasons_to_Outsource(request):
    context = {
        'title': "Reasons to Outsource - Benefits of BPO",
        'meta_description': "Explore the compelling reasons to outsource your business processes with ValueConnectSolution, including cost savings, efficiency gains, and access to specialized expertise for global competitiveness.",
        'meta_keywords': "reasons to outsource, outsourcing benefits, cost savings, operational efficiency, specialized expertise, BPO advantages, global competitiveness, USA, Canada, UK, Australia, India",
        'og_title': "Reasons to Outsource - ValueConnectSolution",
        'og_description': "Understand the strategic advantages of outsourcing your business processes with ValueConnectSolution.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'website',
        'og_image': 'myapp/images/reasons-outsource-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "Reasons to Outsource - ValueConnectSolution",
        'twitter_description': "Unlock growth, reduce costs, and enhance efficiency by leveraging our outsourcing expertise.",
        'twitter_image': 'myapp/images/reasons-outsource-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
    }
    return render(request, 'myapp/Reasons_to_Outsource.html', context)

def Processes(request):
    context = {
        'title': "Our Processes - BPO Service Delivery",
        'meta_description': "Learn about ValueConnectSolution's robust processes for BPO service delivery, from client onboarding to continuous improvement, ensuring seamless and efficient operations for global businesses.",
        'meta_keywords': "BPO processes, service delivery model, operational framework, client onboarding, quality control, continuous improvement, outsourcing process, global operations, USA, Canada, UK, Australia, India",
        'og_title': "Our Processes - ValueConnectSolution",
        'og_description': "Explore the structured processes that ensure high-quality and efficient service delivery at ValueConnectSolution.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'website',
        'og_image': 'myapp/images/processes-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "Our Processes - ValueConnectSolution",
        'twitter_description': "Understand how our systematic approach leads to consistent excellence in BPO services.",
        'twitter_image': 'myapp/images/processes-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
    }
    return render(request, 'myapp/Processes.html', context)

def Security_Standards(request):
    context = {
        'title': "Security Standards - Data Protection",
        'meta_description': "ValueConnectSolution adheres to stringent security standards and data protection protocols, ensuring the confidentiality and integrity of your information in all global operations.",
        'meta_keywords': "security standards, data protection, data privacy, ISO compliance, GDPR, HIPAA compliance, information security, cybersecurity, global security, USA, Canada, UK, Australia, India",
        'og_title': "Security Standards - ValueConnectSolution",
        'og_description': "Our commitment to top-tier security standards ensures the protection of your sensitive data.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'website',
        'og_image': 'myapp/images/security-standards-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "Security Standards - ValueConnectSolution",
        'twitter_description': "Learn about our robust security measures and compliance for absolute data integrity.",
        'twitter_image': 'myapp/images/security-standards-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
    }
    return render(request, 'myapp/Security_Standards.html', context)

#process

def training_view(request):
    context = {
        'title': "Training & Development - Our Workforce",
        'meta_description': "ValueConnectSolution's comprehensive training and development programs ensure our workforce is skilled, up-to-date, and capable of delivering exceptional global BPO services.",
        'meta_keywords': "employee training, staff development, workforce training, skills enhancement, continuous learning, BPO training, global workforce, USA, Canada, UK, Australia, India",
        'og_title': "Training & Development - ValueConnectSolution",
        'og_description': "Discover how our rigorous training programs cultivate top-tier talent for global service delivery.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'website',
        'og_image': 'myapp/images/training-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "Training & Development - ValueConnectSolution",
        'twitter_description': "Our commitment to continuous learning ensures skilled and adaptable teams for your business.",
        'twitter_image': 'myapp/images/training-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
    }
    return render(request, 'myapp/training.html', context)

def quality_assurance_view(request):
    context = {
        'title': "Quality Assurance - Service Excellence",
        'meta_description': "ValueConnectSolution's stringent quality assurance processes guarantee high standards of service delivery and consistent excellence across all BPO operations for global clients.",
        'meta_keywords': "quality assurance, QA, service quality, quality control, performance monitoring, excellence in BPO, continuous improvement, global quality, USA, Canada, UK, Australia, India",
        'og_title': "Quality Assurance - ValueConnectSolution",
        'og_description': "Our rigorous quality assurance framework ensures consistent excellence in every service we deliver.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'website',
        'og_image': 'myapp/images/quality-assurance-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "Quality Assurance - ValueConnectSolution",
        'twitter_description': "Committed to delivering unparalleled service quality through robust QA processes.",
        'twitter_image': 'myapp/images/quality-assurance-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
    }
    return render(request, 'myapp/quality_assurance.html', context)

def recruiting_staffing_view(request):
    context = {
        'title': "Recruiting & Staffing - Talent Acquisition",
        'meta_description': "ValueConnectSolution's expert recruiting and staffing services ensure you get the right talent for your business needs, from agents to specialized professionals, serving global markets.",
        'meta_keywords': "recruiting, staffing, talent acquisition, workforce solutions, hiring services, BPO recruitment, global talent, USA, Canada, UK, Australia, India",
        'og_title': "Recruiting & Staffing - ValueConnectSolution",
        'og_description': "Access top-tier talent for your business needs through our specialized recruiting and staffing solutions.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'website',
        'og_image': 'myapp/images/recruiting-staffing-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "Recruiting & Staffing - ValueConnectSolution",
        'twitter_description': "Build high-performing teams with our strategic talent acquisition and workforce solutions.",
        'twitter_image': 'myapp/images/recruiting-staffing-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
    }
    return render(request, 'myapp/recruiting_and_staffing.html', context)

def implementation_view(request):
    context = {
        'title': "Implementation Process - Smooth Rollout",
        'meta_description': "ValueConnectSolution ensures a smooth and efficient implementation process for all our BPO services, minimizing disruption and maximizing value for global clients.",
        'meta_keywords': "implementation process, service rollout, project implementation, BPO setup, transition management, seamless integration, global implementation, USA, Canada, UK, Australia, India",
        'og_title': "Implementation Process - ValueConnectSolution",
        'og_description': "Our streamlined implementation process ensures a smooth and efficient transition for all services.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'website',
        'og_image': 'myapp/images/implementation-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "Implementation Process - ValueConnectSolution",
        'twitter_description': "Experience a hassle-free start with our expert project implementation and management.",
        'twitter_image': 'myapp/images/implementation-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
    }
    return render(request, 'myapp/implementation.html', context)

def client_services_view(request):
    context = {
        'title': "Client Services - Dedicated Support",
        'meta_description': "ValueConnectSolution offers dedicated client services and support, ensuring strong partnerships and continuous satisfaction for our global clientele.",
        'meta_keywords': "client services, client support, dedicated account manager, partnership, customer satisfaction, relationship management, global client services, USA, Canada, UK, Australia, India",
        'og_title': "Client Services - ValueConnectSolution",
        'og_description': "Dedicated client services designed to foster strong partnerships and ensure your continued success.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'website',
        'og_image': 'myapp/images/client-services-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "Client Services - ValueConnectSolution",
        'twitter_description': "Experience unparalleled support and proactive engagement from our client service team.",
        'twitter_image': 'myapp/images/client-services-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
    }
    return render(request, 'myapp/client_services.html', context)

def contact_us(request):
    context = {
        'title': "Contact Us - Get in Touch with ValueConnectSolution",
        'meta_description': "Reach out to ValueConnectSolution for business inquiries, service details, or partnership opportunities. Contact our global team in USA, Canada, UK, Australia, and India.",
        'meta_keywords': "contact us, ValueConnectSolution contact, business inquiry, get in touch, phone number, email, global contact, USA, Canada, UK, Australia, India",
        'og_title': "Contact Us - ValueConnectSolution",
        'og_description': "Connect with ValueConnectSolution's team for inquiries, support, or partnership opportunities.",
        'og_url': request.build_absolute_uri(),
        'og_type': 'contact.business', # Specific Open Graph type
        'og_image': 'myapp/images/contact-us-og.jpg',
        'og_site_name': "ValueConnectSolution",
        'twitter_card': 'summary_large_image',
        'twitter_title': "Contact Us - ValueConnectSolution",
        'twitter_description': "We're here to help! Reach out to our global team for expert business solutions.",
        'twitter_image': 'myapp/images/contact-us-twitter.jpg',
        'favicon': 'myapp/images/favicon.png',
    }
    return render(request, 'myapp/contact_us.html', context)

def robots_txt(request):
    content = (
        "User-agent: *\n"
        "Disallow: /admin/\n"
        "Allow: /\n"
        "Sitemap: https://valueconnectsolutions.org/sitemap.xml"
    )
    return HttpResponse(content, content_type="text/plain")
from django.contrib import admin
from .models import login_table
from .models import state
from .models import city
from .models import area_table
from .models import detail_table
from .models import service
from .models import booking_service
from .models import feedback
from .models import service_category

# Register your models here.



class LOGIN(admin.ModelAdmin):
    list_display=[ "name","email","phone","password","admin_photos","role"]
admin.site.register(login_table,LOGIN)

class STATE(admin.ModelAdmin):
    list_display=["state_name"]
admin.site.register(state,STATE)

class CITY(admin.ModelAdmin):
    list_display=["city_name","state_id"]
admin.site.register(city,CITY)

class AREA_table(admin.ModelAdmin):
    list_display=["city_id","state_id","area_name"]
admin.site.register(area_table,AREA_table)

class DETAIL_Table(admin.ModelAdmin):
    list_display=["l_id","adphoto","name","dob","address","city_id","state_id"]
admin.site.register(detail_table,DETAIL_Table)

class Service_Category(admin.ModelAdmin):
    list_display = ["service_category_name","service_photos"]
admin.site.register(service_category,Service_Category)

class Service(admin.ModelAdmin):
    list_display=["l_id","service_image","service_name","service_id","service_description","service_price"]
admin.site.register(service,Service)

class Feedback(admin.ModelAdmin):
    list_display=["name","email","comment", 'rating', 'timestamp']
admin.site.register(feedback,Feedback)


from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

def export_to_pdf(modeladmin, request, queryset):
   # Create a new PDF
   response = HttpResponse(content_type='application/pdf')
   response['Content-Disposition'] = 'attachment; filename="report.pdf"'

   # Generate the report using ReportLab
   doc = SimpleDocTemplate(response, pagesize=letter)

   elements = []

   # Define the style for the table
   style = TableStyle([
       ('BACKGROUND', (0,0), (-1,0), colors.grey),
       ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
       ('ALIGN', (0,0), (-1,-1), 'CENTER'),
       ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
       ('FONTSIZE', (0,0), (-1,0), 14),
       ('BOTTOMPADDING', (0,0), (-1,0), 12),
       ('BACKGROUND', (0,1), (-1,-1), colors.beige),
       ('GRID', (0,0), (-1,-1), 1, colors.black),
   ])

   # Create the table headers
   headers = ['Service Person', 'User', 'Date','Time', "Status", "Payment Method"]

   # Create the table data
   data = []
   for obj in queryset:
       data.append([obj.serviceperson, obj.l_id.name, obj.sdate,obj.time, obj.ubr_status , obj.paymethod])

   # Create the table
   t = Table([headers] + data, style=style)

   # Add the table to the elements array
   elements.append(t)

   # Build the PDF document
   doc.build(elements)

   return response

export_to_pdf.short_description = "Export to PDF"


class Booking_Service(admin.ModelAdmin):
    list_display=["serviceperson","l_id","address","date","time","ubr_status","show_approve_button","rejected"]
    actions = [export_to_pdf]


admin.site.register(booking_service,Booking_Service)


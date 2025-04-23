from django.db import models
from django.utils.safestring import mark_safe


def upload_to_profile(instance, filename):
    return f'profile/{filename}'

# Create your models here.
class login_table(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.IntegerField()
    password = models.CharField(max_length=10)
    dp =models.ImageField(upload_to="photos")
    ROLE = (
        ("provider","provider"),
        ("user","user")
    )
    role= models.CharField(max_length=10,choices=ROLE)



    def admin_photos(self):
        return mark_safe ('<img src="{}" width="100"/>'.format(self.dp.url))
    admin_photos.allow_tags = True

    def __str__(self):
        return self.name


class state(models.Model):
     state_name=models.CharField(max_length=25)


     def __str__(self) :
        return self.state_name



class city(models.Model):
    city_name=models.CharField(max_length=25)
    state_id =models.ForeignKey(state,on_delete=models.CASCADE)

    def __str__(self) :
        return self.city_name
    

class area_table(models.Model):
    city_id=models.ForeignKey(city,on_delete=models.CASCADE)
    state_id =models.ForeignKey(state, on_delete=models.CASCADE)
    area_name=models.CharField(max_length=25)

    def __str__(self) :
        return self.area_name

    
class detail_table(models.Model):
    l_id =models.ForeignKey(login_table,on_delete=models.CASCADE)
    name =models.CharField(max_length=25)
    dob=models.DateField()
    address=models.TextField()
    area_id =models.ForeignKey(area_table,on_delete=models.CASCADE,null=True)
    city_id=models.ForeignKey(city,on_delete=models.CASCADE,null=True)
    state_id= models.ForeignKey(state,on_delete=models.CASCADE,null=True)
    provideraadhaar = models.ImageField(upload_to="photos",null=True)

    def adphoto(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.provideraadhaar.url))

    adphoto.allow_tags = True

    def __str__(self) :
        return self.name

class  service_category(models.Model):
    service_category_name=models.CharField(max_length=25)
    service_category_photo=models.ImageField(default='pl.jpg')

    def service_photos(self):
        
        return mark_safe ('<img src="{}" width="100"/>'.format(self.service_category_photo.url))
    service_photos.allow_tags = True

    def __str__(self):
        return self.service_category_name

class service(models.Model):
    l_id =models.ForeignKey(login_table,on_delete=models.CASCADE)
    service_id =models.ForeignKey(service_category,on_delete=models.CASCADE, default="")
    service_name=models.CharField(max_length=200)
    service_description=models.TextField()
    service_price=models.IntegerField()
    service_photo = models.ImageField(default="null", upload_to=upload_to_profile)

    def service_image(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.service_photo.url))

    def __str__(self) :
        return self.service_name

class booking_service(models.Model):
    serviceperson=models.ForeignKey(service, on_delete=models.CASCADE)
    l_id=models.ForeignKey(login_table,on_delete=models.CASCADE)
    address=models.TextField()
    STATUS = (
        ("Waiting for Confirmation", "Waiting for Confirmation"),
        ("Confirmed", "Confirmed"),
        ("Rejected", "Rejected")
    )

    ubr_status = models.CharField(max_length=50, choices=STATUS, default="Waiting for Confirmation")
    paymethod = models.CharField(max_length=50, choices=(("online", "Online"),("cash", "Offline")))
    phone = models.IntegerField(null=True)
    sdate = models.DateField(null=True)
    date=models.DateField(auto_now=True,editable=False)
    time=models.TimeField(auto_now=True,editable=False)
    show_approve_button = models.BooleanField(default=True)
    rejected = models.BooleanField(default=False)
    razorpay_payment_id = models.CharField(max_length=100, null=True, blank=True)

class feedback(models.Model):
    name = models.CharField(max_length=20, default='')
    email = models.EmailField(default='')
    comment=models.TextField(default='')
    rating = models.IntegerField()
    contact = models.TextField()
    timestamp = models.DateField(auto_now=True)


    

    
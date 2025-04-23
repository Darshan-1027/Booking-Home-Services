from django.shortcuts import render, redirect , reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.

from .models import login_table
from .models import city
from .models import state
from .models import area_table
from .models import detail_table
from .models import service
from .models import service_category
from .models import booking_service
from .models import feedback

def index(request):
    servdata = service_category.objects.all()

    try:
        uid = request.session['log_id']
        logdetail = login_table.objects.get(id=uid)
        statedetail = state.objects.all()
        citydetail = city.objects.all()
        areadetail = area_table.objects.all()
        servdata = service_category.objects.all()

        try:
            profiledata = detail_table.objects.get(l_id=uid)
        except detail_table.DoesNotExist:
            profiledata = None



        Provider = False
        if logdetail.role == "provider":
            Provider = True
            print(Provider)
        details = {
            'logdetail': logdetail,
            'statedetail': statedetail,
            'citydetail': citydetail,
            'areadetail': areadetail,
            'profiledata': profiledata,
            'Provider': Provider,
            'servdata':servdata
        }
        return render(request, 'index.html', details)
    except:
        details = {
           
            'servdata':servdata
        }
    return render(request, 'index.html', details)

def basic(request):
    try:
        uid = request.session['log_id']
        logdetail = login_table.objects.get(id=uid)
        statedetail = state.objects.all()
        citydetail = city.objects.all()
        areadetail = area_table.objects.all()

        try:
            profiledata = detail_table.objects.get(l_id=uid)
        except detail_table.DoesNotExist:
            profiledata = None

        Provider = False
        if logdetail.role == "provider":
            Provider = True
            print(Provider)

        details = {
            'logdetail': logdetail,
            'statedetail': statedetail,
            'citydetail': citydetail,
            'areadetail': areadetail,
            'profiledata': profiledata,
            'Provider': Provider,

        }
        print("ASCASDSAD: ",details)
        return render(request, 'basic.html', details)
    except:
        pass
    return render(request, 'basic.html')

def about(request):
    try:
        uid = request.session['log_id']
        logdetail = login_table.objects.get(id=uid)
        statedetail = state.objects.all()
        citydetail = city.objects.all()
        areadetail = area_table.objects.all()


        try:
            profiledata = detail_table.objects.get(l_id=uid)
        except detail_table.DoesNotExist:
            profiledata = None



        Provider = False
        if logdetail.role == "provider":
            Provider = True
            print(Provider)

        details = {
            'logdetail': logdetail,
            'statedetail': statedetail,
            'citydetail': citydetail,
            'areadetail': areadetail,
            'profiledata': profiledata,
            'Provider': Provider,

        }
        return render(request, 'about.html', details)
    except:
        pass
    return render(request, 'about.html')

def completeprofile(request):
    try:
        uid = request.session['log_id']
        logdetail = login_table.objects.get(id=uid)
        statedetail = state.objects.all()
        citydetail = city.objects.all()
        areadetail = area_table.objects.all()

        try:
            profiledata = detail_table.objects.get(l_id=uid)
        except detail_table.DoesNotExist:
            profiledata = None

        Provider = False
        if logdetail.role == "provider":
            Provider = True
            print(Provider)
        from datetime import datetime
        today_date = datetime.today().strftime('%Y-%m-%d')
        print("fcnsdjbd\n",today_date)
        details = {
            'logdetail': logdetail,
            'statedetail': statedetail,
            'citydetail': citydetail,
            'areadetail': areadetail,
            'profiledata': profiledata,
            'Provider': Provider,
            'today_date': today_date,
        }
        return render(request, 'completeprofile.html', details)
    except:
        pass
    return render(request, 'completeprofile.html')

def contact(request):
    try:
        uid = request.session['log_id']
        logdetail = login_table.objects.get(id=uid)
        statedetail = state.objects.all()
        citydetail = city.objects.all()
        areadetail = area_table.objects.all()


        try:
            profiledata = detail_table.objects.get(l_id=uid)
        except detail_table.DoesNotExist:
            profiledata = None



        Provider = False
        if logdetail.role == "provider":
            Provider = True
            print(Provider)

        details = {
            'logdetail': logdetail,
            'statedetail': statedetail,
            'citydetail': citydetail,
            'areadetail': areadetail,
            'profiledata': profiledata,
            'Provider': Provider,

        }
        return render(request, 'contact.html', details)
    except:
        pass
    return render(request, 'contact.html')

def signin(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def viewdata(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        role = request.POST.get("usertype")
        file = request.FILES['dp']

        if login_table.objects.filter(email=email).exists():
            messages.error(request, "Account Exists")
            return redirect(index)

        logindata = login_table(name=name,email=email, phone=phone, password=password,
                                role=role, dp=file)
        logindata.save()

        messages.success(request, 'Data Inserted Successfully. you can login now')
        return redirect(index)
    else:
        messages.error(request, 'error occured')

    return redirect(index)

def checklogin(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        try:
            user = login_table.objects.get(email=username, password=password)
            request.session['log_user'] = user.email
            request.session['log_id'] = user.id
            request.session.save()

        except login_table.DoesNotExist:
            user = None

        if user is not None:
            print("successfully logged in")
            messages.success(request, 'Successfully Logged In')
            redirect(index)

        else:
            print("not logged in")
            messages.error(request, 'Invalid USER ID')
    return redirect(index)

def logout(request):
    try:
        del request.session['log_user']
        del request.session['log_id']
    except:
        pass
    return redirect(index)


from django.core.exceptions import ObjectDoesNotExist


def completeprofilesubmit(request):
    uid = request.session['log_id']
    if request.method == 'POST':
        uname = request.POST.get("name")
        uaddress = request.POST.get("address")
        udob = request.POST.get("dob")
        ucity = request.POST.get("cityname")
        ustate = request.POST.get("statename")
        adpic = request.FILES["ad"]

        if ucity.lower() != "ahmedabad":
            messages.error(request, 'Only Ahmedabad city is allowed.')
            return redirect('completeprofilesubmit')  # or your profile form page

        try:
            citydata = city.objects.get(city_name=ucity)
            statedata = state.objects.get(state_name=ustate)
        except ObjectDoesNotExist:
            messages.error(request, 'Invalid city or state entered.')
            return redirect(completeprofilesubmit)  # or your profile form page

        userdata = detail_table(
            l_id=login_table(id=uid),
            name=uname,
            dob=udob,
            address=uaddress,
            provideraadhaar=adpic,
            city_id=citydata,
            state_id=statedata
        )
        userdata.save()
        messages.success(request, 'Data Inserted Successfully.')
        return redirect(index)
    else:
        # messages.error(request, 'Error occurred.')
        return redirect(index)


def yourprofile(request):
    try:
        uid = request.session['log_id']
        logdetail = login_table.objects.get(id=uid)
        statedetail = state.objects.all()
        citydetail = city.objects.all()
        areadetail = area_table.objects.all()


        try:
            profiledata = detail_table.objects.get(l_id=uid)
        except detail_table.DoesNotExist:
            profiledata = None

        Provider = False
        if logdetail.role == "provider":
            Provider = True
            print(Provider)
            servdata = service.objects.filter(l_id=uid)


        details = {
            'logdetail': logdetail,
            'statedetail': statedetail,
            'citydetail': citydetail,
            'areadetail': areadetail,
            'profiledata': profiledata,
            'Provider': Provider,
            'servdata': servdata,

        }
        return render(request, 'myprofile.html', details)
    except:
        try:
            uid = request.session['log_id']
            logdetail = login_table.objects.get(id=uid)
            statedetail = state.objects.all()
            citydetail = city.objects.all()
            areadetail = area_table.objects.all()

            try:
                profiledata = detail_table.objects.get(l_id=uid)
            except detail_table.DoesNotExist:
                profiledata = None

            Provider = False
            if logdetail.role == "provider":
                Provider = True
                print(Provider)

            details = {
                'logdetail': logdetail,
                'statedetail': statedetail,
                'citydetail': citydetail,
                'areadetail': areadetail,
                'profiledata': profiledata,
                'Provider': Provider,

            }
            return render(request, 'myprofile.html', details)
        except:
            pass

def addservice(request):
    try:
        uid = request.session['log_id']
        logdetail = login_table.objects.get(id=uid)
        statedetail = state.objects.all()
        citydetail = city.objects.all()
        areadetail = area_table.objects.all()
        servicedetail = service_category.objects.all()


        try:
            profiledata = detail_table.objects.get(l_id=uid)
        except detail_table.DoesNotExist:
            profiledata = None

        Provider = False
        if logdetail.role == "provider":
            Provider = True
            print(Provider)

        details = {
            'logdetail': logdetail,
            'statedetail': statedetail,
            'citydetail': citydetail,
            'areadetail': areadetail,
            'profiledata': profiledata,
            'Provider': Provider,
            'servicedetail': servicedetail,

        }
        return render(request, 'addservice.html', details)
    except:
        pass
    return render(request, 'addservice.html')

def servicesubmit(request):
    uid = request.session['log_id']
    if request.method == 'POST':
        sname = request.POST.get("name")
        sdesc = request.POST.get("desc")
        sprice = request.POST.get("price")
        servicename = request.POST.get("servicename")
        simage = request.FILES["service_image"]


        servicedata = service(l_id=login_table(id=uid), service_name=sname, service_description=sdesc, service_price=sprice, service_id=service_category(id=servicename)
                              ,service_photo=simage)
        servicedata.save()
        messages.success(request, 'Data Inserted Successfully.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, 'error occured')

def deleteserv(request, dsid):
    service.objects.filter(id=dsid).delete()
    messages.error(request, 'service Deleted.')

    return redirect(yourprofile)

def allservices(request):
    try:
        uid = request.session['log_id']
        logdetail = login_table.objects.get(id=uid)
        statedetail = state.objects.all()
        citydetail = city.objects.all()
        areadetail = area_table.objects.all()
        servicedetails = service_category.objects.all()

        try:
            profiledata = detail_table.objects.get(l_id=uid)
        except detail_table.DoesNotExist:
            profiledata = None



        Provider = False
        if logdetail.role == "provider":
            Provider = True
            print(Provider)

        details = {
            'logdetail': logdetail,
            'statedetail': statedetail,
            'citydetail': citydetail,
            'areadetail': areadetail,
            'profiledata': profiledata,
            'Provider': Provider,
            'servicedetails': servicedetails,

        }
        return render(request, 'allservices.html', details)
    except:
        servicedetails = service_category.objects.all()
        details = {
            'servicedetails': servicedetails,

        }
        return render(request, 'allservices.html', details)

def catwiseservice(request, cwsid):
    try:
        uid = request.session['log_id']
        logdetail = login_table.objects.get(id=uid)
        statedetail = state.objects.all()
        citydetail = city.objects.all()
        areadetail = area_table.objects.all()
        servicedetails = service.objects.filter(service_id=service_category(id=cwsid))

        try:
            profiledata = detail_table.objects.get(l_id=uid)
        except detail_table.DoesNotExist:
            profiledata = None



        Provider = False
        if logdetail.role == "provider":
            Provider = True
            print(Provider)

        details = {
            'logdetail': logdetail,
            'statedetail': statedetail,
            'citydetail': citydetail,
            'areadetail': areadetail,
            'profiledata': profiledata,
            'Provider': Provider,
            'servicedetails': servicedetails,

        }
        return render(request, 'catwiseservices.html', details)
    except:
        servicedetails = service.objects.filter(service_id=service_category(id=cwsid))
        details = {
            'servicedetails': servicedetails,

        }
        return render(request, 'catwiseservices.html', details)

def servicesingle(request, ssid):
    try:
        uid = request.session['log_id']
        logdetail = login_table.objects.get(id=uid)
        statedetail = state.objects.all()
        citydetail = city.objects.all()
        areadetail = area_table.objects.all()
        servicedetails = service.objects.get(id=ssid)


        try:
            profiledata = detail_table.objects.get(l_id=uid)
        except detail_table.DoesNotExist:
            profiledata = None



        Provider = False
        if logdetail.role == "provider":
            Provider = True
            print(Provider)

        details = {
            'logdetail': logdetail,
            'statedetail': statedetail,
            'citydetail': citydetail,
            'areadetail': areadetail,
            'profiledata': profiledata,
            'Provider': Provider,
            'servicedetails': servicedetails,
        }
        return render(request, 'servicesingle.html', details)
    except:
        servicedetails = service.objects.get(id=ssid)




        details = {
            'servicedetails': servicedetails,
        }
        return render(request, 'servicesingle.html', details)

def bookservice(request):
    uid = request.session['log_id']
    if request.method == "POST":
        serviceid = request.POST.get("serviceid")
        paymentod = request.POST.get("payment")
        razorpay_payment_id = request.POST.get("payment_id")
        # logdetail = detail_table.objects.get(l_id=uid)
        # user_address = logdetail.address

        phone = request.POST.get("phone")
        address = request.POST.get("address")
        sdate = request.POST.get("startdate")

        bookingdata = booking_service(serviceperson=service(id=serviceid), l_id=login_table(id=uid),phone=phone ,address=address,sdate=sdate,paymethod=paymentod, ubr_status="Confirmed", razorpay_payment_id=razorpay_payment_id if paymentod == 'online' else None,show_approve_button=False)
        bookingdata.save()
        messages.success(request, 'Service Booked from your end. Service Provider will contact you as soon as possible.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def userbookings(request):
    try:
        uid = request.session['log_id']
        logdetail = login_table.objects.get(id=uid)
        statedetail = state.objects.all()
        citydetail = city.objects.all()
        areadetail = area_table.objects.all()


        try:
            profiledata = detail_table.objects.get(l_id=uid)
        except detail_table.DoesNotExist:
            profiledata = None

        Provider = False
        if logdetail.role == "provider":
            Provider = True
            print(Provider)
            servdata = service.objects.filter(l_id=uid)

        ubdata = booking_service.objects.filter(l_id=uid)


        details = {
            'logdetail': logdetail,
            'statedetail': statedetail,
            'citydetail': citydetail,
            'areadetail': areadetail,
            'profiledata': profiledata,
            'Provider': Provider,
            'servdata': servdata,
            'ubdata': ubdata,

        }
        return render(request, 'userbookings.html', details)
    except:
        try:
            uid = request.session['log_id']
            logdetail = login_table.objects.get(id=uid)
            statedetail = state.objects.all()
            citydetail = city.objects.all()
            areadetail = area_table.objects.all()

            try:
                profiledata = detail_table.objects.get(l_id=uid)
            except detail_table.DoesNotExist:
                profiledata = None

            ubdata = booking_service.objects.filter(l_id=uid)

            Provider = False
            if logdetail.role == "provider":
                Provider = True
                print(Provider)

            details = {
                'logdetail': logdetail,
                'statedetail': statedetail,
                'citydetail': citydetail,
                'areadetail': areadetail,
                'profiledata': profiledata,
                'Provider': Provider,
                'ubdata': ubdata,

            }
            return render(request, 'userbookings.html', details)
        except:
            pass

def cancelbooking(request, cbid):
    booking_service.objects.get(id=cbid).delete()
    messages.warning(request, 'Your booking has been cancelled. Since it was within 3 days of the scheduled date, please review our refund policy or contact support for assistance.')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def viewagentbookings(request):
    try:
        uid = request.session['log_id']
        logdetail = login_table.objects.get(id=uid)
        statedetail = state.objects.all()
        citydetail = city.objects.all()
        areadetail = area_table.objects.all()
        try:
            profiledata = detail_table.objects.get(l_id=uid)
        except detail_table.DoesNotExist:
            profiledata = None

        Provider = False
        if logdetail.role == "provider":
            Provider = True
            print(Provider)

            servdata = service.objects.filter(l_id=uid)
            # agentobj = servdata.l_id
            # agent_id = agentobj.id
            # print(agent_id)
            print(uid)
        ubdata = booking_service.objects.filter(serviceperson__in=servdata)
        print(ubdata)
        details = {
            'logdetail': logdetail,
            'statedetail': statedetail,
            'citydetail': citydetail,
            'areadetail': areadetail,
            'profiledata': profiledata,
            'Provider': Provider,
            'servdata': servdata,
            'ubdata': ubdata,

        }
        return render(request, 'agentbookings.html', details)
    except Exception as e:
        print("vlsmvvn\n",e)
        try:
            uid = request.session['log_id']
            logdetail = login_table.objects.get(id=uid)
            statedetail = state.objects.all()
            citydetail = city.objects.all()
            areadetail = area_table.objects.all()

            try:
                profiledata = detail_table.objects.get(l_id=uid)
            except detail_table.DoesNotExist:
                profiledata = None

            ubdata = booking_service.objects.filter(serviceperson=service(l_id=uid))
            print(ubdata)

            Provider = False
            if logdetail.role == "provider":
                Provider = True
                print(Provider)
            details = {
                'logdetail': logdetail,
                'statedetail': statedetail,
                'citydetail': citydetail,
                'areadetail': areadetail,
                'profiledata': profiledata,
                'Provider': Provider,
                'ubdata': ubdata,

            }
            return render(request, 'agentbookings.html', details)
        except:
            return render(request, 'agentbookings.html')

def viewDetails(request, id):
    try:
        uid = request.session['log_id']
        logdetail = login_table.objects.get(id=uid)
        statedetail = state.objects.all()
        citydetail = city.objects.all()
        areadetail = area_table.objects.all()

        try:
            profiledata = detail_table.objects.get(l_id=uid)
        except detail_table.DoesNotExist:
            profiledata = None

        Provider = False
        if logdetail.role == "provider":
            Provider = True
            print(Provider)

        details = {
            'logdetail': logdetail,
            'statedetail': statedetail,
            'citydetail': citydetail,
            'areadetail': areadetail,
            'profiledata': profiledata,
            'Provider': Provider,
        }
        try:
            userdetails = detail_table.objects.get(l_id=id)
            print(userdetails)
            if userdetails is not None:
                details.update({"profiledata": userdetails})
                return render(request, "customerdetails.html", details)
            else:
                details.update({"profiledata": None})
                return render(request, "customerdetails.html", details)
        except:
            pass
    except:
        pass
    return render(request, 'index.html')


def acceptbooking(request, abid):
    abook = booking_service.objects.get(id=abid)
    abook.ubr_status = "Confirmed"
    abook.show_approve_button = False
    abook.save(update_fields=['ubr_status','show_approve_button'])
    messages.success(request, 'Booking Accepted')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def rejectbooking(request, rbid):
    rbook = booking_service.objects.get(id=rbid)
    rbook.ubr_status = "Rejected"
    rbook.rejected = True
    rbook.save(update_fields=['ubr_status', 'rejected'])
    messages.success(request, 'Booking Rejected')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def SubmitReview(request):
    if request.method == 'POST':
        name = request.POST.get("Name")
        email = request.POST.get("Sender")
        comment = request.POST.get("Message")

        subreview = feedback(name=name, email=email,comment=comment)
        subreview.save()
        messages.success(request, 'Your response recorded Successfully.')

    return redirect(contact)


def searchservice(request):
    try:
        if request.session['log_id'] is not None:
            if request.method == "POST":
                uname = request.POST.get("search")
                cat_id = service_category.objects.get(service_category_name=uname)
                return HttpResponseRedirect(reverse('catwiseservice', kwargs={'cwsid': cat_id.id}))
    except:
        messages.warning(request," Opps!! Service Not Found Try Other Service!!")
        return redirect(index)


def feedbackpage(request):
    return render(request, "feedback.html")


def storefeedback(request):
    if request.method == "POST":
        name = request.POST.get("username")
        email = request.POST.get("email")
        rating = request.POST.get("rating")
        message = request.POST.get("message")
        contact = request.POST.get("contact")

        insert = feedback(name=name, email=email, rating=rating, comment=message, contact=contact, timestamp="")
        insert.save()

        messages.info(request, "Your Feedback Has Been Submitted")
        return redirect(feedbackpage)

    return render(request, "feedback.html")

import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.conf import settings

# Setup Razorpay client
razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

@csrf_exempt
def create_order(request):
    if request.method == "POST":
        import json
        data = json.loads(request.body)
        service_id = data.get("service_id")

        try:
            selected_service = service.objects.get(id=service_id)
            amount_in_paise = int(float(selected_service.service_price) * 100)  # Convert to paise
        except service.DoesNotExist:
            return JsonResponse({"error": "Service not found"}, status=404)

        # Create Razorpay Order
        payment = razorpay_client.order.create({
            "amount": amount_in_paise,
            "currency": "INR",
            "payment_capture": 1
        })
        return JsonResponse(payment)

    return JsonResponse({"error": "Invalid request"}, status=400)




def myservices(request):
    try:
        uid = request.session['log_id']
        logdetail = login_table.objects.get(id=uid)
        statedetail = state.objects.all()
        citydetail = city.objects.all()
        areadetail = area_table.objects.all()


        try:
            profiledata = detail_table.objects.get(l_id=uid)
        except detail_table.DoesNotExist:
            profiledata = None

        Provider = False
        if logdetail.role == "provider":
            Provider = True
            print(Provider)
            servdata = service.objects.filter(l_id=uid)


        details = {
            'logdetail': logdetail,
            'statedetail': statedetail,
            'citydetail': citydetail,
            'areadetail': areadetail,
            'profiledata': profiledata,
            'Provider': Provider,
            'servdata': servdata,

        }
        return render(request, 'providerservices.html', details)
    except:
        try:
            uid = request.session['log_id']
            logdetail = login_table.objects.get(id=uid)
            statedetail = state.objects.all()
            citydetail = city.objects.all()
            areadetail = area_table.objects.all()

            try:
                profiledata = detail_table.objects.get(l_id=uid)
            except detail_table.DoesNotExist:
                profiledata = None

            Provider = False
            if logdetail.role == "provider":
                Provider = True
                print(Provider)

            details = {
                'logdetail': logdetail,
                'statedetail': statedetail,
                'citydetail': citydetail,
                'areadetail': areadetail,
                'profiledata': profiledata,
                'Provider': Provider,
            }
            return render(request, 'providerservices.html', details)
        except:
            pass


def edit_service_view(request, service_id):
    uid = request.session['log_id']
    try:
        uid = request.session['log_id']
        logdetail = login_table.objects.get(id=uid)
        statedetail = state.objects.all()
        citydetail = city.objects.all()
        areadetail = area_table.objects.all()
        edit_service = service.objects.get(id=service_id, l_id=uid)
        servicedetail = service_category.objects.all()

        try:
            profiledata = detail_table.objects.get(l_id=uid)
        except detail_table.DoesNotExist:
            profiledata = None

        Provider = False
        if logdetail.role == "provider":
            Provider = True
            print(Provider)
            servdata = service.objects.filter(l_id=uid)


        details = {
            'logdetail': logdetail,
            'statedetail': statedetail,
            'citydetail': citydetail,
            'areadetail': areadetail,
            'profiledata': profiledata,
            'Provider': Provider,
            'servdata': servdata,
            "edit_service": edit_service,
            "servicedetail": servicedetail
        }
        return render(request, "editservice.html", details)
    except:
        try:
            uid = request.session['log_id']
            logdetail = login_table.objects.get(id=uid)
            statedetail = state.objects.all()
            citydetail = city.objects.all()
            areadetail = area_table.objects.all()

            try:
                profiledata = detail_table.objects.get(l_id=uid)
            except detail_table.DoesNotExist:
                profiledata = None

            Provider = False
            if logdetail.role == "provider":
                Provider = True
                print(Provider)

            details = {
                'logdetail': logdetail,
                'statedetail': statedetail,
                'citydetail': citydetail,
                'areadetail': areadetail,
                'profiledata': profiledata,
                'Provider': Provider,
            }
            return render(request, "editservice.html", details)
        except:
            pass
def editservicesubmit(request):
    uid = request.session['log_id']
    if request.method == 'POST':
        service_id = request.POST.get("service_id")  # New hidden field for update case
        sname = request.POST.get("name")
        sdesc = request.POST.get("desc")
        sprice = request.POST.get("price")
        servicename = request.POST.get("servicename")

        simage = request.FILES.get("service_image")

        if service_id:  # Update existing service
            try:
                servicedata = service.objects.get(id=service_id, l_id=uid)
                servicedata.service_name = sname
                servicedata.service_description = sdesc
                servicedata.service_price = sprice
                servicedata.service_id = service_category(id=servicename)
                if simage:
                    servicedata.service_photo = simage
                servicedata.save()
                messages.success(request, 'Service Updated Successfully.')
                return redirect(myservices)
            except service.DoesNotExist:
                messages.error(request, 'Service not found.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, 'Invalid request.')
        return redirect('/')


def forgotpasswordpage(request):
    return render(request, "forgotpassword.html")


def forgotpassword(request):
    if request.method == 'POST':
        username = request.POST.get('email')

        try:
            user = login_table.objects.get(email=username)

        except login_table.DoesNotExist:
            user = None

        if user is not None:
            #################### Password Generation ##########################
            import random
            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                       'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

            nr_letters = 6
            nr_symbols = 1
            nr_numbers = 3
            password_list = []

            for char in range(1, nr_letters + 1):
                password_list.append(random.choice(letters))

            for char in range(1, nr_symbols + 1):
                password_list += random.choice(symbols)

            for char in range(1, nr_numbers + 1):
                password_list += random.choice(numbers)

            print(password_list)
            random.shuffle(password_list)
            print(password_list)

            password = ""  #we will get final password in this var.
            for char in password_list:
                password += char

            ##############################################################


            msg = "hello here it is your new password  "+password   #this variable will be passed as message in mail

            ############ code for sending mail ########################

            from django.core.mail import send_mail

            send_mail(
                'Your New Password',
                msg,
                'homeservices@gmail.com',
                [username],
                fail_silently=False,
            )

            #now update the password in model
            cuser = login_table.objects.get(email=username)
            cuser.password = password
            cuser.save(update_fields=['password'])

            print('Mail sent')
            messages.info(request, 'mail is sent successfully to your registered email')
            return redirect(signin)
        else:
            messages.info(request, 'This account does not exist')
    return redirect(forgotpasswordpage)


from django.shortcuts import render, redirect
from .models import login_table, detail_table
from django.utils import timezone

from django.shortcuts import redirect
from django.utils import timezone

def editprofile(request):
    uid = request.session.get("log_id")
    user = login_table.objects.get(id=uid)
    userdetails = detail_table.objects.get(l_id=user)  # Get detail using FK object

    if request.method == "POST":
        name = request.POST.get("name")
        address = request.POST.get("address")
        cityname = request.POST.get("cityname")
        statename = request.POST.get("statename")
        phone = request.POST.get("phone")

        user.name = name
        user.phone = phone

        userdetails.name = name
        userdetails.address = address
        userdetails.cityname = cityname
        userdetails.statename = statename

        if 'image' in request.FILES:
            user.dp = request.FILES['image']  # Update with new image
        # No need for else: if no new image, keep the old one

        user.save()
        userdetails.save()

        return redirect(yourprofile)  # Replace with your profile view name or URL name

    context = {
        "user": userdetails,
        "today_date": timezone.now().date()
    }
    return render(request, "editprofile.html", context)

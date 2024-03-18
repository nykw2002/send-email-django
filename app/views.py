from ipaddress import summarize_address_range
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Value
from django.db.models.functions import Concat
from datetime import datetime, timedelta, date
from django.utils import timezone
import uuid
import win32com.client
import openai
import pythoncom
import requests
from .models import *
from .decorators import unauthentificated_user, allowed_users
from .models import Company


api_key = ""  # Replace with your actual OpenAI API key


def generate_email_body(subject, api_key):
    """
    Generate an email body based on the given subject using OpenAI's GPT-3.5 Turbo model.
    """
    
    openai.api_key = api_key
    conversation = [
        {"role": "user", "content": f"Write a professional email about {subject}."},
        {"role": "assistant", "content": "Sure, here's a draft of an email:"}
    ]
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    return response.choices[0].message.content



def send_email_with_outlook(recipient, subject, message, attachment_path):
    """Send an email using Outlook with an attachment."""
    pythoncom.CoInitialize()
    print("Before dispatching Outlook")
    ol = win32com.client.Dispatch("Outlook.Application")
    print("After dispatching Outlook")
    newmail = ol.CreateItem(0x0)
    newmail.Subject = subject
    newmail.To = recipient
    newmail.Body = message
    # Add attachment
    if attachment_path:
        newmail.Attachments.Add(attachment_path)
    newmail.Send()
    pythoncom.CoUninitialize()
    




# Create your views here.
def get_organization_data(cui):
    endpoint = f"https://api.aipro.ro/get?cui={cui}"
    response = requests.get(endpoint)
    organization_data = {
        "api_record_id": response.json().get("_id"),
        "last_querry_date": response.json().get("date_generale").get("data"),
        "cui": response.json().get("CUI"),
        "denumire": response.json().get("nume_companie"),
        "adresa": response.json().get("date_generale").get("adresa"),
        "nrRegCom": response.json().get("date_generale").get("nrRegCom"),
        "telefon": response.json().get("date_generale").get("telefon"),
        "fax": response.json().get("date_generale").get("fax"),
        "codPostal": response.json().get("date_generale").get("codPostal"),
        "act": response.json().get("date_generale").get("act"),
        "stare_inregistrare": response.json().get("date_generale").get("stare_inregistrare"),
        "data_inregistrare": response.json().get("date_generale").get("data_inregistrare"),
        "cod_CAEN": response.json().get("date_generale").get("cod_CAEN"),
        "iban": response.json().get("date_generale").get("iban"),
        "statusRO_e_Factura": response.json().get("date_generale").get("statusRO_e_Factura"),
        "organFiscalCompetent": response.json().get("date_generale").get("organFiscalCompetent"),
        "forma_de_proprietate": response.json().get("date_generale").get("forma_de_proprietate"),
        "forma_organizare": response.json().get("date_generale").get("forma_organizare"),
        "forma_juridica": response.json().get("date_generale").get("forma_juridica"),
    }

    
    return organization_data


# @allowed_users(allowed_roles=[])
def Home(request):
    if request.method == 'GET':
        context = {}
        return render(request, './templates/get.html', context)
    elif request.method == 'POST':
        cui = request.POST.get("cui")
        data = get_organization_data(cui)
        # company = Company(**data)
        # company.save()
        # Usage Example
        subject = "Job Offer in Developing a Flask App"
        # Generate the email body
        email_body = generate_email_body(subject, api_key)
        # Replace with actual recipient, subject, and attachment path
        recipient = request.POST.get("email")
        attachment_path = "C:\\Users\\nicul\\Downloads\\Vlad_Niculita_CV (2).pdf"
        # Send the email
        send_email_with_outlook(recipient, subject, email_body, attachment_path)
        return render(request, "./templates/companyInfo.html", data)
        # return JsonResponse({'message': 'POST request received.'})
    

def ConfirmEmail(request):

    
    return render(request, "./templates/ConfirmEmail.html")


def WelcomeToRoIMM(request):

    return render(request, "./templates/WelcomeToRoIMM.html")
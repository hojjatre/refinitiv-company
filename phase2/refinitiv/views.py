from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
import pandas as pd
from .models import Refinitiv
from rest_framework.permissions import IsAuthenticated, AllowAny

class AllCompanyDataBase(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = "show_company.html"

    def get(self, request):
        all_data = Refinitiv.objects.all()

        return Response({'datas': all_data})

class AllCompanyCSV(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        all_data = pd.read_csv("dataCompanies.csv").to_dict()
        
        return Response({'datas': all_data})


class GetCompanyByTickerDataBase(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "company.html"

    def get(self, request, ticker):
        company = Refinitiv.objects.get(company_ticker=ticker)
        
        return Response(
            {'data':company})

class GetCompanyByTickerCSV(APIView):
    
    permission_classes = (IsAuthenticated,)
    def get(self, request, ticker):
        company = pd.read_csv("dataCompanies.csv")
        company = company[company['company_ticker']==ticker]
    
        return Response({'data': company.to_dict()})
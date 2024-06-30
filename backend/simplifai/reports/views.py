from django.views.decorators.csrf import csrf_exempt


from django.shortcuts import render
from django.http import JsonResponse
import json

from .serializers import ReportSerializer, ChatsSerializer
from .models import Report, Chats, ReportText
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .qa import QA
import argparse

qa = QA()

def parse_arguments():
    parser = argparse.ArgumentParser(description="Ask questions to your documents.")
    parser.add_argument("--no-rag", action='store_true', help="Get your answer without RAG")
    return parser.parse_args()


class ReportView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        reports = Report.objects.all()
        serializer = ReportSerializer(reports, many=True)
        return Response(serializer.data)

    # def post(self, request, *args, **kwargs):
    #     report_serializer = ReportSerializer(data=request.data)
    #     if report_serializer.is_valid():
    #         report = report_serializer.save()

    #         image_path = report.plot.path

    #         # image_path = image_path.replace('/reports/media/', '')

    #         # Extract text from image
    #         text = extract_text_from_image(image_path)

    #         print(text)
            
    #         ReportText.objects.create(report=report, text=text)
            
    #         text  = text + "\n Summarize the above text "
    #         print(f"text: {text}")
    #         Doctor = False
    #         English = True
    #         response = qa._ask_non_rag(text, Doctor, English)

    #         llm_response = {
    #             "text": response,
    #             "sender": "SimplifAI",
    #             "isUser": False
    #         }
    #         print(f"response: {response}")
    #         response_serializer = ChatsSerializer(data = llm_response)
    #         if response_serializer.is_valid():
    #             response_serializer.save()
    #             return JsonResponse(response_serializer.data, status=201)
    #         else:
    #             return JsonResponse(response_serializer.errors, status=400)

    def post(self, request, *args, **kwargs):
        plot_image = request.data.get('plot')

        body = {
            'plot': plot_image
        }

        isDoctor = request.data.get('isDoctor') == 'True'
        isEnglish = request.data.get('isEnglish') == 'True'


        report_serializer = ReportSerializer(data= body)
        if report_serializer.is_valid():
            report = report_serializer.save()

            image_path = report.plot.path

            # image_path = image_path.replace('/reports/media/', '')

            # Extract text from image
            text = extract_text_from_image(image_path)

            body =  {
                "text": text,
                "sender": "Aashish",
                "isUser": True,
            }

            query_serializer = ChatsSerializer(data = body)
            if query_serializer.is_valid():
                query_serializer.save()
            else:
                return JsonResponse(query_serializer.errors, status=400)

            ReportText.objects.create(report=report, text=text)

            text  = text + "\n Interpret and Summarize the above text"
            print(f"text: {text}")
            response = qa._ask_non_rag(text , isDoctor, isEnglish)

            llm_response = {
                "text": response,
                "sender": "SimplifAI",
                "isUser": False
            }
            print(f"response: {response}")
            response_serializer = ChatsSerializer(data = llm_response)
            if response_serializer.is_valid():
                response_serializer.save()
                return JsonResponse(response_serializer.data, status=201)
            else:
                return JsonResponse(response_serializer.errors, status=400)


 

def get_report_lists(request):
    if request.method == 'GET':
        reports = Report.objects.all()
        report_data = [{'id': report.id,'date': report.date} for report in reports]
        return JsonResponse(report_data, safe=False)

    else:
        return JsonResponse({'message': 'Invalid Request'}, status=400)


def chat_message(request):
    if request.method == 'POST':
        # print(request.body)
        # return JsonResponse({'message':'got'})
        # json_data = json.loads(request.body)

        
       

        json_data = json.loads(request.body)
            # email = json_data['email']
        text = json_data['text']
        sender = json_data['sender']
        isUser = json_data['isUser']
        isEnglish = json_data['isEnglish']
        isDoctor = json_data['isDoctor']
            # fileType = json_data['fileType']

        body =  {
        "text": text,
        "sender": sender,
        "isUser": isUser,
        "isEnglish": isEnglish,
        "isDoctor": isDoctor
        }

        print(f'body : {body}')
        serializer = ChatsSerializer(data = body)
        
        if serializer.is_valid():
            serializer.save()
        else:
            return JsonResponse(serializer.errors, status=400)
   
        # args = parse_arguments()
        

        query = text
        response = qa._ask_non_rag(query, isDoctor, isEnglish)
        print(f'query at: {query}')
        print(f'response: {response}')



        llm_response = {
        "text": response,
        "sender": "SimplifAI",
        "isUser": False
        }

        response_serializer = ChatsSerializer(data = llm_response)
        if response_serializer.is_valid():
            response_serializer.save()
            return JsonResponse(response_serializer.data, status=201)
            print('response Sent')
        else:
            return JsonResponse(response_serializer.errors, status=400)

        

    if request.method == 'GET':
        chats = Chats.objects.all()
        
        serializer = ChatsSerializer(chats, many=True )

        return JsonResponse(serializer.data, safe=False)


# Import the function
from .ocr import get_ocr_result
import os
from django.conf import settings
def extract_text_from_image(image_path):
    image_path = os.path.join(settings.MEDIA_ROOT, image_path)
    print(image_path)
    result = get_ocr_result(image_path)
    return result
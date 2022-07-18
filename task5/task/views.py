from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
import openpyxl

# Removing the authentication & permission classes
@api_view(['GET', 'POST'])
@authentication_classes([])
@permission_classes([])
def task5(request):
    """
    Taking: name, date_of_birth and country as input parameters from user and saving it in excel file.
    :param request: HTTP request object
    :return: Returning the status message as successful or failure
    """

    try:
        name = request.data["name"]
        date_of_birth = request.data["date_of_birth"]
        country = request.data["country"]
    except Exception as e:
        # We should msg also in the response for more clarity
        return Response({'status': 'failure'})
    wb = openpyxl.Workbook()
    wb.save(filename='task5.xlsx')
    wb = openpyxl.load_workbook("task5.xlsx")
    sheet = wb.active
    header_row = (
        ('Name', 'Date of birth', 'Country')
    )
    sheet.append(header_row)
    xlsx_data = (
        (name, date_of_birth, country)
    )
    sheet.append(xlsx_data)
    # for row in xlsx_data:
    #     sheet.append(row)
    wb.save('task5.xlsx')
    return Response({'status': 'successful'})

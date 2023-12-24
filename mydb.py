# import mysql.connector
# dataBase = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     passwd = 'dev123!@#&*('
# )
# # Prepare a cursor object
# cursorObject = dataBase.cursor()

# # One time executable
# cursorObject.execute("CREATE DATABASE crmwebapp") 
from website.models import CustomUser

# Replace 'your_condition' with the condition that identifies the row you want to delete
row_to_delete = CustomUser.objects.get(id=12)

# or use filter if there may be multiple rows matching the condition
# row_to_delete = YourModel.objects.filter(your_condition).first()

# Delete the retrieved object
row_to_delete.delete()
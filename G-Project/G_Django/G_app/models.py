from django.db import models

class user(models.Model):
    Firstname = models.CharField(max_length=255)
    Lastname = models.CharField(max_length=255)
    Phone = models.IntegerField()
    Email = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    
    
# def it_votavo():
#     andry = ['Andry-IT', '0320317201', 'andry.raz@smartone-group.com']
#     rio = ['Rio-IT', '0320317202', 'rio.raz@smartone-group.com']
#     michel = ['Michel-IT', '0320317203', 'michel.raz@smartone-group.com']
#     donat = ['Donat-IT', '0320317204', 'donat.raz@smartone-group.com']
#     fany = ['Fany-IT', '0320317205', 'fany.raz@smartone-group.com']
#     return [andry, rio, michel, donat, fany]


# def data(_user):
#     db = it_votavo()
    
#     for x in db[_user]:

#         tmp = user(
#             Firstname = db[_user][0],
#             Phone = db[_user][1],
#             Email = db[_user][2],
#             )

#         tmp.save()

# def addData():
#     for i in range(0, len(it_votavo())):
#         data(i)

#     print('Finished')
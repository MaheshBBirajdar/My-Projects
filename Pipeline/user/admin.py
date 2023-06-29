from django.contrib import admin
from .models import *
from django.contrib.admin import ModelAdmin


############################################################################################################

class Shot2Admin(admin.ModelAdmin):
    pass
admin.site.register(Shot2, Shot2Admin)




class ArtistInfoAdmin(admin.ModelAdmin):
    pass
admin.site.register(StudentExtra, ArtistInfoAdmin)




class IssuedShotAdmin(admin.ModelAdmin):
    pass
admin.site.register(IssuedShot, IssuedShotAdmin)




class SendFeedbackAdmin(admin.ModelAdmin):
    pass
admin.site.register(SendFeedback, SendFeedbackAdmin)




class ArtistMessageAdmin(admin.ModelAdmin):
    pass
admin.site.register(ArtistMessage, ArtistMessageAdmin)




class ManagementMessageAdmin(admin.ModelAdmin):
    pass
admin.site.register(ManagementMessage, ManagementMessageAdmin)


###############################
#<td><a href="{% url 'deleteissuedshot' each.9 %}"><button type="button" class="btn btn-outline-danger btn-sm">Remove</button></a></td> -->
###################################
from django.contrib import admin
from .models import *



class ShotAdmin(admin.ModelAdmin):
    pass
admin.site.register(Shot2, ShotAdmin)




class ArtistInfoAdmin(admin.ModelAdmin):
    pass
admin.site.register(StudentExtra, ArtistInfoAdmin)




class IssuedShotAdmin(admin.ModelAdmin):
    pass
admin.site.register(IssuedShot, IssuedShotAdmin)




class SendFeedbackAdmin(admin.ModelAdmin):
    pass
admin.site.register(SendFeedback, SendFeedbackAdmin)
from rest_framework import permissions

class MaheshPermission(permissions.BasePermission):
	block_ip_list = ['192.168.159.1']
	def has_permission(self,request,view):
		ip_addr = request.META['REMOTE_ADDR']
		if ip_addr in self.block_ip_list:
			return False
		else:
			return True
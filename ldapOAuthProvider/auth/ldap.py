from django.conf import settings
from django.contrib.auth.models import User
from lmap import lmap, ldap

class LDAPUser:

	def __init__(self, uid, pw):
		ld = ldap.ldap(settings.LDAP_HOST)
		dn = settings.LDAP_USER_DN.format(uid)
		print('Trying to bind with '+dn+'...')
		ld.simple_bind(dn, pw)
		self.group_base = lmap.lmap(dn=settings.LDAP_GROUPS_BASE, ldap=ld)
		self.uid = uid
		self.dn = dn

	@property
	def ldapgroups(self):
		return { group.attrs['cn'].join(' ') for group in self.group_base.search('member='+self.dn) }
	
class LDAPBackend:
	
	def authenticate(self, username=None, password=None, **kwargs):
		try:
			lu = LDAPUser(username, password)
			user = None
			try:
				user = User.objects.get(username=username)
			except User.DoesNotExist:
				# Add the user to the local DB
				user = User(username=username, password='')
				user.save()
			user.ldapuser = lu
			return user
		except ldap.LDAPError as e: # Could not find user etc.
			print('Could not authenticate user '+username+':', e)
			return None

	def get_user(self, user_id):
		try:
			user = User.objects.get(pk=user_id)
			if user.ldapuser:
				return user
			return None
		except User.DoesNotExist:
			return None
		except ldap.LDAPError:
			return None


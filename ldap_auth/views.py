from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render
import ldap
from django_auth_ldap.config import LDAPSearch


#ldapsearch -H ldaps://202.141.81.3:636 -D "uid=swc,ou=stud-offices,ou=stud,dc=iitg,dc=ernet,dc=in" -w 'India$Rising' -b "dc=iitg,dc=ernet,dc=in" -s sub "uid=swc" -LLL dn

AUTH_LDAP_SERVER_URI = "ldaps://202.141.81.3:636"
AUTH_LDAP_CONNECTION_OPTIONS = {
    ldap.OPT_REFERRALS: 0
}

AUTH_LDAP_BIND_DN = "swc"
AUTH_LDAP_BIND_PASSWORD = "'India$Rising'"

AUTHENTICATION_BACKENDS = [
    'django_auth_ldap.backend.LDAPBackend',
    # 'django.contrib.auth.backends.ModelBackend',
]

# Initiate TLS on connection.
LDAP_AUTH_USE_TLS = False

def user_login(request):
    if request.method == 'GET':
        return render(request,'ldap_auth/login.html')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=stud-offices,ou=stud,dc=iitg,dc=ernet,dc=in",
ldap.SCOPE_SUBTREE, "(uid=%(user)s)")

        print(AUTH_LDAP_USER_SEARCH.attrlist)

        return HttpResponse(" Cheking username!")

        """
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse("login successful")
            else:
                return HttpResponse("account not active")
        else:
            return HttpResponse("Invalid Login Credentials")

        """

from rest_framework.generics import CreateAPIView
from .serializers import ProfileSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from firebase_admin import credentials, auth
from .models import Profile
import firebase_admin
from rest_framework.permissions import AllowAny

class ProfileView(ModelViewSet):
    queryset = Profile.objects.all().order_by('-date_joined')
    serializer_class = ProfileSerializer
    http_method_names = ['get', 'patch', 'delete']
    parser_classes = (MultiPartParser,)

    def retrieve(self, request, pk=None):
        if pk == 'i':
            return Response(ProfileSerializer(request.user, context={'request':request}).data)
        else:
            return super(ProfileView, self).retrieve(request, pk)

    def destroy(self, request, pk=None):
        me = self.request.user

        if not me:
            return Response(status=401)

        try:
            cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS)
            firebase_admin.initialize_app(cred)
        except:
            pass

        auth.delete_user(me.id) # delete user from firebase
        me.delete() # delete user from django

        return Response(status=204)

class CreateProfileView(CreateAPIView):
  model = Profile
  serializer_class = ProfileSerializer
  permission_classes = (AllowAny, )

  def create(self, request, *args, **kwargs):
      serializer = self.get_serializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
      return Response(status=400)
from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView 
from .serializers import ClassroomListSerializer, ClassroomDetailSerializer, ClassroomCreateUpdateSerializer
from classes.models import Classroom

class ClassAPIListView(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomListSerializer

class ClassAPIDetailView(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'

class ClassAPICreateView(CreateAPIView):
	serializer_class = ClassroomCreateUpdateSerializer

	def perform_create(self, serializer):
		serializer.save(teacher=self.request.user)

class ClassAPIUpdateView(RetrieveUpdateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomCreateUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'

class ClassAPIDeleteView(DestroyAPIView):
	queryset = Classroom.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'



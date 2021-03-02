from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Course
from .serializers import CourseDetailsSerializer


# Create your views here.


@api_view(['GET', 'POST'])
def coursedetails(request):
    if request.method == 'GET':
        try:
            course = Course.objects.get(courseId=id)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CourseDetailsSerializer(course)
        return Response(serializer.data)
    elif request.method == 'POST':
        print('CourseDetails')
        serializer = CourseDetailsSerializer(data=request.data)
        if serializer.is_valid():
            queryset = Course.objects.filter(courseName=request.data.get('courseName'))
            if queryset.exists():
                serializer = CourseDetailsSerializer(queryset, many=True)
                return Response(serializer.data)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

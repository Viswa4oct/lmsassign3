from rest_framework import serializers

from .models import Course


class CourseDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['courseName', 'courseDescription', 'lecturerName', 'duration', 'startDate',
                  'seatsAvailable', 'credits', 'enrolled']

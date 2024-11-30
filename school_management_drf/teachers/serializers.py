from rest_framework import serializers
from .models import Teacher
from courses.models import Course  # Modelo Course importado para referência
from courses.serializers import CourseSerializer

class TeacherSerializer(serializers.ModelSerializer):
    # Usando PrimaryKeyRelatedField para o campo 'course', permitindo a atualização do ID do curso
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())  # Agora aceita o ID do curso
    
    class Meta:
        model = Teacher
        fields = ['id', 'name', 'registration_number', 'email', 'course', 'date_of_birth', 'hire_date', 'profile_picture']

    def to_representation(self, instance):
        # Customizando o retorno para pegar apenas 'name' e 'description' do curso
        representation = super().to_representation(instance)
        
        # Agora `course` é um ID, então precisamos pegar o objeto Course
        if 'course' in representation:
            # Obter o objeto Course a partir do ID
            course_instance = representation['course']  # Isso é o ID do curso
            course = Course.objects.get(id=course_instance)  # Recuperar o objeto Course pelo ID
            
            # Agora podemos acessar as propriedades do curso
            representation['course'] = {
                'name': course.name,
                'description': course.description,
            }
        
        return representation

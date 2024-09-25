from django.shortcuts import render

def index(request):
    return render(request, 'grades/index.html')

def result(request):
    return render(request, 'grades/result.html')

# from django.shortcuts import render, redirect
# from .forms import StudentForm
# from .models import Student
#
# def index(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             student = form.save(commit=False)
#             student.save()
#             return redirect('result', student_id=student.id)
#     else:
#         form = StudentForm()
#     return render(request, 'grades/index.html', {'form': form})
#
# def result(request, student_id):
#     student = Student.objects.get(id=student_id)
#     return render(request, 'grades/result.html', {'student': student})

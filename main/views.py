from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import *




def home(request):
    if not request.user:
        return redirect('login')
    user=request.user
    mod_user=modified_user.objects.get(user=user)



    # array of skill and star
    map={i.skill:i.stars for i in skill.objects.all()} 

    # education
    edus=modified_user.objects.get(user=user).education.all()
    edu_list=[]
    for edu in edus:
        edu_dict={}
        edu_dict['School/college']=edu.school
        edu_dict['Class']=edu.classes
        edu_dict['Marks/Agreegate CGPA']=edu.marks
        edu_dict['Passed year']=edu.passed_year
        edu_list.append(edu_dict)
        # edu_dict.clear()    

    # about 
    discription={}
    discription['I would like to introduce myself.']=about.objects.get(user=user).discription
    discription['Update By']=about.objects.get(user=user).date

    # internships
    interns=modified_user.objects.get(user=user).internships.all()
    intern_list=[]
    for int in interns:
        intern={}
        intern['company']=int.company
        intern['Working Year']=int.working_year
        intern_list.append(intern)

    # projects
    projects_list=[]
    projects=modified_user.objects.get(user=user).academic_project.all()
    for proj in projects:
        project={}
        project['theme']=proj.theme
        project['completeness']=proj.completeness
        projects_list.append(project)

    # links
    links_list=[]
    links=modified_user.objects.get(user=user).links.all()
    for link in links:
        link_dict={}
        link_dict['platform']=link.platform
        link_dict['link']=link.link
        link_dict['url']=link.get_favicon()
        links_list.append(link_dict)
    

    context={
        'user':mod_user.user,
        'mod_user':mod_user,
        'skill':map,
        'educations':edu_list,
        # [
            # {'school/college':Delhi Technological University}....
        # ]
        'discription':discription,
        'internships':intern_list,
        'projects':projects_list,
        'links':links_list,
    }
    return render(request,"home.html",context)


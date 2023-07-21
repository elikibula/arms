from django.shortcuts import render, redirect
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape
from .models import Arm, ArmIssue, Location, rank_Choices
from django.db.models import CharField, Count
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F
from django.http import JsonResponse


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, "You are now logged in")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

@login_required(login_url='login')
def home(request):
    arm_count = Arm.objects.count()
    total_revolver = Arm.objects.filter(name='revolver').count()
    total_pistol = Arm.objects.filter(name='pistol').count()
    total_holster = Arm.objects.filter(name='holster').count()
    total_machine_gun = Arm.objects.filter(name='machine_gun').count()
    total_shot_gun = Arm.objects.filter(name='shot_gun').count()
    total_rifle = Arm.objects.filter(name='rifle').count()
    total_air_gun = Arm.objects.filter(name='air_gun').count()
    total_grenade_launcher = Arm.objects.filter(name='grenade_launcher').count()
    total_smg = Arm.objects.filter(name='smg').count()
    total_lmg = Arm.objects.filter(name='lmg').count()
    total_mortar = Arm.objects.filter(name='mortar').count()
    total_craft_gun = Arm.objects.filter(name='craft_gun').count()
    total_sniper_rifle = Arm.objects.filter(name='sniper_rifle').count()

    context = {
        'arm_count': arm_count,
        'total_revolver': total_revolver,
        'total_pistol': total_pistol,
        'total_holster': total_holster,
        'total_machine_gun': total_machine_gun,
        'total_shot_gun': total_shot_gun,
        'total_rifle': total_rifle,
        'total_air_gun': total_air_gun,
        'total_grenade_launcher': total_grenade_launcher,
        'total_smg': total_smg,
        'total_lmg': total_lmg,
        'total_mortar': total_mortar,
        'total_craft_gun': total_craft_gun,
        'total_sniper_rifle': total_sniper_rifle,
    }

    return render(request, 'home.html', context)


class ArmListJson(BaseDatatableView):
    model = ArmIssue
    columns = ['name', 'rank', 'unit', 'arm_type', 'serial_number', 'location']

    def render_column(self, row, column):
        if column == 'name':
            return row.name.upper() if row.name else ''
        elif column == 'rank':
            return dict(rank_Choices).get(row.rank, '')
        elif column == 'unit':
            return row.unit if row.unit else ''
        elif column == 'arm_type':
            try:
                # Assuming 'serial_number' is the ForeignKey field between ArmIssue and Arm models
                arm = Arm.objects.get(serial_number=row.serial_number)
                return arm.name
            except Arm.DoesNotExist:
                return ''
        elif column == 'location':
            return row.location.name if row.location else ''  # Assuming 'location' is the ForeignKey field
        elif column == 'serial_number':
            return row.serial_number if row.serial_number else ''
        else:
            return ''  # Default value if column not found

    # ... (your other methods)


@login_required(login_url='login')
def arms_list(request):
    arm_issues = ArmIssue.objects.all()
    context = {'arm_issues': arm_issues}
    return render(request, 'arm_list.html', context)




def logoutUser(request):
	logout(request)
	return redirect('login')

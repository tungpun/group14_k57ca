# pylint: disable=no-member, unexpected-keyword-arg, too-many-public-methods,
# pylint: too-few-public-methods, import-error, relative-import
"""Views implement here"""
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.

from models import Timetable
from periods.models import Period
from forms import InsertTimetableForm


def index(request):
    """Index page view"""
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/users/auth_login')

    content = {
        'username': request.user
    }
    return render(request, 'timetables/index.html', content)


def board(request):    # default of pid is 1
    """Timetable render"""
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/users/auth_login')
    # request.session['a'] = 1
    objs = []

    #try:
        #if Timetable.objects.filter(owner=request.user.id).exist():
    tbarray = Timetable.objects.filter(owner=request.user.id)
    if tbarray.exists():
        pid = tbarray[0].owner
    else:
        pid = 0
        return HttpResponseRedirect("/add")

    periods_array = Period.objects.filter(timetable_id=pid)

    for period in periods_array:
        objs.append(period)

    for i in range(0, 71):
        free = True
        for period in periods_array:
            if period.position == i:
                free = False
                break
        if free:
            mark = False
            for period in periods_array:
                if (period.position < i)and(i < period.position+period.length):
                    mark = True
                    break
            if mark:
                objs.append(Period(position=i, name=0))
            else:
                objs.append(Period(position=i, name="", length=0))

    for obj in objs:
        obj.day = str((obj.position - 1) / 10)
        obj.per = str((obj.position - 1) % 10)

    objs.sort(key=lambda obj: obj.position)
    #objs.sort(cmp=None,key=position,request=False)

    def check_existed(x):
        """Check if periods already existed"""
        for p in periods_array:
            if x.code == p.code:
                return False
        return True

    course_new = filter(check_existed, Period.objects.all().order_by('-id'))[:5]
    course_hot = filter(check_existed, Period.objects.all().order_by('?'))[:5]
    course_recommend = filter(check_existed, Period.objects.all().order_by('?'))[:5]

    current_user = request.user

    if not current_user.is_authenticated():
        request.user = 'Guest'
        #return render(request, '/../users/login')
        return HttpResponseRedirect('/users/auth_login')
    else:
        content = {
            'course_new': course_new,
            'course_hot': course_hot,
            'course_recommend': course_recommend,
            'timetable_id': pid,
            'periods_array': objs,
            'username': current_user,
        }
        return render(request, 'timetables/board/index.html', content)


def add(request):
    """Add page view"""
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/users/auth_login')

        # add Timetable
    if request.method == 'POST':  # if the form has been submitted...
        form = InsertTimetableForm(request.POST)  # form bound to the POST data
        current_user = request.user
        if not current_user.is_authenticated():
            return HttpResponse("<a href='/users/auth_login'>Login</a> first")
        else:
            if form.is_valid():          # All validation rules pass
                new_timetable = Timetable(
                    code=form.cleaned_data['code'],
                    name=form.cleaned_data['name'],
                    owner=current_user.id
                )
                new_timetable.save()
                return HttpResponseRedirect('/')           # Redirect after POST
    else:
        form = InsertTimetableForm()

    return render(request, 'timetables/add/index.html', {
        'form': form})

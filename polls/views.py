# Create your views here.
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from polls.models import Poll, Choice

def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    return render(request,
                  'polls/index.html',
                  {'latest_poll_list': latest_poll_list})

    
def detail(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': p})


def results(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': p})


def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(
                request,
                'polls/detail.html', 
                {   
                    'poll': p,
                    'error_message': "You didn't select a choice.",
                }
                )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(
                reverse('polls.views.results', args=(p.id,))
                )

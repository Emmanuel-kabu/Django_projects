from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse ,resolve
from .models import Topic,Entry
from .forms import TopicForm, NewEntry

# Create your views here.
def index(request):
    """ The home page MylogApp"""
    return render(request, 'MyLogApp/index.html')

def topics(request):
    """ page to show all the topic"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'MyLogApp/topics.html',context)

def topic(request, topic_id):
    """ Show individual single page"""
    topic = Topic.objects.get(id = int(topic_id))
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic' : topic, 'entries' : entries}
    return render(request, 'MyLogApp/topic.html', context)

def new_topic(request):
    """ Add topic by the  user"""
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return  HttpResponseRedirect(reverse('MyLogApp:topics'))
            print(request.POST)
    else:
        # post data submitted
        form = TopicForm()
        

    context = {'form': form}
    return render(request, 'MyLogApp/new_topic.html', context)


def new_entry(request, topic_id):
    """ Adding new entry """
    topic = Topic.objects.get(id = int(topic_id))
    if request.method != 'POST':
        # create a blank form
        form = NewEntry()
    else:
        """ submit your data """
        form = NewEntry(data = request.POST)
        if form.is_valid():
            new_entry = form.save(commit = False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('MyLogApp:topic', args = [topic_id]))
    context ={'topic': topic, 'form': form}
    return render(request, 'MyLogApp/new_entry.html', context)     
           



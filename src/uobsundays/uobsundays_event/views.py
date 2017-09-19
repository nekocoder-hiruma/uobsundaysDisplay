from django.views.generic import ListView, TemplateView
from uobsundays_event.models import EventImage, EventImage2, EventImage3


class EventOverviewTemplateView(TemplateView):
    template_name = 'uobsundays_event/events.html'


class EventOverviewTemplateView2(TemplateView):
    template_name = 'uobsundays_event/events2.html'


class EventImagesListView(ListView):
    template_name = 'uobsundays_event/eventgallery.html'
    model = EventImage
    context_object_name = 'images'
    paginate_by = 15


class EventImagesLatestListView(ListView):
    template_name = 'uobsundays_event/eventgallery.html'
    model = EventImage
    context_object_name = 'images'
    paginate_by = 15
    queryset = EventImage.objects.order_by('-created')


class EventImagesReverseListView(ListView):
    template_name = 'uobsundays_event/eventgallery.html'
    model = EventImage
    context_object_name = 'images'
    paginate_by = 15
    queryset = EventImage.objects.order_by('created')


class EventImagesJulyListView(ListView):
    template_name = 'uobsundays_event/eventgallery2.html'
    model = EventImage2
    context_object_name = 'images'
    paginate_by = 15


class EventImagesJulyLatestListView(ListView):
    template_name = 'uobsundays_event/eventgallery2.html'
    model = EventImage2
    context_object_name = 'images'
    paginate_by = 15
    queryset = EventImage.objects.order_by('-created')


class EventImagesJulyReverseListView(ListView):
    template_name = 'uobsundays_event/eventgallery2.html'
    model = EventImage2
    context_object_name = 'images'
    paginate_by = 15
    queryset = EventImage.objects.order_by('created')


class EventImagesNovemberListView(ListView):
    template_name = 'uobsundays_event/eventgallery3.html'
    model = EventImage3
    context_object_name = 'images'
    paginate_by = 15


class EventImagesNovemberLatestListView(ListView):
    template_name = 'uobsundays_event/eventgallery3.html'
    model = EventImage3
    context_object_name = 'images'
    paginate_by = 15
    queryset = EventImage.objects.order_by('-created')


class EventImagesNovemberReverseListView(ListView):
    template_name = 'uobsundays_event/eventgallery3.html'
    model = EventImage3
    context_object_name = 'images'
    paginate_by = 15
    queryset = EventImage.objects.order_by('created')



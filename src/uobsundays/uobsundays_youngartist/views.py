import datetime

from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from uobsundays_youngartist.forms import YoungArtistFilterForm
from uobsundays_youngartist.models import YoungArtistOverview, YoungArtistSubmission, YoungArtistWinner
from django.utils import timezone
from django.contrib.auth import logout


class YoungArtistOverviewView(ListView):
    template_name = 'uobsundays_youngartist/youngartist.html'
    model = YoungArtistOverview
    context_object_name = 'contents'


class YoungArtistSubmissionView(FormMixin, ListView):
    template_name = 'uobsundays_youngartist/submissions.html'
    model = YoungArtistSubmission
    context_object_name = 'images'
    paginate_by = '15'
    form_class = YoungArtistFilterForm

    def get_context_data(self, **kwargs):
        context = super(YoungArtistSubmissionView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):

        form = self.get_form(self.get_form_class())

        if form.is_valid():

            created = form.cleaned_data['created']
            location = form.cleaned_data['location']

            queryset = self.get_queryset()

            if location == 'JEM':
                queryset = queryset.filter(location='JEM')
            if location == 'NEX':
                queryset = queryset.filter(location='NEX')
            if created == "1":
                queryset = queryset.order_by('created')
            if created == "2":
                queryset = queryset.order_by('-created')

            self.queryset = queryset

            return super(YoungArtistSubmissionView, self).get(request, args, kwargs)
        else:
            return self.form_invalid(form)

# class YoungArtistShortlistedView(FormMixin, ListView):
#     template_name = 'uobsundays_youngartist/shortlisted.html'
#     model = YoungArtistShortlisted
#     context_object_name = 'images'
#     paginate_by = '15'
#     form_class = YoungArtistFilterForm
#
#     def get_context_data(self, **kwargs):
#         context = super(YoungArtistShortlistedView, self).get_context_data(**kwargs)
#         context['form'] = self.get_form()
#         return context
#
#     def post(self, request, *args, **kwargs):
#
#         form = self.get_form(self.get_form_class())
#
#         if form.is_valid():
#
#             created = form.cleaned_data['created']
#             location = form.cleaned_data['location']
#
#             queryset = self.get_queryset()
#
#             if location == 'JEM':
#                 queryset = queryset.filter(location='JEM')
#             if location == 'NEX':
#                 queryset = queryset.filter(location='NEX')
#             if created == "1":
#                 queryset = queryset.order_by('-created')
#             if created == "2":
#                 queryset = queryset.order_by('created')
#
#             self.queryset = queryset
#
#             return super(YoungArtistShortlistedView, self).get(request, args, kwargs)
#         else:
#             return self.form_invalid(form)


class YoungArtistSubmissionDetailVoteView(DetailView):
    template_name = 'uobsundays_youngartist/submission_vote.html'
    model = YoungArtistSubmission

    def get_context_data(self, **kwargs):
        pk = kwargs.get('pk')

        context = super(YoungArtistSubmissionDetailVoteView, self).get_context_data(**kwargs)
        context['image'] = kwargs.values()[0].image
        context['artist'] = kwargs.values()[0].artist
        context['age'] = kwargs.values()[0].age
        context['location'] = kwargs.values()[0].location

        return context


class YoungArtistWinnersView(ListView):
    template_name = 'uobsundays_youngartist/winners.html'
    model = YoungArtistWinner
    context_object_name = 'winners'

    def get_context_data(self, **kwargs):
        category = kwargs.get('category')

        context = super(YoungArtistWinnersView, self).get_context_data(**kwargs)
        context['prize'] = kwargs.get('prize')
        context['artist_photo'] = kwargs.get('artist_photo')
        context['artist'] = kwargs.get('artist')
        context['artist_age'] = kwargs.get('artist_age')
        context['likes'] = kwargs.get('number_of_likes')

        return context

    queryset = YoungArtistWinner.objects.order_by('prize', 'category')


class YoungArtistWinnersDetailView(DetailView):
    template_name = 'uobsundays_youngartist/winner_detail.html'
    model = YoungArtistWinner

    def get_context_data(self, **kwargs):
        pk = kwargs.get('pk')

        context = super(YoungArtistWinnersDetailView, self).get_context_data(**kwargs)
        context['artist_photo'] = kwargs.values()[0].artist_photo
        context['artist'] = kwargs.values()[0].artist
        context['artist_age'] = kwargs.values()[0].artist_age

        return context


def vote(request, youngartistsubmission_id):
    User = request.user
    if User and not User.is_anonymous():
        if User.first_time_vote:
            p = get_object_or_404(YoungArtistSubmission, pk=youngartistsubmission_id)
            p.likes += 1
            p.save()
            User.first_time_vote = False
            User.last_time_vote = timezone.localtime(timezone.now())
            User.save()
            logout(request)
            q = str(p.id)

            return HttpResponse('<script type="text/javascript">window.close(); window.opener.parent.location.href = "/littleartcontest/' + q +'/option=thank";</script>')

        else:
            if User.has_voted_recently():
                p = get_object_or_404(YoungArtistSubmission, pk=youngartistsubmission_id)
                logout(request)
                q = str(p.id)
                return HttpResponse('<script type="text/javascript">window.close(); window.opener.parent.location.href = "/littleartcontest/' + q +'/option=fail";</script>')

            else:
                p = get_object_or_404(YoungArtistSubmission, pk=youngartistsubmission_id)
                p.likes += 1
                p.save()
                User.last_time_vote = timezone.localtime(timezone.now())
                User.save()
                logout(request)
                q = str(p.id)


                return HttpResponse('<script type="text/javascript">window.close(); window.opener.parent.location.href = "/littleartcontest/' + q +'/option=thank";</script>')

    else:
        p = get_object_or_404(YoungArtistSubmission, pk=youngartistsubmission_id)
        q = str(p.id)

        return HttpResponse('<script type="text/javascript">window.close(); window.opener.parent.location.href = "/littleartcontest/' + q +'/option=thank";</script>')
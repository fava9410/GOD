from django.shortcuts import render, HttpResponseRedirect
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count
from django.core import serializers
from rest_framework import generics
from .components import *
from .models import Match, Match_Detail
from .serializer import MatchSerializer, MatchDetailSerializer

@csrf_exempt
def start(request):
    if request.method == "POST":
        m = Match.objects.create(number_of_rounds = 1)
        game = {
                'player1':{'name':request.POST.get('player1'),'score':0},
                'player2':{'name':request.POST.get('player2'),'score':0},
                'round':1,
                'match_id':m.id}
        request.session['game'] = game
        return HttpResponseRedirect('/rsp/choose_move')
    return render(request,"RSP/new_game.html")

@csrf_exempt
def choose_move(request):
    game = request.session.get('game')
    context = {}
    context['choices'] = ['Rock','Scissors','Paper']

    if request.method == "POST":
        game = request.session.get('game')

        p1 = Player(**game['player1'])
        p2 = Player(**game['player2'])

        p1.choice = MoveFactory().create_move(request.POST.get("player1_choice"))
        p2.choice = MoveFactory().create_move(request.POST.get("player2_choice"))

        round = Round(p1,p2, game['round'],game['match_id'])
        round.decide_winner()
        Match_Detail.objects.create(**round.round_history)
        round.clean_choices()

        game['player1'] = p1.__dict__
        game['player2'] = p2.__dict__
        game['round'] = round.round + 1
        game['match_id'] = round.match
        request.session['game'] = game

        if round.winner == True:
            match = Match.objects.get(id=round.match)
            match.number_of_rounds=round.round
            match.winner=round.pwin.name
            match.save()
            return render(request,"RSP/winner.html",{'winner':round.pwin.name})

    context['game'] = game
    return render(request,"RSP/choose_move.html",context)

class MatchesList(generics.ListAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class MatchDetail(generics.ListAPIView):
    serializer_class = MatchDetailSerializer

    def get_queryset(self):
        return Match_Detail.objects.filter(match_id=self.kwargs['match_id'])

def matches_history(request):
    return render(request,"RSP/matches.html")

def top_leaders(request):
    qs = Match.objects.values('winner').annotate(victories=Count('winner')).order_by('-victories')
    data = {'data':list(qs)}
    return JsonResponse(data, safe=False)

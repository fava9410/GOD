from django.db import models

class AuditLog(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True

class Match(AuditLog):
    winner = models.CharField(max_length = 50,  null = True, blank = True)
    number_of_rounds = models.IntegerField(null = False, blank = False)
    final_score = models.CharField(max_length = 10, null = True, blank = True)

class Match_Detail(AuditLog):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, null = False, blank = False, related_name = 'match_id')
    round = models.IntegerField(null = False, blank = False)
    round_winner = models.CharField(max_length = 50, null = False, blank = False)
    winner_move = models.CharField(max_length = 50, null = False, blank = False)

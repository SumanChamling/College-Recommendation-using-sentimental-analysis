from django.db import models
from .collegereview import Review
from .AddCollege import AddColleges

class Review_College(models.Model):
    addcollege_id = models.ForeignKey(Review, on_delete=models.CASCADE)
    collegereview_id = models.ForeignKey(AddColleges, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.collegereview_id


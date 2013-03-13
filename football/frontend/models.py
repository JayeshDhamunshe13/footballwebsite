from django.db import models

class Player(models.Model):
        """
        Register's Players
        """
        username = models.CharField(max_length=50)
        age =models.IntegerField(max_length=4)
        phoneno = models.IntegerField(max_length=10)
        email = models.EmailField(max_length=75)
        address = models.CharField(max_length=300)

        def __unicode__(self):
            return '{}'.format(self.username)

        def register(self, username, age, phoneno, email, address):
            """
            This function register players
            """
            if username != None and age != None and phoneno != None and email != None and address !=None:

                if Players.objects.filter(email=email):
                    return 5

                if Players.objects.filter(username=username):
                    return 2

                if not varify_email(email):
                    return 8

                playerobj = Players.objects.create(username=username, age=age , phoneno=phoneno, email=email, address=address)
                playerobj.save()

                return 1
            return 0

class Coach(models.Model):
        """
        Register's Coach
        """
        username = models.CharField(max_length=50)
        age =models.IntegerField(max_length=4)
        phoneno = models.IntegerField(max_length=10)
        email = models.EmailField(max_length=75)
        address = models.CharField(max_length=300)

        def __unicode__(self):
            return '{}'.format(self.username)

        def register(self, username, age, phoneno, email, address):
            """
            This function register coach
            """
            if username != None and age != None and phoneno != None and email != None and address !=None:

                if Coach.objects.filter(email=email):
                    return 5

                if Coach.objects.filter(username=username):
                    return 2

                if not varify_email(email):
                    return 8

                coachobj = Coach.objects.create(username=username, age=age, phoneno=phoneno, email=email, address=address)
                coachobj.save()

                return 1
            return 0

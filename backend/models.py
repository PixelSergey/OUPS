from django.db import models

class Letter(models.Model):
    class Colleges(models.TextChoices):
        all_souls = ("all_souls", "All Souls College")
        balliol = ("balliol", "Balliol College")
        blackfriars = ("blackfriars", "Blackfriars")
        brasenose = ("brasenose", "Brasenose College")
        campion_hall = ("campion_hall", "Campion Hall")
        christ_church = ("christ_church", "Christ Church")
        corpus_christi = ("corpus_christi", "Corpus Christi College")
        exeter = ("exeter", "Exeter College")
        green_templeton = ("green_templeton", "Green Templeton College")
        harris_manchester = ("harris_manchester", "Harris Manchester College")
        hertford = ("hertford", "Hertford College")
        jesus = ("jesus", "Jesus College")
        keble = ("keble", "Keble College")
        kellogg = ("kellogg", "Kellogg College")
        lady_margaret_hall = ("lady_margaret_hall", "Lady Margaret Hall")
        linacre = ("linacre", "Linacre College")
        lincoln = ("lincoln", "Lincoln College")
        magdalen = ("magdalen", "Magdalen College")
        mansfield = ("mansfield", "Mansfield College")
        merton = ("merton", "Merton College")
        new = ("new", "New College")
        nuffield = ("nuffield", "Nuffield College")
        oriel = ("oriel", "Oriel College")
        pembroke = ("pembroke", "Pembroke College")
        queens = ("queens", "The Queen's College")
        regents_park = ("regents_park", "Regent's Park College")
        reuben = ("reuben", "Reuben College")
        st_annes = ("st_annes", "St Anne's College")
        st_antonys = ("st_antonys", "St Antony's College")
        st_catherines = ("st_catherines", "St Catherine's College")
        st_cross = ("st_cross", "St Cross College")
        st_edmund_hall = ("st_edmund_hall", "St Edmund Hall")
        st_hildas = ("st_hildas", "St Hilda's College")
        st_hughs = ("st_hughs", "St Hugh's College")
        st_johns = ("st_johns", "St John's College")
        st_peters = ("st_peters", "St Peter's College")
        somerville = ("somerville", "Somerville College")
        trinity = ("trinity", "Trinity College")
        university = ("university", "University College")
        wadham = ("wadham", "Wadham College")
        wolfson = ("wolfson", "Wolfson College")
        worcester = ("worcester", "Worcester College")
        wycliffe_hall = ("wycliffe_hall", "Wycliffe Hall")

    class LetterStatus(models.IntegerChoices):
        SENT = 0
        ASSIGNED = 1
        DELIVERED = 2
        READ = 3
    
    addressee = models.CharField(max_length=50)
    college = models.CharField(max_length=25, choices=Colleges.choices)
    message = models.CharField(max_length=280)
    status = models.IntegerField(choices=LetterStatus)
    submitted_at = models.TimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return f"Message (currently {self.status}) to {self.addressee} at {self.college}: {self.message}"


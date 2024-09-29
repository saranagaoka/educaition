from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

from notes.models import Subject, Topic

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        data = {
            'Matematyka': [
                'Zastosowanie funkcji kwadratowej w praktycznych problemach',
                'Twierdzenie Pitagorasa i jego zastosowanie w geometrii płaskiej',
                'Liczby zespolone i ich zastosowania w fizyce',
                'Wprowadzenie do rachunku różniczkowego – pochodne funkcji',
                'Statystyka i prawdopodobieństwo – analiza danych na przykładzie sondaży',
                'Macierze i ich zastosowanie w kryptografii',
                'Geometria analityczna – równanie prostej i okręgu w układzie współrzędnych',
                'Zastosowanie ciągów arytmetycznych i geometrycznych w ekonomii',
                'Funkcje trygonometryczne i ich rola w fizyce i inżynierii',
                'Układy równań liniowych – metody rozwiązywania i zastosowania',
            ],
            'Biologia': [
                'Budowa i funkcje komórki roślinnej i zwierzęcej',
                'Proces fotosyntezy – znaczenie dla roślin i życia na Ziemi',
                'Układ krwionośny człowieka – budowa i funkcjonowanie',
                'Rola enzymów w procesach metabolicznych organizmów',
                'Dziedziczenie cech – podstawy genetyki',
                'Rozmnażanie się organizmów – porównanie rozmnażania płciowego i bezpłciowego',
                'Ekosystem – struktura i funkcje',
                'Znaczenie bioróżnorodności dla stabilności ekosystemów',
                'Budowa i funkcje układu nerwowego człowieka',
                'Zjawisko ewolucji – mechanizmy i dowody ewolucji',
            ],
            'Chemia': [
                'Budowa atomu i układ okresowy pierwiastków',
                'Reakcje chemiczne – typy reakcji i ich równania',
                'Właściwości kwasów i zasad – reakcje chemiczne i zastosowanie',
                'Alkany, alkeny, alkiny – budowa i właściwości węglowodorów',
                'Woda jako rozpuszczalnik – znaczenie chemiczne i biologiczne',
                'Reakcje utleniania i redukcji – przykłady w przyrodzie i technice',
                'Równowaga chemiczna – zasady i przykłady zastosowania w praktyce',
                'Polimery – budowa, właściwości i zastosowanie w życiu codziennym',
                'Chemia organiczna – podstawowe grupy funkcyjne związków organicznych',
                'Związki chemiczne w żywności – analiza i znaczenie dla zdrowia człowieka',
            ],
            'Fizyka': [
                'Zasady dynamiki Newtona i ich zastosowanie w życiu codziennym',
                'Prawo Archimedesa – dlaczego statki pływają, a balony latają',
                'Energia kinetyczna i potencjalna – przykłady zastosowań w technice',
                'Zjawisko odbicia i załamania światła – podstawy optyki',
                'Ruch falowy – fale dźwiękowe i ich właściwości',
                'Elektromagnetyzm – pole elektryczne i magnetyczne oraz ich zastosowania',
                'Termodynamika – prawo zachowania energii i zastosowanie w silnikach cieplnych',
                'Zjawisko fotoelektryczne – wstęp do mechaniki kwantowej',
                'Grawitacja – prawa Keplera i ruch planet wokół Słońca',
                'Prąd elektryczny – obwody elektryczne, napięcie, natężenie i opór',
            ]
        }

        user = User.objects.get(email='kamil@example.com')

        for subject_name, topic_names in data.items():
            subject, _ = Subject.objects.get_or_create(name=subject_name, owner=user)

            for topic_name in topic_names:
                topic, _ = Topic.objects.get_or_create(subject=subject, name=topic_name, owner=user)

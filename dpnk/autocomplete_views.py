from dal import autocomplete

from .models import (Company, Subsidiary, Team)


class CompanyAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Company.objects.none()

        qs = Company.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


class SubsidiaryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Subsidiary.objects.none()

        qs = Subsidiary.objects.all()

        company = self.forwarded.get('company', None)

        if company:
            qs = qs.filter(company=company)
        else:
            return Subsidiary.objects.none()

        if self.q:
            qs = sorted(
                (s for s in qs.all() if self.q.lower() in s.name().lower()),
                key=lambda s: s.name().lower(),
            )

        return qs


class TeamAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Team.objects.none()

        qs = Team.objects.all()

        subsidiary = self.forwarded.get('subsidiary', None)

        if subsidiary:
            qs = qs.filter(subsidiary=subsidiary, campaign=self.request.campaign)
        else:
            return Team.objects.none()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

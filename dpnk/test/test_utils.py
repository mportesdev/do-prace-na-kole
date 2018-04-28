# -*- coding: utf-8 -*-

# Author: Petr Dlouhý <petr.dlouhy@auto-mat.cz>
#
# Copyright (C) 2016 o.s. Auto*Mat
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
import datetime

from django.conf import settings
from django.test import TestCase
from django.test.utils import override_settings

from dpnk import util
from dpnk.models import Campaign


@override_settings(
    FAKE_DATE=datetime.date(year=2010, month=11, day=20),
)
class UtilTests(TestCase):
    fixtures = ['sites', 'campaign', 'auth_user', 'users']

    def test_day_active_last(self):
        campaign = Campaign.objects.get(pk=339)
        self.assertTrue(util.day_active_last(datetime.date(2010, 11, 14), campaign))
        self.assertTrue(util.day_active_last(datetime.date(2010, 11, 20), campaign))
        self.assertFalse(util.day_active_last(datetime.date(2010, 11, 13), campaign))
        self.assertFalse(util.day_active_last(datetime.date(2010, 11, 21), campaign))

    def test_day_active_last_cut_after_may(self):
        campaign = Campaign.objects.get(pk=339)
        self.assertTrue(util.day_active_last_cut_after_may(datetime.date(2010, 11, 14), campaign))
        self.assertTrue(util.day_active_last_cut_after_may(datetime.date(2010, 11, 20), campaign))
        self.assertFalse(util.day_active_last_cut_after_may(datetime.date(2010, 11, 13), campaign))
        self.assertFalse(util.day_active_last_cut_after_may(datetime.date(2010, 11, 21), campaign))

    @override_settings(
        FAKE_DATE=datetime.date(year=2016, month=6, day=3),
    )
    def test_day_active_last_cut_after_may_may(self):
        campaign = Campaign.objects.get(pk=339)
        self.assertTrue(util.day_active_last_cut_after_may(datetime.date(2016, 6, 1), campaign))
        self.assertTrue(util.day_active_last_cut_after_may(datetime.date(2016, 6, 3), campaign))
        self.assertFalse(util.day_active_last_cut_after_may(datetime.date(2016, 5, 31), campaign))
        self.assertFalse(util.day_active_last_cut_after_may(datetime.date(2016, 6, 4), campaign))

    @override_settings(
        FAKE_DATE=datetime.date(year=2016, month=6, day=7),
    )
    def test_day_active_last_cut_after_may_may9(self):
        campaign = Campaign.objects.get(pk=339)
        self.assertTrue(util.day_active_last_cut_after_may(datetime.date(2016, 6, 1), campaign))
        self.assertTrue(util.day_active_last_cut_after_may(datetime.date(2016, 6, 7), campaign))
        self.assertFalse(util.day_active_last_cut_after_may(datetime.date(2016, 5, 31), campaign))
        self.assertFalse(util.day_active_last_cut_after_may(datetime.date(2016, 6, 8), campaign))

    def test_working_day(self):
        self.assertTrue(util.working_day(datetime.date(2016, 6, 1)))
        self.assertFalse(util.working_day(datetime.date(2020, 5, 1)))
        self.assertFalse(util.working_day(datetime.date(2034, 5, 8)))
        self.assertFalse(util.working_day(datetime.date(2018, 1, 20)))
        self.assertTrue(util.working_day(datetime.date(2018, 1, 19)))
        self.assertFalse(util.working_day(datetime.date(2018, 5, 8)))
        self.assertFalse(util.working_day(datetime.date(2018, 5, 1)))


class TodayTests(TestCase):
    def test_today(self):
        if hasattr(settings, 'FAKE_DATE'):
            del settings.FAKE_DATE  # pragma: no cover
        self.assertEquals(util._today(), datetime.date.today())


class FormatPSCTests(TestCase):
    def test_format_psc(self):
        """ Test format_psc function """
        self.assertEqual(util.format_psc(12345), "123 45")
        self.assertEqual(util.format_psc(12345678), "123456 78")
        self.assertEqual(util.format_psc(0), "0")
        self.assertEqual(util.format_psc(None), "")

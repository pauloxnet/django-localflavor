# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

# areas are divided into governorates

AREA_CHOICES = \
    (
        (_('Kuwait City'),
         (
             ('AS', _('Abdullah Al-Salem')),
             ('AD', _('Adailiya')),
             ('BQ', _('Bneid Al Qar')),
             ('DY', _('Daiya')),
             ('DS', _('Dasma')),
             ('DN', _('Dasman')),
             ('DH', _('Doha')),
             ('FH', _('Faiha')),
             ('GR', _('Granada')),
             ('JA', _('Jaber Al Ahmad')),
             ('JB', _('Jibla')),
             ('KF', _('Kaifan')),
             ('KH', _('Khaldiya')),
             ('KC', _('Kuwait City')),
             ('KZ', _('Kuwait Free Trade Zone')),
             ('MS', _('Mansouriya')),
             ('MR', _('Mirqab')),
             ('MC', _('Mubarekiya Camps')),
             ('NT', _('Nahdha')),
             ('NS', _('North West Al-Sulaibikhat')),
             ('NZ', _('Nuzha')),
             ('QD', _('Qadsiya')),
             ('QA', _('Qairawan')),
             ('QT', _('Qortuba')),
             ('RW', _('Rawda')),
             ('SH', _('Salhiya')),
             ('SM', _('Shamiya')),
             ('SQ', _('Sharq')),
             ('SA', _('Shuwaikh Administrative')),
             ('SI', _('Shuwaikh Industrial')),
             ('SR', _('Shuwaikh Residential')),
             ('ST', _('Sulaibikhat')),
             ('SU', _('Surra')),
             ('YR', _('Yarmouk')),
        )),
        (_('Farwaniya'),
         (
             ('AB', _('Abbasiya')),
             ('AM', _('Abdullah Al Mubarak Al Sabah')),
             ('AK', _('Abraq Khaitan')),
             ('DJ', _('Al-Dajeej')),
             ('SD', _('Al-Shadadiya')),
             ('AN', _('Andalous')),
             ('AR', _('Ardiya')),
             ('AI', _('Ardiya Small Industrial')),
             ('AZ', _('Ardiya Storage Zone')),
             ('FR', _('Farwaniya')),
             ('FD', _('Firdous')),
             ('IS', _('Ishbiliya')),
             ('JS', _('Jeleeb Al-Shuyoukh')),
             ('KT', _('Khaitan')),
             ('OM', _('Omariya')),
             ('RA', _('Rabia')),
             ('RI', _('Rai')),
             ('RH', _('Rehab')),
             ('RG', _('Rigai')),
             ('SN', _('Sabah Al Nasser')),
             ('SK', _('South Khaitan - Exhibits')),
        )),
        (_('Mubarak Al Kabir'),
         (
             ('AH', _('Abu Al Hasaniya')),
             ('AF', _('Abu Fatira')),
             ('AA', _('Adan')),
             ('MS', _('Al-Masayel')),
             ('CS', _('Coast Strip B')),
             ('FN', _('Fnaitees')),
             ('ME', _('Messila')),
             ('MK', _('Mubarak Al Kabeer')),
             ('QU', _('Qurain')),
             ('QS', _('Qusor')),
             ('SS', _('Sabah Al Salem')),
             ('SL', _('Sabhan Industrial Area')),
             ('SW', _('South Wista')),
             ('WA', _('West Abu Fatira Small Industrial')),
        )),
        (_('Hawally'),
         (
             ('AQ', _('Al-Siddeeq')),
             ('AJ', _('Anjafa')),
             ('BY', _('Bayan')),
             ('HT', _('Hateen')),
             ('HW', _('Hawally')),
             ('JR', _('Jabriya')),
             ('MH', _('Maidan Hawally')),
             ('MI', _('Mishref')),
             ('MA', _('Mubarak Al-Abdullah')),
             ('RU', _('Rumaithiya')),
             ('AL', _('Al-Salam')),
             ('SY', _('Salmiya')),
             ('LW', _('Salwa')),
             ('SB', _('Shaab')),
             ('DA', _('Shuhada')),
             ('ZH', _('Zahra')),
        )),
        (_('Ahmadi'),
         (
             ('BH', _('Abu Halifa')),
             ('MD', _('Ahmadi')),
             ('KI', _('Al Khiran')),
             ('AW', _('Al Wafrah')),
             ('JU', "Al-Julaia_'a"),
             ('NU', _('Al-Nuwaiseeb')),
             ('RQ', _('Al-Riqqa')),
             ('SE', _('Ali Sabah Al Salem')),
             ('HI', _('Assabahiyah')),
             ('BN', _('Bnaider')),
             ('DR', _('Dahar')),
             ('EQ', _('Eqaila')),
             ('FA', _('Fahad Al Ahmad')),
             ('FE', _('Fahaheel')),
             ('FI', _('Fintas')),
             ('HD', _('Hadiya')),
             ('JI', _('Jaber Al Ali')),
             ('MB', _('Mahboula')),
             ('MG', _('Mangaf')),
             ('BA', _('Sabah Al Ahmad')),
             ('DU', _('Al Dubaiya')),
             ('MU', _('Mina Abdullah')),
             ('HU', _('Shuaiba Block 1')),
             ('WI', _('West Industrial Shuaiba')),
             ('ZR', _('Zour')),
        )),
        (
            _('Jahra'), (
                ('S1', _('Al Sulaibiya Industrial 1')),
                ('S2', _('Al Sulaibiya Industrial 2')),
                ('IA', _('Amgarah Industrial Area')),
                ('JH', _('Jahra')),
                ('NA', _('Naeem')),
                ('NM', _('Naseem')),
                ('OY', _('Oyoun')),
                ('QR', _('Qasr')),
                ('BD', _('Saad Al Abdullah')),
                ('S0', _('Sulaibiya')),
                ('TA', _('Taima\'')),
                ('WH', _('Waha')),
            )
        ),
    )

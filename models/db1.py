# -*- coding: utf-8 -*-
db.define_table(
    'kablo_tv',
    Field('sirket_id','integer',label='Şirket id',requires=IS_NOT_EMPTY()),
    Field('sirket_adi','string',label='Şirket Adı',requires=IS_NOT_EMPTY()),
    Field('kapsama_alani','string',label='Kapsama Alanı',requires=IS_NOT_EMPTY()),
    Field('tel','string',label='Tel',requires=IS_NOT_EMPTY()),
    Field('mail','string',label='Mail',requires=IS_NOT_EMPTY()),
    Field('satis_yeri','string',label='Satış Yeri',requires=IS_NOT_EMPTY()),
    format='%(sirket_adi)s')

db.define_table(
    'tv_paketleri',
    Field('tv_paket_id','integer',label='Paket id',requires=IS_NOT_EMPTY()),
    Field('tv_sirket_adi',db.kablo_tv,label='Şirket Adı'),
    Field('tv_paket_adi','string',label='Paket Adı',requires=IS_NOT_EMPTY()),
    Field('kanal_sayisi','integer',label='Kanal Sayısı',requires=IS_NOT_EMPTY()),
    Field('goruntu_kalitesi',label='Görüntü Kalitesi',requires=IS_IN_SET(('4K','1080p','HD','SD'))),
    Field('paket_suresi','datetime',default=request.now),
    Field('kurulum_ucreti','integer',label='Kurulum Ücreti',requires=IS_NOT_EMPTY()),
    Field('promosyon',label='Promosyon',requires=IS_IN_SET(('var','yok'))),
    format='%(tv_paket_adi)s')

db.define_table(
    'internet_paketleri',
    Field('internet_paket_id','integer',label='Paket id',requires=IS_NOT_EMPTY()),
    Field('internet_sirket_adi',db.kablo_tv,label='Şirket Adı'),
    Field('internet_paket_adi','string',label='Paket Adı',requires=IS_NOT_EMPTY()),
    Field('akk',label='AKK',requires=IS_IN_SET(('3mbit','6mbit'))),
    Field('internet_hizi',label='İnternet Hızı',requires=IS_IN_SET(('16mbit/s','32mbit/s','100mbit/s','1gbit/s'))),
    Field('kurulum_ucreti','integer',label='Kurulum Ücreti',requires=IS_NOT_EMPTY()),
    Field('sure',label='Aylık Süre',requires=IS_IN_SET(('1 ay','3 ay','6 ay','12 ay'))),
    format='%(internet_paket_adi)s')

db.define_table(
    'uye',
    Field('uye_id','integer',label='Uye id',requires=IS_NOT_EMPTY()),
    Field('adi_soyadi','string',label='Adı Soyadı',requires=IS_NOT_EMPTY()),
    Field('uye_tel','string',label='Tel'),
    Field('il','string',label='İl',requires=IS_NOT_EMPTY()),
    Field('uye_tv_paketi',db.tv_paketleri,label='TV Paketi'),
    Field('uye_internet_paketi',db.internet_paketleri,label='İnternet Paketi'))

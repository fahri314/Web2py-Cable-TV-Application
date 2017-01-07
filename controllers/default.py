# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------

def index():
    form1 = SQLFORM(db.kablo_tv).process()
    form2 = SQLFORM(db.tv_paketleri).process()
    form3 = SQLFORM(db.internet_paketleri).process()
    form4 = SQLFORM(db.uye).process()
    return locals()

def show_kablo_tv():
    rows = db(db.kablo_tv).select()
    if request.vars.sil:
        del db.kablo_tv[request.vars.sil]
        redirect(URL('show_kablo_tv'))
        response.flash='Veri Silindi'
    return locals()

def show_tv_paketleri():
    rows = db(db.tv_paketleri).select()
    if request.vars.sil:
        del db.tv_paketleri[request.vars.sil]
        redirect(URL('show_tv_paketleri'))
        response.flash='Veri Silindi'
    return locals()

def show_internet_paketleri():
    rows = db(db.internet_paketleri).select()
    if request.vars.sil:
        del db.internet_paketleri[request.vars.sil]
        redirect(URL('show_internet_paketleri'))
        response.flash='Veri Silindi'
    return locals()

def show_uye():
    rows = db(db.uye).select()
    if request.vars.sil:
        del db.uye[request.vars.sil]
        redirect(URL('show_uye'))
        response.flash='Veri Silindi'
    return locals()

def edit_kablo_tv():
    record=None
    if request.vars.edit:
        record = db.kablo_tv[request.vars.edit]
        form = SQLFORM(db.kablo_tv,record)
        form.add_button('İptal','index')
    if form.process().accepted:
        if record:
            session.flash = 'Şirket Güncellendi'
        else:
            session.flash = 'Kayıt Tamamlandı'
        redirect(URL('index'))
    return {'form':form}

def edit_tv_paketleri():
    record=None
    if request.vars.edit:
        record = db.tv_paketleri[request.vars.edit]
        form = SQLFORM(db.tv_paketleri,record)
        form.add_button('İptal','index')
    if form.process().accepted:
        if record:
            session.flash = 'TV Paketi Güncellendi'
        else:
            session.flash = 'Kayıt Tamamlandı'
        redirect(URL('index'))
    return {'form':form}

def edit_internet_paketleri():
    record=None
    if request.vars.edit:
        record = db.internet_paketleri[request.vars.edit]
        form = SQLFORM(db.internet_paketleri,record)
        form.add_button('İptal','index')
    if form.process().accepted:
        if record:
            session.flash = 'İnternet Paketi Güncellendi'
        else:
            session.flash = 'Kayıt Tamamlandı'
        redirect(URL('index'))
    return {'form':form}

def edit_uye():
    record=None
    if request.vars.edit:
        record = db.uye[request.vars.edit]
        form = SQLFORM(db.uye,record)
        form.add_button('İptal','index')
    if form.process().accepted:
        if record:
            session.flash = 'Uye Güncellendi'
        else:
            session.flash = 'Kayıt Tamamlandı'
        redirect(URL('index'))
    return {'form':form}

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

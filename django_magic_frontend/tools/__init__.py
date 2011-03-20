def build_generic_CRUD_urls(models):
    from django.conf.urls.defaults import url, patterns
    r=[]
    for model in models:
        #~ print model().build_generic_CRUD_urls(model)
        r.extend(model().build_generic_CRUD_urls(model))
    print r
    return r
        

from django.shortcuts import render_to_response
from django.template import RequestContext

def create_object_related(request,  model=None, form_class=None, #foreign_model=None,
    foreign_id=0,foreign_model=None, foreign_field_name='',#~ initial={}
    extra_context={},template_name=None,post_save_redirect=None, ajax=None):
    """
    This view allows you to add an object that belongs to a father model. 
    In the template you won't view the foreign key field. It will take the 
    parent id automatically. 
    """
    from django.views.generic.create_update import get_model_and_form_class
    from django.views.generic.create_update import redirect
    from django.utils.translation import ugettext
    #~ if login_required and not request.user.is_authenticated():
        #~ return redirect_to_login(request.path)
    model, form_class = get_model_and_form_class(model, form_class)
    if request.method == 'POST':
        if not post_save_redirect:
            try:
                post_save_redirect=foreign_model.objects.get(pk=foreign_id).get_absolute_url()
            except:
                pass
        form = form_class(request.POST, request.FILES)
        del form.fields[foreign_field_name]
        if form.is_valid():
            new_object = form.save(commit=False)
            #~ new_object.contact=foreign_id
            setattr(new_object,foreign_field_name+'_id',foreign_id)
            new_object.save()
            msg = ugettext("The %(verbose_name)s was created successfully.") %\
                                    {"verbose_name": model._meta.verbose_name}
            #~ messages.success(request, msg, fail_silently=True)
            return redirect(post_save_redirect, new_object)
    else:
        form = form_class()
        del form.fields[foreign_field_name]
    # Create the template, context, response
    if not template_name:
        template_name = "%s/%s_form.html" % (model._meta.app_label, model._meta.object_name.lower())
    return render_to_response(template_name, {'foreign_id':foreign_id,'form': form,'opts':model._meta}, context_instance=RequestContext(request))

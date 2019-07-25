from pyramid.view import view_config


@view_config(route_name='home', renderer='../templates/mytemplate.mako')
def my_view(request):
    return {'project': 'rankpage'}

@view_config(route_name='rankpage', renderer='../templates/rankpage.mako')
def my_view_rank(request):
    return {'project': 'rankpage'}

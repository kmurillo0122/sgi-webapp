"""



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login_view'),
    path('base/', views.baseAdmin_view, name='baseAdmin_view'),
    path('regUsuario/', views.registroUsuario_view, name='registroUsuario_view'),
    path('formPrestamos/', views.formPrestamos_view, name='formPrestamos_view'),
    path('formElementos/', views.formElementos_view, name='formElementos_view'),
    path('consultarUsuario/', views.consultarUsuario_view, name='consultarUsuario_view'),
    path('listarPrestamo/', views.listar_prestamos, name='listar_prestamos'),

]

# Configuración para servir archivos multimedia en entorno de desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

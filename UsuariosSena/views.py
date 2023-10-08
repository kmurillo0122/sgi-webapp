from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import UsuariosSenaForm, LoginForm, ElementosForm, PrestamosForm
from .models import UsuariosSena, Prestamo


# Create your views here.

def login_view(request):
    return render(request, 'indexLogin.html')

def baseAdmin_view(request):
    return render(request, 'superAdmin/basesuadmin.html')

def registroUsuario_view(request):
    return render(request, 'superAdmin/registroUsuario.html')

def formPrestamos_view(request):
    return render(request, 'superAdmin/formPrestamos.html')

def formElementos_view(request):
    return render(request, 'superAdmin/formElementos.html')

def consultarUsuario_view(request):
    return render(request, 'superAdmin/consultarUsuario.html')


#prueba de loginnnnnnnnnnn
def login_view(request):
    if request.method == 'POST':
        # Procesa el formulario si se envió
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            # Aquí puedes realizar acciones adicionales, como la autenticación
            # Si el formulario es válido, redirige al usuario a la página de inicio o a donde sea necesario.
            return HttpResponseRedirect('baseAdmin_view')
    else:
        # Renderiza un formulario vacío si no se envió uno
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})


#Esto funcionaaaaaaaa

def registroUsuario_view(request):

    if request.method == 'POST':

        nombreVar=request.POST.get('nombre')
        apellidoVar=request.POST.get('apellidoo')
        tipoIdentificacionVar=request.POST.get('tipoIdentificacion')
        numeroIdentificacionVar=request.POST.get('numeroIdentificacion')
        correoSenaVar=request.POST.get('correoSena')
        celularVar=request.POST.get('celular')
        rolVar=request.POST.get('rol')
        cuentadanteVar=request.POST.get('cuentadante')
        tipoContratoVar=request.POST.get('tipoContrato')
        duracionContratoVar=request.POST.get('cantidad')
        contraSenaVar=request.POST.get('contraSena')
        validacionContraSenaVar = request.POST.get('validacionContraSena')
        fotoUsuarioVar=request.POST.get('fotoUsuario')

        user= UsuariosSena(nombre=nombreVar, apellidoo=apellidoVar, tipoIdentificacion=tipoIdentificacionVar, numeroIdentificacion=numeroIdentificacionVar, correoSena=correoSenaVar, celular=celularVar, rol=rolVar, cuentadante=cuentadanteVar, tipoContrato=tipoContratoVar, duracionContrato=duracionContratoVar, contraSena=contraSenaVar, validacionContraSena=validacionContraSenaVar, fotoUsuario=fotoUsuarioVar)
        user.save()

        variable = UsuariosSena.objects.get(id = 1)

        print(variable.apellidoo)



    return render(request, 'superAdmin/registroUsuario.html')

def formPrestamos_view(request):
    
    if request.method == 'POST':

        fechaEntregaVar=request.POST.get('fechaEntrega')
        fechaDevolucionVar=request.POST.get('fechaDevolucion')
        #serialSenaElementoVar=request.POST.get('serialSenaElemento')
        #nombreVar=request.POST.get('nombre')
        observacionesPrestamoVar=request.POST.get('observacionesPrestamo')

        user= Prestamo(fechaEntrega=fechaEntregaVar, fechaDevolucion=fechaDevolucionVar, observacionesPrestamo=observacionesPrestamoVar)
        user.save()

    return render(request, 'superAdmin/formPrestamos.html')

def listar_prestamos(request):
    prestamos = Prestamo.objects.all()
    return render(request, 'superAdmin/listarPrestamos.html', {'prestamos': prestamos})


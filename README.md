 <h1>Desarrollo de un modelo de Blog</h1>

Es proyecto consiste en un canal en donde se puedan volcar opiniones y comentarios de propósito general de forma de interactuar con cualquier usuario del modelo.

El tipo de interacción permitirá lograr conectar información entre usuarios mediante la publicación de temas específicos o libres.

El objetivo general de esta publicación es el desarrollo de un WebBlog utilizando el lenguaje de programación Python y el framework Django a través del uso de un patrón MVT.

<h6>Autor</h6>
<h6>Daniel Collao</h6>

Para el uso de la base de datos los usuarios son: 
SUPERUSUARIO : danielcollao 
PASSWORD : 123123Dc

USUARIO : ADMIN
PASSWORD : 123123Dc

<h1>Uso de la Aplicación</h1>
En primer lugar para asegurar que funcionará sin inconvenientes, se sugiere la creación
de un entorno virtual, con el fin de mantener los mismos requerimientos donde se ha desarrollado la aplicación.
Comandos a ejecutar para crear el entorno virtual
Solo la primera vez:
pip install virtualenv
virtualenv --version
virtualenv <nombre del entorno a crear>

Cada vez que se quiera utilizar la Aplicación:
env\Scripts\activate <env>
venv\Scripts\activate

<h6>Requerimientos: Django==4.1</h6>

<h1>Funcionalidades de la Aplicación</h1>
La aplicación inicia con un menú compuesto por diferentes opciones que son explicadas a continuación.

<h2>Inicio</h2>
Seleccionando esta opción permite volver a la página Web principal de la aplicación donde se procederá a visualizar nuevamente el menú principal.

<h2>Usuarios</h2>
Eligiendo la opción Usuarios le permitirá ingresar a la página Web para dar de alta los usuarios que harán uso de la apliación de Blog. En este caso los datos que se solicitarán son
el nombre real del usuario, el nombre del usuario que utilizará en la aplicación para ingresar, su contraseña que será utilizada para validar su ingreso a la aplicación, un correo electrónico que sea representativo del usuario, la fecha del último ingreso, la fecha de registro, el día de nacimiento o cumpleaños y finalmente el estado que indicará si está activo, inactivo, bloqueado o eliminado.
Campos solicitados: nombre, usuario, password, email, lastlogin, dateregistro, datecupleanho estado.

<h2>Categorías</h2>
En la sección de categorías se pueden dar de alta las diversas categorías de los ingresos o post que se vayan realizando de forma de poder clasificarlos en base a esta opción y así a futuro poder realizar un filtrado de los ingresos realizados hasta el momento. En este caso los atributos que se utilizan corresponden al nombre que identifica a la categoría y a la relación con el posteo correspondiente para su clasificación.
Campos solicitados: nombre y parent.
    
<h2>Búsqueda</h2>
En el apartado de búsqueda se puede proceder a realizar la búsqueda de un usuario en particular. Este proceso se realiza con los usuarios que ya están dados de alta en el sistema de WebBlog analizando la información que contiene la base de datos.

<h2>OBSERVACIONES</h2>
 - El formulario de contacto no envia mails ya que se debe colocar la clave del correo 
 - 

<h2>PROXIMMA VERSIÓN </h2>
<ul>
<li>Poder realizar comentarios en cada post una vez estando logeado</li>
<li>Poder mostrar en el menú, las categorias que se ingresen</li>
<li>Poder mostrar los post hacia el lado y no hacia abajo</li>
<li>Poder mostrar en el menú, las categorias que se ingresen</li>
<li>Poder mostrar los awesome</li>
<li>Poder mostrar la cantidad de comentarios sin leer</li>
<li>Poder dar like en los post</li>
</ul>
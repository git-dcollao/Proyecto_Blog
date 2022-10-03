 <h1>Desarrollo de un modelo de Blog</h1>

Es proyecto consiste en un canal en donde se puedan volcar opiniones y comentarios de propósito general de forma de interactuar con cualquier usuario del modelo.

El tipo de interacción permitirá lograr conectar información entre usuarios mediante la publicación de temas específicos o libres.

El objetivo general de esta publicación es el desarrollo de un WebBlog utilizando el lenguaje de programación Python y el framework Django a través del uso de un patrón MVT.

<h6>Autores</h6>
<h6>Daniel Collao</h6>

Para el uso de la base de datos el usuario es admin y la clave: XXXXX

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
    
<h2>Etiquetas</h2>
En la sección de etiquetas se pueden dar de alta las diferentes formas de marcar los mensajes que se vayan incorporando al WebBlog, por un lado un posteo tiene una categoría definida pero puede tener varias etiquetas que lo representen, de forma de realizar un proceso de búsqueda que filtre en una forma más adecuada los contenidos y así encontrar más fácilmente los diversos mensajes involucrados. En este caso los campos que se utilizan para su alta son la etiqueta correspondiente y la relación con los mensajes o posteos realizados. 
Campos solicitados: tag y relacion

<h2>Búsqueda</h2>
En el apartado de búsqueda se puede proceder a realizar la búsqueda de un usuario en particular. Este proceso se realiza con los usuarios que ya están dados de alta en el sistema de WebBlog analizando la información que contiene la base de datos.

<h6>Por el momento los formularios para la generación de posteos y los correspondientes comentarios no han sido implementados ya que serán incorporados en próximas versiones</h6>

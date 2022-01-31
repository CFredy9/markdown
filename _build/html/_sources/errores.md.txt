# ERRORES COMUNES
---
## <span style="color:blue"> Problema de Botón de Pánico Teltonika </span>

### Descripción:
>No funciona el botón de alerta de pánico, modelo de dispotivo: 130fmb

### Soluciones posibles:

>1. Revisar que el dispositivo apunte al puerto 6903
>2. Revisar que la entrada de ignición esté en 87A_12V

**Luego de los 2 pasos anteriores sacar la batería, volver a armarlo y enviar el comando cpureset.**

---

## <span style="color:blue"> Error en envío de comandos </span>

### Descripción:
>Al enviar comandos al dispositivo no genera la acción correspondiente, al enviarlo un número determinada de veces logra funcionar.

### Soluciones posibles:

>1. Verificar la configuración del dispositivo. 

**No es error de la plataforma, el inconveniente es que el dispositivo se desconecta cada tiempo determinado (depende de su 			configuración) y al enviar el comando no se ejecuta porque el dispositivo esta fuera de linea.**

**NOTA: Se implementará en un mediano plazo lo siguiente: Se detectará que el dispositivo esté fuera de línea y se mandará un error especificando la conectividad del dispositivo.**

---

## <span style="color:blue"> Error al iniciar sesión </span>

### Descripción:
>Al tratar de iniciar sesión la aplicación se reinicia y hay que volver a colocar los datos en en login.

### Soluciones posibles:

>1. Revisar que el usuario tenga acceso a la lista de conductores. 
>2. Revisar que la cuenta pertenezca a la versión 2.
>3. Revisar que tenga permisos del mapa, notificaciones y conductores. 

**Esto sucede porque no tiene los permisos correspondientes para iniciar sesión.**

---

## <span style="color:blue"> Error al asignar comandos </span>

### Descripción:
>A la hora de enviar comandos no manda ni aparece ninguno.

### Soluciones posibles:

>1. Darle en el botón editar y guardar los cambios.

**NOTA: Esto error ya fue solucionado, pero los dispositivos que se crearon antes del 13 de Enero tendrán este inconveniente.**

---

## <span style="color:blue"> Pasos para la integración de nuevos protocolos: </span>
1. Crear ticket.
2. Identificar adecuadamente el protocolo.
3. Enviar toda la documentación que tengan del dispositivo y del protocolo, incluyendo pdf (opcional).
4. Conectar el dispositivo y si se interpreta bien en traccar, enviar todos los eventos que quieren homologar: como encendidos de motor, apagados, temperaturas, etc.
5. Se verificará que todos los eventos que se enviaron hayan sido interpretados bien por el sistema (si no funciona correctamente pase al paso 6, si funciona se realiza el paso 7).
6. Se programa una junta con el cliente para definir de que manera trabajar.
7. Se empieza a trabajar.

---


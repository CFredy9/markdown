# ERRORES AREA TÉCNICA
---
## <span style="color:blue"> Problema Botón de Pánico Teltonika </span>

### Descripción:
>No funciona el botón de alerta de pánico, modelo de dispotivo: 130fmb

### Soluciones posibles:

>1. Revisar que en la base de datos deltatracking BD, en la tabla EquipmentCommandsQueue el status del comando sea "executed"
>2. Verificar que esté llegando información a los puertos

**Si al realizar estos pasos no se encuentra ningún error, es mala configuración de parte del cliente**

---

## <span style="color:blue"> Error en tamaño de columnas en Reporte </span>

### Descripción:
>No se logra visualizar todas las columnas porque excede el tamaño de la hoja en pdf.

### Soluciones posibles:

>1. Revisar el siguiente enlace, contiene el código que se utilizó para hacer que las columnas se ajusten al tamaño de la hoja.
>>[Ver Código](https://bitbucket.org/deltaGT/report-builder/commits/2b18dc838473cfa4bc4fdca524f835d500f3e7bb)
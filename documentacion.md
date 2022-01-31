# DOCUMENTACIÓN
---
## <span style="color:blue"> Pasos para homologación de dispositivos: </span>

1. Tener los datos tomados desde Traccar, que lleguen bien y que tengamos dispositivos marcando, mejor si nos envían pruebas de todo lo que necesiten validar, alarmas, encendidos y apagados (Andrea y alguno de ventas).
2. Ver que traccar no esté generando muchas tramas sin reconocer de ese puerto y de algún dispositivo en especial (Andrea).
3. Opcionalmente hay que validar si tenemos listado de comandos que podamos enviar, ésto se puede validar en el código de traccar y también cotejarlo con la documentación del dispositivo (Andrea).
4. Se verifica con los eventos que toma el Ingestor (es otra api quien procesa los datos de traccar) para validar que reconozca los eventos correctos (Andrea - Carlos).
5. Se habilita en Ingestor el paso de ese protocolo (Dhaby).
6. Hemos terminado la homologación.

---

## <span style="color:blue"> Pasos para agregar un nuevo dispositivo: </span>

1. Agregar el dispositivo a la coleccion GpsModel de erebus(deltaBD en qa) si el brand y el protocol existen solo se agrega el brandID y el protocolID, si no deben crearse en sus respectivas colecciones de erebus (Brand , Protocol) y se agregan los ids generados.
2. Agregar los comandos que se asignarán al nuevo dispositivo en la colección EquipmentTypeCommands de efesto (deltatrackingBD) usando el dato de device de GpsModel como typeID en esta colección.
3. Asignarle el configEquipmentID que corresponde en la colección EquipmentConfiguration de efesto (deltatrackingBD) normalmente se agrega un _na o _nc (esto se debe a que en la versión anterior skyguard configuraba puertos normalmente abiertos o normalmente cerrados por lo que se requieren comandos distintos para realizar determinada accion), se asigna el accountID (antes de guardar este registro ver el siguiente paso).
4. En la misma colección de EquipmentConfiguration en el campo commands se agregan los Json de los comandos que deben listarse  y mostrarse para ser enviados.
5. Comprobar que si se listan los comandos en ui.

# DOCUMENTACIÓN
---
## <span style="color:nature"> Pasos para homologación de dispositivos: </span>
~~~
1. Verificar que el protocolo esté funcionando y activo en Traccar (Andrea)
2. Verificar que tengamos tramas de éste protocolo ya recibidas con anterioridad para 
   validar que todo se esta recibiendo correctamente, de lo contrario se espera a que un 
   cliente nuevo conecte su dispositivo y se empieza a revisar los datos procesados (Andrea)
3. Se obtienen todos los datos importantes de la columna attributes, que se obtiene del 
   procesamiento de datos del protocolo
4. Se verifica en el Ingestor que el protocolo esté activado (Carlos)
5. Se valida que los datos como alarmas, encendidos, apagados, etc se estén validando 
   correctamente en el ingestor, basado en los diagramas de procesamiento de eventos del 
   ingestor (Carlos)
6. Si no se tienen todos se debe programar los que la plataforma puede procesar
7. Ya corroborada ésta parte, se puede indicar cuales son los eventos homologados del 
   protocolo.
~~~
**En caso de que alguno de éstos pasos no esté completo, la Homologación se considera incompleta, puesto que puede que solo una parte del sistema esté lista y no todo lo que usamos para procesarlo**

---

## <span style="color:nature"> Pasos para agregar un nuevo dispositivo: </span>

1. Agregar el dispositivo a la coleccion GpsModel de erebus(deltaBD en qa) si el brand y el protocol existen solo se agrega el brandID y el protocolID, si no deben crearse en sus respectivas colecciones de erebus (Brand , Protocol) y se agregan los ids generados.
2. Agregar los comandos que se asignarán al nuevo dispositivo en la colección EquipmentTypeCommands de efesto (deltatrackingBD) usando el dato de device de GpsModel como typeID en esta colección.
3. Asignarle el configEquipmentID que corresponde en la colección EquipmentConfiguration de efesto (deltatrackingBD) normalmente se agrega un _na o _nc (esto se debe a que en la versión anterior skyguard configuraba puertos normalmente abiertos o normalmente cerrados por lo que se requieren comandos distintos para realizar determinada accion), se asigna el accountID (antes de guardar este registro ver el siguiente paso).
4. En la misma colección de EquipmentConfiguration en el campo commands se agregan los Json de los comandos que deben listarse  y mostrarse para ser enviados.
5. Comprobar que si se listan los comandos en ui.

# Proyecto: Plan de Asientos Interactivo para Boda con Raspberry Pi y Lector RFID

## Descripción
Este proyecto permite mostrar de manera interactiva la asignación de asientos en una boda utilizando una Raspberry Pi y un lector RFID. Cada invitado, al presentar su tarjeta RFID, verá en una pantalla una imagen con su mesa asignada. Si el asiento no se encuentra, se mostrará una imagen general con todas las mesas.

## Estructura del Proyecto
```
|-- proyecto-seating-plan
|   |-- main.py                 # Script principal que gestiona la lectura RFID y muestra las imágenes de las mesas
|   |-- data
|   |   |-- asientos.csv        # Archivo CSV con las asignaciones de tarjetas y asientos
|   |-- images
|   |   |-- mesa1.png           # Imágenes de las mesas iluminadas
|   |   |-- mesa2.png
|   |   |-- todas_mesas.png     # Imagen con todas las mesas sin iluminar
|-- README.md                   # Archivo de documentación del proyecto
```

## Requisitos
- Raspberry Pi con sistema operativo configurado
- Lector RFID modelo RC522
- Tarjetas RFID
- Python 3 instalado en la Raspberry Pi
- Biblioteca `RPi.GPIO` y `mfrc522`
- Paquetes adicionales: `Pillow`, `tkinter`

1. **Configurar la Raspberry Pi**:
   - Actualizar el sistema:
     ```bash
     sudo apt-get update
     sudo apt-get upgrade
     ```
2. **Instalar dependencias**:
   ```bash
   sudo apt-get install python3-pip
   pip3 install spidev pillow
   git clone https://github.com/pimylifeup/MFRC522.git
   cd MFRC522
   ```

## Preparación de Archivos
1. Coloca `main.py` en la carpeta raíz del proyecto.
2. Asegúrate de que `asientos.csv` esté en la carpeta `data/` con la siguiente estructura:
    ```csv
    ID_tarjeta,Nombre,Asiento
    123456789,Juan Pérez,Mesa_1
    987654321,Ana García,Mesa_2
    ```
    ## Estructura de `asientos.csv`

3. Coloca las imágenes de las mesas en la carpeta `images/`.

## Ejecución del Proyecto
1. Conecta el lector RFID a la Raspberry Pi siguiendo la configuración adecuada de pines.
2. Ejecuta el script principal:
    ```bash
    python3 main.py
    ```
3. Cuando se lea una tarjeta RFID, el sistema buscará el asiento en `asientos.csv` y mostrará la imagen de la mesa correspondiente en la pantalla.

## Funcionamiento
- **Lectura de la tarjeta**: El script utiliza `SimpleMFRC522` para leer el ID de la tarjeta RFID.
- **Búsqueda de asiento**: La función `buscar_asiento` busca el ID en el archivo `asientos.csv`.
- **Visualización de la mesa**: La función `mostrar_imagen_mesa` carga y muestra la imagen correspondiente con `tkinter` y `Pillow`.

## Notas
- Asegúrate de que los nombres de las imágenes coincidan con las entradas en `asientos.csv`.
- `GPIO.cleanup()` se ejecuta al finalizar para evitar conflictos de pines.

## Contacto
Para más información o asistencia, por favor contacta al desarrollador del proyecto.


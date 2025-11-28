import board, time, displayio, busio, digitalio ,math

# --- Konfiguration ---
BMP_FILENAME = "test.bmp"  # Name deiner BMP-Datei
LED_COUNT = 116             # Anzahl der APA102 LEDs auf dem Streifen

APA_DATA_PIN = board.GP10
APA_CLOCK_PIN = board.GP11

IMAGE_CENTER_X = 0 # Wird später dynamisch gesetzt
IMAGE_CENTER_Y = 0 # Wird später dynamisch gesetzt

MAX_RADIUS = 0 # Wird später dynamisch gesetzt

NUM_SPOKES = 72
ANGLE_STEP_RAD = (2 * math.pi) / NUM_SPOKES

# --- Bild laden ---
try:
    bitmap = displayio.OnDiskBitmap(open(BMP_FILENAME, "rb"))
    # Nach dem Laden der Bitmap können wir die tatsächlichen Dimensionen abrufen
    IMAGE_WIDTH = bitmap.width
    IMAGE_HEIGHT = bitmap.height

    # Setzen Sie den Mittelpunkt des Bildes
    IMAGE_CENTER_X = IMAGE_WIDTH // 2
    IMAGE_CENTER_Y = IMAGE_HEIGHT // 2

    # Der maximale Radius kann z.B. die Hälfte der Bildbreite oder -höhe sein,
    # je nachdem, welche Dimension kleiner ist oder wie Sie das Bild mappen möchten.
    MAX_RADIUS = min(IMAGE_WIDTH, IMAGE_HEIGHT) // 2

    print(f"BMP geladen: {BMP_FILENAME} ({IMAGE_WIDTH}x{IMAGE_HEIGHT})")
    print(f"Zentrum: ({IMAGE_CENTER_X},{IMAGE_CENTER_Y}), Max Radius: {MAX_RADIUS}")

except Exception as e:
    print(f"Fehler beim Laden des BMP: {e}")
    print("Stellen Sie sicher, dass 'image.bmp' vorhanden und eine gültige 24/32-Bit unkomprimierte BMP ist.")
    while True:
        time.sleep(1) # Endlosschleife bei Fehler

# --- Hauptloop für die Speichengenerierung ---
print("Starte Speichengenerierung (dies ist der CPU-intensive Teil)...")
last_time = time.monotonic()
frame_count = 0

while True:
    for spoke_index in range(NUM_SPOKES):
        current_angle_rad = spoke_index * ANGLE_STEP_RAD

        for led_index in range(LED_COUNT):
            # Berechne den Radius für die aktuelle LED
            current_radius = (led_index / (LED_COUNT - 1)) * MAX_RADIUS

            # Konvertiere Polarkoordinaten zu Kartesischen Koordinaten
            x = int(IMAGE_CENTER_X + current_radius * math.cos(current_angle_rad))
            y = int(IMAGE_CENTER_Y + current_radius * math.sin(current_angle_rad))

            # Sicherstellen, dass die Koordinaten innerhalb der Bildgrenzen liegen
            x = max(0, min(x, IMAGE_WIDTH - 1))
            y = max(0, min(y, IMAGE_HEIGHT - 1))

            # Pixel aus der Bitmap lesen
            try:
                pixel_rgb = bitmap[x, y]
            except IndexError:
                # Dies sollte nicht passieren, wenn x,y korrekt begrenzt sind
                pixel_rgb = (0, 0, 0) # Schwarz bei Fehler

            # Setze den Pixel auf dem APA102 Streifen
            print(pixel_rgb)
            #pixels[led_index] = pixel_rgb
            
        # Sende die aktualisierten Pixeldaten an den Streifen
        pixels.show()
        frame_count += 1

        # Optional: Eine kurze Pause, um die CPU nicht zu überlasten
        # oder um eine sichtbare Bewegung zu simulieren, wenn nicht schnell genug
        time.sleep(0.0003) # Kleine Pause, wenn die Berechnung sehr schnell ist

    # FPS-Berechnung (zur Debugging-Hilfe)
    current_time = time.monotonic()
    if current_time - last_time >= 1.0: # Jede Sekunde FPS ausgeben
        fps = frame_count / (current_time - last_time)
        print(f"Aktuelle Speichen-FPS (Berechnung + Übertragung): {fps:.2f}")
        frame_count = 0
        last_time = current_time
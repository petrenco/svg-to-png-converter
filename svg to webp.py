import os
import cairosvg

# Папки
input_folder = r"C:\1\svg"
output_folder = r"C:\1\png"

# Создаём папку для результата
os.makedirs(output_folder, exist_ok=True)

# Проходим по всем SVG
for filename in os.listdir(input_folder):
    if filename.lower().endswith(".svg"):
        svg_path = os.path.join(input_folder, filename)
        png_filename = os.path.splitext(filename)[0] + ".png"
        png_path = os.path.join(output_folder, png_filename)

        try:
            # SVG → PNG с прозрачным фоном
            cairosvg.svg2png(
                url=svg_path,
                write_to=png_path,
                background_color="rgba(0,0,0,0)"
            )
            print(f"✅ {filename} → {png_filename}")
        except Exception as e:
            print(f"❌ Ошибка при обработке {filename}: {e}")

print("🎉 Конвертация завершена!")

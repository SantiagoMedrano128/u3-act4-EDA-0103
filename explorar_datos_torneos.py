import pandas as pd
import matplotlib.pyplot as plt

# Santiago Medrano NC 0103
# 1. Crear diccionario con datos de torneos locales
torneos_locales = {
    'id_torneo': [401, 402, 403, 404, 405, 406],
    'nombre': ['Copa Primavera', 'Liga de Verano', 'Torneo Relampago', 'Maraton Ciudad', 'Torneo de Tenis', 'Copa Invierno'],
    'deporte': ['Futbol', 'Futbol', 'Futbol', 'Atletismo', 'Tenis', 'Basquetbol'],
    'fecha_inicio': ['2024-03-01', '2024-06-01', '2024-04-15', '2024-09-01', '2024-05-10', '2024-11-01'],
    'fecha_fin': ['2024-05-30', '2024-08-30', '2024-04-16', '2024-09-01', '2024-05-15', '2024-12-30'],
    'equipos_participantes': [16, 20, 8, 500, 32, 12],
    'cuota_inscripcion': [1500, 2000, 800, 300, 500, 1200],
    'premio_primer_lugar': [10000, 15000, 3000, 5000, 4000, 8000],
    'sede': ['Deportivo Norte', 'Deportivo Sur', 'Cancha Municipal', 'Paseo Principal', 'Club Tenis', 'Gimnasio Central'],
    'estado': ['Inscripcion', 'Planificacion', 'Inscripcion', 'Planificacion', 'Inscripcion', 'Planificacion']
}

print("**Análisis Exploratorio de Datos EDA")
print("Exploratory Data Analysis por Santiago Medrano NC 0103**")
print("Crear el diccionario con 10 listas y 6 elementos")

# 2. Convertir diccionario en DataFrame
df = pd.DataFrame(torneos_locales)
print("\n--- TABLA ORIGINAL DE TORNEOS LOCALES ---")
print(df)

# 3. Exportar los datos a CSV
print("-+-+-+- Convertir el DataFrame en archivo CSV -+-+-+-")
df.to_csv(
    'torneos_locales_0103.csv',
    index=False,
    encoding='utf-8-sig'
)
print("\n✅ Archivo CSV creado correctamente")
print("-+-+ 8. Leer los datos desde el archivo CSV +-+-")
print("torneos_locales_0103.csv")

# 4. Leer el archivo CSV
df = pd.read_csv('torneos_locales_0103.csv')
print("\n--- DATOS LEÍDOS DESDE CSV ---")
print(df)
print("-+-+-+- 9. Análisis Exploratorio de Datos (EDA)-+-+-+-")

# 5. Primeros y últimos registros
print("+-+-+-+\n1. PRIMEROS REGISTROS (Head): +-+-+-+")
print(df.head(3))  # Muestra los primeros 3
print("+-+-+-+\n2. ÚLTIMOS REGISTROS (Tail): +-+-+-+")
print(df.tail(2))  # Muestra los últimos 2

# 6. Dimensiones y estructura
print("+-+-+-+ 6. Dimensiones y estructura +-+-+-+")
print(df)  # Mostrar tabla o matriz
print("\n3. DIMENSIONES (Filas, Columnas):", df.shape)
print("\n4. NOMBRES DE COLUMNAS:\n", df.columns)
print("\n5. TIPOS DE DATOS:\n", df.dtypes)
print("\n6. INFORMACIÓN GENERAL:")
df.info()

# 7. Estadísticas y limpieza
print("+-+-+-+-+- 7. ESTADÍSTICAS DESCRIPTIVAS: -+-+-+-+-+")
print(df.describe())
print("\n8. VALORES FALTANTES (Nulls):")
print(df.isnull().sum())
print("\n9. REGISTROS DUPLICADOS:")
print(df.duplicated().sum())
print("\n10. VALORES ÚNICOS POR COLUMNA:")
print(df.nunique())
print("Deportes únicos:", df['deporte'].unique())

# 8. Análisis específico
print(df)
print("------------------------------------------------------------------")
print("-+-+-+-+- 11. TORNEOS POR DEPORTE: -+-+-+-+-")
print(df['deporte'].value_counts())

print("\n12. PROMEDIO DE PREMIO PRIMER LUGAR: $", df['premio_primer_lugar'].mean())
print("13. PREMIO MÁXIMO: $", df['premio_primer_lugar'].max())
print("14. PREMIO MÍNIMO: $", df['premio_primer_lugar'].min())

# 9. Ordenamiento, filtrado y agrupación
print("9. Ordenamiento, filtrado y agrupación")
print("+-+-+- 15. TORNEOS ORDENADOS POR PREMIO (Mayor a menor): -+-+-+")
print(df.sort_values(by='premio_primer_lugar', ascending=False))

print("\n16. TORNEOS CON PREMIO MAYOR A $5,000:")
filtro = df[df['premio_primer_lugar'] > 5000]
print(filtro)

print("\n17. RESUMEN POR DEPORTE:")
resumen = df.groupby('deporte').agg(
    torneos=('id_torneo', 'count'),
    premio_promedio=('premio_primer_lugar', 'mean'),
    premio_maximo=('premio_primer_lugar', 'max')
)
print(resumen)

# 18. Gráfica de barras: Torneos por deporte
print("18. Gráfica de barras: Torneos por deporte")
conteo = df['deporte'].value_counts()
plt.figure(figsize=(8, 5))
plt.bar(conteo.index, conteo.values, color='skyblue')
plt.title('Torneos por deporte Santiago 0103')
plt.xlabel('Deporte')
plt.ylabel('Cantidad de torneos')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 19. Gráfica de barras: Premio primer lugar por torneo
plt.figure(figsize=(9, 5))
plt.bar(df['nombre'], df['premio_primer_lugar'], color='lightgreen')
plt.title('Premio primer lugar por torneo EDA por Santiago 0103')
plt.xlabel('Torneo')
plt.ylabel('Premio en pesos')
plt.xticks(rotation=25)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 20. Histograma: Distribución de cuotas de inscripción
plt.figure(figsize=(8, 5))
plt.hist(df['cuota_inscripcion'], bins=5, color='orange', edgecolor='black')
plt.title('Distribución de cuotas de inscripción EDA Santiago 0103')
plt.xlabel('Cuota de inscripción ($)')
plt.ylabel('Frecuencia')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 21. Gráfica de dispersión: Cuota de inscripción vs Premio primer lugar
plt.figure(figsize=(8, 5))
plt.scatter(df['cuota_inscripcion'], df['premio_primer_lugar'], color='red', s=100)
plt.title('Relación entre cuota de inscripción y premio EDA Santiago 0103')
plt.xlabel('Cuota de inscripción ($)')
plt.ylabel('Premio primer lugar ($)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 22. Diagrama de caja: Distribución de premios
plt.figure(figsize=(7, 5))
plt.boxplot(df['premio_primer_lugar'], patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title('Distribución de premios primer lugar (Boxplot) EDA Santiago 0103')
plt.ylabel('Premio primer lugar ($)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 23. Matriz de correlación
correlacion = df.corr(numeric_only=True)
print("\n--- MATRIZ DE CORRELACIÓN ---")
print(correlacion)

plt.figure(figsize=(9, 6))
plt.imshow(correlacion, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(range(len(correlacion.columns)), correlacion.columns, rotation=45)
plt.yticks(range(len(correlacion.columns)), correlacion.columns)
plt.title('Matriz de correlación de variables numéricas')
plt.tight_layout()
plt.show()
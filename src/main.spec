block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=['/'],  # Caminho para o diretÃ³rio raiz do seu projeto
    binaries=[],
    datas=[
        ('controllers', 'controllers'),
        ('views', 'views'),
        ('models', 'models'),
        ('utils', 'utils'),
        ('images', 'images'),  
        ('C:/Python312/Lib/site-packages/pygame_gui', 'pygame_gui'),  # Inclui a pasta pygame_gui completa
        ('C:/Python312/Lib/site-packages/pygame_widgets', 'pygame_widgets'),  # Inclui a pasta pygame_widgets completa
    ],
    hiddenimports = ['pygame', 'pygame_widgets', 'pygame_gui'],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Simulador de Rotas em Labirintos',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    icon='images/icon.ico',
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ProjetoFinalMaze',
    icon='images/icon.ico',
)

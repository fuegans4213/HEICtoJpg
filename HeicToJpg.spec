# -*- mode: python ; coding: utf-8 -*-
#pyinstaller --onefile --windowed --add-data "ImageMagick-6.9.13-14-portable-Q16-HDRI-x64;ImageMagick-6.9.13-14-portable-Q16-HDRI-x64" HeicToJpg.py

a = Analysis(
    ['HeicToJpg.py'],
    pathex=[],
    binaries=[],
    datas=[('ImageMagick-6.9.13-14-portable-Q16-HDRI-x64', 'ImageMagick-6.9.13-14-portable-Q16-HDRI-x64')],
    hiddenimports=['tk'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='HeicToJpg',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

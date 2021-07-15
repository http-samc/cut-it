# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_submodules

hiddenimports = ['webdriver_manager']
hiddenimports += collect_submodules('webdriver_manager')


block_cipher = None


a = Analysis(['C:/Programming/OffTime/cut-it/Cut-It/app.py'],
             pathex=['C:/Programming/OffTime/cut-it/env/Lib/site-packages', 'C:\\Programming\\OffTime\\Cut-It'],
             binaries=[],
             datas=[('C:/Programming/OffTime/cut-it/images', 'images/'), ('C:/Programming/OffTime/cut-it/env/Lib/site-packages/qtmodern', 'qtmodern/'), ('C:/Programming/OffTime/cut-it/bypass.crx', '.')],
             hiddenimports=hiddenimports,
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='app',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='C:\\Programming\\OffTime\\cut-it\\images\\cut-it.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='app')

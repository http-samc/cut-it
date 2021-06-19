# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['C:/Programming/OffTime/cut-it/Cut-It/app.py'],
             pathex=['C:\\Programming\\OffTime\\cut-it'],
             binaries=[],
             datas=[('C:/Programming/OffTime/cut-it/Cut-It/images', 'images/'), ('C:/Programming/OffTime/cut-it/userData', 'userData/'), ('C:/Programming/OffTime/cut-it/env/Lib/site-packages/qtmodern', 'qtmodern/')],
             hiddenimports=[],
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
          name='Cut-It',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='C:\\Programming\\OffTime\\cut-it\\Cut-It\\images\\otr_icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Cut-It v.1.0@Release')

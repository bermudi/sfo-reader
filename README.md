Organize game folders based on game titles extracted from param.sfo and optionally include SFO data in a text file.

It changes your library from this:

```
.
├── PCSE00240
│   ├── eboot.bin
│   ├── NinPri.cpk
│   ├── SaveIcon
│   ├── sce_module
│   ├── sce_pfs
│   └── sce_sys
├── PCSE00268
│   ├── Config.xml
│   ├── data
│   ├── eboot.bin
│   ├── limbo_boot.pkgpsp2
│   ├── limbo_runtime.pkgpsp2
│   ├── sce_module
│   ├── sce_pfs
│   ├── sce_sys
│   ├── Shaders
│   └── titleid.txt
├── PCSE00286
│   ├── Audio
│   ├── AudioExtra
│   ├── data.psarc
│   ├── eboot.bin
│   ├── Images
│   ├── sce_module
│   ├── sce_pfs
│   └── sce_sys
├── PCSE00288
│   ├── data.arc
│   ├── eboot.bin
│   ├── sce_module
│   ├── sce_pfs
│   └── sce_sys
├── PCSE00349
│   ├── eboot.bin
│   ├── Resources
│   ├── sce_module
│   ├── sce_pfs
│   └── sce_sys
├── PCSE00529
│   ├── BOX.PSARC
│   ├── CHARACTERS.PSARC
│   ├── CUT_SCENES.PSARC
│   ├── DATA.PSARC
│   ├── eboot.bin
│   ├── GFXPAK.PSARC
│   ├── GFX.PSARC
│   ├── LEGENDS.PSARC
│   ├── MEDIA.PSARC
│   ├── MENU3D.PSARC
│   ├── MENU.PSARC
│   ├── MIXFILES.LST
│   ├── MOTO2.PSARC
│   ├── MOTO3.PSARC
│   ├── MOTOGP2013.PSARC
│   ├── MOTOGP2014.PSARC
│   ├── MOTORHOME.PSARC
│   ├── Movies
│   ├── MOVIES.PSARC
│   ├── Music
│   ├── MUSIC.PSARC
│   ├── PITLANE.PSARC
│   ├── saves
│   ├── sce_module
│   ├── sce_pfs
│   ├── sce_sys
│   ├── SFX.PSARC
│   └── Tracks
├── PCSE00567
│   ├── data
│   ├── data.psarc
│   ├── eboot.bin
│   ├── NIGORO
│   ├── sce_module
│   ├── sce_pfs
│   └── sce_sys
├── PCSE00589
│   ├── eboot.bin
│   ├── levels.dat
│   ├── media
│   ├── misc.dat
│   ├── resources.dat
│   ├── sce_module
│   ├── sce_pfs
│   ├── sce_sys
│   ├── shaders.dat.psp2
│   └── thumbnail
└── PCSE00672
    ├── archive.psarc
    ├── eboot.bin
    ├── Media
    ├── sce_module
    ├── sce_pfs
    └── sce_sys
```

To somthing that looks like this:

```
.
├── 1001 Spikes
│   └── PCSE00349
│       ├── 1001 Spikes.txt
│       ├── eboot.bin
│       ├── Resources
│       ├── sce_module
│       ├── sce_pfs
│       └── sce_sys
├── Civilization Revolution 2 Plus
│   └── PCSE00672
│       ├── archive.psarc
│       ├── Civilization Revolution 2 Plus.txt
│       ├── eboot.bin
│       ├── Media
│       ├── sce_module
│       ├── sce_pfs
│       └── sce_sys
├── LA-MULANA EX
│   └── PCSE00567
│       ├── data
│       ├── data.psarc
│       ├── eboot.bin
│       ├── LA-MULANA EX.txt
│       ├── NIGORO
│       ├── sce_module
│       ├── sce_pfs
│       └── sce_sys
├── Limbo
│   └── PCSE00268
│       ├── Config.xml
│       ├── data
│       ├── eboot.bin
│       ├── limbo_boot.pkgpsp2
│       ├── limbo_runtime.pkgpsp2
│       ├── Limbo.txt
│       ├── sce_module
│       ├── sce_pfs
│       ├── sce_sys
│       ├── Shaders
│       └── titleid.txt
├── MotoGP™14
│   └── PCSE00529
│       ├── BOX.PSARC
│       ├── CHARACTERS.PSARC
│       ├── CUT_SCENES.PSARC
│       ├── DATA.PSARC
│       ├── eboot.bin
│       ├── GFXPAK.PSARC
│       ├── GFX.PSARC
│       ├── LEGENDS.PSARC
│       ├── MEDIA.PSARC
│       ├── MENU3D.PSARC
│       ├── MENU.PSARC
│       ├── MIXFILES.LST
│       ├── MOTO2.PSARC
│       ├── MOTO3.PSARC
│       ├── MOTOGP2013.PSARC
│       ├── MOTOGP2014.PSARC
│       ├── MotoGP™14.txt
│       ├── MOTORHOME.PSARC
│       ├── Movies
│       ├── MOVIES.PSARC
│       ├── Music
│       ├── MUSIC.PSARC
│       ├── PITLANE.PSARC
│       ├── saves
│       ├── sce_module
│       ├── sce_pfs
│       ├── sce_sys
│       ├── SFX.PSARC
│       └── Tracks
├── Muramasa Rebirth
│   └── PCSE00240
│       ├── eboot.bin
│       ├── Muramasa Rebirth.txt
│       ├── NinPri.cpk
│       ├── SaveIcon
│       ├── sce_module
│       ├── sce_pfs
│       └── sce_sys
├── Severed
│   └── PCSE00589
│       ├── eboot.bin
│       ├── levels.dat
│       ├── media
│       ├── misc.dat
│       ├── resources.dat
│       ├── sce_module
│       ├── sce_pfs
│       ├── sce_sys
│       ├── Severed.txt
│       ├── shaders.dat.psp2
│       └── thumbnail
├── Spelunky
│   └── PCSE00288
│       ├── data.arc
│       ├── eboot.bin
│       ├── sce_module
│       ├── sce_pfs
│       ├── sce_sys
│       └── Spelunky.txt
└── WORMS REVOLUTION EXTREME
    └── PCSE00286
        ├── Audio
        ├── AudioExtra
        ├── data.psarc
        ├── eboot.bin
        ├── Images
        ├── sce_module
        ├── sce_pfs
        ├── sce_sys
        └── WORMS REVOLUTION EXTREME.txt
```

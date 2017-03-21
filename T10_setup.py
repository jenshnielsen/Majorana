

SD_TOPO = 11    # Topo Bias channel
SD_SENS_L = 7  # Left sensor bias channel
SD_SENS_R = 34  # Right sensor bias channel

BG = 32         # backgate channel

IV_GAIN_TOPO = 1e6
IV_GAIN_R = 1e7
IV_GAIN_L = 1e7

AC_FACTOR_TOPO = 1e4
AC_FACTOR_R = 1e4
AC_FACTOR_L = 1e4

DC_FACTOR_TOPO = 1e2
DC_FACTOR_R = 1e2
DC_FACTOR_L = 1e2
#DC_FACTOR_CH = 4.32
#DC_FACTOR_CH2 = 1

MAX_RAMPSPEED_QCH = 0.4 # qDac channel ramp slope (except bias) [V/s]
MAX_RAMPSPEED_BIAS = 0.4e-2 # bias channel [V/s]
MAX_RAMPSPEED_BG = 0.1 # backgate ramp slope [V/s]

QDAC_LABELS = {2:           'Topo Outer Left Plunger (BNC-2)',
               5:           'Topo Left Cutter (BNC-5)',
               9:           'Topo Left Open (BNC-9)',
               SD_TOPO:     'Topo Bias (BNC-11)',
               12:          'Topo Right Dot Plunger (BNC-12)',
               17:          'Topo Right Cutter (BNC-17)',
               18:          'Topo Outer Right Plunger (BNC-18)',
               20:          'Topo Open (BNC-20)',
               29:          'Sens Left LC (BNC-29)',
              # 24:          'Test (BNC-24)',
               30:          'Sens Left RC (BNC-30)',
               BG:          'Backgate (BNC-32)',
               33:          'Sens Left Plunger (BNC-33)',
               SD_SENS_R:   'Sens Right Bias (BNC-34)',
               SD_SENS_L:   'Sens Left Bias (BNC-7)',
               37:          'Sens Right LC (BNC-37)',
               38:          'Sens Right Plunger (BNC-38)',
               39:          'Sens Right RC (BNC-39)',
               45:          'Topo Middle Cutter (BNC-45)',
               48:          'Topo Left Dot Plunger (BNC-48)'}

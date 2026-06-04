# drivers/mmc/host/sdhci-pci-arasan.c

Subsystem: drivers/mmc

## Functions (9)

### arasan_pci_probe_slot
- Return type: static int
- Signature: arasan_pci_probe_slot(struct sdhci_pci_slot * slot)
- Line: 300

### arasan_phy_addr_poll
- Return type: static int
- Signature: arasan_phy_addr_poll(struct sdhci_host * host,u32 offset,u32 mask)
- Line: 93

### arasan_phy_init
- Return type: static int
- Signature: arasan_phy_init(struct sdhci_host * host)
- Line: 149

### arasan_phy_read
- Return type: static int
- Signature: arasan_phy_read(struct sdhci_host * host,u8 offset,u8 * data)
- Line: 116

### arasan_phy_set
- Return type: static int
- Signature: arasan_phy_set(struct sdhci_host * host,u8 mode,u8 otap,u8 drv_type,u8 itap,u8 trim,u8 clk)
- Line: 189

### arasan_phy_sts_poll
- Return type: static int
- Signature: arasan_phy_sts_poll(struct sdhci_host * host,u32 offset,u32 mask)
- Line: 129

### arasan_phy_write
- Return type: static int
- Signature: arasan_phy_write(struct sdhci_host * host,u8 data,u8 offset)
- Line: 109

### arasan_sdhci_set_clock
- Return type: static void
- Signature: arasan_sdhci_set_clock(struct sdhci_host * host,unsigned int clock)
- Line: 311

### arasan_select_phy_clock
- Return type: static int
- Signature: arasan_select_phy_clock(struct sdhci_host * host)
- Line: 244

## Structs (1)

### arasan_host
- Line: 89
- Members:
  - chg_clk: u32

## Variables (2)

- static **arasan_sdhci_pci_ops** : const struct sdhci_ops (line 319)
- **sdhci_arasan** : const struct sdhci_pci_fixes (line 327)

## Macros (57)

- **CALDONE_MASK** (line 66)
- **CLKBUF_SEL** (line 37)
- **CLK_CTRL** (line 43)
- **CMD_CTRL** (line 40)
- **DATA_CTRL** (line 41)
- **DATA_MASK** (line 23)
- **DDR50_MODE** (line 74)
- **DLLTRM_ICP** (line 61)
- **DLL_ENBL** (line 46)
- **DLL_RDY_MASK** (line 67)
- **DLL_STATUS** (line 26)
- **DLL_TRIM** (line 39)
- **ENHSTRB_MODE** (line 71)
- **FREQSEL**(x) (line 85)
- **HISPD_MODE** (line 81)
- **HS200_MODE** (line 80)
- **HS400_MODE** (line 72)
- **IOPAD**(x,y) (line 86)
- **IOPU_CTRL1** (line 32)
- **IOPU_CTRL2** (line 33)
- **IOREN_CTRL1** (line 30)
- **IOREN_CTRL2** (line 31)
- **IPAD_CTRL1** (line 27)
- **IPAD_CTRL2** (line 28)
- **IPAD_STS** (line 29)
- **ITAPDLY**(x) (line 84)
- **ITAPDLY_EN** (line 57)
- **ITAP_DELAY** (line 34)
- **LEGACY_MODE** (line 73)
- **MAX_CLK_BUF** (line 68)
- **MODE_CTRL** (line 38)
- **ODEN_CMD** (line 50)
- **ODEN_DAT** (line 51)
- **OD_REL_CMD** (line 59)
- **OD_REL_DAT** (line 60)
- **OTAPDLY**(x) (line 83)
- **OTAPDLY_EN** (line 58)
- **OTAP_DELAY** (line 35)
- **PDB_CLOCK** (line 65)
- **PDB_CMND** (line 62)
- **PDB_DATA** (line 63)
- **PDB_ENBL** (line 48)
- **PDB_STRB** (line 64)
- **PHY_ADDR_REG** (line 18)
- **PHY_BUSY** (line 22)
- **PHY_CTRL** (line 44)
- **PHY_DAT_REG** (line 19)
- **PHY_WRITE** (line 21)
- **PU_CMD** (line 55)
- **PU_DAT** (line 56)
- **REN_CMND** (line 53)
- **REN_DATA** (line 54)
- **REN_STRB** (line 52)
- **RETB_ENBL** (line 49)
- **RTRIM_EN** (line 47)
- **STRB_CTRL** (line 42)
- **STRB_SEL** (line 36)

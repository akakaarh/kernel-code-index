# drivers/mmc/host/sdhci-pic32.c

Subsystem: drivers/mmc

## Functions (7)

### pic32_sdhci_get_max_clock
- Return type: static unsigned int
- Signature: pic32_sdhci_get_max_clock(struct sdhci_host * host)
- Line: 48

### pic32_sdhci_get_ro
- Return type: static unsigned int
- Signature: pic32_sdhci_get_ro(struct sdhci_host * host)
- Line: 79

### pic32_sdhci_probe
- Return type: static int
- Signature: pic32_sdhci_probe(struct platform_device * pdev)
- Line: 134

### pic32_sdhci_probe_platform
- Return type: static void
- Signature: pic32_sdhci_probe_platform(struct platform_device * pdev,struct pic32_sdhci_priv * pdata)
- Line: 121

### pic32_sdhci_remove
- Return type: static void
- Signature: pic32_sdhci_remove(struct platform_device * pdev)
- Line: 208

### pic32_sdhci_set_bus_width
- Return type: static void
- Signature: pic32_sdhci_set_bus_width(struct sdhci_host * host,int width)
- Line: 55

### pic32_sdhci_shared_bus
- Return type: static void
- Signature: pic32_sdhci_shared_bus(struct platform_device * pdev)
- Line: 103

## Structs (1)

### pic32_sdhci_priv
- Line: 42
- Members:
  - pdev: platform_device *
  - sys_clk: clk *
  - base_clk: clk *

## Variables (4)

- static **pic32_sdhci_driver** : platform_driver (line 226)
- static **pic32_sdhci_id_table** : const struct of_device_id[] (line 220)
- static **pic32_sdhci_ops** : const struct sdhci_ops (line 88)
- static **sdhci_pic32_pdata** : const struct sdhci_pltfm_data (line 97)

## Macros (13)

- **ADMA_FIFO_RD_THSHLD** (line 39)
- **ADMA_FIFO_WR_THSHLD** (line 40)
- **SDHCI_CTRL_CDSSEL** (line 36)
- **SDHCI_CTRL_CDTLVL** (line 37)
- **SDH_CAPS_SDH_SLOT_TYPE_MASK** (line 32)
- **SDH_SHARED_BUS_CLK_PINS** (line 30)
- **SDH_SHARED_BUS_CTRL** (line 27)
- **SDH_SHARED_BUS_IRQ_PINS** (line 31)
- **SDH_SHARED_BUS_NR_CLK_PINS_MASK** (line 28)
- **SDH_SHARED_BUS_NR_IRQ_PINS_MASK** (line 29)
- **SDH_SLOT_TYPE_EMBEDDED** (line 34)
- **SDH_SLOT_TYPE_REMOVABLE** (line 33)
- **SDH_SLOT_TYPE_SHARED_BUS** (line 35)

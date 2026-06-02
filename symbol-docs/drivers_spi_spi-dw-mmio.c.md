# drivers/spi/spi-dw-mmio.c

Subsystem: drivers/spi

## Functions (19)

### dw_spi_alpine_init
- Return type: static int
- Signature: dw_spi_alpine_init(struct platform_device * pdev,struct dw_spi_mmio * dwsmmio)
- Line: 203

### dw_spi_canaan_k210_init
- Return type: static int
- Signature: dw_spi_canaan_k210_init(struct platform_device * pdev,struct dw_spi_mmio * dwsmmio)
- Line: 255

### dw_spi_elba_init
- Return type: static int
- Signature: dw_spi_elba_init(struct platform_device * pdev,struct dw_spi_mmio * dwsmmio)
- Line: 296

### dw_spi_elba_override_cs
- Return type: static void
- Signature: dw_spi_elba_override_cs(struct regmap * syscon,int cs,int enable)
- Line: 270

### dw_spi_elba_set_cs
- Return type: static void
- Signature: dw_spi_elba_set_cs(struct spi_device * spi,bool enable)
- Line: 276

### dw_spi_hssi_init
- Return type: static int
- Signature: dw_spi_hssi_init(struct platform_device * pdev,struct dw_spi_mmio * dwsmmio)
- Line: 219

### dw_spi_intel_init
- Return type: static int
- Signature: dw_spi_intel_init(struct platform_device * pdev,struct dw_spi_mmio * dwsmmio)
- Line: 229

### dw_spi_mmio_probe
- Return type: static int
- Signature: dw_spi_mmio_probe(struct platform_device * pdev)
- Line: 313

### dw_spi_mmio_remove
- Return type: static void
- Signature: dw_spi_mmio_remove(struct platform_device * pdev)
- Line: 425

### dw_spi_mmio_resume
- Return type: static int
- Signature: dw_spi_mmio_resume(struct device * dev)
- Line: 410

### dw_spi_mmio_suspend
- Return type: static int
- Signature: dw_spi_mmio_suspend(struct device * dev)
- Line: 393

### dw_spi_mountevans_imc_init
- Return type: static int
- Signature: dw_spi_mountevans_imc_init(struct platform_device * pdev,struct dw_spi_mmio * dwsmmio)
- Line: 240

### dw_spi_mscc_init
- Return type: static int
- Signature: dw_spi_mscc_init(struct platform_device * pdev,struct dw_spi_mmio * dwsmmio,const char * cpu_syscon,u32 if_si_owner_offset)
- Line: 96

### dw_spi_mscc_jaguar2_init
- Return type: static int
- Signature: dw_spi_mscc_jaguar2_init(struct platform_device * pdev,struct dw_spi_mmio * dwsmmio)
- Line: 135

### dw_spi_mscc_ocelot_init
- Return type: static int
- Signature: dw_spi_mscc_ocelot_init(struct platform_device * pdev,struct dw_spi_mmio * dwsmmio)
- Line: 128

### dw_spi_mscc_set_cs
- Return type: static void
- Signature: dw_spi_mscc_set_cs(struct spi_device * spi,bool enable)
- Line: 77

### dw_spi_mscc_sparx5_init
- Return type: static int
- Signature: dw_spi_mscc_sparx5_init(struct platform_device * pdev,struct dw_spi_mmio * dwsmmio)
- Line: 174

### dw_spi_pssi_init
- Return type: static int
- Signature: dw_spi_pssi_init(struct platform_device * pdev,struct dw_spi_mmio * dwsmmio)
- Line: 211

### dw_spi_sparx5_set_cs
- Return type: static void
- Signature: dw_spi_sparx5_set_cs(struct spi_device * spi,bool enable)
- Line: 148

## Structs (2)

### dw_spi_mmio
- Line: 28
- Members:
  - dws: dw_spi
  - clk: clk *
  - pclk: clk *
  - priv: void *
  - rstc: reset_control *
  - syscon: regmap *
  - spi_mst: void __iomem *

### dw_spi_mscc
- Line: 51
- Members:
  - dws: dw_spi
  - clk: clk *
  - pclk: clk *
  - priv: void *
  - rstc: reset_control *
  - syscon: regmap *
  - spi_mst: void __iomem *

## Variables (3)

- static **dw_spi_mmio_acpi_match** : const struct acpi_device_id[] (line 454)
- static **dw_spi_mmio_driver** : platform_driver (line 461)
- static **dw_spi_mmio_of_match** : const struct of_device_id[] (line 434)

## Macros (17)

- **DRIVER_NAME** (line 26)
- **ELBA_SPICS_MASK**(cs) (line 66)
- **ELBA_SPICS_OFFSET**(cs) (line 65)
- **ELBA_SPICS_REG** (line 64)
- **ELBA_SPICS_SET**(cs,val) (line 67)
- **JAGUAR2_IF_SI_OWNER_OFFSET** (line 38)
- **MSCC_CPU_SYSTEM_CTRL_GENERAL_CTRL** (line 36)
- **MSCC_IF_SI_OWNER_MASK** (line 39)
- **MSCC_IF_SI_OWNER_SIBM** (line 41)
- **MSCC_IF_SI_OWNER_SIMC** (line 42)
- **MSCC_IF_SI_OWNER_SISL** (line 40)
- **MSCC_SPI_MST_SW_MODE** (line 44)
- **MSCC_SPI_MST_SW_MODE_SW_PIN_CTRL_MODE** (line 45)
- **MSCC_SPI_MST_SW_MODE_SW_SPI_CS**(x) (line 46)
- **OCELOT_IF_SI_OWNER_OFFSET** (line 37)
- **SPARX5_FORCE_ENA** (line 48)
- **SPARX5_FORCE_VAL** (line 49)

# drivers/spi/spi-altera-dfl.c

Subsystem: drivers/spi

## Functions (4)

### config_spi_host
- Return type: static void
- Signature: config_spi_host(void __iomem * base,struct spi_controller * host)
- Line: 107

### dfl_spi_altera_probe
- Return type: static int
- Signature: dfl_spi_altera_probe(struct dfl_device * dfl_dev)
- Line: 124

### indirect_bus_reg_read
- Return type: static int
- Signature: indirect_bus_reg_read(void * context,unsigned int reg,unsigned int * val)
- Line: 49

### indirect_bus_reg_write
- Return type: static int
- Signature: indirect_bus_reg_write(void * context,unsigned int reg,unsigned int val)
- Line: 75

## Variables (3)

- static **dfl_spi_altera_driver** : dfl_driver (line 188)
- static **dfl_spi_altera_ids** : const struct dfl_device_id[] (line 183)
- static **indirect_regbus_cfg** : const struct regmap_config (line 96)

## Macros (21)

- **CLK_PHASE** (line 35)
- **CLK_POLARITY** (line 34)
- **DATA_WIDTH** (line 32)
- **FME_FEATURE_ID_MAX10_SPI** (line 25)
- **FME_FEATURE_REV_MAX10_SPI_N5010** (line 26)
- **INDIRECT_ADDR** (line 40)
- **INDIRECT_DATA_MASK** (line 44)
- **INDIRECT_DEBUG** (line 45)
- **INDIRECT_RD** (line 42)
- **INDIRECT_RD_DATA** (line 43)
- **INDIRECT_TIMEOUT** (line 47)
- **INDIRECT_WR** (line 41)
- **INDIRECT_WR_DATA** (line 46)
- **NUM_CHIPSELECT** (line 33)
- **PERIPHERAL_ID** (line 36)
- **SHIFT_MODE** (line 29)
- **SHIFT_MODE_LSB** (line 31)
- **SHIFT_MODE_MSB** (line 30)
- **SPI_CLK** (line 37)
- **SPI_CORE_PARAMETER** (line 28)
- **SPI_INDIRECT_ACC_OFST** (line 38)

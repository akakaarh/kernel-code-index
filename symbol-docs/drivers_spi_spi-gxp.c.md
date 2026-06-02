# drivers/spi/spi-gxp.c

Subsystem: drivers/spi

## Functions (9)

### do_gxp_exec_mem_op
- Return type: static int
- Signature: do_gxp_exec_mem_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 200

### gxp_exec_mem_op
- Return type: static int
- Signature: gxp_exec_mem_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 221

### gxp_spi_read
- Return type: static ssize_t
- Signature: gxp_spi_read(struct gxp_spi_chip * chip,const struct spi_mem_op * op)
- Line: 142

### gxp_spi_read_reg
- Return type: static int
- Signature: gxp_spi_read_reg(struct gxp_spi_chip * chip,const struct spi_mem_op * op)
- Line: 67

### gxp_spi_set_mode
- Return type: static void
- Signature: gxp_spi_set_mode(struct gxp_spi * spifi,int mode)
- Line: 50

### gxp_spi_setup
- Return type: static int
- Signature: gxp_spi_setup(struct spi_device * spi)
- Line: 236

### gxp_spi_write
- Return type: static ssize_t
- Signature: gxp_spi_write(struct gxp_spi_chip * chip,const struct spi_mem_op * op)
- Line: 155

### gxp_spi_write_reg
- Return type: static int
- Signature: gxp_spi_write_reg(struct gxp_spi_chip * chip,const struct spi_mem_op * op)
- Line: 105

### gxp_spifi_probe
- Return type: static int
- Signature: gxp_spifi_probe(struct platform_device * pdev)
- Line: 250

## Structs (3)

### gxp_spi
- Line: 41
- Members:
  - spifi: gxp_spi *
  - cs: u32
  - max_cs: u32
  - mode_bits: u32
  - data: const struct gxp_spi_data *
  - reg_base: void __iomem *
  - dat_base: void __iomem *
  - dir_base: void __iomem *
  - dev: device *
  - chips: gxp_spi_chip[]

### gxp_spi_chip
- Line: 31
- Members:
  - spifi: gxp_spi *
  - cs: u32
  - max_cs: u32
  - mode_bits: u32
  - data: const struct gxp_spi_data *
  - reg_base: void __iomem *
  - dat_base: void __iomem *
  - dir_base: void __iomem *
  - dev: device *
  - chips: gxp_spi_chip[]

### gxp_spi_data
- Line: 36
- Members:
  - spifi: gxp_spi *
  - cs: u32
  - max_cs: u32
  - mode_bits: u32
  - data: const struct gxp_spi_data *
  - reg_base: void __iomem *
  - dat_base: void __iomem *
  - dir_base: void __iomem *
  - dev: device *
  - chips: gxp_spi_chip[]

## Variables (4)

- static **gxp_spi_mem_ops** : const struct spi_controller_mem_ops (line 232)
- static **gxp_spifi_data** : const struct gxp_spi_data (line 297)
- static **gxp_spifi_driver** : platform_driver (line 308)
- static **gxp_spifi_match** : const struct of_device_id[] (line 302)

## Macros (15)

- **DIRECT_MODE** (line 15)
- **GXP_SPI0_MAX_CHIPSELECT** (line 10)
- **GXP_SPI_SLEEP_TIME** (line 11)
- **GXP_SPI_TIMEOUT** (line 12)
- **MANUAL_MODE** (line 14)
- **OFFSET_SPIADDR** (line 22)
- **OFFSET_SPICMD** (line 20)
- **OFFSET_SPIDCNT** (line 21)
- **OFFSET_SPIINTSTS** (line 23)
- **OFFSET_SPIMCFG** (line 18)
- **OFFSET_SPIMCTRL** (line 19)
- **SPILDAT_LEN** (line 16)
- **SPIMCTRL_BUSY** (line 26)
- **SPIMCTRL_DIR** (line 27)
- **SPIMCTRL_START** (line 25)

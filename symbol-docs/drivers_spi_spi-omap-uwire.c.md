# drivers/spi/spi-omap-uwire.c

Subsystem: drivers/spi

## Functions (15)

### omap_uwire_configure_mode
- Return type: static void
- Signature: omap_uwire_configure_mode(u8 cs,unsigned long flags)
- Line: 115

### omap_uwire_exit
- Return type: static void __exit
- Signature: omap_uwire_exit(void)
- Line: 536

### omap_uwire_init
- Return type: static int __init
- Signature: omap_uwire_init(void)
- Line: 531

### uwire_chipselect
- Return type: static void
- Signature: uwire_chipselect(struct spi_device * spi,int value)
- Line: 171

### uwire_cleanup
- Return type: static void
- Signature: uwire_cleanup(struct spi_device * spi)
- Line: 442

### uwire_off
- Return type: static void
- Signature: uwire_off(struct uwire_spi * uwire)
- Line: 447

### uwire_probe
- Return type: static int
- Signature: uwire_probe(struct platform_device * pdev)
- Line: 454

### uwire_read_reg
- Return type: static u16
- Signature: uwire_read_reg(int idx)
- Line: 110

### uwire_remove
- Return type: static void
- Signature: uwire_remove(struct platform_device * pdev)
- Line: 508

### uwire_set_clk1_div
- Return type: static void
- Signature: uwire_set_clk1_div(int div1_idx)
- Line: 161

### uwire_setup
- Return type: static int
- Signature: uwire_setup(struct spi_device * spi)
- Line: 421

### uwire_setup_transfer
- Return type: static int
- Signature: uwire_setup_transfer(struct spi_device * spi,struct spi_transfer * t)
- Line: 306

### uwire_txrx
- Return type: static int
- Signature: uwire_txrx(struct spi_device * spi,struct spi_transfer * t)
- Line: 202

### uwire_write_reg
- Return type: static void
- Signature: uwire_write_reg(int idx,u16 val)
- Line: 105

### wait_uwire_csr_flag
- Return type: static int
- Signature: wait_uwire_csr_flag(u16 mask,u16 val,int might_not_catch)
- Line: 138

## Structs (2)

### uwire_spi
- Line: 88
- Members:
  - bitbang: spi_bitbang
  - ck: clk *
  - div1_idx: unsigned

### uwire_state
- Line: 93
- Members:
  - bitbang: spi_bitbang
  - ck: clk *
  - div1_idx: unsigned

## Variables (3)

- static **uwire_base** : void __iomem * (line 103)
- static **uwire_driver** : platform_driver (line 521)
- static **uwire_idx_shift** : unsigned int (line 102)

## Macros (25)

- **CSRB** (line 70)
- **CS_CMD** (line 72)
- **RDRB** (line 69)
- **START** (line 71)
- **UWIRE_BASE_PHYS** (line 55)
- **UWIRE_CHK_READY** (line 84)
- **UWIRE_CLK_INVERTED** (line 85)
- **UWIRE_CSR** (line 61)
- **UWIRE_CS_ACTIVE_HIGH** (line 80)
- **UWIRE_CS_ACTIVE_LOW** (line 79)
- **UWIRE_FREQ_DIV_2** (line 81)
- **UWIRE_FREQ_DIV_4** (line 82)
- **UWIRE_FREQ_DIV_8** (line 83)
- **UWIRE_IO_SIZE** (line 58)
- **UWIRE_RDR** (line 60)
- **UWIRE_READ_FALLING_EDGE** (line 75)
- **UWIRE_READ_RISING_EDGE** (line 76)
- **UWIRE_SR1** (line 62)
- **UWIRE_SR2** (line 63)
- **UWIRE_SR3** (line 64)
- **UWIRE_SR4** (line 65)
- **UWIRE_SR5** (line 66)
- **UWIRE_TDR** (line 59)
- **UWIRE_WRITE_FALLING_EDGE** (line 77)
- **UWIRE_WRITE_RISING_EDGE** (line 78)

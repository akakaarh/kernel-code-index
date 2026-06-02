# drivers/spi/spi-sh-hspi.c

Subsystem: drivers/spi

## Functions (9)

### hspi_bit_set
- Return type: static void
- Signature: hspi_bit_set(struct hspi_priv * hspi,int reg,u32 mask,u32 set)
- Line: 56

### hspi_hw_cs_ctrl
- Return type: static void
- Signature: hspi_hw_cs_ctrl(struct hspi_priv * hspi,int hi)
- Line: 90

### hspi_hw_setup
- Return type: static void
- Signature: hspi_hw_setup(struct hspi_priv * hspi,struct spi_message * msg,struct spi_transfer * t)
- Line: 95

### hspi_probe
- Return type: static int
- Signature: hspi_probe(struct platform_device * pdev)
- Line: 212

### hspi_read
- Return type: static u32
- Signature: hspi_read(struct hspi_priv * hspi,int reg)
- Line: 51

### hspi_remove
- Return type: static void
- Signature: hspi_remove(struct platform_device * pdev)
- Line: 278

### hspi_status_check_timeout
- Return type: static int
- Signature: hspi_status_check_timeout(struct hspi_priv * hspi,u32 mask,u32 val)
- Line: 69

### hspi_transfer_one_message
- Return type: static int
- Signature: hspi_transfer_one_message(struct spi_controller * ctlr,struct spi_message * msg)
- Line: 143

### hspi_write
- Return type: static void
- Signature: hspi_write(struct hspi_priv * hspi,int reg,u32 val)
- Line: 46

## Structs (1)

### hspi_priv
- Line: 36
- Members:
  - addr: void __iomem *
  - ctlr: spi_controller *
  - dev: device *
  - clk: clk *

## Variables (2)

- static **hspi_driver** : platform_driver (line 299)
- static **hspi_of_match** : const struct of_device_id[] (line 293)

## Macros (9)

- **RXFL** (line 34)
- **SPCR** (line 26)
- **SPCR2** (line 31)
- **SPRBR** (line 30)
- **SPSCR** (line 28)
- **SPSR** (line 27)
- **SPTBR** (line 29)
- **hspi_hw_cs_disable**(hspi) (line 89)
- **hspi_hw_cs_enable**(hspi) (line 88)

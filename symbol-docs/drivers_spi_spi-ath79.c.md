# drivers/spi/spi-ath79.c

Subsystem: drivers/spi

## Functions (12)

### ath79_exec_mem_op
- Return type: static int
- Signature: ath79_exec_mem_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 137

### ath79_spi_chipselect
- Return type: static void
- Signature: ath79_spi_chipselect(struct spi_device * spi,int is_active)
- Line: 70

### ath79_spi_delay
- Return type: static void
- Signature: ath79_spi_delay(struct ath79_spi * sp,unsigned int nsecs)
- Line: 64

### ath79_spi_disable
- Return type: static void
- Signature: ath79_spi_disable(struct ath79_spi * sp)
- Line: 100

### ath79_spi_enable
- Return type: static void
- Signature: ath79_spi_enable(struct ath79_spi * sp)
- Line: 84

### ath79_spi_probe
- Return type: static int
- Signature: ath79_spi_probe(struct platform_device * pdev)
- Line: 169

### ath79_spi_remove
- Return type: static void
- Signature: ath79_spi_remove(struct platform_device * pdev)
- Line: 233

### ath79_spi_rr
- Return type: static u32
- Signature: ath79_spi_rr(struct ath79_spi * sp,unsigned int reg)
- Line: 49

### ath79_spi_shutdown
- Return type: static void
- Signature: ath79_spi_shutdown(struct platform_device * pdev)
- Line: 242

### ath79_spi_txrx_mode0
- Return type: static u32
- Signature: ath79_spi_txrx_mode0(struct spi_device * spi,unsigned int nsecs,u32 word,u8 bits,unsigned flags)
- Line: 108

### ath79_spi_wr
- Return type: static void
- Signature: ath79_spi_wr(struct ath79_spi * sp,unsigned int reg,u32 val)
- Line: 54

### ath79_spidev_to_sp
- Return type: static ath79_spi *
- Signature: ath79_spidev_to_sp(struct spi_device * spi)
- Line: 59

## Structs (1)

### ath79_spi
- Line: 40
- Members:
  - bitbang: spi_bitbang
  - ioc_base: u32
  - reg_ctrl: u32
  - base: void __iomem *
  - clk: clk *
  - rrw_delay: unsigned int

## Variables (3)

- static **ath79_mem_ops** : const struct spi_controller_mem_ops (line 165)
- static **ath79_spi_driver** : platform_driver (line 253)
- static **ath79_spi_of_match** : const struct of_device_id[] (line 247)

## Macros (11)

- **AR71XX_SPI_FS_GPIO** (line 34)
- **AR71XX_SPI_IOC_CLK** (line 37)
- **AR71XX_SPI_IOC_CS**(n) (line 38)
- **AR71XX_SPI_IOC_DO** (line 36)
- **AR71XX_SPI_REG_CTRL** (line 30)
- **AR71XX_SPI_REG_FS** (line 29)
- **AR71XX_SPI_REG_IOC** (line 31)
- **AR71XX_SPI_REG_RDS** (line 32)
- **ATH79_SPI_RRW_DELAY_FACTOR** (line 26)
- **DRV_NAME** (line 24)
- **MHZ** (line 27)

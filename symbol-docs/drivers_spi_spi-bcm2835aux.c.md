# drivers/spi/spi-bcm2835aux.c

Subsystem: drivers/spi

## Functions (21)

### __bcm2835aux_spi_transfer_one_irq
- Return type: static int
- Signature: __bcm2835aux_spi_transfer_one_irq(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * tfr)
- Line: 260

### bcm2835aux_debugfs_create
- Return type: static void
- Signature: bcm2835aux_debugfs_create(struct bcm2835aux_spi * bs,const char * dname)
- Line: 105

### bcm2835aux_debugfs_create
- Return type: static void
- Signature: bcm2835aux_debugfs_create(struct bcm2835aux_spi * bs,const char * dname)
- Line: 133

### bcm2835aux_debugfs_remove
- Return type: static void
- Signature: bcm2835aux_debugfs_remove(struct bcm2835aux_spi * bs)
- Line: 127

### bcm2835aux_debugfs_remove
- Return type: static void
- Signature: bcm2835aux_debugfs_remove(struct bcm2835aux_spi * bs)
- Line: 138

### bcm2835aux_rd
- Return type: static u32
- Signature: bcm2835aux_rd(struct bcm2835aux_spi * bs,unsigned int reg)
- Line: 143

### bcm2835aux_rd_fifo
- Return type: static void
- Signature: bcm2835aux_rd_fifo(struct bcm2835aux_spi * bs)
- Line: 154

### bcm2835aux_spi_handle_err
- Return type: static void
- Signature: bcm2835aux_spi_handle_err(struct spi_controller * host,struct spi_message * msg)
- Line: 435

### bcm2835aux_spi_interrupt
- Return type: static irqreturn_t
- Signature: bcm2835aux_spi_interrupt(int irq,void * dev_id)
- Line: 232

### bcm2835aux_spi_prepare_message
- Return type: static int
- Signature: bcm2835aux_spi_prepare_message(struct spi_controller * host,struct spi_message * msg)
- Line: 401

### bcm2835aux_spi_probe
- Return type: static int
- Signature: bcm2835aux_spi_probe(struct platform_device * pdev)
- Line: 474

### bcm2835aux_spi_remove
- Return type: static void
- Signature: bcm2835aux_spi_remove(struct platform_device * pdev)
- Line: 555

### bcm2835aux_spi_reset_hw
- Return type: static void
- Signature: bcm2835aux_spi_reset_hw(struct bcm2835aux_spi * bs)
- Line: 206

### bcm2835aux_spi_setup
- Return type: static int
- Signature: bcm2835aux_spi_setup(struct spi_device * spi)
- Line: 443

### bcm2835aux_spi_transfer_helper
- Return type: static void
- Signature: bcm2835aux_spi_transfer_helper(struct bcm2835aux_spi * bs)
- Line: 214

### bcm2835aux_spi_transfer_one
- Return type: static int
- Signature: bcm2835aux_spi_transfer_one(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * tfr)
- Line: 340

### bcm2835aux_spi_transfer_one_irq
- Return type: static int
- Signature: bcm2835aux_spi_transfer_one_irq(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * tfr)
- Line: 275

### bcm2835aux_spi_transfer_one_poll
- Return type: static int
- Signature: bcm2835aux_spi_transfer_one_poll(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * tfr)
- Line: 300

### bcm2835aux_spi_unprepare_message
- Return type: static int
- Signature: bcm2835aux_spi_unprepare_message(struct spi_controller * host,struct spi_message * msg)
- Line: 425

### bcm2835aux_wr
- Return type: static void
- Signature: bcm2835aux_wr(struct bcm2835aux_spi * bs,unsigned int reg,u32 val)
- Line: 148

### bcm2835aux_wr_fifo
- Return type: static void
- Signature: bcm2835aux_wr_fifo(struct bcm2835aux_spi * bs)
- Line: 177

## Structs (1)

### bcm2835aux_spi
- Line: 86
- Members:
  - regs: void __iomem *
  - clk: clk *
  - irq: int
  - cntl: u32[2]
  - tx_buf: const u8 *
  - rx_buf: u8 *
  - tx_len: int
  - rx_len: int
  - pending: int
  - count_transfer_polling: u64
  - count_transfer_irq: u64
  - count_transfer_irq_after_poll: u64
  - debugfs_dir: dentry *

## Variables (3)

- static **bcm2835aux_spi_driver** : platform_driver (line 573)
- static **bcm2835aux_spi_match** : const struct of_device_id[] (line 567)
- static **polling_limit_us** : unsigned int (line 29)

## Macros (34)

- **BCM2835_AUX_SPI_CNTL0** (line 45)
- **BCM2835_AUX_SPI_CNTL0_CLEARFIFO** (line 63)
- **BCM2835_AUX_SPI_CNTL0_CPOL** (line 65)
- **BCM2835_AUX_SPI_CNTL0_CS** (line 56)
- **BCM2835_AUX_SPI_CNTL0_DOUTHOLD** (line 60)
- **BCM2835_AUX_SPI_CNTL0_ENABLE** (line 61)
- **BCM2835_AUX_SPI_CNTL0_IN_RISING** (line 62)
- **BCM2835_AUX_SPI_CNTL0_MSBF_OUT** (line 66)
- **BCM2835_AUX_SPI_CNTL0_OUT_RISING** (line 64)
- **BCM2835_AUX_SPI_CNTL0_POSTINPUT** (line 57)
- **BCM2835_AUX_SPI_CNTL0_SHIFTLEN** (line 67)
- **BCM2835_AUX_SPI_CNTL0_SPEED** (line 53)
- **BCM2835_AUX_SPI_CNTL0_SPEED_MAX** (line 54)
- **BCM2835_AUX_SPI_CNTL0_SPEED_SHIFT** (line 55)
- **BCM2835_AUX_SPI_CNTL0_VAR_CS** (line 58)
- **BCM2835_AUX_SPI_CNTL0_VAR_WIDTH** (line 59)
- **BCM2835_AUX_SPI_CNTL1** (line 46)
- **BCM2835_AUX_SPI_CNTL1_CSHIGH** (line 70)
- **BCM2835_AUX_SPI_CNTL1_IDLE** (line 72)
- **BCM2835_AUX_SPI_CNTL1_KEEP_IN** (line 74)
- **BCM2835_AUX_SPI_CNTL1_MSBF_IN** (line 73)
- **BCM2835_AUX_SPI_CNTL1_TXEMPTY** (line 71)
- **BCM2835_AUX_SPI_IO** (line 49)
- **BCM2835_AUX_SPI_PEEK** (line 48)
- **BCM2835_AUX_SPI_STAT** (line 47)
- **BCM2835_AUX_SPI_STAT_BITCOUNT** (line 84)
- **BCM2835_AUX_SPI_STAT_BUSY** (line 83)
- **BCM2835_AUX_SPI_STAT_RX_EMPTY** (line 82)
- **BCM2835_AUX_SPI_STAT_RX_FULL** (line 81)
- **BCM2835_AUX_SPI_STAT_RX_LVL** (line 78)
- **BCM2835_AUX_SPI_STAT_TX_EMPTY** (line 80)
- **BCM2835_AUX_SPI_STAT_TX_FULL** (line 79)
- **BCM2835_AUX_SPI_STAT_TX_LVL** (line 77)
- **BCM2835_AUX_SPI_TXHOLD** (line 50)

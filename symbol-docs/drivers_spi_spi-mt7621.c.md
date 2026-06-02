# drivers/spi/spi-mt7621.c

Subsystem: drivers/spi

## Functions (13)

### mt7621_spi_flush
- Return type: static void
- Signature: mt7621_spi_flush(struct mt7621_spi * rs)
- Line: 219

### mt7621_spi_prepare
- Return type: static int
- Signature: mt7621_spi_prepare(struct spi_device * spi,unsigned int speed)
- Line: 105

### mt7621_spi_prepare_message
- Return type: static int
- Signature: mt7621_spi_prepare_message(struct spi_controller * host,struct spi_message * m)
- Line: 160

### mt7621_spi_probe
- Return type: static int
- Signature: mt7621_spi_probe(struct platform_device * pdev)
- Line: 316

### mt7621_spi_read
- Return type: static u32
- Signature: mt7621_spi_read(struct mt7621_spi * rs,u32 reg)
- Line: 70

### mt7621_spi_read_half_duplex
- Return type: static void
- Signature: mt7621_spi_read_half_duplex(struct mt7621_spi * rs,int rx_len,u8 * buf)
- Line: 177

### mt7621_spi_set_native_cs
- Return type: static void
- Signature: mt7621_spi_set_native_cs(struct spi_device * spi,bool enable)
- Line: 80

### mt7621_spi_setup
- Return type: static int
- Signature: mt7621_spi_setup(struct spi_device * spi)
- Line: 293

### mt7621_spi_transfer_one
- Return type: static int
- Signature: mt7621_spi_transfer_one(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * t)
- Line: 269

### mt7621_spi_wait_till_ready
- Return type: static int
- Signature: mt7621_spi_wait_till_ready(struct mt7621_spi * rs)
- Line: 143

### mt7621_spi_write
- Return type: static void
- Signature: mt7621_spi_write(struct mt7621_spi * rs,u32 reg,u32 val)
- Line: 75

### mt7621_spi_write_half_duplex
- Return type: static void
- Signature: mt7621_spi_write_half_duplex(struct mt7621_spi * rs,int tx_len,const u8 * buf)
- Line: 224

### spidev_to_mt7621_spi
- Return type: static mt7621_spi *
- Signature: spidev_to_mt7621_spi(struct spi_device * spi)
- Line: 65

## Structs (1)

### mt7621_spi
- Line: 57
- Members:
  - host: spi_controller *
  - base: void __iomem *
  - sys_freq: unsigned int
  - speed: unsigned int
  - pending_write: int

## Variables (2)

- static **mt7621_spi_driver** : platform_driver (line 375)
- static **mt7621_spi_match** : const struct of_device_id[] (line 310)

## Macros (23)

- **DRIVER_NAME** (line 23)
- **MASTER_FULL_DUPLEX** (line 42)
- **MASTER_MORE_BUFMODE** (line 41)
- **MASTER_RS_CLK_SEL** (line 43)
- **MASTER_RS_CLK_SEL_SHIFT** (line 44)
- **MASTER_RS_SLAVE_SEL** (line 45)
- **MT7621_CPHA** (line 51)
- **MT7621_CPOL** (line 52)
- **MT7621_LSB_FIRST** (line 53)
- **MT7621_NATIVE_CS_COUNT** (line 55)
- **MT7621_SPI_DATA0** (line 35)
- **MT7621_SPI_DATA4** (line 36)
- **MT7621_SPI_MASTER** (line 40)
- **MT7621_SPI_MOREBUF** (line 47)
- **MT7621_SPI_OPCODE** (line 34)
- **MT7621_SPI_POLAR** (line 48)
- **MT7621_SPI_SPACE** (line 49)
- **MT7621_SPI_TRANS** (line 31)
- **RALINK_SPI_WAIT_MAX_LOOP** (line 26)
- **SPISTAT_BUSY** (line 29)
- **SPITRANS_BUSY** (line 32)
- **SPI_CTL_START** (line 38)
- **SPI_CTL_TX_RX_CNT_MASK** (line 37)

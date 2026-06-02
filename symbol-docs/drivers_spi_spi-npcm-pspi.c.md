# drivers/spi/spi-npcm-pspi.c

Subsystem: drivers/spi

## Functions (18)

### bytes_per_word
- Return type: static unsigned int
- Signature: bytes_per_word(unsigned int bits)
- Line: 61

### npcm_pspi_disable
- Return type: static void
- Signature: npcm_pspi_disable(struct npcm_pspi * priv)
- Line: 93

### npcm_pspi_enable
- Return type: static void
- Signature: npcm_pspi_enable(struct npcm_pspi * priv)
- Line: 84

### npcm_pspi_handler
- Return type: static irqreturn_t
- Signature: npcm_pspi_handler(int irq,void * dev_id)
- Line: 294

### npcm_pspi_irq_disable
- Return type: static void
- Signature: npcm_pspi_irq_disable(struct npcm_pspi * priv,u16 mask)
- Line: 75

### npcm_pspi_irq_enable
- Return type: static void
- Signature: npcm_pspi_irq_enable(struct npcm_pspi * priv,u16 mask)
- Line: 66

### npcm_pspi_prepare_transfer_hardware
- Return type: static int
- Signature: npcm_pspi_prepare_transfer_hardware(struct spi_controller * host)
- Line: 269

### npcm_pspi_probe
- Return type: static int
- Signature: npcm_pspi_probe(struct platform_device * pdev)
- Line: 340

### npcm_pspi_recv
- Return type: static void
- Signature: npcm_pspi_recv(struct npcm_pspi * priv)
- Line: 222

### npcm_pspi_remove
- Return type: static void
- Signature: npcm_pspi_remove(struct platform_device * pdev)
- Line: 432

### npcm_pspi_reset_hw
- Return type: static void
- Signature: npcm_pspi_reset_hw(struct npcm_pspi * priv)
- Line: 287

### npcm_pspi_send
- Return type: static void
- Signature: npcm_pspi_send(struct npcm_pspi * priv)
- Line: 195

### npcm_pspi_set_baudrate
- Return type: static void
- Signature: npcm_pspi_set_baudrate(struct npcm_pspi * priv,unsigned int speed)
- Line: 146

### npcm_pspi_set_mode
- Return type: static void
- Signature: npcm_pspi_set_mode(struct spi_device * spi)
- Line: 102

### npcm_pspi_set_transfer_size
- Return type: static void
- Signature: npcm_pspi_set_transfer_size(struct npcm_pspi * priv,int size)
- Line: 128

### npcm_pspi_setup_transfer
- Return type: static void
- Signature: npcm_pspi_setup_transfer(struct spi_device * spi,struct spi_transfer * t)
- Line: 159

### npcm_pspi_transfer_one
- Return type: static int
- Signature: npcm_pspi_transfer_one(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * t)
- Line: 248

### npcm_pspi_unprepare_transfer_hardware
- Return type: static int
- Signature: npcm_pspi_unprepare_transfer_hardware(struct spi_controller * host)
- Line: 278

## Structs (1)

### npcm_pspi
- Line: 20
- Members:
  - xfer_done: completion
  - reset: reset_control *
  - host: spi_controller *
  - tx_bytes: unsigned int
  - rx_bytes: unsigned int
  - base: void __iomem *
  - is_save_param: bool
  - bits_per_word: u8
  - tx_buf: const u8 *
  - clk: clk *
  - speed_hz: u32
  - rx_buf: u8 *
  - mode: u16
  - id: u32

## Variables (2)

- static **npcm_pspi_driver** : platform_driver (line 454)
- static **npcm_pspi_match** : const struct of_device_id[] (line 447)

## Macros (17)

- **DRIVER_NAME** (line 37)
- **NPCM_PSPI_CTL1** (line 40)
- **NPCM_PSPI_CTL1_EIR** (line 46)
- **NPCM_PSPI_CTL1_EIW** (line 47)
- **NPCM_PSPI_CTL1_MOD** (line 45)
- **NPCM_PSPI_CTL1_SCDV6_0** (line 50)
- **NPCM_PSPI_CTL1_SCIDL** (line 49)
- **NPCM_PSPI_CTL1_SCM** (line 48)
- **NPCM_PSPI_CTL1_SPIEN** (line 44)
- **NPCM_PSPI_DATA** (line 39)
- **NPCM_PSPI_DEFAULT_CLK** (line 59)
- **NPCM_PSPI_MAX_CLK_DIVIDER** (line 57)
- **NPCM_PSPI_MIN_CLK_DIVIDER** (line 58)
- **NPCM_PSPI_STAT** (line 41)
- **NPCM_PSPI_STAT_BSY** (line 52)
- **NPCM_PSPI_STAT_RBF** (line 53)
- **NPCM_PSPI_TIMEOUT_MS** (line 56)
